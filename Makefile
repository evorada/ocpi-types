JSON_FILES := $(wildcard schemas/*.json)

LANGUAGES := go python rust typescript

# Targets for each language
.PHONY: all go python rust prepare_dirs clean

all: prepare_dirs go python rust typescript

# Prepare output directories
prepare_dirs:
	@$(foreach dir,$(LANGUAGES),mkdir -p $(dir);)

# Define rules for Go
# Go requires one package per directory, so each schema version is generated
# into its own subpackage (e.g. schemas/v2.1.1.json -> go/v211/v211.go, package v211).
# This lets multiple OCPI versions coexist without redeclaring the same types.
go:
	@for f in $(JSON_FILES); do \
		pkg=$$(basename $$f .json | tr -cd '[:alnum:]'); \
		echo "Generating Go definition for $$f into go/$$pkg/$$pkg.go"; \
		mkdir -p go/$$pkg; \
		quicktype -s schema $$f -o go/$$pkg/$$pkg.go --lang go --package $$pkg; \
	done

# Define rules for Python
python: $(patsubst schemas/%.json,python/%.py,$(JSON_FILES))

python/%.py: schemas/%.json
	@echo "Generating Python definition for $< into $@"
	@quicktype -s schema $< -o $@ --lang python

# Define rules for Rust
rust: $(patsubst schemas/%.json,rust/%.rs,$(JSON_FILES))

rust/%.rs: schemas/%.json
	@echo "Generating Rust definition for $< into $@"
	@quicktype -s schema $< -o $@ --lang rust

# Clean target to remove generated files
clean:
	@echo "Cleaning up..."
	@rm -rf $(LANGUAGES)
