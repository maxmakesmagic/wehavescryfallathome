"""Parser and optional live validation tests for `id:`/`identity:` values."""

import pytest
from conftest import ScryfallQuerier

from wehavescryfallathome import (
    KeywordQueryToken,
    QuerySemanticError,
    QuerySyntaxError,
    parse_query,
    tokenize_query,
)


def test_parser_accepts_all_known_id_values(color_value: str) -> None:
    """Ensure grammar-derived color identity values parse for `id:`."""
    query = f"id:{color_value}"
    parse_query(query)

    tokens = tokenize_query(query)
    assert len(tokens) == 1
    token = tokens[0]
    assert isinstance(token, KeywordQueryToken)
    assert token.type == "keyword"
    assert token.key == "identity"
    assert token.operator == ":"
    assert token.value == color_value


def test_parser_accepts_all_known_identity_values(color_value: str) -> None:
    """Ensure grammar-derived color identity values parse for `identity:`."""
    query = f"identity:{color_value}"
    parse_query(query)

    tokens = tokenize_query(query)
    assert len(tokens) == 1
    token = tokens[0]
    assert isinstance(token, KeywordQueryToken)
    assert token.type == "keyword"
    assert token.key == "identity"
    assert token.operator == ":"
    assert token.value == color_value


@pytest.mark.parametrize(
    "query",
    ["id:paper", "identity:foo", "id:english", "identity:mtgo"],
)
def test_parser_rejects_invalid_identity_values(query: str) -> None:
    """Reject values outside constrained identity value grammar."""
    with pytest.raises((QuerySyntaxError, QuerySemanticError)):
        parse_query(query)


@pytest.mark.live_scryfall
@pytest.mark.parametrize(
    "query",
    [
        "id:w",
        "id:ub",
        "id<=wub",
        "identity:c",
        "identity:m",
        "identity:2",
        "identity:azorius",
        "identity:chaos",
    ],
)
def test_live_scryfall_accepts_known_identity_values(
    request: pytest.FixtureRequest,
    scryfall_querier: ScryfallQuerier,
    query: str,
) -> None:
    """Validate representative `id:`/`identity:` expressions live."""
    if not bool(request.config.getoption("--live-scryfall")):
        pytest.skip("Pass --live-scryfall to enable live Scryfall validation")

    ok, details = scryfall_querier.accepts_query(query)
    if details == "rate-limited":
        pytest.skip("Scryfall rate limited this test run")

    assert ok, f"Scryfall rejected {query} -> {details}"
