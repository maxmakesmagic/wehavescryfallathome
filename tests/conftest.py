"""Shared pytest fixtures and grammar introspection helpers for test modules."""

import json
import re
import threading
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from pathlib import Path

import pytest


class ScryfallQuerier:
    """Thread-safe Scryfall query helper with global request pacing."""

    _headers = {
        "User-Agent": "wehavescryfallathome/0.1 (pytest live validation)",
        "Accept": "application/json",
    }

    def __init__(self, min_interval_seconds: float = 0.12) -> None:
        """Initialize a querier with a minimum interval between all requests."""
        self._min_interval_seconds = min_interval_seconds
        self._lock = threading.Lock()
        self._next_request_at = 0.0

    def _wait_for_turn(self) -> None:
        """Block until this caller can issue the next request globally."""
        with self._lock:
            now = time.monotonic()
            wait_seconds = self._next_request_at - now
            if wait_seconds > 0:
                time.sleep(wait_seconds)
                now = time.monotonic()
            self._next_request_at = now + self._min_interval_seconds

    def accepts_query(
        self, query: str, timeout_seconds: float = 20.0
    ) -> tuple[bool, str]:
        """Check whether live Scryfall accepts the provided query term expression."""
        self._wait_for_turn()
        url = "https://api.scryfall.com/cards/search?" + urllib.parse.urlencode(
            {"q": query}
        )
        request = urllib.request.Request(url, headers=self._headers)

        try:
            with urllib.request.urlopen(request, timeout=timeout_seconds):
                return True, "ok"
        except urllib.error.HTTPError as exc:
            payload = json.loads(exc.read().decode("utf-8"))
            details = str(payload.get("details", ""))
            if exc.code == 404:
                return True, details
            if exc.code == 400:
                return False, details
            if exc.code == 429:
                return False, "rate-limited"
            return False, f"HTTP {exc.code}: {details}"
        except urllib.error.URLError as exc:
            return False, f"network error: {exc}"

    def accepts_is_value(
        self, is_value: str, timeout_seconds: float = 20.0
    ) -> tuple[bool, str]:
        """Check whether live Scryfall accepts `is:<value>` as a valid query term."""
        return self.accepts_query(f"is:{is_value}", timeout_seconds=timeout_seconds)

    def accepts_color_value(
        self, color_value: str, timeout_seconds: float = 20.0
    ) -> tuple[bool, str]:
        """Check whether live Scryfall accepts `color:<value>` as a valid query term."""
        return self.accepts_query(
            f"color:{color_value}", timeout_seconds=timeout_seconds
        )


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

    def get_color_values(self) -> list[str]:
        """Return representative valid `color:` values for test parameterization."""
        symbols = self.get_rule_symbols_in_order("colorValue")
        literal_map = self.get_lexer_literal_map()
        values: list[str] = []

        for symbol in symbols:
            if symbol in literal_map:
                values.append(literal_map[symbol])
            elif symbol == "NUMBER":
                values.append("2")
            elif symbol == "COLOR_SET":
                values.extend(["w", "ub", "wubrg"])
            else:
                raise AssertionError(f"Unsupported colorValue symbol: {symbol}")

        return sorted(set(values))

    def get_language_values(self) -> list[str]:
        """Return known `lang:`/`language:` values from grammar."""
        return sorted(set(self.get_rule_values_in_order("languageValue")))


@pytest.fixture
def scryfall_query_grammar() -> ScryfallQueryGrammarFile:
    """Provide an introspection helper for the main Scryfall grammar file."""
    return ScryfallQueryGrammarFile.default()


def pytest_generate_tests(metafunc: pytest.Metafunc) -> None:
    """Parameterize `is_value` indirectly from grammar-defined `isValue` entries."""
    grammar = ScryfallQueryGrammarFile.default()

    if "is_value" in metafunc.fixturenames:
        metafunc.parametrize("is_value", grammar.get_is_values(), indirect=True)

    if "color_value" in metafunc.fixturenames:
        metafunc.parametrize("color_value", grammar.get_color_values(), indirect=True)

    if "language_value" in metafunc.fixturenames:
        metafunc.parametrize(
            "language_value", grammar.get_language_values(), indirect=True
        )


@pytest.fixture
def is_value(request: pytest.FixtureRequest) -> str:
    """Indirect fixture carrying one `is:` value from grammar-driven parameterization."""
    return str(request.param)


@pytest.fixture
def color_value(request: pytest.FixtureRequest) -> str:
    """Indirect fixture carrying one `color:` value from grammar parameterization."""
    return str(request.param)


@pytest.fixture
def language_value(request: pytest.FixtureRequest) -> str:
    """Indirect fixture carrying one language value from grammar parameterization."""
    return str(request.param)


def pytest_addoption(parser: pytest.Parser) -> None:
    """Register CLI flags used by this test suite."""
    parser.addoption(
        "--live-scryfall",
        action="store_true",
        default=False,
        help="Run live Scryfall API validation tests.",
    )


@pytest.fixture(scope="session")
def scryfall_querier() -> ScryfallQuerier:
    """Provide a thread-safe, rate-limited querier for live Scryfall tests."""
    return ScryfallQuerier()
