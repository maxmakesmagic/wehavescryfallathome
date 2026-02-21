"""Parser and optional live validation tests for `lang:`/`language:` values."""

import pytest
from conftest import ScryfallQuerier

from wehavescryfallathome import (
    KeywordQueryToken,
    QuerySemanticError,
    QuerySyntaxError,
    parse_query,
    tokenize_query,
)


def test_parser_accepts_all_known_lang_values(language_value: str) -> None:
    """Ensure every grammar-defined language value parses for `lang:`."""
    query = f"lang:{language_value}"
    parse_query(query)

    tokens = tokenize_query(query)
    assert len(tokens) == 1
    token = tokens[0]
    assert isinstance(token, KeywordQueryToken)
    assert token.type == "keyword"
    assert token.key == "language"
    assert token.operator == ":"
    assert token.value == language_value


def test_parser_accepts_all_known_language_values(language_value: str) -> None:
    """Ensure every grammar-defined language value parses for `language:`."""
    query = f"language:{language_value}"
    parse_query(query)

    tokens = tokenize_query(query)
    assert len(tokens) == 1
    token = tokens[0]
    assert isinstance(token, KeywordQueryToken)
    assert token.type == "keyword"
    assert token.key == "language"
    assert token.operator == ":"
    assert token.value == language_value


@pytest.mark.parametrize(
    "query",
    [
        "lang:piglatin",
        "language:elvish",
        "lang:simplified_chinese",
        "language:traditional_chinese",
    ],
)
def test_parser_rejects_invalid_language_values(query: str) -> None:
    """Reject language names/codes outside the grammar-defined language set."""
    with pytest.raises((QuerySyntaxError, QuerySemanticError)):
        parse_query(query)


@pytest.mark.live_scryfall
def test_live_scryfall_accepts_all_language_values(
    request: pytest.FixtureRequest,
    scryfall_querier: ScryfallQuerier,
    language_value: str,
) -> None:
    """Validate each grammar-defined language value against live Scryfall."""
    if not bool(request.config.getoption("--live-scryfall")):
        pytest.skip("Pass --live-scryfall to enable live Scryfall validation")

    ok, details = scryfall_querier.accepts_query(f"lang:{language_value}")
    if details == "rate-limited":
        pytest.skip("Scryfall rate limited this test run")

    assert ok, f"Scryfall rejected lang:{language_value} -> {details}"
