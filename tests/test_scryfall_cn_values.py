"""Parser and optional live validation tests for `cn:`/`number:` values."""

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
        ("cn:123", "123"),
        ("number:45", "45"),
        ("cn:123a", "123a"),
        ("cn:a-268", "a-268"),
        ("number:u30", "u30"),
        ("cn>=100", "100"),
    ],
)
def test_parser_accepts_known_cn_values(query: str, value: str) -> None:
    """Ensure constrained collector-number forms parse for `cn:`/`number:`."""
    parse_query(query)

    tokens = tokenize_query(query)
    assert len(tokens) == 1
    token = tokens[0]
    assert isinstance(token, KeywordQueryToken)
    assert token.type == "keyword"
    assert token.key == "number"
    assert token.value == value


@pytest.mark.parametrize(
    "query",
    [
        "cn:rare",
        "number:paper",
        "cn:foo",
        "number:a",
    ],
)
def test_parser_rejects_invalid_cn_values(query: str) -> None:
    """Reject non-collector-number values for `cn:`/`number:`."""
    with pytest.raises((QuerySyntaxError, QuerySemanticError)):
        parse_query(query)


@pytest.mark.live_scryfall
@pytest.mark.parametrize(
    "query",
    [
        "cn:1",
        "number:45",
        "cn>=100",
        "number<=10",
    ],
)
def test_live_scryfall_accepts_known_cn_values(
    request: pytest.FixtureRequest,
    scryfall_querier: ScryfallQuerier,
    query: str,
) -> None:
    """Validate representative `cn:`/`number:` expressions against live Scryfall."""
    if not bool(request.config.getoption("--live-scryfall")):
        pytest.skip("Pass --live-scryfall to enable live Scryfall validation")

    ok, details = scryfall_querier.accepts_query(query)
    if details == "rate-limited":
        pytest.skip("Scryfall rate limited this test run")

    assert ok, f"Scryfall rejected {query} -> {details}"
