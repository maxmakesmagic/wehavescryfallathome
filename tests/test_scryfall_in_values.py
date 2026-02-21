"""Parser and optional live validation tests for constrained `in:` values."""

import pytest
from conftest import ScryfallQuerier

from wehavescryfallathome import (
    KeywordQueryToken,
    QuerySemanticError,
    QuerySyntaxError,
    parse_query,
    tokenize_query,
)


@pytest.mark.parametrize("in_value", ["paper", "mtgo", "arena"])
def test_parser_accepts_known_in_values(in_value: str) -> None:
    """Ensure `in:` accepts constrained game availability values."""
    query = f"in:{in_value}"
    parse_query(query)

    tokens = tokenize_query(query)
    assert len(tokens) == 1
    token = tokens[0]
    assert isinstance(token, KeywordQueryToken)
    assert token.type == "keyword"
    assert token.key == "in"
    assert token.operator == ":"
    assert token.value == in_value


@pytest.mark.parametrize("query", ["in:rare", "in:ru", "in:lea", "in:foo"])
def test_parser_rejects_invalid_in_values(query: str) -> None:
    """Reject values outside constrained `in:` game-value grammar."""
    with pytest.raises((QuerySyntaxError, QuerySemanticError)):
        parse_query(query)


@pytest.mark.live_scryfall
@pytest.mark.parametrize("in_value", ["paper", "mtgo", "arena"])
def test_live_scryfall_accepts_known_in_values(
    request: pytest.FixtureRequest,
    scryfall_querier: ScryfallQuerier,
    in_value: str,
) -> None:
    """Validate constrained `in:` values against live Scryfall."""
    if not bool(request.config.getoption("--live-scryfall")):
        pytest.skip("Pass --live-scryfall to enable live Scryfall validation")

    ok, details = scryfall_querier.accepts_query(f"in:{in_value}")
    if details == "rate-limited":
        pytest.skip("Scryfall rate limited this test run")

    assert ok, f"Scryfall rejected in:{in_value} -> {details}"
