# `ocpi-types`

Auto-generated type definitions for the OCPI protocol. Mostly generated with [`quicktype`]().

Currently generating packages for following languages:
* [Go](./go)
* [Python](./python) using `typing` and type hints
* [Rust](./rust)
* [TypeScript](./typescript)

The generated code had to be manually tweaked and cleaned up therefore running `quicktype` to regenerate the files can be destructive!

* The 2.1.1 schemas have been adapted from [`ChargeMap/ocpi-protocol`](https://github.com/ChargeMap/ocpi-protocol/tree/master/resources/jsonSchemas).
* The 2.2.1 schemas have been derived from the official [`ocpi/ocpi` `v2.2.1-d2`](https://github.com/ocpi/ocpi/tree/v2.2.1-d2) specification.

## Continuous integration

Two GitHub Actions workflows run on every push and pull request:

* [`compile-check`](.github/workflows/compile-check.yml) — builds the generated bindings in each language (one parallel job per language) to verify they compile.
* [`docs`](.github/workflows/docs.yml) — generates API documentation per language (Go via `gomarkdoc`, Python via `pdoc`, Rust via `cargo doc`, TypeScript via `ts-docs`) and publishes a combined site to GitHub Pages: https://evorada.github.io/ocpi-types/