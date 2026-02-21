"""Parser tests for constrained `r:`/`rarity:` values."""

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
        ("r:common", "common"),
        ("r:u", "u"),
        ("rarity:mythic", "mythic"),
        ("r>=r", "r"),
    ],
)
def test_parser_accepts_known_rarity_values(query: str, value: str) -> None:
    """Ensure known rarity values parse for `r:` and `rarity:`."""
    parse_query(query)

    tokens = tokenize_query(query)
    assert len(tokens) == 1
    token = tokens[0]
    assert isinstance(token, KeywordQueryToken)
    assert token.type == "keyword"
    assert token.key == "rarity"
    assert token.value == value


@pytest.mark.parametrize("query", ["r:pink", "rarity:foo", "rarity:standard"])
def test_parser_rejects_invalid_rarity_values(query: str) -> None:
    """Reject values outside the constrained rarity value set."""
    with pytest.raises((QuerySyntaxError, QuerySemanticError)):
        parse_query(query)


@pytest.mark.live_scryfall
@pytest.mark.parametrize(
    "query",
    [
        "r:common",
        "r:uncommon",
        "r:rare",
        "r:special",
        "r:mythic",
        "r:bonus",
        "rarity:common",
        "rarity:mythic",
        "r>=r",
    ],
)
def test_live_scryfall_accepts_known_rarity_values(
    request: pytest.FixtureRequest,
    scryfall_querier: ScryfallQuerier,
    query: str,
) -> None:
    """Validate known `r:`/`rarity:` expressions against live Scryfall."""
    if not bool(request.config.getoption("--live-scryfall")):
        pytest.skip("Pass --live-scryfall to enable live Scryfall validation")

    ok, details = scryfall_querier.accepts_query(query)
    if details == "rate-limited":
        pytest.skip("Scryfall rate limited this test run")

    assert ok, f"Scryfall rejected {query} -> {details}"
