"""Parser and optional live validation tests for `tou:`/`toughness:` values."""

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
    "query,value",
    [
        ("tou>=8", "8"),
        ("toughness=2", "2"),
        ("tou>pow", "pow"),
        ("toughness>power", "power"),
    ],
)
def test_parser_accepts_known_toughness_values(query: str, value: str) -> None:
    """Ensure known toughness comparisons parse for `tou:`/`toughness:`."""
    parse_query(query)

    tokens = tokenize_query(query)
    assert len(tokens) == 1
    token = tokens[0]
    assert isinstance(token, KeywordQueryToken)
    assert token.type == "keyword"
    assert token.key == "toughness"
    assert token.value == value


@pytest.mark.parametrize(
    "query",
    ["tou:foo", "toughness:legendary", "tou:mtgo", "tou>tou"],
)
def test_parser_rejects_invalid_toughness_values(query: str) -> None:
    """Reject values outside constrained toughness grammar."""
    with pytest.raises((QuerySyntaxError, QuerySemanticError)):
        parse_query(query)


@pytest.mark.live_scryfall
@pytest.mark.parametrize(
    "query",
    [
        "tou>=8",
        "toughness=2",
        "tou>pow",
        "toughness>power",
    ],
)
def test_live_scryfall_accepts_known_toughness_values(
    request: pytest.FixtureRequest,
    scryfall_querier: ScryfallQuerier,
    query: str,
) -> None:
    """Validate constrained toughness expressions against live Scryfall."""
    if not bool(request.config.getoption("--live-scryfall")):
        pytest.skip("Pass --live-scryfall to enable live Scryfall validation")

    ok, details = scryfall_querier.accepts_query(query)
    if details == "rate-limited":
        pytest.skip("Scryfall rate limited this test run")

    assert ok, f"Scryfall rejected {query} -> {details}"


@pytest.mark.live_scryfall
@pytest.mark.parametrize("query", ["tou>tou"])
def test_live_scryfall_rejects_known_bad_toughness_values(
    request: pytest.FixtureRequest,
    scryfall_querier: ScryfallQuerier,
    query: str,
) -> None:
    """Validate known unsupported toughness expressions against live Scryfall."""
    if not bool(request.config.getoption("--live-scryfall")):
        pytest.skip("Pass --live-scryfall to enable live Scryfall validation")

    ok, details = scryfall_querier.accepts_query(query)
    if details == "rate-limited":
        pytest.skip("Scryfall rate limited this test run")

    assert not ok, f"Scryfall unexpectedly accepted {query}"
