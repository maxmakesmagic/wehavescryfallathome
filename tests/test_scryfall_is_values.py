"""Grammar-derived `is:`/`not:` coverage tests."""

from conftest import ScryfallQueryGrammarFile

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
