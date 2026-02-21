"""Parser and optional live validation tests for `frame:` values."""

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
    "frame_value",
    [
        "1993",
        "1997",
        "2003",
        "2015",
        "future",
        "legendary",
        "colorshifted",
        "tombstone",
        "enchantment",
    ],
)
def test_parser_accepts_known_frame_values(frame_value: str) -> None:
    """Ensure documented `frame:` values parse under constrained grammar."""
    query = f"frame:{frame_value}"
    parse_query(query)

    tokens = tokenize_query(query)
    assert len(tokens) == 1
    token = tokens[0]
    assert isinstance(token, KeywordQueryToken)
    assert token.type == "keyword"
    assert token.key == "frame"
    assert token.operator == ":"
    assert token.value == frame_value


@pytest.mark.parametrize("query", ["frame:foo", "frame:arena", "frame:1994"])
def test_parser_rejects_invalid_frame_values(query: str) -> None:
    """Reject values outside the constrained documented frame set."""
    with pytest.raises((QuerySyntaxError, QuerySemanticError)):
        parse_query(query)


@pytest.mark.live_scryfall
@pytest.mark.parametrize(
    "frame_value",
    [
        "1993",
        "1997",
        "2003",
        "2015",
        "future",
        "legendary",
        "colorshifted",
        "tombstone",
        "enchantment",
    ],
)
def test_live_scryfall_accepts_known_frame_values(
    request: pytest.FixtureRequest,
    scryfall_querier: ScryfallQuerier,
    frame_value: str,
) -> None:
    """Validate known `frame:` values against live Scryfall."""
    if not bool(request.config.getoption("--live-scryfall")):
        pytest.skip("Pass --live-scryfall to enable live Scryfall validation")

    ok, details = scryfall_querier.accepts_query(f"frame:{frame_value}")
    if details == "rate-limited":
        pytest.skip("Scryfall rate limited this test run")

    assert ok, f"Scryfall rejected frame:{frame_value} -> {details}"
