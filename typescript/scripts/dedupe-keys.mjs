#!/usr/bin/env node
// Remove duplicate object-literal keys from generated TypeScript.
//
// quicktype output is hand-tweaked after generation (see README), and an edit
// can leave a stale entry behind — e.g. the same key twice in the runtime
// `typeMap`. TypeScript rejects that with TS1117, and at runtime JavaScript
// silently keeps only the LAST occurrence.
//
// This codemod removes every duplicate key except the last one, which makes the
// source match the behaviour the code already had at runtime — a safe,
// behaviour-preserving fix. It edits text ranges directly so formatting and
// alignment of the surrounding generated code are preserved.
//
// Usage:
//   node scripts/dedupe-keys.mjs --check  <files...>   # exit 1 if duplicates exist
//   node scripts/dedupe-keys.mjs --write  <files...>   # fix in place
// With no files, defaults to ./v*.ts
import ts from "typescript";
import { readFileSync, writeFileSync, readdirSync } from "node:fs";

function propName(p) {
  if (
    (ts.isPropertyAssignment(p) || ts.isShorthandPropertyAssignment(p)) &&
    p.name &&
    (ts.isIdentifier(p.name) || ts.isStringLiteral(p.name) || ts.isNumericLiteral(p.name))
  ) {
    return p.name.text;
  }
  return null; // spreads, accessors, computed names → leave untouched
}

// Returns the nodes to delete (all but the last occurrence of each duplicated
// key) and a flag noting whether we had to skip anything we couldn't prove safe.
function findDuplicates(sourceText, fileName) {
  const sf = ts.createSourceFile(fileName, sourceText, ts.ScriptTarget.Latest, true);
  const remove = [];
  const reports = [];

  function visit(node) {
    if (ts.isObjectLiteralExpression(node)) {
      const hasSpread = node.properties.some((p) => ts.isSpreadAssignment(p));
      const byName = new Map();
      for (const p of node.properties) {
        const name = propName(p);
        if (name == null) continue;
        if (!byName.has(name)) byName.set(name, []);
        byName.get(name).push(p);
      }
      for (const [name, props] of byName) {
        if (props.length < 2) continue;
        if (hasSpread) {
          // A spread between duplicates can change which value wins; don't guess.
          reports.push({ name, line: lineOf(sf, props[0]), skipped: true });
          continue;
        }
        // Keep the last occurrence (JS runtime semantics); drop the earlier ones.
        for (const p of props.slice(0, -1)) {
          remove.push(p);
          reports.push({ name, line: lineOf(sf, p), skipped: false });
        }
      }
    }
    ts.forEachChild(node, visit);
  }
  visit(sf);
  return { remove, reports };
}

function lineOf(sf, node) {
  return sf.getLineAndCharacterOfPosition(node.getStart(sf)).line + 1;
}

// Delete a property node along with its leading trivia (newline + indentation)
// and its trailing separator comma, so no dangling/double commas remain.
function deleteRanges(text, nodes) {
  const ranges = nodes.map((n) => {
    const start = n.getFullStart();
    let end = n.getEnd();
    let j = end;
    while (j < text.length && (text[j] === " " || text[j] === "\t")) j++;
    if (text[j] === ",") end = j + 1;
    return [start, end];
  });
  ranges.sort((a, b) => b[0] - a[0]); // delete back-to-front to keep offsets valid
  for (const [start, end] of ranges) text = text.slice(0, start) + text.slice(end);
  return text;
}

// ---- CLI -------------------------------------------------------------------

const args = process.argv.slice(2);
const check = args.includes("--check");
const write = args.includes("--write");
let files = args.filter((a) => !a.startsWith("--"));
if (files.length === 0) files = readdirSync(".").filter((f) => /^v.*\.ts$/.test(f)).sort();

if (!check && !write) {
  console.error("error: pass --check or --write");
  process.exit(2);
}

let totalDupes = 0;
let totalSkipped = 0;

for (const file of files) {
  const original = readFileSync(file, "utf8");
  const { remove, reports } = findDuplicates(original, file);
  const fixable = reports.filter((r) => !r.skipped);
  const skipped = reports.filter((r) => r.skipped);
  totalSkipped += skipped.length;

  for (const r of skipped) {
    console.warn(`⚠️  ${file}:${r.line}  duplicate key "${r.name}" near a spread — left untouched, fix by hand`);
  }
  if (fixable.length === 0) {
    console.log(`✓ ${file}: no removable duplicate keys`);
    continue;
  }
  totalDupes += fixable.length;
  for (const r of fixable) {
    console.log(`${write ? "fixed" : "found"} ${file}:${r.line}  duplicate key "${r.name}"`);
  }
  if (write) {
    writeFileSync(file, deleteRanges(original, remove));
  }
}

if (check && (totalDupes > 0 || totalSkipped > 0)) {
  console.error(`\n✗ duplicate object keys present. Run: npm run dedupe-keys`);
  process.exit(1);
}
if (totalSkipped > 0) process.exit(1);
console.log(write ? "\nDone." : "\nNo duplicates.");
