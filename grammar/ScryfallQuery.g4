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
    | inTerm
    | rarityTerm
    | powerTerm
    | toughnessTerm
    | mvTerm
    | manaTerm
    | colorTerm
    | borderTerm
    | frameTerm
    | languageTerm
    | stampTerm
    | cnTerm
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
    : ABNORMAL
    | ADVENTURE
    | ALCHEMY
    | ALTERNATE
    | AMPERSAND
    | ARCHENEMY
    | ARCHIVAL
    | ARENA_LEAGUE
    | ARENAID
    | ARENALEAGUE
    | ARTIST
    | ARTISTMISPRINT
    | ARTSERIES
    | ATYPICAL
    | AUGMENTATION
    | BACK
    | BASELINE
    | BATTLELAND
    | BEAR
    | BEGINNERBOX
    | BELZENLOK
    | BICYCLELAND
    | BIKELAND
    | BOB
    | BONDLAND
    | BOOSTER
    | BOOSTERFUN
    | BORDERLESS
    | BOUNCELAND
    | BOX
    | BOXTOPPER
    | BRAWLCOMMANDER
    | BRAWLDECK
    | BRAWLER
    | BUNDLE
    | BURSTFOIL
    | BUYABOX
    | CANLAND
    | CANOPYLAND
    | CARDMARKET
    | CHECKLAND
    | CHOCOBOTRACKFOIL
    | CHRIMBY
    | CI
    | CLASS
    | COLORSHIFTED
    | COMMANDER
    | COMMANDERPARTY
    | COMMANDERPROMO
    | COMPANION
    | CONCEPT
    | CONFETTIFOIL
    | CONJUREONLY
    | CONTENTWARNING
    | CONVENTION
    | CORE
    | COSMICFOIL
    | COVERED
    | CREATURELAND
    | CUTE
    | CYCLELAND
    | DATESTAMPED
    | DEFAULT
    | DEN
    | DFC
    | DIGITAL
    | DOUBLEEXPOSURE
    | DOUBLERAINBOW
    | DOUBLESIDED
    | DRACULASERIES
    | DRAFTINNOVATION
    | DRAFTWEEKEND
    | DUAL
    | DUELCOMMANDER
    | DUELDECK
    | DUELS
    | ENGLISHART
    | ESCAPED
    | ETB
    | ETCH
    | ETCHED
    | EVENT
    | EXPANSION
    | EXTENDED
    | EXTRA
    | FASTLAND
    | FBB
    | FETCHLAND
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
    | FILTERLAND
    | FINALFANTASY
    | FINALFANTASY1
    | FINALFANTASY10
    | FINALFANTASY11
    | FINALFANTASY12
    | FINALFANTASY13
    | FINALFANTASY14
    | FINALFANTASY15
    | FINALFANTASY16
    | FINALFANTASY2
    | FINALFANTASY3
    | FINALFANTASY4
    | FINALFANTASY5
    | FINALFANTASY6
    | FINALFANTASY7
    | FINALFANTASY8
    | FINALFANTASY9
    | FINALFANTASYI
    | FINALFANTASYII
    | FINALFANTASYIII
    | FINALFANTASYIV
    | FINALFANTASYIX
    | FINALFANTASYV
    | FINALFANTASYVI
    | FINALFANTASYVII
    | FINALFANTASYVIII
    | FINALFANTASYX
    | FINALFANTASYXI
    | FINALFANTASYXII
    | FINALFANTASYXIII
    | FINALFANTASYXIV
    | FINALFANTASYXV
    | FINALFANTASYXVI
    | FINKEL
    | FIRSTPLACEFOIL
    | FIRSTPRINT
    | FIRSTPRINTING
    | FIXED
    | FLAVOR
    | FLAVORNAME
    | FLIP
    | FMB1
    | FNM
    | FOIL
    | FRAMEODDITY
    | FRENCHVANILLA
    | FROMTHEVAULT
    | FULLART
    | FULLTEXT
    | FUNNY
    | FUTURE
    | FUTURESHIFTED
    | FWB
    | GAINLAND
    | GALAXYFOIL
    | GAMECHANGER
    | GAMEDAY
    | GARY
    | GATEWAY
    | GIFTBOX
    | GILDED
    | GLOSSY
    | GODZILLASERIES
    | HALO
    | HALOFOIL
    | HEADLINER
    | HIRES
    | HISTORIC
    | HORIZ
    | HYBRID
    | ILLUSTRATION
    | IMAGEQA
    | IMAGINE
    | INDICATOR
    | INSTORE
    | INTRO_PACK
    | INTROPACK
    | INVITATIONAL
    | JPWALKER
    | JUDGE_GIFT
    | JUDGEGIFT
    | JUMPSTART
    | KAROO
    | LEAGUE
    | LEVELER
    | LIGHTS
    | LISTWHITE
    | LOCALIZEDIMAGE
    | LOCALIZEDNAME
    | LOSTLEGENDS
    | MAGICSPOTLIGHT
    | MANLAND
    | MASTERPIECE
    | MASTERS
    | MB1
    | MB2
    | MDFC
    | MEDIA_INSERT
    | MEDIAINSERT
    | MELD
    | MELDPART
    | MELDRESULT
    | MEMORABILIA
    | METAL
    | MISPRINT
    | MODAL
    | MODERN
    | MOM
    | MOONLITLAND
    | MTGOID
    | MULTIPLAYER
    | MULTIVERSE
    | NEONINK
    | NEW
    | NEWINPAUPER
    | NONDEFAULT
    | NONFOIL
    | NONTRADITIONAL
    | NORMAL
    | NOTUNIVERSESBEYOND
    | OATHBREAKER
    | ODDFRAME
    | OILSLICK
    | OLD
    | ONLYPRINT
    | OPENHOUSE
    | OUTLAW
    | OVERSIZED
    | PAGL
    | PAINLAND
    | PAPERART
    | PARTNER
    | PARTY
    | PATHWAY
    | PAUPERCOMMANDER
    | PCTB
    | PERMANENT
    | PHED
    | PHYREXIA
    | PHYREXIAN
    | PIKULA
    | PLACEHOLDERIMAGE
    | PLANAR
    | PLANECHASE
    | PLANESWALKER_DECK
    | PLANESWALKERDECK
    | PLASTIC
    | PLAYER_REWARDS
    | PLAYERREWARDS
    | PLAYPROMO
    | PLAYTEST
    | PORTAL
    | PORTRAIT
    | POSTER
    | PREMIERESHOP
    | PREMIUMDECK
    | PRERELEASE
    | PRINTEDTEXT
    | PROMO
    | PROMOPACK
    | RAINBOWFOIL
    | RAISEDFOIL
    | REBALANCED
    | RELATED
    | RELEASE
    | REPRINT
    | RESALE
    | RESERVED
    | REVERSIBLE
    | RIPPLEFOIL
    | SCANNEEDED
    | SCENE
    | SCHINESEALTART
    | SCROLL
    | SCRYFALLPREVIEW
    | SCRYLAND
    | SERIALIZED
    | SET_PROMO
    | SETEXTENSION
    | SETPROMO
    | SHADOWLAND
    | SHOCKLAND
    | SHOWCASE
    | SINGULARITYFOIL
    | SLDBONUS
    | SLOWLAND
    | SNARL
    | SOURCEMATERIAL
    | SPELL
    | SPELLBOOK
    | SPIKEY
    | SPLIT
    | SPLITMANA
    | SPOTLIGHT
    | STAMP
    | STAMPED
    | STARTER
    | STARTERCOLLECTION
    | STARTERDECK
    | STEPANDCOMPLEAT
    | STORAGELAND
    | STORECHAMPIONSHIP
    | STORY
    | SURVEILLAND
    | TANGOLAND
    | TCGPLAYER
    | TDFC
    | TEXTLESS
    | TEXTURED
    | THEMEPACK
    | THICK
    | TIMESHIFTED
    | TOKEN
    | TOMBSTONE
    | TOURNEY
    | TRADITIONAL
    | TRANSFORM
    | TRANSLUCENT
    | TREASURECHEST
    | TRICYCLELAND
    | TRIKELAND
    | TRILAND
    | TRIOME
    | TRON
    | TYPICAL
    | UB
    | UNIQUE
    | UNIVERSESBEYOND
    | UNSET
    | UPSIDEDOWN
    | UPSIDEDOWNBACK
    | USELESS
    | VANGUARD
    | VANILLA
    | VARIATION
    | VAULT
    | VERT
    | WANTED
    | WATERMARK
    | WIZARDSPLAYNETWORK
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
inTerm: IN COLON gameValueToken;

colorTerm: (C | COLOR) compOp colorValue;
colorValue
    : NUMBER
    // U/B/R are explicit here because those literals are tokenized as
    // dedicated lexer tokens (`U`, `B`, `R`) before `COLOR_SET` is considered.
    | C
    | M
    | U
    | B
    | R
    | COLOR_SET
    | WHITE
    | BLUE
    | BLACK
    | RED
    | GREEN
    | COLORLESS
    | MULTICOLOR
    // `ub` is tokenized as dedicated `UB` (rule-order tie with COLOR_SET),
    // so we must allow `UB` explicitly in this parser rule.
    | UB
    | AZORIUS
    | DIMIR
    | RAKDOS
    | GRUUL
    | SELESNYA
    | ORZHOV
    | IZZET
    | GOLGARI
    | BOROS
    | SIMIC
    | BANT
    | ESPER
    | GRIXIS
    | JUND
    | NAYA
    | ABZAN
    | JESKAI
    | SULTAI
    | MARDU
    | TEMUR
    | QUANDRIX
    | PRISMARI
    | WITHERBLOOM
    | LOREHOLD
    | SILVERQUILL
    | CHAOS
    | AGGRESSION
    | ALTRUISM
    | GROWTH
    | ARTIFICE
    ;

borderTerm: BORDER COLON borderValue;
borderValue
    : BLACK
    | WHITE
    | SILVER
    | BORDERLESS
    ;

frameTerm: FRAME COLON frameValue;
frameValue
    : FRAME_1993
    | FRAME_1997
    | FRAME_2003
    | FRAME_2015
    | FUTURE
    | LEGENDARY
    | COLORSHIFTED
    | TOMBSTONE
    | ENCHANTMENT
    ;

languageTerm: (LANG | LANGUAGE) COLON languageValue;
languageValue
    : ANY
    | EN
    | ES
    | FR
    | DE
    | IT
    | PT
    | JA
    | KO
    | RU
    | ZHS
    | ZHT
    | HE
    | LA
    | GRC
    | AR
    | SA
    | PH
    | QYA
    | ENGLISH
    | SPANISH
    | FRENCH
    | GERMAN
    | ITALIAN
    | PORTUGUESE
    | JAPANESE
    | KOREAN
    | RUSSIAN
    | SIMPLIFIED_CHINESE
    | TRADITIONAL_CHINESE
    | HEBREW
    | LATIN
    | ANCIENT_GREEK
    | ARABIC
    | SANSKRIT
    | PHYREXIAN
    | QUENYA
    ;

stampTerm: STAMP COLON stampValue;
stampValue
    : OVAL
    | ACORN
    | TRIANGLE
    | ARENA
    | CIRCLE
    | HEART
    ;

rarityTerm: (R | RARITY) compOp rarityValue;
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

powerTerm: (POW | POWER) compOp powerValue;
powerValue
    : NUMBER
    | TOU
    | TOUGHNESS
    ;

toughnessTerm: (TOU | TOUGHNESS) compOp toughnessValue;
toughnessValue
    : NUMBER
    | POW
    | POWER
    ;

mvTerm: (MV | MANAVALUE) compOp (EVEN | ODD | NUMBER);

manaTerm: (M | MANA) compOp manaValue;
manaValue: manaValuePart+;
manaValuePart
    : MANA_BRACED_SYMBOL
    | MANA_UNBRACED_SYMBOL
    | COLOR_SET
    | U
    | B
    | R
    ;

cnTerm: (CN | NUMBER_KEY) compOp cnValue;
cnValue
    : NUMBER
    | COLLECTOR_NUMBER
    ;

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
    | KEYWORD
    | KW
    | LOY
    | LOYALTY
    | N
    | NAME
    | NEW
    | O
    | ORACLE
    | PAPERPRINTS
    | PAPERSETS
    | PT
    | POWTOU
    | PRINTS
    | PRODUCES
    | S
    | SET
    | SETS
    | ST
    | T
    | TYPE
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
    | languageValue
    ;
quotedText: QUOTED_TEXT;
regex: REGEX;
word: WORD | COLOR_SET;
bareValue: BARE_VALUE | COLOR_SET;

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
ANY: 'any';

ENGLISH: 'english';
SPANISH: 'spanish';
FRENCH: 'french';
GERMAN: 'german';
ITALIAN: 'italian';
PORTUGUESE: 'portuguese';
JAPANESE: 'japanese';
KOREAN: 'korean';
RUSSIAN: 'russian';
SIMPLIFIED_CHINESE: 'simplifiedchinese';
TRADITIONAL_CHINESE: 'traditionalchinese';
HEBREW: 'hebrew';
LATIN: 'latin';
ANCIENT_GREEK: 'ancientgreek';
ARABIC: 'arabic';
SANSKRIT: 'sanskrit';
QUENYA: 'quenya';

EN: 'en';
ES: 'es';
FR: 'fr';
DE: 'de';
IT: 'it';
JA: 'ja';
KO: 'ko';
RU: 'ru';
ZHS: 'zhs';
ZHT: 'zht';
HE: 'he';
LA: 'la';
GRC: 'grc';
AR: 'ar';
SA: 'sa';
PH: 'ph';
QYA: 'qya';

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
WHITE: 'white';
BLUE: 'blue';
BLACK: 'black';
RED: 'red';
GREEN: 'green';
SILVER: 'silver';
COLORLESS: 'colorless';
MULTICOLOR: 'multicolor';
AZORIUS: 'azorius';
DIMIR: 'dimir';
RAKDOS: 'rakdos';
GRUUL: 'gruul';
SELESNYA: 'selesnya';
ORZHOV: 'orzhov';
IZZET: 'izzet';
GOLGARI: 'golgari';
BOROS: 'boros';
SIMIC: 'simic';
BANT: 'bant';
ESPER: 'esper';
GRIXIS: 'grixis';
JUND: 'jund';
NAYA: 'naya';
ABZAN: 'abzan';
JESKAI: 'jeskai';
SULTAI: 'sultai';
MARDU: 'mardu';
TEMUR: 'temur';
QUANDRIX: 'quandrix';
PRISMARI: 'prismari';
WITHERBLOOM: 'witherbloom';
LOREHOLD: 'lorehold';
SILVERQUILL: 'silverquill';
CHAOS: 'chaos';
AGGRESSION: 'aggression';
ALTRUISM: 'altruism';
GROWTH: 'growth';
ARTIFICE: 'artifice';
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
ALTERNATE: 'alternate';
AMPERSAND: 'ampersand';
ARCHENEMY: 'archenemy';
ARCHIVAL: 'archival';
ARENALEAGUE: 'arenaleague';
BOB: 'bob';
BOOSTERFUN: 'boosterfun';
BOX: 'box';
BOXTOPPER: 'boxtopper';
BRAWLDECK: 'brawldeck';
BUNDLE: 'bundle';
BURSTFOIL: 'burstfoil';
CHOCOBOTRACKFOIL: 'chocobotrackfoil';
CHRIMBY: 'chrimby';
COMMANDERPARTY: 'commanderparty';
COMMANDERPROMO: 'commanderpromo';
CONCEPT: 'concept';
CONFETTIFOIL: 'confettifoil';
CONJUREONLY: 'conjureonly';
COSMICFOIL: 'cosmicfoil';
CUTE: 'cute';
DEN: 'den';
DOUBLEEXPOSURE: 'doubleexposure';
DOUBLERAINBOW: 'doublerainbow';
DRACULASERIES: 'draculaseries';
DRAFTINNOVATION: 'draftinnovation';
DRAFTWEEKEND: 'draftweekend';
DUELDECK: 'dueldeck';
DUELS: 'duels';
ESCAPED: 'escaped';
EVENT: 'event';
FINKEL: 'finkel';
FIRSTPLACEFOIL: 'firstplacefoil';
FIXED: 'fixed';
FRAMEODDITY: 'frameoddity';
FROMTHEVAULT: 'fromthevault';
FULLTEXT: 'fulltext';
FUTURESHIFTED: 'futureshifted';
GALAXYFOIL: 'galaxyfoil';
GARY: 'gary';
GATEWAY: 'gateway';
GILDED: 'gilded';
GODZILLASERIES: 'godzillaseries';
HALOFOIL: 'halofoil';
HEADLINER: 'headliner';
HORIZ: 'horiz';
IMAGEQA: 'imageqa';
IMAGINE: 'imagine';
JPWALKER: 'jpwalker';
JUDGEGIFT: 'judgegift';
JUMPSTART: 'jumpstart';
LISTWHITE: 'listwhite';
LOCALIZEDIMAGE: 'localizedimage';
LOSTLEGENDS: 'lostlegends';
MAGICSPOTLIGHT: 'magicspotlight';
MASTERS: 'masters';
MB2: 'mb2';
MEDIAINSERT: 'mediainsert';
MEMORABILIA: 'memorabilia';
METAL: 'metal';
MISPRINT: 'misprint';
MOM: 'mom';
MOONLITLAND: 'moonlitland';
MULTIPLAYER: 'multiplayer';
NEONINK: 'neonink';
OILSLICK: 'oilslick';
OPENHOUSE: 'openhouse';
PIKULA: 'pikula';
PLANECHASE: 'planechase';
PLASTIC: 'plastic';
PLAYERREWARDS: 'playerrewards';
PLAYPROMO: 'playpromo';
PORTAL: 'portal';
PORTRAIT: 'portrait';
POSTER: 'poster';
PREMIERESHOP: 'premiereshop';
PREMIUMDECK: 'premiumdeck';
PROMOPACK: 'promopack';
RAINBOWFOIL: 'rainbowfoil';
RAISEDFOIL: 'raisedfoil';
RESALE: 'resale';
RIPPLEFOIL: 'ripplefoil';
SCANNEEDED: 'scanneeded';
SCENE: 'scene';
SCHINESEALTART: 'schinesealtart';
SCROLL: 'scroll';
SERIALIZED: 'serialized';
SETPROMO: 'setpromo';
SINGULARITYFOIL: 'singularityfoil';
SLDBONUS: 'sldbonus';
SOURCEMATERIAL: 'sourcematerial';
STARTER: 'starter';
STEPANDCOMPLEAT: 'stepandcompleat';
STORECHAMPIONSHIP: 'storechampionship';
TEXTURED: 'textured';
THEMEPACK: 'themepack';
THICK: 'thick';
TIMESHIFTED: 'timeshifted';
TOURNEY: 'tourney';
TREASURECHEST: 'treasurechest';
TRON: 'tron';
UNSET: 'unset';
USELESS: 'useless';
VANGUARD: 'vanguard';
VAULT: 'vault';
VERT: 'vert';
WANTED: 'wanted';
WIZARDSPLAYNETWORK: 'wizardsplaynetwork';
ABNORMAL: 'abnormal';
BASELINE: 'baseline';
BATTLELAND: 'battleland';
BELZENLOK: 'belzenlok';
BICYCLELAND: 'bicycleland';
BIKELAND: 'bikeland';
BONDLAND: 'bondland';
BOUNCELAND: 'bounceland';
CANLAND: 'canland';
CANOPYLAND: 'canopyland';
CHECKLAND: 'checkland';
CORE: 'core';
CREATURELAND: 'creatureland';
CYCLELAND: 'cycleland';
DUAL: 'dual';
EXPANSION: 'expansion';
FASTLAND: 'fastland';
FETCHLAND: 'fetchland';
FILTERLAND: 'filterland';
FINALFANTASY1: 'finalfantasy1';
FINALFANTASY10: 'finalfantasy10';
FINALFANTASY11: 'finalfantasy11';
FINALFANTASY12: 'finalfantasy12';
FINALFANTASY13: 'finalfantasy13';
FINALFANTASY14: 'finalfantasy14';
FINALFANTASY15: 'finalfantasy15';
FINALFANTASY16: 'finalfantasy16';
FINALFANTASY2: 'finalfantasy2';
FINALFANTASY3: 'finalfantasy3';
FINALFANTASY4: 'finalfantasy4';
FINALFANTASY5: 'finalfantasy5';
FINALFANTASY6: 'finalfantasy6';
FINALFANTASY7: 'finalfantasy7';
FINALFANTASY8: 'finalfantasy8';
FINALFANTASY9: 'finalfantasy9';
FINALFANTASYI: 'finalfantasyi';
FINALFANTASYII: 'finalfantasyii';
FINALFANTASYIII: 'finalfantasyiii';
FINALFANTASYIV: 'finalfantasyiv';
FINALFANTASYIX: 'finalfantasyix';
FINALFANTASYV: 'finalfantasyv';
FINALFANTASYVI: 'finalfantasyvi';
FINALFANTASYVII: 'finalfantasyvii';
FINALFANTASYVIII: 'finalfantasyviii';
FINALFANTASYX: 'finalfantasyx';
FINALFANTASYXI: 'finalfantasyxi';
FINALFANTASYXII: 'finalfantasyxii';
FINALFANTASYXIII: 'finalfantasyxiii';
FINALFANTASYXIV: 'finalfantasyxiv';
FINALFANTASYXV: 'finalfantasyxv';
FINALFANTASYXVI: 'finalfantasyxvi';
FIRSTPRINTING: 'firstprinting';
FMB1: 'fmb1';
GAINLAND: 'gainland';
HALO: 'halo';
KAROO: 'karoo';
MB1: 'mb1';
NONDEFAULT: 'nondefault';
NONTRADITIONAL: 'nontraditional';
NORMAL: 'normal';
ODDFRAME: 'oddframe';
PAGL: 'pagl';
PAINLAND: 'painland';
PATHWAY: 'pathway';
PCTB: 'pctb';
PHED: 'phed';
PLACEHOLDERIMAGE: 'placeholderimage';
PLAYTEST: 'playtest';
SCRYLAND: 'scryland';
SETEXTENSION: 'setextension';
SHADOWLAND: 'shadowland';
SHOCKLAND: 'shockland';
SLOWLAND: 'slowland';
SNARL: 'snarl';
STORAGELAND: 'storageland';
SURVEILLAND: 'surveilland';
TANGOLAND: 'tangoland';
TRADITIONAL: 'traditional';
TRICYCLELAND: 'tricycleland';
TRIKELAND: 'trikeland';
TRILAND: 'triland';
TRIOME: 'triome';
TYPICAL: 'typical';
UPSIDEDOWN: 'upsidedown';
UPSIDEDOWNBACK: 'upsidedownback';

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

OVAL: 'oval';
ACORN: 'acorn';
TRIANGLE: 'triangle';
CIRCLE: 'circle';
HEART: 'heart';

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
FRAME: 'frame';
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

FRAME_1993: '1993';
FRAME_1997: '1997';
FRAME_2003: '2003';
FRAME_2015: '2015';
LEGENDARY: 'legendary';
ENCHANTMENT: 'enchantment';

//
// Primitive lexical forms
//
// NUMBER supports integers and decimal numeric literals.
NUMBER: [0-9]+ ('.' [0-9]+)?;
// Collector number token forms that include alphabetic components, e.g.
// 123a, a-268, u30.
COLLECTOR_NUMBER
    : [0-9]+ [a-z]
    | [a-z] '-' [0-9]+ [a-z]?
    | [a-z]+ [0-9]+ [a-z]?
    ;
// QUOTED_TEXT allows escaped characters in double-quoted strings.
QUOTED_TEXT: '"' (~["\\\r\n] | '\\' .)* '"';
// REGEX supports slash-delimited expressions with escaped slash support.
REGEX: '/' (~[/\\\r\n] | '\\' .)+ '/';
// COLOR_SET supports compact color letter combinations like "rg" or "wub".
// Dedicated tokens such as `U`, `B`, `R`, and `UB` may shadow this rule when
// they tie on length and appear earlier in lexer rule order.
COLOR_SET: [wWuUbBrRgG]+;
// Mana symbol fragments for `m:`/`mana:` value parsing.
fragment MANA_SYMBOL_CHAR: [wWuUbBrRgGcCsSpPxXyYzZ];
fragment MANA_SYMBOL_PART: [0-9]+ | MANA_SYMBOL_CHAR;
// One or more balanced mana symbol blocks, e.g. {R/P}, {2/G}, {W/U}{W/U}.
MANA_BRACED_SYMBOL: ('{' MANA_SYMBOL_PART ('/' MANA_SYMBOL_PART)? '}')+;
// Unbraced shorthand mana expression, e.g. 2WW or 3WU.
// Intentionally after COLOR_SET so color tokens keep precedence where relevant.
MANA_UNBRACED_SYMBOL: [0-9wWuUbBrRgGcCsSpPxXyYzZ]+;
// WORD is an unquoted atom token used for names/terms.
WORD: ~[ \t\r\n()"!:/<>=-] ~[ \t\r\n()"!:/<>=-]*;
// BARE_VALUE is like WORD but used in value positions.
BARE_VALUE: ~[ \t\r\n()"!:/<>=-] ~[ \t\r\n()":!<>=-]*;

// Whitespace is skipped globally.
WS: [ \t\r\n]+ -> skip;
