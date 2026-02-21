"""Shared pytest fixtures and grammar introspection helpers for test modules."""

import re
from dataclasses import dataclass
from pathlib import Path

import pytest


@dataclass(frozen=True)
class ScryfallQueryGrammarFile:
    """Small helper wrapper around `ScryfallQuery.g4` for test-time introspection."""

    path: Path

    @classmethod
    def default(cls) -> "ScryfallQueryGrammarFile":
        """Return a wrapper bound to the repository's grammar file."""
        grammar_path = (
            Path(__file__).resolve().parents[1] / "grammar" / "ScryfallQuery.g4"
        )
        return cls(path=grammar_path)

    def read_text(self) -> str:
        """Read and return the full grammar file text."""
        return self.path.read_text(encoding="utf-8")

    def get_rule_symbols_in_order(self, rule_name: str) -> list[str]:
        """Return alternative symbols for a parser rule in declaration order."""
        grammar = self.read_text()
        block_match = re.search(
            rf"{rule_name}\s*\n\s*:(.*?)\n\s*;", grammar, flags=re.S
        )
        if block_match is None:
            raise AssertionError(f"Failed to locate {rule_name} rule in grammar")

        block = block_match.group(1)
        symbols = re.findall(r"\|\s*([A-Za-z_][A-Za-z0-9_]*)", block)
        first = re.search(r"^\s*([A-Za-z_][A-Za-z0-9_]*)", block)
        if first is None:
            raise AssertionError(f"{rule_name} rule did not contain alternatives")

        return [first.group(1), *symbols]

    def get_lexer_literal_map(self) -> dict[str, str]:
        """Map lexer symbol names to their literal string values."""
        grammar = self.read_text()
        return dict(
            re.findall(r"^([A-Z_][A-Z0-9_]*)\s*:\s*'([^']+)'\s*;", grammar, flags=re.M)
        )

    def get_rule_values_in_order(self, rule_name: str) -> list[str]:
        """Resolve parser-rule alternatives to literal values in declaration order."""
        symbols = self.get_rule_symbols_in_order(rule_name)
        literal_map = self.get_lexer_literal_map()
        values = [literal_map[symbol] for symbol in symbols]
        if not values:
            raise AssertionError(f"No values extracted for rule {rule_name}")
        return values

    def get_is_values(self) -> list[str]:
        """Return all known `is:` values sorted alphabetically."""
        return sorted(set(self.get_rule_values_in_order("isValue")))

    def get_is_values_in_order(self) -> list[str]:
        """Return `is:` values in the exact order declared in grammar."""
        return self.get_rule_values_in_order("isValue")


@pytest.fixture
def scryfall_query_grammar() -> ScryfallQueryGrammarFile:
    """Provide an introspection helper for the main Scryfall grammar file."""
    return ScryfallQueryGrammarFile.default()


def pytest_generate_tests(metafunc: pytest.Metafunc) -> None:
    """Parameterize `is_value` indirectly from grammar-defined `isValue` entries."""
    if "is_value" not in metafunc.fixturenames:
        return

    grammar = ScryfallQueryGrammarFile.default()
    metafunc.parametrize("is_value", grammar.get_is_values(), indirect=True)


@pytest.fixture
def is_value(request: pytest.FixtureRequest) -> str:
    """Indirect fixture carrying one `is:` value from grammar-driven parameterization."""
    return str(request.param)
