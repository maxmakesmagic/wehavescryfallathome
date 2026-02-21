"""Grammar-derived `is:`/`not:` coverage tests."""

import pytest
from conftest import ScryfallQuerier, ScryfallQueryGrammarFile

from wehavescryfallathome import (
    IsQueryToken,
    NotQueryToken,
    parse_query,
    tokenize_query,
)


def test_is_value_list_is_sorted(
    scryfall_query_grammar: ScryfallQueryGrammarFile,
) -> None:
    """Keep `isValue` ordered alphabetically by literal value."""
    declared = scryfall_query_grammar.get_is_values_in_order()
    assert declared == sorted(declared)


def test_parser_accepts_all_known_is_values(is_value: str) -> None:
    """Ensure every declared `is` value parses and tokenizes as `IsQueryToken`."""
    query = f"is:{is_value}"
    parse_query(query)

    tokens = tokenize_query(query)
    assert len(tokens) == 1
    token = tokens[0]
    assert isinstance(token, IsQueryToken)
    assert token.type == "keyword"
    assert token.key == "is"
    assert token.operator == ":"
    assert token.value == is_value


def test_parser_accepts_all_known_not_values(is_value: str) -> None:
    """Ensure every declared `is` value parses under `not:` as well."""
    query = f"not:{is_value}"
    parse_query(query)

    tokens = tokenize_query(query)
    assert len(tokens) == 1
    token = tokens[0]
    assert isinstance(token, NotQueryToken)
    assert token.type == "keyword"
    assert token.key == "not"
    assert token.operator == ":"
    assert token.value == is_value


@pytest.mark.live_scryfall
def test_live_scryfall_accepts_all_is_values(
    request: pytest.FixtureRequest,
    scryfall_querier: ScryfallQuerier,
    is_value: str,
) -> None:
    """Validate each grammar-declared `is` value against live Scryfall."""
    if not bool(request.config.getoption("--live-scryfall")):
        pytest.skip("Pass --live-scryfall to enable live Scryfall validation")

    ok, details = scryfall_querier.accepts_is_value(is_value)
    if details == "rate-limited":
        pytest.skip("Scryfall rate limited this test run")

    assert ok, f"Scryfall rejected is:{is_value} -> {details}"
