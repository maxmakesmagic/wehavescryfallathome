grammar ScryfallQuery;

//
// Parser rules
//
start: topExpr EOF;

// Top-level expression: allows all terms, including display/ordering controls.
topExpr: topAndExpr (OR topAndExpr)*;
topAndExpr: topFactor+;
topFactor: topGroup | topTerm;
topGroup: LPAREN parenExpr RPAREN;
topTerm: NEG? topAtom;

// Parenthesized expression: excludes display/ordering controls because those
// can't be included in parentheses.
parenExpr: parenAndExpr (OR parenAndExpr)*;
parenAndExpr: parenFactor+;
parenFactor: parenGroup | parenTerm;
parenGroup: LPAREN parenExpr RPAREN;
parenTerm: NEG? parenAtom;

topAtom
    : displayAtom
    | nonDisplayAtom
    ;

displayAtom
    : uniqueTerm
    | displayTerm
    | orderTerm
    | directionTerm
    | preferTerm
    ;

parenAtom: nonDisplayAtom;

nonDisplayAtom
    : exactName
    | includeTerm
    | isTerm
    | notTerm
    | formatTerm
    | bannedTerm
    | restrictedTerm
    | gameTerm
    | rarityTerm
    | mvTerm
    | genericTerm
    | quotedText
    | word
    ;

exactName: BANG (quotedText | word);

uniqueTerm: uniqueKey COLON uniqueValue;
uniqueKey: UNIQUE;
uniqueValue: CARDS | PRINTS | ART;

displayTerm: DISPLAY COLON displayValue;
displayValue: GRID | CHECKLIST | FULL | TEXT;

orderTerm: ORDER COLON orderValue;
orderValue
    : ARTIST
    | CMC
    | POWER
    | TOUGHNESS
    | SET
    | NAME
    | USD
    | TIX
    | EUR
    | RARITY
    | COLOR
    | RELEASED
    | SPOILED
    | EDHREC
    | PENNY
    | REVIEW
    ;

directionTerm: DIRECTION COLON directionValue;
directionValue: ASC | DESC;

preferTerm: PREFER COLON preferValue;
preferValue
    : OLDEST
    | NEWEST
    | USD_LOW
    | USD_HIGH
    | TIX_LOW
    | TIX_HIGH
    | EUR_LOW
    | EUR_HIGH
    | PROMO
    | DEFAULT
    | ATYPICAL
    | UNIVERSESBEYOND
    | UB
    | NOTUNIVERSESBEYOND
    | NOTUB
    ;

includeTerm: INCLUDE COLON EXTRAS;

isTerm: IS COLON isValue;
notTerm: NOT COLON isValue;
isValue
    : ADVENTURE
    | ALCHEMY
    | ARENA_LEAGUE
    | ARENAID
    | ARTIST
    | ARTISTMISPRINT
    | ARTSERIES
    | ATYPICAL
    | AUGMENTATION
    | BACK
    | BEAR
    | BEGINNERBOX
    | BOOSTER
    | BORDERLESS
    | BRAWLCOMMANDER
    | BRAWLER
    | BUYABOX
    | CARDMARKET
    | CI
    | CLASS
    | COLORSHIFTED
    | COMMANDER
    | COMPANION
    | CONTENTWARNING
    | CONVENTION
    | COVERED
    | DATESTAMPED
    | DEFAULT
    | DFC
    | DIGITAL
    | DOUBLESIDED
    | DUELCOMMANDER
    | ENGLISHART
    | ETB
    | ETCH
    | ETCHED
    | EXTENDED
    | EXTRA
    | FBB
    | FF
    | FF1
    | FF10
    | FF11
    | FF12
    | FF13
    | FF14
    | FF15
    | FF16
    | FF2
    | FF3
    | FF4
    | FF5
    | FF6
    | FF7
    | FF8
    | FF9
    | FFI
    | FFII
    | FFIII
    | FFIV
    | FFIX
    | FFV
    | FFVI
    | FFVII
    | FFVIII
    | FFX
    | FFXI
    | FFXII
    | FFXIII
    | FFXIV
    | FFXV
    | FFXVI
    | FINALFANTASY
    | FIRSTPRINT
    | FLAVOR
    | FLAVORNAME
    | FLIP
    | FNM
    | FOIL
    | FRENCHVANILLA
    | FULLART
    | FUNNY
    | FUTURE
    | FWB
    | GAMECHANGER
    | GAMEDAY
    | GIFTBOX
    | GLOSSY
    | HIRES
    | HISTORIC
    | HYBRID
    | ILLUSTRATION
    | INDICATOR
    | INSTORE
    | INTRO_PACK
    | INTROPACK
    | INVITATIONAL
    | JUDGE_GIFT
    | LEAGUE
    | LEVELER
    | LIGHTS
    | LOCALIZEDNAME
    | MANLAND
    | MASTERPIECE
    | MDFC
    | MEDIA_INSERT
    | MELD
    | MELDPART
    | MELDRESULT
    | MODAL
    | MODERN
    | MTGOID
    | MULTIVERSE
    | NEW
    | NEWINPAUPER
    | NONFOIL
    | NOTUNIVERSESBEYOND
    | OATHBREAKER
    | OLD
    | ONLYPRINT
    | OUTLAW
    | OVERSIZED
    | PAPERART
    | PARTNER
    | PARTY
    | PERMANENT
    | PHYREXIA
    | PHYREXIAN
    | PLANAR
    | PLANESWALKER_DECK
    | PLANESWALKERDECK
    | PLAYER_REWARDS
    | PRERELEASE
    | PRINTEDTEXT
    | PROMO
    | REBALANCED
    | RELATED
    | RELEASE
    | REPRINT
    | RESERVED
    | REVERSIBLE
    | SCRYFALLPREVIEW
    | SET_PROMO
    | SHOWCASE
    | SPELL
    | SPELLBOOK
    | SPIKEY
    | SPLIT
    | SPLITMANA
    | SPOTLIGHT
    | STAMP
    | STAMPED
    | STARTERCOLLECTION
    | STARTERDECK
    | STORY
    | TCGPLAYER
    | TDFC
    | TEXTLESS
    | TOKEN
    | TOMBSTONE
    | TRANSFORM
    | TRANSLUCENT
    | UNIQUE
    | UNIVERSESBEYOND
    | VANILLA
    | VARIATION
    | WATERMARK
    ;

formatTerm: (F | FORMAT) COLON formatValue;
bannedTerm: BANNED COLON formatValue;
restrictedTerm: RESTRICTED COLON formatValue;
formatValue
    : STANDARD
    | FUTURE
    | HISTORIC
    | TIMELESS
    | GLADIATOR
    | PIONEER
    | MODERN
    | LEGACY
    | PAUPER
    | VINTAGE
    | PENNY
    | COMMANDER
    | OATHBREAKER
    | STANDARDBRAWL
    | BRAWL
    | ALCHEMY
    | PAUPERCOMMANDER
    | DUEL
    | OLDSCHOOL
    | PREMODERN
    | PREDH
    ;

gameTerm: GAME COLON (PAPER | MTGO | ARENA);
gameValueToken: PAPER | MTGO | ARENA;

rarityTerm: (R | RARITY | IN) compOp rarityValue;
rarityValue
    : COMMON
    | UNCOMMON
    | RARE
    | SPECIAL
    | MYTHIC
    | BONUS
    | C
    | U
    | R
    | M
    | B
    ;

mvTerm: (MV | MANAVALUE) compOp (EVEN | ODD | NUMBER);

// Generic keyword form: <key><op><value>
// Example: t:elf, o:"draw", pow>tou, date>=2020-01-01
genericTerm: genericKey compOp genericValue;

genericKey
    : A
    | ARTIST
    | ARTISTS
    | ART
    | ATAG
    | ARTTAG
    | B
    | BLOCK
    | BORDER
    | C
    | COLOR
    | CN
    | NUMBER_KEY
    | CUBE
    | DATE
    | DEVOTION
    | E
    | EDITION
    | FO
    | FULLORACLE
    | FT
    | FLAVOR
    | FUNCTION
    | OTAG
    | ORACLETAG
    | ID
    | IDENTITY
    | ILLUSTRATIONS
    | IN
    | KEYWORD
    | KW
    | LANG
    | LANGUAGE
    | LOY
    | LOYALTY
    | M
    | MANA
    | N
    | NAME
    | NEW
    | O
    | ORACLE
    | PAPERPRINTS
    | PAPERSETS
    | POW
    | POWER
    | PT
    | POWTOU
    | PRINTS
    | PRODUCES
    | R
    | RARITY
    | S
    | SET
    | SETS
    | STAMP
    | ST
    | GAME
    | T
    | TYPE
    | TOU
    | TOUGHNESS
    | USD
    | EUR
    | TIX
    | CHEAPEST
    | WM
    | WATERMARK
    | YEAR
    ;

// Comparison/operator tokens accepted between key and value.
compOp: COLON | NEQ | GTE | LTE | EQ | GT | LT;

// Values accepted for generic terms. We include both lexical forms (word,
// quoted text, regex) and many reserved-token enums so cases like c:w and
// pow>tou parse even though `w`/`tou` are reserved elsewhere.
genericValue
    : regex
    | quotedText
    | bareValue
    | word
    | genericKey
    | rarityValue
    | formatValue
    | isValue
    | orderValue
    | preferValue
    | directionValue
    | uniqueValue
    | displayValue
    | gameValueToken
    ;
quotedText: QUOTED_TEXT;
regex: REGEX;
word: WORD;
bareValue: BARE_VALUE;

//
// Lexer rules (fixed symbols and keywords)
//
LPAREN: '(';
RPAREN: ')';
NEG: '-';
BANG: '!';
COLON: ':';
NEQ: '!=';
GTE: '>=';
LTE: '<=';
EQ: '=';
GT: '>';
LT: '<';

OR: 'or';

UNIQUE: 'unique';
DISPLAY: 'display';
ORDER: 'order';
DIRECTION: 'direction';
PREFER: 'prefer';
INCLUDE: 'include';
IS: 'is';
NOT: 'not';
F: 'f';
FORMAT: 'format';
BANNED: 'banned';
RESTRICTED: 'restricted';
GAME: 'game';
RARITY: 'rarity';
MV: 'mv';
MANAVALUE: 'manavalue';

CARDS: 'cards';
PRINTS: 'prints';
GRID: 'grid';
CHECKLIST: 'checklist';
FULL: 'full';
TEXT: 'text';
ASC: 'asc';
DESC: 'desc';
EXTRAS: 'extras';

ARTIST: 'artist';
ARTISTS: 'artists';
CMC: 'cmc';
POWER: 'power';
TOUGHNESS: 'toughness';
SET: 'set';
NAME: 'name';
USD: 'usd';
TIX: 'tix';
EUR: 'eur';
COLOR: 'color';
RELEASED: 'released';
SPOILED: 'spoiled';
EDHREC: 'edhrec';
PENNY: 'penny';
REVIEW: 'review';

OLDEST: 'oldest';
NEWEST: 'newest';
USD_LOW: 'usd-low';
USD_HIGH: 'usd-high';
TIX_LOW: 'tix-low';
TIX_HIGH: 'tix-high';
EUR_LOW: 'eur-low';
EUR_HIGH: 'eur-high';
PROMO: 'promo';
DEFAULT: 'default';
ATYPICAL: 'atypical';
UNIVERSESBEYOND: 'universesbeyond';
UB: 'ub';
NOTUNIVERSESBEYOND: 'notuniversesbeyond';
NOTUB: 'notub';

INDICATOR: 'indicator';
HYBRID: 'hybrid';
PHYREXIAN: 'phyrexian';
SPLIT: 'split';
FLIP: 'flip';
TRANSFORM: 'transform';
TDFC: 'tdfc';
MELD: 'meld';
MELDPART: 'meldpart';
MELDRESULT: 'meldresult';
LEVELER: 'leveler';
DFC: 'dfc';
MDFC: 'mdfc';
SPELL: 'spell';
PERMANENT: 'permanent';
HISTORIC: 'historic';
PARTY: 'party';
OUTLAW: 'outlaw';
MODAL: 'modal';
VANILLA: 'vanilla';
FRENCHVANILLA: 'frenchvanilla';
BEAR: 'bear';
MANLAND: 'manland';
FUNNY: 'funny';
BOOSTER: 'booster';
PLANESWALKER_DECK: 'planeswalker_deck';
LEAGUE: 'league';
BUYABOX: 'buyabox';
GIFTBOX: 'giftbox';
INTRO_PACK: 'intro_pack';
GAMEDAY: 'gameday';
PRERELEASE: 'prerelease';
RELEASE: 'release';
FNM: 'fnm';
JUDGE_GIFT: 'judge_gift';
ARENA_LEAGUE: 'arena_league';
PLAYER_REWARDS: 'player_rewards';
MEDIA_INSERT: 'media_insert';
INSTORE: 'instore';
CONVENTION: 'convention';
SET_PROMO: 'set_promo';
COMMANDER: 'commander';
BRAWLER: 'brawler';
COMPANION: 'companion';
DUELCOMMANDER: 'duelcommander';
OATHBREAKER: 'oathbreaker';
PARTNER: 'partner';
GAMECHANGER: 'gamechanger';
RESERVED: 'reserved';
NEW: 'new';
OLD: 'old';
NONFOIL: 'nonfoil';
FOIL: 'foil';
ETCHED: 'etched';
GLOSSY: 'glossy';
HIRES: 'hires';
DIGITAL: 'digital';
ALCHEMY: 'alchemy';
REBALANCED: 'rebalanced';
SPOTLIGHT: 'spotlight';
SCRYFALLPREVIEW: 'scryfallpreview';
REPRINT: 'reprint';
FF7: 'ff7';
FF: 'ff';
NEWINPAUPER: 'newinpauper';
DATESTAMPED: 'datestamped';
ADVENTURE: 'adventure';
ARENAID: 'arenaid';
ARTISTMISPRINT: 'artistmisprint';
ARTSERIES: 'artseries';
AUGMENTATION: 'augmentation';
BACK: 'back';
BEGINNERBOX: 'beginnerbox';
BORDERLESS: 'borderless';
BRAWLCOMMANDER: 'brawlcommander';
CARDMARKET: 'cardmarket';
CI: 'ci';
CLASS: 'class';
COLORSHIFTED: 'colorshifted';
CONTENTWARNING: 'contentwarning';
COVERED: 'covered';
DOUBLESIDED: 'doublesided';
ENGLISHART: 'englishart';
ETB: 'etb';
ETCH: 'etch';
EXTENDED: 'extended';
EXTRA: 'extra';
FBB: 'fbb';
FIRSTPRINT: 'firstprint';
FLAVORNAME: 'flavorname';
FULLART: 'fullart';
FWB: 'fwb';
ILLUSTRATION: 'illustration';
FF1: 'ff1';
FF10: 'ff10';
FF11: 'ff11';
FF12: 'ff12';
FF13: 'ff13';
FF14: 'ff14';
FF15: 'ff15';
FF16: 'ff16';
FF2: 'ff2';
FF3: 'ff3';
FF4: 'ff4';
FF5: 'ff5';
FF6: 'ff6';
INTROPACK: 'intropack';
FF8: 'ff8';
FF9: 'ff9';
FFI: 'ffi';
FFII: 'ffii';
FFIII: 'ffiii';
FFIV: 'ffiv';
FFIX: 'ffix';
FFV: 'ffv';
FFVI: 'ffvi';
FFVII: 'ffvii';
FFVIII: 'ffviii';
FFX: 'ffx';
FFXI: 'ffxi';
FFXII: 'ffxii';
FFXIII: 'ffxiii';
FFXIV: 'ffxiv';
FFXV: 'ffxv';
FFXVI: 'ffxvi';
FINALFANTASY: 'finalfantasy';
INVITATIONAL: 'invitational';
LIGHTS: 'lights';
LOCALIZEDNAME: 'localizedname';
MASTERPIECE: 'masterpiece';
MTGOID: 'mtgoid';
MULTIVERSE: 'multiverse';
ONLYPRINT: 'onlyprint';
OVERSIZED: 'oversized';
PAPERART: 'paperart';
PHYREXIA: 'phyrexia';
PLANAR: 'planar';
PLANESWALKERDECK: 'planeswalkerdeck';
PRINTEDTEXT: 'printedtext';
RELATED: 'related';
REVERSIBLE: 'reversible';
SHOWCASE: 'showcase';
SPELLBOOK: 'spellbook';
SPIKEY: 'spikey';
SPLITMANA: 'splitmana';
STAMPED: 'stamped';
STARTERCOLLECTION: 'startercollection';
STARTERDECK: 'starterdeck';
STORY: 'story';
TCGPLAYER: 'tcgplayer';
TEXTLESS: 'textless';
TOKEN: 'token';
TOMBSTONE: 'tombstone';
TRANSLUCENT: 'translucent';
VARIATION: 'variation';

STANDARD: 'standard';
FUTURE: 'future';
TIMELESS: 'timeless';
GLADIATOR: 'gladiator';
PIONEER: 'pioneer';
MODERN: 'modern';
LEGACY: 'legacy';
PAUPER: 'pauper';
VINTAGE: 'vintage';
STANDARDBRAWL: 'standardbrawl';
BRAWL: 'brawl';
PAUPERCOMMANDER: 'paupercommander';
DUEL: 'duel';
OLDSCHOOL: 'oldschool';
PREMODERN: 'premodern';
PREDH: 'predh';

PAPER: 'paper';
MTGO: 'mtgo';
ARENA: 'arena';

COMMON: 'common';
UNCOMMON: 'uncommon';
RARE: 'rare';
SPECIAL: 'special';
MYTHIC: 'mythic';
BONUS: 'bonus';

EVEN: 'even';
ODD: 'odd';

A: 'a';
ART: 'art';
ATAG: 'atag';
ARTTAG: 'arttag';
B: 'b';
BLOCK: 'block';
BORDER: 'border';
C: 'c';
CN: 'cn';
NUMBER_KEY: 'number';
CUBE: 'cube';
DATE: 'date';
DEVOTION: 'devotion';
E: 'e';
EDITION: 'edition';
FO: 'fo';
FULLORACLE: 'fulloracle';
FT: 'ft';
FLAVOR: 'flavor';
FUNCTION: 'function';
OTAG: 'otag';
ORACLETAG: 'oracletag';
ID: 'id';
IDENTITY: 'identity';
ILLUSTRATIONS: 'illustrations';
IN: 'in';
KEYWORD: 'keyword';
KW: 'kw';
LANG: 'lang';
LANGUAGE: 'language';
LOY: 'loy';
LOYALTY: 'loyalty';
M: 'm';
MANA: 'mana';
N: 'n';
O: 'o';
ORACLE: 'oracle';
PAPERPRINTS: 'paperprints';
PAPERSETS: 'papersets';
POW: 'pow';
PT: 'pt';
POWTOU: 'powtou';
PRODUCES: 'produces';
R: 'r';
U: 'u';
S: 's';
SETS: 'sets';
STAMP: 'stamp';
ST: 'st';
T: 't';
TYPE: 'type';
TOU: 'tou';
CHEAPEST: 'cheapest';
WM: 'wm';
WATERMARK: 'watermark';
YEAR: 'year';

//
// Primitive lexical forms
//
// NUMBER supports integers and decimal numeric literals.
NUMBER: [0-9]+ ('.' [0-9]+)?;
// QUOTED_TEXT allows escaped characters in double-quoted strings.
QUOTED_TEXT: '"' (~["\\\r\n] | '\\' .)* '"';
// REGEX supports slash-delimited expressions with escaped slash support.
REGEX: '/' (~[/\\\r\n] | '\\' .)+ '/';
// WORD is an unquoted atom token used for names/terms.
WORD: ~[ \t\r\n()"!:/<>=-] ~[ \t\r\n()"!:/<>=-]*;
// BARE_VALUE is like WORD but used in value positions.
BARE_VALUE: ~[ \t\r\n()"!:/<>=-] ~[ \t\r\n()":!<>=-]*;

// Whitespace is skipped globally.
WS: [ \t\r\n]+ -> skip;
