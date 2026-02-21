"""Parser and optional live validation tests for `game:` values."""

import pytest
from conftest import ScryfallQuerier

from wehavescryfallathome import (
    KeywordQueryToken,
    QuerySemanticError,
    QuerySyntaxError,
    parse_query,
    tokenize_query,
)


@pytest.mark.parametrize("game_value", ["paper", "mtgo", "arena"])
def test_parser_accepts_known_game_values(game_value: str) -> None:
    """Ensure `game:` accepts known Scryfall game environment values."""
    query = f"game:{game_value}"
    parse_query(query)

    tokens = tokenize_query(query)
    assert len(tokens) == 1
    token = tokens[0]
    assert isinstance(token, KeywordQueryToken)
    assert token.type == "keyword"
    assert token.key == "game"
    assert token.operator == ":"
    assert token.value == game_value


@pytest.mark.parametrize("query", ["game:alchemy", "game:digital", "game:foo"])
def test_parser_rejects_unknown_game_values(query: str) -> None:
    """Reject values outside the constrained `game:` grammar."""
    with pytest.raises((QuerySyntaxError, QuerySemanticError)):
        parse_query(query)


@pytest.mark.live_scryfall
@pytest.mark.parametrize("game_value", ["paper", "mtgo", "arena"])
def test_live_scryfall_accepts_known_game_values(
    request: pytest.FixtureRequest,
    scryfall_querier: ScryfallQuerier,
    game_value: str,
) -> None:
    """Validate known `game:` values against live Scryfall."""
    if not bool(request.config.getoption("--live-scryfall")):
        pytest.skip("Pass --live-scryfall to enable live Scryfall validation")

    ok, details = scryfall_querier.accepts_query(f"game:{game_value}")
    if details == "rate-limited":
        pytest.skip("Scryfall rate limited this test run")

    assert ok, f"Scryfall rejected game:{game_value} -> {details}"
