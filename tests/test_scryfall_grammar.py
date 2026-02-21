"""Core parser acceptance/rejection tests and selected live Scryfall checks."""

import urllib.error

import pytest
from scrython.cards import Search

from wehavescryfallathome import (
    QuerySemanticError,
    QuerySyntaxError,
    parse_query,
    tokenize_query,
)

KNOWN_GOOD = [
    'c:rg t:creature o:"draw a card"',
    "t:land (a:titus or a:avon)",
    "is:ff7",
    "is:adventure",
    "is:borderless",
    "is:fullart",
    "name:/\\bizzet\\b/ t:instant",
    "pow>tou c:w t:creature",
    "m:{R/P} mv<=3",
    "lang:any t:planeswalker unique:prints",
    '!"Lightning Bolt" unique:prints',
    "-fire c:r t:instant",
    "through (depths or sands or mists)",
    "date>ori order:released direction:asc",
]

KNOWN_BAD = [
    "(unique:prints)",  # display keyword inside grouping
    "woo:bar",  # unknown/unsupported pre-colon operator
    "t:land (a:titus or a:avon",  # missing closing parenthesis
    "((t:elf)",  # unbalanced parentheses (extra opening paren)
    "t::elf",  # malformed operator (double colon)
    "name:/unclosed",  # unterminated regex literal
    'o:"unterminated',  # unterminated quoted string literal
]


def _scrython_accepts(query: str) -> bool:
    try:
        Search(q=query)
        return True
    except urllib.error.URLError as exc:
        pytest.skip(f"Network unavailable for live Scryfall validation: {exc}")
    except Exception as exc:  # noqa: BLE001 - third-party exceptions are inconsistent
        message = str(exc)
        if "HTTP Error 400" in message:
            return False
        if "HTTP Error 429" in message:
            pytest.skip("Scryfall rate limited this test run")
        if "timed out" in message.lower() or "temporary failure" in message.lower():
            pytest.skip(f"Network unavailable for live Scryfall validation: {message}")
        raise


@pytest.mark.parametrize("query", KNOWN_GOOD)
def test_local_parser_accepts_known_good(query: str) -> None:
    """Ensure local parsing/tokenization accepts representative valid queries."""
    parse_query(query)
    tokens = tokenize_query(query)
    assert len(tokens) >= 1


@pytest.mark.parametrize("query", KNOWN_BAD)
def test_local_parser_rejects_known_bad(query: str) -> None:
    """Ensure local parser rejects malformed or unsupported query shapes."""
    with pytest.raises((QuerySyntaxError, QuerySemanticError)):
        parse_query(query)


@pytest.mark.parametrize("query", KNOWN_GOOD[:5])
def test_live_scrython_accepts_good_queries(query: str) -> None:
    """Sanity-check that known-good samples are accepted by live Scryfall."""
    assert _scrython_accepts(query)


@pytest.mark.parametrize("query", ["(unique:prints)", "t:land (a:titus or a:avon"])
def test_live_scrython_rejects_bad_queries(query: str) -> None:
    """Sanity-check that known-bad samples are rejected by live Scryfall."""
    assert not _scrython_accepts(query)
