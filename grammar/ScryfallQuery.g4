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
    | identityTerm
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
    : ABNORMAL /* cards aren't printed with standard frames and effects */
    | ADVENTURE /* cards have Adventures */
    | ADVENTURER /* cards have Adventures */
    | ALCHEMY /* the set type is alchemy */
    | ALIGHTS /* cards have attraction lights */
    | ALTERNATE /* cards are one of several alternate versions of the card in the same set */
    | AMPERSAND /* cards are embossed */
    | ARCHENEMY /* the set type is archenemy */
    | ARCHIVAL /* cards require additional archival work */
    | ARENA_LEAGUE /* cards are Arena League prizes */
    | ARENAID /* cards have an Arena ID */
    | ARENALEAGUE /* cards are Arena League prizes */
    | ARTCARD /* cards are Art Series */
    | ARTIST /* have artists */
    | ARTISTID /* have artists */
    | ARTISTMISPRINT /* cards are cards with a misprinted artist */
    | ARTSERIES /* cards are Art Series */
    | ATTRACTIONLIGHTS /* cards have attraction lights */
    | ATYPICAL /* cards aren't printed with standard frames and effects */
    | AUGMENT /* cards are augment pieces */
    | AUGMENTATION /* cards are augment pieces */
    | AUGMENTING /* cards are augment pieces */
    | AUGMENTS /* cards are augment pieces */
    | BACK /* cards have non-standard backs */
    | BASELINE /* cards are printed with standard frames and effects */
    | BATTLELAND /* cards are dual lands from the 'takes-two-to-tango' cycle */
    | BEAR /* cards are 2/2/2 bears */
    | BEGINNERBOX /* cards are part of a Beginner Box */
    | BELZENLOK /* cards are Demonlord Belzenlok, Evincar of the Stronghold, Scion of Darkness, Doom of Fools, Lord of the Wastes, Master of the Ebon Hand, Eternal Patriarch of the Cabal */
    | BICYCLELAND /* cards are cycling dual lands */
    | BIKELAND /* cards are cycling dual lands */
    | BOB /* cards are Bob Maher's Invitational card */
    | BONDLAND /* cards are dual lands that require two or more opponents */
    | BOOSTER /* cards are cards that are included in the standard contents of draft boosters */
    | BOOSTERFUN /* cards are special versions that are part of "Project Booster Fun" */
    | BORDERLESS /* cards are borderless */
    | BOUNCELAND /* cards are land-bouncing duals */
    | BOX /* the set type is box */
    | BOXTOPPER /* cards are box toppers */
    | BRAWLCOMMANDER /* cards can be your Brawl commander */
    | BRAWLDECK /* cards are cards found in Brawl decks */
    | BRAWLER /* cards can be your Brawl commander */
    | BREAKER /* cards can be your oathbreaker */
    | BUNDLE /* cards are bundle promos */
    | BURSTFOIL /* cards are burst foils */
    | BUYABOX /* cards are Buy-a-Box promos */
    | CANLAND /* cards are dual lands that cantrip */
    | CANOPYLAND /* cards are dual lands that cantrip */
    | CARDBACK /* cards have non-standard backs */
    | CARDMARKET /* cards have a Cardmarket ID */
    | CARDMARKETID /* cards have a Cardmarket ID */
    | CHECKLAND /* cards are dual lands that check for other types */
    | CHOCOBOTRACKFOIL /* cards are Chocobo Track foils */
    | CHRIMBY /* cards are winners of Good Luck High Five's 'Chrimby Award' */
    | CI /* cards have color indicators */
    | CLASS /* cards are Class-type */
    | COLORINDICATOR /* cards have color indicators */
    | COLORSHIFTED /* cards have a colorshifted frame */
    | COMMANDER /* cards can be your commander */
    | COMMANDERPARTY /* cards are Commander Party promos */
    | COMMANDERPROMO /* cards are Commander promos */
    | COMPANION /* cards are Companions */
    | CONCEPT /* cards are concept treatments */
    | CONFETTIFOIL /* cards are confetti foil */
    | CONJUREONLY /* cards are can only be conjured in their set */
    | CONTENTWARNING /* cards have content warnings */
    | CONVENTION /* cards are convention promos */
    | CORE /* the set type is core */
    | COSMICFOIL /* cards are Cosmic foils */
    | COVERED /* cards are covered */
    | CREATURELAND /* cards are lands that become creatures */
    | CUTE /* cards are Good Luck High Five's 'Cutest Card' in a set */
    | CYCLELAND /* cards are cycling dual lands */
    | DATESTAMPED /* cards are cards with a date stamp */
    | DEFAULT /* cards are printed with standard frames and effects */
    | DEN /* cards are monster Dens */
    | DFC /* cards are double-sided */
    | DIGITAL /* cards are digital prints */
    | DOUBLEEXPOSURE /* cards are Double Exposure cards */
    | DOUBLEFACED /* cards are double-sided */
    | DOUBLERAINBOW /* cards are Double Rainbow foils */
    | DOUBLESIDED /* cards are double-sided */
    | DRACULASERIES /* cards are in the Innistrad: Crimson Vow Dracula Series */
    | DRAFTINNOVATION /* the set type is draftinnovation */
    | DRAFTWEEKEND /* cards are Draft Weekend promos */
    | DUAL /* cards are dual lands */
    | DUALCOMMANDER /* cards have multi-commander mechanics */
    | DUELCOMMANDER /* cards can be your Duel Commander */
    | DUELDECK /* the set type is dueldeck */
    | DUELS /* cards are promo cards for Duels of the Planeswalkers */
    | ENGLISHART /* cards have art that has been printed in English */
    | ESCAPED /* cards are cards that were never officially distributed by WotC */
    | ETB /* cards have an ETB effect */
    | ETCH /* cards are available in etched foil */
    | ETCHED /* cards are available in etched foil */
    | ETCHEDFOIL /* cards are available in etched foil */
    | EVENT /* cards are promos for a special event */
    | EXPANSION /* the set type is expansion */
    | EXTENDED /* cards are extended art frames */
    | EXTENDEDART /* cards are extended art frames */
    | EXTRA /* cards are Scryfall “extras” */
    | FASTLAND /* cards are duals lands that are 'fast' */
    | FBB /* cards are Cards printed in black border in non-English editions of white-border sets */
    | FETCHLAND /* cards are dual lands that fetches lands from the library */
    | FF /* from Final Fantasy */
    | FF1 /* cards are from Final Fantasy I */
    | FF10 /* cards are from Final Fantasy X */
    | FF11 /* cards are from Final Fantasy XI */
    | FF12 /* cards are from Final Fantasy XII */
    | FF13 /* cards are from Final Fantasy XIII */
    | FF14 /* cards are from Final Fantasy XIV */
    | FF15 /* cards are from Final Fantasy XV */
    | FF16 /* cards are from Final Fantasy XVI */
    | FF2 /* cards are from Final Fantasy II */
    | FF3 /* cards are from Final Fantasy III */
    | FF4 /* cards are from Final Fantasy IV */
    | FF5 /* cards are from Final Fantasy V */
    | FF6 /* cards are from Final Fantasy VI */
    | FF7 /* cards are from Final Fantasy VII */
    | FF8 /* cards are from Final Fantasy VIII */
    | FF9 /* cards are from Final Fantasy IX */
    | FFANTASY /* from Final Fantasy */
    | FFI /* cards are from Final Fantasy I */
    | FFII /* cards are from Final Fantasy II */
    | FFIII /* cards are from Final Fantasy III */
    | FFIV /* cards are from Final Fantasy IV */
    | FFIX /* cards are from Final Fantasy IX */
    | FFV /* cards are from Final Fantasy V */
    | FFVI /* cards are from Final Fantasy VI */
    | FFVII /* cards are from Final Fantasy VII */
    | FFVIII /* cards are from Final Fantasy VIII */
    | FFX /* cards are from Final Fantasy X */
    | FFXI /* cards are from Final Fantasy XI */
    | FFXII /* cards are from Final Fantasy XII */
    | FFXIII /* cards are from Final Fantasy XIII */
    | FFXIV /* cards are from Final Fantasy XIV */
    | FFXV /* cards are from Final Fantasy XV */
    | FFXVI /* cards are from Final Fantasy XVI */
    | FILTERLAND /* cards are dual lands that filters mana into other colors */
    | FIN /* from Final Fantasy */
    | FINALFANTASY /* from Final Fantasy */
    | FINALFANTASY1 /* cards are from Final Fantasy I */
    | FINALFANTASY10 /* cards are from Final Fantasy X */
    | FINALFANTASY11 /* cards are from Final Fantasy XI */
    | FINALFANTASY12 /* cards are from Final Fantasy XII */
    | FINALFANTASY13 /* cards are from Final Fantasy XIII */
    | FINALFANTASY14 /* cards are from Final Fantasy XIV */
    | FINALFANTASY15 /* cards are from Final Fantasy XV */
    | FINALFANTASY16 /* cards are from Final Fantasy XVI */
    | FINALFANTASY2 /* cards are from Final Fantasy II */
    | FINALFANTASY3 /* cards are from Final Fantasy III */
    | FINALFANTASY4 /* cards are from Final Fantasy IV */
    | FINALFANTASY5 /* cards are from Final Fantasy V */
    | FINALFANTASY6 /* cards are from Final Fantasy VI */
    | FINALFANTASY7 /* cards are from Final Fantasy VII */
    | FINALFANTASY8 /* cards are from Final Fantasy VIII */
    | FINALFANTASY9 /* cards are from Final Fantasy IX */
    | FINALFANTASYI /* cards are from Final Fantasy I */
    | FINALFANTASYII /* cards are from Final Fantasy II */
    | FINALFANTASYIII /* cards are from Final Fantasy III */
    | FINALFANTASYIV /* cards are from Final Fantasy IV */
    | FINALFANTASYIX /* cards are from Final Fantasy IX */
    | FINALFANTASYV /* cards are from Final Fantasy V */
    | FINALFANTASYVI /* cards are from Final Fantasy VI */
    | FINALFANTASYVII /* cards are from Final Fantasy VII */
    | FINALFANTASYVIII /* cards are from Final Fantasy VIII */
    | FINALFANTASYX /* cards are from Final Fantasy X */
    | FINALFANTASYXI /* cards are from Final Fantasy XI */
    | FINALFANTASYXII /* cards are from Final Fantasy XII */
    | FINALFANTASYXIII /* cards are from Final Fantasy XIII */
    | FINALFANTASYXIV /* cards are from Final Fantasy XIV */
    | FINALFANTASYXV /* cards are from Final Fantasy XV */
    | FINALFANTASYXVI /* cards are from Final Fantasy XVI */
    | FINKEL /* cards are Jon Finkel's Invitational card */
    | FIRSTPLACEFOIL /* cards are First-Place foils */
    | FIRSTPRINT /* the card is the first printing */
    | FIRSTPRINTING /* the card is the first printing */
    | FIXED /* cards are from sets with fixed contents */
    | FLAVOR /* cards have flavor text */
    | FLAVORNAME /* cards have flavor names */
    | FLAVORTEXT /* cards have flavor text */
    | FLIP /* cards flip */
    | FMB1 /* cards are fmb1 */
    | FNM /* cards are FNM promos */
    | FOIL /* cards are available in foil */
    | FRAMEODDITY /* cards are cards with an unusual frame that doesn't fit any other specific category */
    | FRENCHVANILLA /* cards are French vanilla */
    | FROMTHEVAULT /* the set type is fromthevault */
    | FT /* cards have flavor text */
    | FULLART /* cards are cards with full extended art */
    | FULLTEXT /* cards are the cards are only text */
    | FUNNY /* cards are funny */
    | FUTURE /* cards have the future frame */
    | FUTURESHIFTED /* cards have the future frame */
    | FWB /* cards are “foreign white border” prints */
    | GAINLAND /* cards are dual lands from the cycle that gains 1 life */
    | GALAXYFOIL /* cards are Galaxy foils */
    | GAMECHANGER /* cards are on the Commander Game Changer list */
    | GAMEDAY /* cards are Game Day promos */
    | GARY /* cards are the Gray Merchant of Asphodel a.k.a. 'Gary' */
    | GATEWAY /* cards are Gateway prizes */
    | GIFTBOX /* cards are Gift Box promos */
    | GILDED /* cards are cards with a gilded foil treatment */
    | GLOSSY /* cards are glossy foils */
    | GODZILLASERIES /* cards are in the Ikoria Godzilla Monsters Series */
    | HALO /* cards are Halo foils */
    | HALOFOIL /* cards are Halo foils */
    | HEADLINER /* cards are Headliner cards */
    | HIGHRES /* cards have hi-res scans */
    | HIRES /* cards have hi-res scans */
    | HISTORIC /* cards are historic */
    | HORIZ /* cards are a non-standard horizontal orientation */
    | HOST /* cards are augment pieces */
    | HYBRID /* cards have hybrid mana */
    | HYBRIDMANA /* cards have hybrid mana */
    | ILLUSTRATION /* have illustration IDs */
    | ILLUSTRATIONID /* have illustration IDs */
    | IMAGE /* cards have images */
    | IMAGEDATA /* cards have images */
    | IMAGEQA /* cards are pending image fixes */
    | IMAGINE /* cards are Imagine cards */
    | INDICATOR /* cards have color indicators */
    | INSTORE /* cards are prize cards for in-store play */
    | INTRO_PACK /* cards are exclusive Intro Pack cards */
    | INTROPACK /* cards are exclusive Intro Pack cards */
    | INVITATIONAL /* cards are Invitational cards */
    | JPWALKER /* cards are Japanese-exclusive alternate-art War of the Spark planeswalkers */
    | JUDGE_GIFT /* cards are Judge Gift Cards */
    | JUDGEGIFT /* cards are Judge Gift Cards */
    | JUMPSTART /* cards are Jumpstart cards */
    | KAROO /* cards are land-bouncing duals */
    | KEEPER /* cards can be your oathbreaker */
    | LEAGUE /* cards are League promos */
    | LEVELER /* cards have Level Up */
    | LIGHTS /* cards have attraction lights */
    | LISTWHITE /* cards are printed with strange white mana symbols */
    | LOCALIZEDIMAGE /* cards are non-English cards with localized images */
    | LOCALIZEDNAME /* cards have localized names */
    | LOSTLEGENDS /* cards are Dominaria United Lost Legends */
    | MAGICSPOTLIGHT /* cards are part of the Magic Spotlight promo series */
    | MANLAND /* cards are lands that become creatures */
    | MASTERPIECE /* cards are masterpieces */
    | MASTERS /* the set type is masters */
    | MB1 /* cards are printed in Mystery Booster */
    | MB2 /* cards are printed in Mystery Booster 2 */
    | MDFC /* cards are modal DFCs */
    | MEDIA_INSERT /* cards are cards inserted into books or magazines */
    | MEDIAINSERT /* cards are cards inserted into books or magazines */
    | MELD /* cards meld */
    | MELDPART /* cards are parts of a meld */
    | MELDRESULT /* cards are the result of a meld */
    | MEMORABILIA /* the set type is memorabilia */
    | METAL /* cards are metal finishes */
    | MISPRINT /* cards are printed with a mistake or error */
    | MODAL /* cards have modal effects */
    | MODALDFC /* cards are modal DFCs */
    | MODERN /* cards have the 2003 frame */
    | MOM /* cards are the Mother of Runes a.k.a. 'Mom' */
    | MOONLITLAND /* cards are Moonlit Lands promos */
    | MTGOID /* cards have a MTGO ID (CatID) */
    | MULTICOMMANDER /* cards have multi-commander mechanics */
    | MULTIPLAYER /* cards are in a multiplayer-oriented set */
    | MULTIVERSE /* cards have a Multiverse ID */
    | MULTIVERSEID /* cards have a Multiverse ID */
    | NEONINK /* cards are cards with a neon ink treatment */
    | NEW /* cards have a new frame */
    | NEWINPAUPER /* cards are paper commons added to the Pauper format */
    | NONDEFAULT /* cards aren't printed with standard frames and effects */
    | NONFOIL /* cards are available in nonfoil */
    | NONTRADITIONAL /* cards aren't printed with standard frames and effects */
    | NORMAL /* cards are printed with standard frames and effects */
    | NOTUB /* Printings not from Universes Beyond products */
    | NOTUNIVERSEBEYOND /* Printings not from Universes Beyond products */
    | NOTUNIVERSESBEYOND /* Printings not from Universes Beyond products */
    | OATHBREAKER /* cards can be your oathbreaker */
    | OATHKEEPER /* cards can be your oathbreaker */
    | OB /* cards can be your oathbreaker */
    | OBREAKER /* cards can be your oathbreaker */
    | ODDFRAME /* cards are cards with an unusual frame that doesn't fit any other specific category */
    | OILSLICK /* cards are cards with the raised 'oil slick' foil treatment */
    | OK /* cards can be your oathbreaker */
    | OKEEPER /* cards can be your oathbreaker */
    | OLD /* cards have the ‘93/97 frame */
    | ONLYPRINT /* the card has been printed exactly once */
    | ONLYPRINTING /* the card has been printed exactly once */
    | OPENHOUSE /* cards are Open House promos */
    | OUTLAW /* cards are Assassins, Mercenaries, Pirates, Rogues, or Warlocks */
    | OUTLAWS /* cards are Assassins, Mercenaries, Pirates, Rogues, or Warlocks */
    | OVERSIZED /* cards are larger than standard card size */
    | PAGL /* cards are printed in Angels: They're Just Like Us but Cooler and with Wings */
    | PAINLAND /* cards are dual lands that damage you when you get colored mana */
    | PAIRCOMMANDER /* cards have multi-commander mechanics */
    | PAIREDCOMMANDER /* cards have multi-commander mechanics */
    | PAPERART /* cards have art that has been printed in paper */
    | PARTNER /* cards have multi-commander mechanics */
    | PARTY /* cards are Clerics, Rogues, Warriors, or Wizards */
    | PATHWAY /* cards are Pathway duals */
    | PAUPERCOMMANDER /* cards are can be your Pauper Commander */
    | PCTB /* cards are printed in From Cute to Brute */
    | PERMANENT /* cards become permanents */
    | PHED /* cards are printed in Heads I Win, Tails You Lose */
    | PHYREXIA /* cards have Phyrexian mana */
    | PHYREXIAN /* cards have Phyrexian mana */
    | PHYREXIANMANA /* cards have Phyrexian mana */
    | PIKULA /* cards are Chris Pikula's Invitational card */
    | PLACEHOLDERIMAGE /* cards are non-English cards with placeholder images */
    | PLANAR /* cards are planar deck cards */
    | PLANECHASE /* the set type is planechase */
    | PLANESWALKER_DECK /* cards are exclusive Planeswalker Deck cards */
    | PLANESWALKERDECK /* cards are exclusive Planeswalker Deck cards */
    | PLASTIC /* cards are plastic finishes */
    | PLAYER_REWARDS /* cards are Magic Player Rewards */
    | PLAYERREWARDS /* cards are Magic Player Rewards */
    | PLAYPROMO /* cards are WPN play promos */
    | PLAYTEST /* cards are playtest cards */
    | PORTAL /* cards are Portal cards */
    | PORTRAIT /* cards are Commander portraits */
    | POSTER /* cards are poster-frame prints */
    | PREMIERESHOP /* cards are Magic Premier Shop promos */
    | PREMIUM /* cards are available in foil */
    | PREMIUMDECK /* the set type is premiumdeck */
    | PRERELEASE /* cards are set prerelease event promos */
    | PRINTEDNAME /* cards have localized names */
    | PRINTEDTEXT /* cards have their printed text listed */
    | PROMO /* cards are promotional prints */
    | PROMOPACK /* cards are promos found in WPN promo packs */
    | RAINBOWFOIL /* cards are Rainbow foils */
    | RAISEDFOIL /* cards are raised foils */
    | REBALANCED /* cards are rebalanced Alchemy cards */
    | RELATED /* cards have related cards */
    | RELATEDCARDS /* cards have related cards */
    | RELATIONSHIPS /* cards have related cards */
    | RELEASE /* cards are set release event promos */
    | REPRINT /* cards are reprints */
    | RESALE /* cards are resale promos */
    | RESERVED /* cards are on the Reserved List */
    | REVERSABLE /* cards are reversible cards */
    | REVERSEABLE /* cards are reversible cards */
    | REVERSIBLE /* cards are reversible cards */
    | RIPPLEFOIL /* cards are Ripple foils */
    | SCANNEEDED /* cards need to be scanned */
    | SCENE /* cards are panoramic scene pieces */
    | SCHINESEALTART /* cards are cards with alternate art in S-Chinese */
    | SCROLL /* cards are scroll-frame prints */
    | SCRYFALLPREVIEW /* cards are cards that were previewed by Scryfall */
    | SCRYLAND /* cards are dual lands that scry when they enter the battlefield */
    | SECSTAMP /* cards have a security stamp */
    | SECURITYSTAMP /* cards have a security stamp */
    | SERIALIZED /* cards are marked with serial numbers */
    | SET_PROMO /* cards are promo cards for a booster product */
    | SETEXTENSION /* cards are boosterfun cards appended to an older set */
    | SETPROMO /* cards are promo cards for a booster product */
    | SHADOWLAND /* cards are dual lands from the land-revealing/snarl cycle */
    | SHINY /* cards are available in foil */
    | SHOCKLAND /* cards are dual lands that deal 2 damage to you */
    | SHOWCASE /* cards are showcases */
    | SINGULARITYFOIL /* cards are Singularity foils */
    | SLDBONUS /* cards are Secret Lair bonus cards */
    | SLOWLAND /* cards are dual lands that check for two other lands */
    | SNARL /* cards are dual lands from the land-revealing/snarl cycle */
    | SOURCEMATERIAL /* cards are Source Material cards */
    | SPECIALBACK /* cards have non-standard backs */
    | SPELL /* cards are spells */
    | SPELLBOOK /* cards have spellbooks */
    | SPIKEY /* cards are cards that have ever been banned or restricted */
    | SPLIT /* cards are split */
    | SPLITMANA /* cards have hybrid mana */
    | SPOTLIGHT /* cards are Story Spotlights */
    | STAMP /* cards have a security stamp */
    | STAMPED /* cards are cards with a non-date stamp */
    | STARTER /* the set type is starter */
    | STARTERCOLLECTION /* cards are part of a Starter Collection */
    | STARTERDECK /* cards are exclusive to a Starter deck */
    | STEPANDCOMPLEAT /* cards are cards with the 'Step-and-Compleat' Phyrexian foil treatment */
    | STORAGELAND /* cards are lands that allow you to store up mana for later use */
    | STORECHAMPIONSHIP /* cards are Store Championship promos */
    | STORY /* cards are Story Spotlights */
    | SURVEILLAND /* cards are dual lands that surveil when they enter the battlefield */
    | TANGOLAND /* cards are dual lands from the 'takes-two-to-tango' cycle */
    | TCGPLAYER /* cards have a TCGplayer ID */
    | TCGPLAYERID /* cards have a TCGplayer ID */
    | TDFC /* cards transform */
    | TEXTLESS /* cards are printed without rules text */
    | TEXTURED /* cards are cards with a textured foil treatment */
    | THEMEPACK /* cards are exclusive to Theme Boosters */
    | THICK /* cards are made with extra-thick stock */
    | TIMESHIFTED /* cards are timeshifted in Time Spiral */
    | TOKEN /* cards are tokens */
    | TOMBSTONE /* cards have the Odyssey tombstone mark */
    | TOURNEY /* cards are tournament event prizes */
    | TRADITIONAL /* cards are printed with standard frames and effects */
    | TRANSFORM /* cards transform */
    | TRANSFORMINGDFC /* cards transform */
    | TRANSLUCENT /* cards are cards with a translucent card frame */
    | TREASURECHEST /* the set type is treasurechest */
    | TRICYCLELAND /* cards are tricycleland */
    | TRIKELAND /* cards are tricycleland */
    | TRILAND /* cards are lands that produce three colors of mana */
    | TRIOME /* cards are tricycleland */
    | TRON /* cards are members of the 'Urzatron' */
    | TWOCOMMANDER /* cards have multi-commander mechanics */
    | TYPICAL /* cards are printed with standard frames and effects */
    | UB /* Printings from Universes Beyond products */
    | UNIQUE /* the card has been printed exactly once */
    | UNIVERSEBEYOND /* Printings from Universes Beyond products */
    | UNIVERSESBEYOND /* Printings from Universes Beyond products */
    | UNSET /* cards are from an Unset */
    | UPSIDEDOWN /* cards are cards with the front face upside-down */
    | UPSIDEDOWNBACK /* cards are cards with the back face upside-down */
    | USELESS /* cards are Jace's useless island */
    | VANGUARD /* the set type is vanguard */
    | VANILLA /* cards are vanilla */
    | VARIATION /* cards are variations of standard printings */
    | VAULT /* cards are vault frames */
    | VERT /* cards are a non-standard vertical orientation */
    | WANTED /* cards are wanted Scryfall scans */
    | WATERMARK /* cards have watermarks */
    | WIZARDSPLAYNETWORK /* cards are Wizards Play Network prize */
    | WM /* cards have watermarks */
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

identityTerm: (ID | IDENTITY) compOp identityValue;
identityValue: colorValue;

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

ADVENTURER: 'adventurer';
ALIGHTS: 'alights';
ARTCARD: 'artcard';
ARTISTID: 'artistid';
ATTRACTIONLIGHTS: 'attractionlights';
AUGMENT: 'augment';
AUGMENTING: 'augmenting';
AUGMENTS: 'augments';
BREAKER: 'breaker';
CARDBACK: 'cardback';
CARDMARKETID: 'cardmarketid';
COLORINDICATOR: 'colorindicator';
DOUBLEFACED: 'doublefaced';
DUALCOMMANDER: 'dualcommander';
ETCHEDFOIL: 'etchedfoil';
EXTENDEDART: 'extendedart';
FFANTASY: 'ffantasy';
FIN: 'fin';
FLAVORTEXT: 'flavortext';
HIGHRES: 'highres';
HOST: 'host';
HYBRIDMANA: 'hybridmana';
ILLUSTRATIONID: 'illustrationid';
IMAGE: 'image';
IMAGEDATA: 'imagedata';
KEEPER: 'keeper';
MODALDFC: 'modaldfc';
MULTICOMMANDER: 'multicommander';
MULTIVERSEID: 'multiverseid';
NOTUNIVERSEBEYOND: 'notuniversebeyond';
OATHKEEPER: 'oathkeeper';
OB: 'ob';
OBREAKER: 'obreaker';
OK: 'ok';
OKEEPER: 'okeeper';
ONLYPRINTING: 'onlyprinting';
OUTLAWS: 'outlaws';
PAIRCOMMANDER: 'paircommander';
PAIREDCOMMANDER: 'pairedcommander';
PHYREXIANMANA: 'phyrexianmana';
PREMIUM: 'premium';
PRINTEDNAME: 'printedname';
RELATEDCARDS: 'relatedcards';
RELATIONSHIPS: 'relationships';
REVERSABLE: 'reversable';
REVERSEABLE: 'reverseable';
SECSTAMP: 'secstamp';
SECURITYSTAMP: 'securitystamp';
SHINY: 'shiny';
SPECIALBACK: 'specialback';
TCGPLAYERID: 'tcgplayerid';
TRANSFORMINGDFC: 'transformingdfc';
TWOCOMMANDER: 'twocommander';
UNIVERSEBEYOND: 'universebeyond';

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
