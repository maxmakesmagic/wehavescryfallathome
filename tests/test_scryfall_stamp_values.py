"""Parser and optional live validation tests for `stamp:` values."""

import pytest
from conftest import ScryfallQuerier

from wehavescryfallathome import (
    KeywordQueryToken,
    QuerySemanticError,
    QuerySyntaxError,
    parse_query,
    tokenize_query,
)


@pytest.mark.parametrize(
    "stamp_value",
    ["oval", "acorn", "triangle", "arena", "circle", "heart"],
)
def test_parser_accepts_known_stamp_values(stamp_value: str) -> None:
    """Ensure `stamp:` accepts known Scryfall security stamp values."""
    query = f"stamp:{stamp_value}"
    parse_query(query)

    tokens = tokenize_query(query)
    assert len(tokens) == 1
    token = tokens[0]
    assert isinstance(token, KeywordQueryToken)
    assert token.type == "keyword"
    assert token.key == "stamp"
    assert token.operator == ":"
    assert token.value == stamp_value


@pytest.mark.parametrize("query", ["stamp:gold", "stamp:pink", "stamp:foo"])
def test_parser_rejects_unknown_stamp_values(query: str) -> None:
    """Reject values outside the constrained `stamp:` grammar."""
    with pytest.raises((QuerySyntaxError, QuerySemanticError)):
        parse_query(query)


@pytest.mark.live_scryfall
@pytest.mark.parametrize(
    "stamp_value",
    ["oval", "acorn", "triangle", "arena", "circle", "heart"],
)
def test_live_scryfall_accepts_known_stamp_values(
    request: pytest.FixtureRequest,
    scryfall_querier: ScryfallQuerier,
    stamp_value: str,
) -> None:
    """Validate known `stamp:` values against live Scryfall."""
    if not bool(request.config.getoption("--live-scryfall")):
        pytest.skip("Pass --live-scryfall to enable live Scryfall validation")

    ok, details = scryfall_querier.accepts_query(f"stamp:{stamp_value}")
    if details == "rate-limited":
        pytest.skip("Scryfall rate limited this test run")

    assert ok, f"Scryfall rejected stamp:{stamp_value} -> {details}"
