"""Grammar-derived parser tests for `color:`/`c:` values."""

import pytest
from conftest import ScryfallQuerier

from wehavescryfallathome import (
    KeywordQueryToken,
    QuerySemanticError,
    QuerySyntaxError,
    parse_query,
    tokenize_query,
)


def test_parser_accepts_all_known_color_values(color_value: str) -> None:
    """Ensure every grammar-derived color value parses for `color:`."""
    query = f"color:{color_value}"
    parse_query(query)

    tokens = tokenize_query(query)
    assert len(tokens) == 1
    token = tokens[0]
    assert isinstance(token, KeywordQueryToken)
    assert token.type == "keyword"
    assert token.key == "color"
    assert token.operator == ":"
    assert token.value == color_value


def test_parser_accepts_all_known_c_values(color_value: str) -> None:
    """Ensure every grammar-derived color value parses for `c:`."""
    query = f"c:{color_value}"
    parse_query(query)

    tokens = tokenize_query(query)
    assert len(tokens) == 1
    token = tokens[0]
    assert isinstance(token, KeywordQueryToken)
    assert token.type == "keyword"
    assert token.key == "color"
    assert token.operator == ":"
    assert token.value == color_value


@pytest.mark.parametrize(
    "query", ["color:pink", "c:pink", "color:phyrexian", "c:phyrexian"]
)
def test_parser_rejects_invalid_color_values(query: str) -> None:
    """Reject values not supported by the constrained `color` grammar."""
    with pytest.raises((QuerySyntaxError, QuerySemanticError)):
        parse_query(query)


@pytest.mark.live_scryfall
def test_live_scryfall_accepts_all_color_values(
    request: pytest.FixtureRequest,
    scryfall_querier: ScryfallQuerier,
    color_value: str,
) -> None:
    """Validate each grammar-derived `color` value against live Scryfall."""
    if not bool(request.config.getoption("--live-scryfall")):
        pytest.skip("Pass --live-scryfall to enable live Scryfall validation")

    ok, details = scryfall_querier.accepts_color_value(color_value)
    if details == "rate-limited":
        pytest.skip("Scryfall rate limited this test run")

    assert ok, f"Scryfall rejected color:{color_value} -> {details}"
