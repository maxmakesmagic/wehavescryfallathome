#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

GRAMMAR_FILE="$REPO_ROOT/grammar/ScryfallQuery.g4"
OUTPUT_DIR="$REPO_ROOT/src/wehavescryfallathome/antlr_generated"

if ! command -v antlr4 >/dev/null 2>&1; then
	echo "error: antlr4 command not found. Install antlr4-tools first." >&2
	exit 1
fi

if [[ ! -f "$GRAMMAR_FILE" ]]; then
	echo "error: missing grammar file at $GRAMMAR_FILE" >&2
	exit 1
fi

mkdir -p "$OUTPUT_DIR"

# Clean previously generated files while preserving __init__.py.
rm -f \
	"$OUTPUT_DIR/ScryfallQuery.interp" \
	"$OUTPUT_DIR/ScryfallQuery.tokens" \
	"$OUTPUT_DIR/ScryfallQueryLexer.interp" \
	"$OUTPUT_DIR/ScryfallQueryLexer.py" \
	"$OUTPUT_DIR/ScryfallQueryLexer.tokens" \
	"$OUTPUT_DIR/ScryfallQueryListener.py" \
	"$OUTPUT_DIR/ScryfallQueryParser.py" \
	"$OUTPUT_DIR/ScryfallQueryVisitor.py"

antlr4 \
	-Dlanguage=Python3 \
	-listener \
	-visitor \
	-Xexact-output-dir \
	-o "$OUTPUT_DIR" \
	"$GRAMMAR_FILE"

# Normalize generated header comments so local absolute paths are not embedded.
for generated_file in \
	"$OUTPUT_DIR/ScryfallQueryLexer.py" \
	"$OUTPUT_DIR/ScryfallQueryListener.py" \
	"$OUTPUT_DIR/ScryfallQueryParser.py" \
	"$OUTPUT_DIR/ScryfallQueryVisitor.py"
do
	if [[ -f "$generated_file" ]]; then
		sed -i '1s|^# Generated from .* by ANTLR |# Generated from grammar/ScryfallQuery.g4 by ANTLR |' "$generated_file"
	fi
done

echo "Grammar regenerated in $OUTPUT_DIR"
