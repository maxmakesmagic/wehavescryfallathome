"""Parser and optional live validation tests for `border:` values."""

import pytest
from conftest import ScryfallQuerier

from wehavescryfallathome import (
    KeywordQueryToken,
    QuerySemanticError,
    QuerySyntaxError,
    parse_query,
    tokenize_query,
)


@pytest.mark.parametrize("border_value", ["black", "white", "silver", "borderless"])
def test_parser_accepts_known_border_values(border_value: str) -> None:
    """Ensure `border:` accepts known Scryfall border values."""
    query = f"border:{border_value}"
    parse_query(query)

    tokens = tokenize_query(query)
    assert len(tokens) == 1
    token = tokens[0]
    assert isinstance(token, KeywordQueryToken)
    assert token.type == "keyword"
    assert token.key == "border"
    assert token.operator == ":"
    assert token.value == border_value


@pytest.mark.parametrize("query", ["border:pink", "border:phyrexian", "border:gold"])
def test_parser_rejects_unknown_border_values(query: str) -> None:
    """Reject values not supported by `border:` in Scryfall syntax."""
    with pytest.raises((QuerySyntaxError, QuerySemanticError)):
        parse_query(query)


@pytest.mark.live_scryfall
@pytest.mark.parametrize("border_value", ["black", "white", "silver", "borderless"])
def test_live_scryfall_accepts_known_border_values(
    request: pytest.FixtureRequest,
    scryfall_querier: ScryfallQuerier,
    border_value: str,
) -> None:
    """Validate known `border:` values against live Scryfall."""
    if not bool(request.config.getoption("--live-scryfall")):
        pytest.skip("Pass --live-scryfall to enable live Scryfall validation")

    ok, details = scryfall_querier.accepts_query(f"border:{border_value}")
    if details == "rate-limited":
        pytest.skip("Scryfall rate limited this test run")

    assert ok, f"Scryfall rejected border:{border_value} -> {details}"
