"""Parser tests for constrained `m:`/`mana:` value syntax."""

import pytest

from wehavescryfallathome import (
    KeywordQueryToken,
    QuerySemanticError,
    QuerySyntaxError,
    parse_query,
    tokenize_query,
)


@pytest.mark.parametrize(
    "query,key,value",
    [
        ("m:{R/P}", "m", "{R/P}"),
        ("m:2WW", "m", "2WW"),
        ("mana:{2/G}", "mana", "{2/G}"),
        ("m>3WU", "m", "3WU"),
        ("mana:{W/U}{W/U}", "mana", "{W/U}{W/U}"),
    ],
)
def test_parser_accepts_known_mana_values(query: str, key: str, value: str) -> None:
    """Ensure common Scryfall mana expressions parse under `m:` and `mana:`."""
    parse_query(query)

    tokens = tokenize_query(query)
    assert len(tokens) == 1
    token = tokens[0]
    assert isinstance(token, KeywordQueryToken)
    assert token.type == "keyword"
    assert token.key == key
    assert token.value == value


@pytest.mark.parametrize("query", ["m:phyrexian", "mana:pink", "m:{R/P", "mana:{W/U)"])
def test_parser_rejects_invalid_mana_values(query: str) -> None:
    """Reject free-form words and malformed symbol syntax for mana keys."""
    with pytest.raises((QuerySyntaxError, QuerySemanticError)):
        parse_query(query)
