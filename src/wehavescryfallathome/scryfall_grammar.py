"""ANTLR-backed parsing and tokenization for Scryfall-style query strings.

Design goals:
- Keep a small public API for callers (`parse_query`, `lex_query`, `tokenize_query`).
- Build a clean intermediate AST so a SQL backend can be added naturally.
- Keep lexer/parser concerns separate from semantic concerns.
"""

import re
from dataclasses import dataclass
from typing import ClassVar, TypeAlias

from antlr4 import CommonTokenStream, InputStream, Token
from antlr4.error.ErrorListener import ErrorListener

from .antlr_generated.ScryfallQueryLexer import ScryfallQueryLexer
from .antlr_generated.ScryfallQueryParser import ScryfallQueryParser

_OPERATOR_RE = re.compile(r"^([a-z_]+)(:|!=|>=|<=|=|>|<)(.+)$")


@dataclass(frozen=True)
class QueryToken:
    """Base token for normalized query terms."""

    raw: str
    negated: bool

    @property
    def type(self) -> str:
        """A stable token category label."""
        return "token"

    @property
    def key(self) -> str | None:
        """Keyword key when this token represents `key<op>value`."""
        return None

    @property
    def operator(self) -> str | None:
        """Keyword operator when this token represents `key<op>value`."""
        return None

    @property
    def value(self) -> str | None:
        """Keyword value when this token represents `key<op>value`."""
        return None


@dataclass(frozen=True)
class WordQueryToken(QueryToken):
    """A plain bare word term."""

    @property
    def type(self) -> str:
        """Return the stable category label for word tokens."""
        return "word"


@dataclass(frozen=True)
class QuotedQueryToken(QueryToken):
    """A quoted-string term."""

    @property
    def type(self) -> str:
        """Return the stable category label for quoted tokens."""
        return "quoted"


@dataclass(frozen=True)
class ExactNameQueryToken(QueryToken):
    """An exact-name term introduced by `!`."""

    @property
    def type(self) -> str:
        """Return the stable category label for exact-name tokens."""
        return "exact_name"


@dataclass(frozen=True)
class KeywordQueryToken(QueryToken):
    """Generic `key<op>value` token."""

    keys: ClassVar[tuple[str, ...]] = ()

    token_key: str
    token_operator: str
    token_value: str

    @property
    def type(self) -> str:
        """Return the stable category label for keyword tokens."""
        return "keyword"

    @property
    def key(self) -> str:
        """Return the keyword name (for example `is`, `t`, `mv`)."""
        return self.token_key

    @property
    def operator(self) -> str:
        """Return the keyword comparison operator."""
        return self.token_operator

    @property
    def value(self) -> str:
        """Return the keyword value payload."""
        return self.token_value


@dataclass(frozen=True)
class IsQueryToken(KeywordQueryToken):
    """Specialized token for `is:<value>` operations."""

    keys: ClassVar[tuple[str, ...]] = ("is",)


@dataclass(frozen=True)
class NotQueryToken(KeywordQueryToken):
    """Specialized token for `not:<value>` operations."""

    keys: ClassVar[tuple[str, ...]] = ("not",)


@dataclass(frozen=True)
class IncludeQueryToken(KeywordQueryToken):
    """Specialized token for `include:<value>` operations."""

    keys: ClassVar[tuple[str, ...]] = ("include",)


@dataclass(frozen=True)
class UniqueQueryToken(KeywordQueryToken):
    """Specialized token for `unique:<value>` operations."""

    keys: ClassVar[tuple[str, ...]] = ("unique",)


@dataclass(frozen=True)
class FormatQueryToken(KeywordQueryToken):
    """Specialized token for `format`/`f` operations."""

    keys: ClassVar[tuple[str, ...]] = ("format", "f")


@dataclass(frozen=True)
class BannedQueryToken(KeywordQueryToken):
    """Specialized token for `banned:<value>` operations."""

    keys: ClassVar[tuple[str, ...]] = ("banned",)


@dataclass(frozen=True)
class RestrictedQueryToken(KeywordQueryToken):
    """Specialized token for `restricted:<value>` operations."""

    keys: ClassVar[tuple[str, ...]] = ("restricted",)


@dataclass(frozen=True)
class GameQueryToken(KeywordQueryToken):
    """Specialized token for `game:<value>` operations."""

    keys: ClassVar[tuple[str, ...]] = ("game",)


@dataclass(frozen=True)
class RarityQueryToken(KeywordQueryToken):
    """Specialized token for `rarity`/`r` operations."""

    keys: ClassVar[tuple[str, ...]] = ("rarity", "r")


@dataclass(frozen=True)
class InQueryToken(KeywordQueryToken):
    """Specialized token for `in:<value>` operations."""

    keys: ClassVar[tuple[str, ...]] = ("in",)


@dataclass(frozen=True)
class ManaValueQueryToken(KeywordQueryToken):
    """Specialized token for `manavalue`/`mv` operations."""

    keys: ClassVar[tuple[str, ...]] = ("manavalue", "mv")


@dataclass(frozen=True)
class ArtistQueryToken(KeywordQueryToken):
    """Specialized token for artist-key operations."""

    keys: ClassVar[tuple[str, ...]] = ("artist", "a", "artists")


@dataclass(frozen=True)
class ArtQueryToken(KeywordQueryToken):
    """Specialized token for `art:<value>` operations."""

    keys: ClassVar[tuple[str, ...]] = ("art",)


@dataclass(frozen=True)
class ArtTagQueryToken(KeywordQueryToken):
    """Specialized token for `arttag`/`atag` operations."""

    keys: ClassVar[tuple[str, ...]] = ("arttag", "atag")


@dataclass(frozen=True)
class BlockQueryToken(KeywordQueryToken):
    """Specialized token for `block`/`b` operations."""

    keys: ClassVar[tuple[str, ...]] = ("block", "b")


@dataclass(frozen=True)
class BorderQueryToken(KeywordQueryToken):
    """Specialized token for `border:<value>` operations."""

    keys: ClassVar[tuple[str, ...]] = ("border",)


@dataclass(frozen=True)
class ColorQueryToken(KeywordQueryToken):
    """Specialized token for `color`/`c` operations."""

    keys: ClassVar[tuple[str, ...]] = ("color", "c")


@dataclass(frozen=True)
class CheapestQueryToken(KeywordQueryToken):
    """Specialized token for `cheapest:<value>` operations."""

    keys: ClassVar[tuple[str, ...]] = ("cheapest",)


@dataclass(frozen=True)
class NumberQueryToken(KeywordQueryToken):
    """Specialized token for `number`/`cn` operations."""

    keys: ClassVar[tuple[str, ...]] = ("number", "cn")


@dataclass(frozen=True)
class CubeQueryToken(KeywordQueryToken):
    """Specialized token for `cube:<value>` operations."""

    keys: ClassVar[tuple[str, ...]] = ("cube",)


@dataclass(frozen=True)
class DateQueryToken(KeywordQueryToken):
    """Specialized token for `date:<value>` operations."""

    keys: ClassVar[tuple[str, ...]] = ("date",)


@dataclass(frozen=True)
class DevotionQueryToken(KeywordQueryToken):
    """Specialized token for `devotion:<value>` operations."""

    keys: ClassVar[tuple[str, ...]] = ("devotion",)


@dataclass(frozen=True)
class EditionQueryToken(KeywordQueryToken):
    """Specialized token for `edition`/`e` operations."""

    keys: ClassVar[tuple[str, ...]] = ("edition", "e")


@dataclass(frozen=True)
class EurQueryToken(KeywordQueryToken):
    """Specialized token for `eur:<value>` operations."""

    keys: ClassVar[tuple[str, ...]] = ("eur",)


@dataclass(frozen=True)
class FlavorQueryToken(KeywordQueryToken):
    """Specialized token for `flavor`/`ft` operations."""

    keys: ClassVar[tuple[str, ...]] = ("flavor", "ft")


@dataclass(frozen=True)
class FoQueryToken(KeywordQueryToken):
    """Specialized token for `fo:<value>` operations."""

    keys: ClassVar[tuple[str, ...]] = ("fo",)


@dataclass(frozen=True)
class FullOracleQueryToken(KeywordQueryToken):
    """Specialized token for `fulloracle:<value>` operations."""

    keys: ClassVar[tuple[str, ...]] = ("fulloracle",)


@dataclass(frozen=True)
class FunctionQueryToken(KeywordQueryToken):
    """Specialized token for `function:<value>` operations."""

    keys: ClassVar[tuple[str, ...]] = ("function",)


@dataclass(frozen=True)
class IdentityQueryToken(KeywordQueryToken):
    """Specialized token for `identity`/`id` operations."""

    keys: ClassVar[tuple[str, ...]] = ("identity", "id")


@dataclass(frozen=True)
class IllustrationsQueryToken(KeywordQueryToken):
    """Specialized token for `illustrations:<value>` operations."""

    keys: ClassVar[tuple[str, ...]] = ("illustrations",)


@dataclass(frozen=True)
class KeywordKeyQueryToken(KeywordQueryToken):
    """Specialized token for `keyword`/`kw` operations."""

    keys: ClassVar[tuple[str, ...]] = ("keyword", "kw")


@dataclass(frozen=True)
class LanguageQueryToken(KeywordQueryToken):
    """Specialized token for `language`/`lang` operations."""

    keys: ClassVar[tuple[str, ...]] = ("language", "lang")


@dataclass(frozen=True)
class LoyaltyQueryToken(KeywordQueryToken):
    """Specialized token for `loyalty`/`loy` operations."""

    keys: ClassVar[tuple[str, ...]] = ("loyalty", "loy")


@dataclass(frozen=True)
class ManaQueryToken(KeywordQueryToken):
    """Specialized token for `mana`/`m` operations."""

    keys: ClassVar[tuple[str, ...]] = ("mana", "m")


@dataclass(frozen=True)
class NameQueryToken(KeywordQueryToken):
    """Specialized token for `name`/`n` operations."""

    keys: ClassVar[tuple[str, ...]] = ("name", "n")


@dataclass(frozen=True)
class NewQueryToken(KeywordQueryToken):
    """Specialized token for `new:<value>` operations."""

    keys: ClassVar[tuple[str, ...]] = ("new",)


@dataclass(frozen=True)
class OracleQueryToken(KeywordQueryToken):
    """Specialized token for `oracle`/`o` operations."""

    keys: ClassVar[tuple[str, ...]] = ("oracle", "o")


@dataclass(frozen=True)
class OracleTagQueryToken(KeywordQueryToken):
    """Specialized token for `oracletag`/`otag` operations."""

    keys: ClassVar[tuple[str, ...]] = ("oracletag", "otag")


@dataclass(frozen=True)
class PaperPrintsQueryToken(KeywordQueryToken):
    """Specialized token for `paperprints:<value>` operations."""

    keys: ClassVar[tuple[str, ...]] = ("paperprints",)


@dataclass(frozen=True)
class PaperSetsQueryToken(KeywordQueryToken):
    """Specialized token for `papersets:<value>` operations."""

    keys: ClassVar[tuple[str, ...]] = ("papersets",)


@dataclass(frozen=True)
class PowerQueryToken(KeywordQueryToken):
    """Specialized token for `power`/`pow` operations."""

    keys: ClassVar[tuple[str, ...]] = ("power", "pow")


@dataclass(frozen=True)
class PowTouQueryToken(KeywordQueryToken):
    """Specialized token for `powtou`/`pt` operations."""

    keys: ClassVar[tuple[str, ...]] = ("powtou", "pt")


@dataclass(frozen=True)
class PrintsQueryToken(KeywordQueryToken):
    """Specialized token for `prints:<value>` operations."""

    keys: ClassVar[tuple[str, ...]] = ("prints",)


@dataclass(frozen=True)
class ProducesQueryToken(KeywordQueryToken):
    """Specialized token for `produces:<value>` operations."""

    keys: ClassVar[tuple[str, ...]] = ("produces",)


@dataclass(frozen=True)
class SetQueryToken(KeywordQueryToken):
    """Specialized token for `set`/`s` operations."""

    keys: ClassVar[tuple[str, ...]] = ("set", "s")


@dataclass(frozen=True)
class SetsQueryToken(KeywordQueryToken):
    """Specialized token for `sets:<value>` operations."""

    keys: ClassVar[tuple[str, ...]] = ("sets",)


@dataclass(frozen=True)
class StampQueryToken(KeywordQueryToken):
    """Specialized token for `stamp`/`st` operations."""

    keys: ClassVar[tuple[str, ...]] = ("stamp", "st")


@dataclass(frozen=True)
class TypeQueryToken(KeywordQueryToken):
    """Specialized token for `type`/`t` operations."""

    keys: ClassVar[tuple[str, ...]] = ("type", "t")


@dataclass(frozen=True)
class TixQueryToken(KeywordQueryToken):
    """Specialized token for `tix:<value>` operations."""

    keys: ClassVar[tuple[str, ...]] = ("tix",)


@dataclass(frozen=True)
class ToughnessQueryToken(KeywordQueryToken):
    """Specialized token for `toughness`/`tou` operations."""

    keys: ClassVar[tuple[str, ...]] = ("toughness", "tou")


@dataclass(frozen=True)
class UsdQueryToken(KeywordQueryToken):
    """Specialized token for `usd:<value>` operations."""

    keys: ClassVar[tuple[str, ...]] = ("usd",)


@dataclass(frozen=True)
class WatermarkQueryToken(KeywordQueryToken):
    """Specialized token for `watermark`/`wm` operations."""

    keys: ClassVar[tuple[str, ...]] = ("watermark", "wm")


@dataclass(frozen=True)
class YearQueryToken(KeywordQueryToken):
    """Specialized token for `year:<value>` operations."""

    keys: ClassVar[tuple[str, ...]] = ("year",)


def _iter_keyword_token_subclasses() -> tuple[type[KeywordQueryToken], ...]:
    """Return all keyword token subclasses recursively."""
    pending = list(KeywordQueryToken.__subclasses__())
    discovered: list[type[KeywordQueryToken]] = []

    while pending:
        subclass = pending.pop()
        discovered.append(subclass)
        pending.extend(subclass.__subclasses__())

    return tuple(discovered)


def _build_keyword_token_registry() -> dict[str, type[KeywordQueryToken]]:
    """Build a key-alias to token-class registry from subclass declarations."""
    registry: dict[str, type[KeywordQueryToken]] = {}
    for token_class in _iter_keyword_token_subclasses():
        for key in token_class.keys:
            registry[key] = token_class
    return registry


_KEYWORD_TOKEN_REGISTRY = _build_keyword_token_registry()


@dataclass(frozen=True)
class LexToken:
    """A raw lexer token emitted directly by ANTLR (EOF excluded)."""

    type: str
    raw: str
    index: int
    start: int
    stop: int


class QuerySyntaxError(ValueError):
    """Raised when a query fails parser-level syntax validation."""


class QuerySemanticError(ValueError):
    """Raised when a query fails semantic validation after parsing."""


@dataclass(frozen=True)
class Predicate:
    """A `key op value` predicate extracted from a query term."""

    key: str
    operator: str
    value: str


@dataclass(frozen=True)
class Term:
    """A single query term, optionally negated."""

    kind: str
    raw: str
    negated: bool
    predicate: Predicate | None = None


@dataclass(frozen=True)
class AndExpr:
    """Implicit AND of child expressions."""

    children: tuple["Expr", ...]


@dataclass(frozen=True)
class OrExpr:
    """Explicit OR of child expressions."""

    children: tuple["Expr", ...]


Expr: TypeAlias = Term | AndExpr | OrExpr


@dataclass(frozen=True)
class QueryAst:
    """Parsed query AST root.

    `root` is a boolean expression tree composed of `OrExpr`, `AndExpr`, and
    leaf `Term` nodes.
    """

    root: Expr


class _FailFastErrorListener(ErrorListener):
    """ANTLR error listener that converts parser/lexer errors into exceptions."""

    def syntaxError(  # noqa: N802 - ANTLR callback name
        self,
        _recognizer: object,
        _offending_symbol: object,
        line: int,
        column: int,
        msg: str,
        _error: Exception | None,
    ) -> None:
        raise QuerySyntaxError(f"Invalid query syntax at {line}:{column}: {msg}")


def _new_lexer(query: str) -> ScryfallQueryLexer:
    lexer = ScryfallQueryLexer(InputStream(query.lower()))
    lexer.removeErrorListeners()
    lexer.addErrorListener(_FailFastErrorListener())
    return lexer


def parse_query(query: str) -> ScryfallQueryParser.StartContext:
    """Parse `query` and return the ANTLR parse tree root."""
    lexer = _new_lexer(query)
    stream = CommonTokenStream(lexer)
    parser = ScryfallQueryParser(stream)
    parser.removeErrorListeners()
    parser.addErrorListener(_FailFastErrorListener())
    tree = parser.start()
    return tree


def parse_ast(query: str) -> QueryAst:
    """Parse `query` and return a normalized boolean-expression AST."""
    tree = parse_query(query)
    return QueryAst(root=_build_top_expr(tree.topExpr()))


def lex_query(query: str) -> list[LexToken]:
    """Lex `query` into raw ANTLR tokens, excluding EOF."""
    lexer = _new_lexer(query)
    stream = CommonTokenStream(lexer)
    stream.fill()

    symbols = ScryfallQueryParser.symbolicNames
    out: list[LexToken] = []
    for tok in stream.tokens:
        if tok.type == Token.EOF:
            continue
        token_type = symbols[tok.type] if tok.type < len(symbols) else str(tok.type)
        out.append(
            LexToken(
                type=token_type,
                raw=tok.text or "",
                index=tok.tokenIndex,
                start=tok.start,
                stop=tok.stop,
            )
        )
    return out


def tokenize_query(query: str) -> list[QueryToken]:
    """Parse and flatten all leaf terms into normalized query tokens."""
    ast = parse_ast(query)
    terms: list[Term] = []
    _collect_terms(ast.root, terms)
    return [_term_to_query_token(term) for term in terms]


def _collect_terms(expr: Expr, out: list[Term]) -> None:
    if isinstance(expr, Term):
        out.append(expr)
        return
    for child in expr.children:
        _collect_terms(child, out)


def _term_to_query_token(term: Term) -> QueryToken:
    if term.predicate is None:
        if term.kind == "exact_name":
            return ExactNameQueryToken(raw=term.raw, negated=term.negated)
        if term.kind == "quoted":
            return QuotedQueryToken(raw=term.raw, negated=term.negated)
        return WordQueryToken(raw=term.raw, negated=term.negated)

    raw_key = term.predicate.key
    token_cls = _KEYWORD_TOKEN_REGISTRY.get(raw_key, KeywordQueryToken)
    canonical_key = token_cls.keys[0] if token_cls.keys else raw_key

    return token_cls(
        raw=term.raw,
        negated=term.negated,
        token_key=canonical_key,
        token_operator=term.predicate.operator,
        token_value=term.predicate.value,
    )


def _build_top_expr(ctx: ScryfallQueryParser.TopExprContext) -> Expr:
    and_nodes = tuple(_build_top_and_expr(node) for node in ctx.topAndExpr())
    if len(and_nodes) == 1:
        return and_nodes[0]
    return OrExpr(children=and_nodes)


def _build_top_and_expr(ctx: ScryfallQueryParser.TopAndExprContext) -> Expr:
    factors = tuple(_build_top_factor(factor) for factor in ctx.topFactor())
    if len(factors) == 1:
        return factors[0]
    return AndExpr(children=factors)


def _build_top_factor(ctx: ScryfallQueryParser.TopFactorContext) -> Expr:
    if ctx.topGroup() is not None:
        return _build_paren_expr(ctx.topGroup().parenExpr())
    return _build_top_term(ctx.topTerm())


def _build_top_term(ctx: ScryfallQueryParser.TopTermContext) -> Term:
    negated = ctx.NEG() is not None
    return _term_from_raw(ctx.topAtom().getText(), negated=negated)


def _build_paren_expr(ctx: ScryfallQueryParser.ParenExprContext) -> Expr:
    and_nodes = tuple(_build_paren_and_expr(node) for node in ctx.parenAndExpr())
    if len(and_nodes) == 1:
        return and_nodes[0]
    return OrExpr(children=and_nodes)


def _build_paren_and_expr(ctx: ScryfallQueryParser.ParenAndExprContext) -> Expr:
    factors = tuple(_build_paren_factor(factor) for factor in ctx.parenFactor())
    if len(factors) == 1:
        return factors[0]
    return AndExpr(children=factors)


def _build_paren_factor(ctx: ScryfallQueryParser.ParenFactorContext) -> Expr:
    if ctx.parenGroup() is not None:
        return _build_paren_expr(ctx.parenGroup().parenExpr())
    return _build_paren_term(ctx.parenTerm())


def _build_paren_term(ctx: ScryfallQueryParser.ParenTermContext) -> Term:
    negated = ctx.NEG() is not None
    return _term_from_raw(ctx.parenAtom().getText(), negated=negated)


def _term_from_raw(raw: str, *, negated: bool) -> Term:
    if raw.startswith("!"):
        return Term(kind="exact_name", raw=raw, negated=negated)

    if raw.startswith('"') and raw.endswith('"'):
        return Term(kind="quoted", raw=raw, negated=negated)

    match = _OPERATOR_RE.match(raw)
    if match is not None:
        key, operator, value = match.groups()
        return Term(
            kind="keyword",
            raw=raw,
            negated=negated,
            predicate=Predicate(key=key, operator=operator, value=value),
        )

    return Term(kind="word", raw=raw, negated=negated)
