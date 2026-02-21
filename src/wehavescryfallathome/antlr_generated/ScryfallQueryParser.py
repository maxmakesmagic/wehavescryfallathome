# Generated from grammar/ScryfallQuery.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,543,304,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,
        7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,
        13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,
        20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,
        26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,
        33,7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,
        39,2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,
        46,7,46,2,47,7,47,2,48,7,48,2,49,7,49,1,0,1,0,1,0,1,1,1,1,1,1,5,
        1,107,8,1,10,1,12,1,110,9,1,1,2,4,2,113,8,2,11,2,12,2,114,1,3,1,
        3,3,3,119,8,3,1,4,1,4,1,4,1,4,1,5,3,5,126,8,5,1,5,1,5,1,6,1,6,1,
        6,5,6,133,8,6,10,6,12,6,136,9,6,1,7,4,7,139,8,7,11,7,12,7,140,1,
        8,1,8,3,8,145,8,8,1,9,1,9,1,9,1,9,1,10,3,10,152,8,10,1,10,1,10,1,
        11,1,11,3,11,158,8,11,1,12,1,12,1,12,1,12,1,12,3,12,165,8,12,1,13,
        1,13,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,
        1,14,1,14,3,14,183,8,14,1,15,1,15,1,15,3,15,188,8,15,1,16,1,16,1,
        16,1,16,1,17,1,17,1,18,1,18,1,19,1,19,1,19,1,19,1,20,1,20,1,21,1,
        21,1,21,1,21,1,22,1,22,1,23,1,23,1,23,1,23,1,24,1,24,1,25,1,25,1,
        25,1,25,1,26,1,26,1,27,1,27,1,27,1,27,1,28,1,28,1,28,1,28,1,29,1,
        29,1,29,1,29,1,30,1,30,1,31,1,31,1,31,1,31,1,32,1,32,1,32,1,32,1,
        33,1,33,1,33,1,33,1,34,1,34,1,35,1,35,1,35,1,35,1,36,1,36,1,37,1,
        37,1,37,1,37,1,38,1,38,1,39,1,39,1,39,1,39,1,40,1,40,1,41,1,41,1,
        41,1,41,1,42,1,42,1,42,1,42,1,43,1,43,1,44,1,44,1,45,1,45,1,45,1,
        45,1,45,1,45,1,45,1,45,1,45,1,45,1,45,1,45,1,45,1,45,3,45,294,8,
        45,1,46,1,46,1,47,1,47,1,48,1,48,1,49,1,49,1,49,0,0,50,0,2,4,6,8,
        10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,
        54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,88,90,92,94,96,
        98,0,19,2,0,29,30,482,482,1,0,31,34,4,0,26,26,38,38,40,48,86,90,
        1,0,35,36,1,0,91,105,10,0,13,13,38,38,99,104,106,453,455,455,459,
        459,465,465,499,499,528,528,535,535,1,0,21,22,6,0,89,89,121,121,
        147,147,151,151,163,163,454,469,1,0,470,472,2,0,48,48,488,488,8,
        0,49,85,103,103,485,485,488,488,513,513,524,525,537,537,540,540,
        3,0,26,26,506,506,524,524,5,0,473,478,485,485,488,488,513,513,524,
        525,1,0,27,28,2,0,479,480,537,537,8,0,25,26,30,30,38,39,41,47,155,
        155,481,487,489,524,526,536,1,0,5,11,1,0,540,541,2,0,540,540,542,
        542,293,0,100,1,0,0,0,2,103,1,0,0,0,4,112,1,0,0,0,6,118,1,0,0,0,
        8,120,1,0,0,0,10,125,1,0,0,0,12,129,1,0,0,0,14,138,1,0,0,0,16,144,
        1,0,0,0,18,146,1,0,0,0,20,151,1,0,0,0,22,157,1,0,0,0,24,164,1,0,
        0,0,26,166,1,0,0,0,28,182,1,0,0,0,30,184,1,0,0,0,32,189,1,0,0,0,
        34,193,1,0,0,0,36,195,1,0,0,0,38,197,1,0,0,0,40,201,1,0,0,0,42,203,
        1,0,0,0,44,207,1,0,0,0,46,209,1,0,0,0,48,213,1,0,0,0,50,215,1,0,
        0,0,52,219,1,0,0,0,54,221,1,0,0,0,56,225,1,0,0,0,58,229,1,0,0,0,
        60,233,1,0,0,0,62,235,1,0,0,0,64,239,1,0,0,0,66,243,1,0,0,0,68,247,
        1,0,0,0,70,249,1,0,0,0,72,253,1,0,0,0,74,255,1,0,0,0,76,259,1,0,
        0,0,78,261,1,0,0,0,80,265,1,0,0,0,82,267,1,0,0,0,84,271,1,0,0,0,
        86,275,1,0,0,0,88,277,1,0,0,0,90,293,1,0,0,0,92,295,1,0,0,0,94,297,
        1,0,0,0,96,299,1,0,0,0,98,301,1,0,0,0,100,101,3,2,1,0,101,102,5,
        0,0,1,102,1,1,0,0,0,103,108,3,4,2,0,104,105,5,12,0,0,105,107,3,4,
        2,0,106,104,1,0,0,0,107,110,1,0,0,0,108,106,1,0,0,0,108,109,1,0,
        0,0,109,3,1,0,0,0,110,108,1,0,0,0,111,113,3,6,3,0,112,111,1,0,0,
        0,113,114,1,0,0,0,114,112,1,0,0,0,114,115,1,0,0,0,115,5,1,0,0,0,
        116,119,3,8,4,0,117,119,3,10,5,0,118,116,1,0,0,0,118,117,1,0,0,0,
        119,7,1,0,0,0,120,121,5,1,0,0,121,122,3,12,6,0,122,123,5,2,0,0,123,
        9,1,0,0,0,124,126,5,3,0,0,125,124,1,0,0,0,125,126,1,0,0,0,126,127,
        1,0,0,0,127,128,3,22,11,0,128,11,1,0,0,0,129,134,3,14,7,0,130,131,
        5,12,0,0,131,133,3,14,7,0,132,130,1,0,0,0,133,136,1,0,0,0,134,132,
        1,0,0,0,134,135,1,0,0,0,135,13,1,0,0,0,136,134,1,0,0,0,137,139,3,
        16,8,0,138,137,1,0,0,0,139,140,1,0,0,0,140,138,1,0,0,0,140,141,1,
        0,0,0,141,15,1,0,0,0,142,145,3,18,9,0,143,145,3,20,10,0,144,142,
        1,0,0,0,144,143,1,0,0,0,145,17,1,0,0,0,146,147,5,1,0,0,147,148,3,
        12,6,0,148,149,5,2,0,0,149,19,1,0,0,0,150,152,5,3,0,0,151,150,1,
        0,0,0,151,152,1,0,0,0,152,153,1,0,0,0,153,154,3,26,13,0,154,21,1,
        0,0,0,155,158,3,24,12,0,156,158,3,28,14,0,157,155,1,0,0,0,157,156,
        1,0,0,0,158,23,1,0,0,0,159,165,3,32,16,0,160,165,3,38,19,0,161,165,
        3,42,21,0,162,165,3,46,23,0,163,165,3,50,25,0,164,159,1,0,0,0,164,
        160,1,0,0,0,164,161,1,0,0,0,164,162,1,0,0,0,164,163,1,0,0,0,165,
        25,1,0,0,0,166,167,3,28,14,0,167,27,1,0,0,0,168,183,3,30,15,0,169,
        183,3,54,27,0,170,183,3,56,28,0,171,183,3,58,29,0,172,183,3,62,31,
        0,173,183,3,64,32,0,174,183,3,66,33,0,175,183,3,70,35,0,176,183,
        3,78,39,0,177,183,3,82,41,0,178,183,3,74,37,0,179,183,3,84,42,0,
        180,183,3,92,46,0,181,183,3,96,48,0,182,168,1,0,0,0,182,169,1,0,
        0,0,182,170,1,0,0,0,182,171,1,0,0,0,182,172,1,0,0,0,182,173,1,0,
        0,0,182,174,1,0,0,0,182,175,1,0,0,0,182,176,1,0,0,0,182,177,1,0,
        0,0,182,178,1,0,0,0,182,179,1,0,0,0,182,180,1,0,0,0,182,181,1,0,
        0,0,183,29,1,0,0,0,184,187,5,4,0,0,185,188,3,92,46,0,186,188,3,96,
        48,0,187,185,1,0,0,0,187,186,1,0,0,0,188,31,1,0,0,0,189,190,3,34,
        17,0,190,191,5,5,0,0,191,192,3,36,18,0,192,33,1,0,0,0,193,194,5,
        13,0,0,194,35,1,0,0,0,195,196,7,0,0,0,196,37,1,0,0,0,197,198,5,14,
        0,0,198,199,5,5,0,0,199,200,3,40,20,0,200,39,1,0,0,0,201,202,7,1,
        0,0,202,41,1,0,0,0,203,204,5,15,0,0,204,205,5,5,0,0,205,206,3,44,
        22,0,206,43,1,0,0,0,207,208,7,2,0,0,208,45,1,0,0,0,209,210,5,16,
        0,0,210,211,5,5,0,0,211,212,3,48,24,0,212,47,1,0,0,0,213,214,7,3,
        0,0,214,49,1,0,0,0,215,216,5,17,0,0,216,217,5,5,0,0,217,218,3,52,
        26,0,218,51,1,0,0,0,219,220,7,4,0,0,220,53,1,0,0,0,221,222,5,18,
        0,0,222,223,5,5,0,0,223,224,5,37,0,0,224,55,1,0,0,0,225,226,5,19,
        0,0,226,227,5,5,0,0,227,228,3,60,30,0,228,57,1,0,0,0,229,230,5,20,
        0,0,230,231,5,5,0,0,231,232,3,60,30,0,232,59,1,0,0,0,233,234,7,5,
        0,0,234,61,1,0,0,0,235,236,7,6,0,0,236,237,5,5,0,0,237,238,3,68,
        34,0,238,63,1,0,0,0,239,240,5,23,0,0,240,241,5,5,0,0,241,242,3,68,
        34,0,242,65,1,0,0,0,243,244,5,24,0,0,244,245,5,5,0,0,245,246,3,68,
        34,0,246,67,1,0,0,0,247,248,7,7,0,0,248,69,1,0,0,0,249,250,5,25,
        0,0,250,251,5,5,0,0,251,252,7,8,0,0,252,71,1,0,0,0,253,254,7,8,0,
        0,254,73,1,0,0,0,255,256,7,9,0,0,256,257,3,88,44,0,257,258,3,76,
        38,0,258,75,1,0,0,0,259,260,7,10,0,0,260,77,1,0,0,0,261,262,7,11,
        0,0,262,263,3,88,44,0,263,264,3,80,40,0,264,79,1,0,0,0,265,266,7,
        12,0,0,266,81,1,0,0,0,267,268,7,13,0,0,268,269,3,88,44,0,269,270,
        7,14,0,0,270,83,1,0,0,0,271,272,3,86,43,0,272,273,3,88,44,0,273,
        274,3,90,45,0,274,85,1,0,0,0,275,276,7,15,0,0,276,87,1,0,0,0,277,
        278,7,16,0,0,278,89,1,0,0,0,279,294,3,94,47,0,280,294,3,92,46,0,
        281,294,3,98,49,0,282,294,3,96,48,0,283,294,3,86,43,0,284,294,3,
        80,40,0,285,294,3,68,34,0,286,294,3,60,30,0,287,294,3,44,22,0,288,
        294,3,52,26,0,289,294,3,48,24,0,290,294,3,36,18,0,291,294,3,40,20,
        0,292,294,3,72,36,0,293,279,1,0,0,0,293,280,1,0,0,0,293,281,1,0,
        0,0,293,282,1,0,0,0,293,283,1,0,0,0,293,284,1,0,0,0,293,285,1,0,
        0,0,293,286,1,0,0,0,293,287,1,0,0,0,293,288,1,0,0,0,293,289,1,0,
        0,0,293,290,1,0,0,0,293,291,1,0,0,0,293,292,1,0,0,0,294,91,1,0,0,
        0,295,296,5,538,0,0,296,93,1,0,0,0,297,298,5,539,0,0,298,95,1,0,
        0,0,299,300,7,17,0,0,300,97,1,0,0,0,301,302,7,18,0,0,302,99,1,0,
        0,0,13,108,114,118,125,134,140,144,151,157,164,182,187,293
    ]

class ScryfallQueryParser ( Parser ):

    grammarFileName = "ScryfallQuery.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'-'", "'!'", "':'", "'!='", 
                     "'>='", "'<='", "'='", "'>'", "'<'", "'or'", "'unique'", 
                     "'display'", "'order'", "'direction'", "'prefer'", 
                     "'include'", "'is'", "'not'", "'f'", "'format'", "'banned'", 
                     "'restricted'", "'game'", "'rarity'", "'mv'", "'manavalue'", 
                     "'cards'", "'prints'", "'grid'", "'checklist'", "'full'", 
                     "'text'", "'asc'", "'desc'", "'extras'", "'artist'", 
                     "'artists'", "'cmc'", "'power'", "'toughness'", "'set'", 
                     "'name'", "'usd'", "'tix'", "'eur'", "'color'", "'white'", 
                     "'blue'", "'black'", "'red'", "'green'", "'colorless'", 
                     "'multicolor'", "'azorius'", "'dimir'", "'rakdos'", 
                     "'gruul'", "'selesnya'", "'orzhov'", "'izzet'", "'golgari'", 
                     "'boros'", "'simic'", "'bant'", "'esper'", "'grixis'", 
                     "'jund'", "'naya'", "'abzan'", "'jeskai'", "'sultai'", 
                     "'mardu'", "'temur'", "'quandrix'", "'prismari'", "'witherbloom'", 
                     "'lorehold'", "'silverquill'", "'chaos'", "'aggression'", 
                     "'altruism'", "'growth'", "'artifice'", "'released'", 
                     "'spoiled'", "'edhrec'", "'penny'", "'review'", "'oldest'", 
                     "'newest'", "'usd-low'", "'usd-high'", "'tix-low'", 
                     "'tix-high'", "'eur-low'", "'eur-high'", "'promo'", 
                     "'default'", "'atypical'", "'universesbeyond'", "'ub'", 
                     "'notuniversesbeyond'", "'notub'", "'indicator'", "'hybrid'", 
                     "'phyrexian'", "'split'", "'flip'", "'transform'", 
                     "'tdfc'", "'meld'", "'meldpart'", "'meldresult'", "'leveler'", 
                     "'dfc'", "'mdfc'", "'spell'", "'permanent'", "'historic'", 
                     "'party'", "'outlaw'", "'modal'", "'vanilla'", "'frenchvanilla'", 
                     "'bear'", "'manland'", "'funny'", "'booster'", "'planeswalker_deck'", 
                     "'league'", "'buyabox'", "'giftbox'", "'intro_pack'", 
                     "'gameday'", "'prerelease'", "'release'", "'fnm'", 
                     "'judge_gift'", "'arena_league'", "'player_rewards'", 
                     "'media_insert'", "'instore'", "'convention'", "'set_promo'", 
                     "'commander'", "'brawler'", "'companion'", "'duelcommander'", 
                     "'oathbreaker'", "'partner'", "'gamechanger'", "'reserved'", 
                     "'new'", "'old'", "'nonfoil'", "'foil'", "'etched'", 
                     "'glossy'", "'hires'", "'digital'", "'alchemy'", "'rebalanced'", 
                     "'spotlight'", "'scryfallpreview'", "'reprint'", "'ff7'", 
                     "'ff'", "'newinpauper'", "'datestamped'", "'adventure'", 
                     "'arenaid'", "'artistmisprint'", "'artseries'", "'augmentation'", 
                     "'back'", "'beginnerbox'", "'borderless'", "'brawlcommander'", 
                     "'cardmarket'", "'ci'", "'class'", "'colorshifted'", 
                     "'contentwarning'", "'covered'", "'doublesided'", "'englishart'", 
                     "'etb'", "'etch'", "'extended'", "'extra'", "'fbb'", 
                     "'firstprint'", "'flavorname'", "'fullart'", "'fwb'", 
                     "'illustration'", "'ff1'", "'ff10'", "'ff11'", "'ff12'", 
                     "'ff13'", "'ff14'", "'ff15'", "'ff16'", "'ff2'", "'ff3'", 
                     "'ff4'", "'ff5'", "'ff6'", "'intropack'", "'ff8'", 
                     "'ff9'", "'ffi'", "'ffii'", "'ffiii'", "'ffiv'", "'ffix'", 
                     "'ffv'", "'ffvi'", "'ffvii'", "'ffviii'", "'ffx'", 
                     "'ffxi'", "'ffxii'", "'ffxiii'", "'ffxiv'", "'ffxv'", 
                     "'ffxvi'", "'finalfantasy'", "'invitational'", "'lights'", 
                     "'localizedname'", "'masterpiece'", "'mtgoid'", "'multiverse'", 
                     "'onlyprint'", "'oversized'", "'paperart'", "'phyrexia'", 
                     "'planar'", "'planeswalkerdeck'", "'printedtext'", 
                     "'related'", "'reversible'", "'showcase'", "'spellbook'", 
                     "'spikey'", "'splitmana'", "'stamped'", "'startercollection'", 
                     "'starterdeck'", "'story'", "'tcgplayer'", "'textless'", 
                     "'token'", "'tombstone'", "'translucent'", "'variation'", 
                     "'alternate'", "'ampersand'", "'archenemy'", "'archival'", 
                     "'arenaleague'", "'bob'", "'boosterfun'", "'box'", 
                     "'boxtopper'", "'brawldeck'", "'bundle'", "'burstfoil'", 
                     "'chocobotrackfoil'", "'chrimby'", "'commanderparty'", 
                     "'commanderpromo'", "'concept'", "'confettifoil'", 
                     "'conjureonly'", "'cosmicfoil'", "'cute'", "'den'", 
                     "'doubleexposure'", "'doublerainbow'", "'draculaseries'", 
                     "'draftinnovation'", "'draftweekend'", "'dueldeck'", 
                     "'duels'", "'escaped'", "'event'", "'finkel'", "'firstplacefoil'", 
                     "'fixed'", "'frameoddity'", "'fromthevault'", "'fulltext'", 
                     "'futureshifted'", "'galaxyfoil'", "'gary'", "'gateway'", 
                     "'gilded'", "'godzillaseries'", "'halofoil'", "'headliner'", 
                     "'horiz'", "'imageqa'", "'imagine'", "'jpwalker'", 
                     "'judgegift'", "'jumpstart'", "'listwhite'", "'localizedimage'", 
                     "'lostlegends'", "'magicspotlight'", "'masters'", "'mb2'", 
                     "'mediainsert'", "'memorabilia'", "'metal'", "'misprint'", 
                     "'mom'", "'moonlitland'", "'multiplayer'", "'neonink'", 
                     "'oilslick'", "'openhouse'", "'pikula'", "'planechase'", 
                     "'plastic'", "'playerrewards'", "'playpromo'", "'portal'", 
                     "'portrait'", "'poster'", "'premiereshop'", "'premiumdeck'", 
                     "'promopack'", "'rainbowfoil'", "'raisedfoil'", "'resale'", 
                     "'ripplefoil'", "'scanneeded'", "'scene'", "'schinesealtart'", 
                     "'scroll'", "'serialized'", "'setpromo'", "'singularityfoil'", 
                     "'sldbonus'", "'sourcematerial'", "'starter'", "'stepandcompleat'", 
                     "'storechampionship'", "'textured'", "'themepack'", 
                     "'thick'", "'timeshifted'", "'tourney'", "'treasurechest'", 
                     "'tron'", "'unset'", "'useless'", "'vanguard'", "'vault'", 
                     "'vert'", "'wanted'", "'wizardsplaynetwork'", "'abnormal'", 
                     "'baseline'", "'battleland'", "'belzenlok'", "'bicycleland'", 
                     "'bikeland'", "'bondland'", "'bounceland'", "'canland'", 
                     "'canopyland'", "'checkland'", "'core'", "'creatureland'", 
                     "'cycleland'", "'dual'", "'expansion'", "'fastland'", 
                     "'fetchland'", "'filterland'", "'finalfantasy1'", "'finalfantasy10'", 
                     "'finalfantasy11'", "'finalfantasy12'", "'finalfantasy13'", 
                     "'finalfantasy14'", "'finalfantasy15'", "'finalfantasy16'", 
                     "'finalfantasy2'", "'finalfantasy3'", "'finalfantasy4'", 
                     "'finalfantasy5'", "'finalfantasy6'", "'finalfantasy7'", 
                     "'finalfantasy8'", "'finalfantasy9'", "'finalfantasyi'", 
                     "'finalfantasyii'", "'finalfantasyiii'", "'finalfantasyiv'", 
                     "'finalfantasyix'", "'finalfantasyv'", "'finalfantasyvi'", 
                     "'finalfantasyvii'", "'finalfantasyviii'", "'finalfantasyx'", 
                     "'finalfantasyxi'", "'finalfantasyxii'", "'finalfantasyxiii'", 
                     "'finalfantasyxiv'", "'finalfantasyxv'", "'finalfantasyxvi'", 
                     "'firstprinting'", "'fmb1'", "'gainland'", "'halo'", 
                     "'karoo'", "'mb1'", "'nondefault'", "'nontraditional'", 
                     "'normal'", "'oddframe'", "'pagl'", "'painland'", "'pathway'", 
                     "'pctb'", "'phed'", "'placeholderimage'", "'playtest'", 
                     "'scryland'", "'setextension'", "'shadowland'", "'shockland'", 
                     "'slowland'", "'snarl'", "'storageland'", "'surveilland'", 
                     "'tangoland'", "'traditional'", "'tricycleland'", "'trikeland'", 
                     "'triland'", "'triome'", "'typical'", "'upsidedown'", 
                     "'upsidedownback'", "'standard'", "'future'", "'timeless'", 
                     "'gladiator'", "'pioneer'", "'modern'", "'legacy'", 
                     "'pauper'", "'vintage'", "'standardbrawl'", "'brawl'", 
                     "'paupercommander'", "'duel'", "'oldschool'", "'premodern'", 
                     "'predh'", "'paper'", "'mtgo'", "'arena'", "'common'", 
                     "'uncommon'", "'rare'", "'special'", "'mythic'", "'bonus'", 
                     "'even'", "'odd'", "'a'", "'art'", "'atag'", "'arttag'", 
                     "'b'", "'block'", "'border'", "'c'", "'cn'", "'number'", 
                     "'cube'", "'date'", "'devotion'", "'e'", "'edition'", 
                     "'fo'", "'fulloracle'", "'ft'", "'flavor'", "'function'", 
                     "'otag'", "'oracletag'", "'id'", "'identity'", "'illustrations'", 
                     "'in'", "'keyword'", "'kw'", "'lang'", "'language'", 
                     "'loy'", "'loyalty'", "'m'", "'mana'", "'n'", "'o'", 
                     "'oracle'", "'paperprints'", "'papersets'", "'pow'", 
                     "'pt'", "'powtou'", "'produces'", "'r'", "'u'", "'s'", 
                     "'sets'", "'stamp'", "'st'", "'t'", "'type'", "'tou'", 
                     "'cheapest'", "'wm'", "'watermark'", "'year'" ]

    symbolicNames = [ "<INVALID>", "LPAREN", "RPAREN", "NEG", "BANG", "COLON", 
                      "NEQ", "GTE", "LTE", "EQ", "GT", "LT", "OR", "UNIQUE", 
                      "DISPLAY", "ORDER", "DIRECTION", "PREFER", "INCLUDE", 
                      "IS", "NOT", "F", "FORMAT", "BANNED", "RESTRICTED", 
                      "GAME", "RARITY", "MV", "MANAVALUE", "CARDS", "PRINTS", 
                      "GRID", "CHECKLIST", "FULL", "TEXT", "ASC", "DESC", 
                      "EXTRAS", "ARTIST", "ARTISTS", "CMC", "POWER", "TOUGHNESS", 
                      "SET", "NAME", "USD", "TIX", "EUR", "COLOR", "WHITE", 
                      "BLUE", "BLACK", "RED", "GREEN", "COLORLESS", "MULTICOLOR", 
                      "AZORIUS", "DIMIR", "RAKDOS", "GRUUL", "SELESNYA", 
                      "ORZHOV", "IZZET", "GOLGARI", "BOROS", "SIMIC", "BANT", 
                      "ESPER", "GRIXIS", "JUND", "NAYA", "ABZAN", "JESKAI", 
                      "SULTAI", "MARDU", "TEMUR", "QUANDRIX", "PRISMARI", 
                      "WITHERBLOOM", "LOREHOLD", "SILVERQUILL", "CHAOS", 
                      "AGGRESSION", "ALTRUISM", "GROWTH", "ARTIFICE", "RELEASED", 
                      "SPOILED", "EDHREC", "PENNY", "REVIEW", "OLDEST", 
                      "NEWEST", "USD_LOW", "USD_HIGH", "TIX_LOW", "TIX_HIGH", 
                      "EUR_LOW", "EUR_HIGH", "PROMO", "DEFAULT", "ATYPICAL", 
                      "UNIVERSESBEYOND", "UB", "NOTUNIVERSESBEYOND", "NOTUB", 
                      "INDICATOR", "HYBRID", "PHYREXIAN", "SPLIT", "FLIP", 
                      "TRANSFORM", "TDFC", "MELD", "MELDPART", "MELDRESULT", 
                      "LEVELER", "DFC", "MDFC", "SPELL", "PERMANENT", "HISTORIC", 
                      "PARTY", "OUTLAW", "MODAL", "VANILLA", "FRENCHVANILLA", 
                      "BEAR", "MANLAND", "FUNNY", "BOOSTER", "PLANESWALKER_DECK", 
                      "LEAGUE", "BUYABOX", "GIFTBOX", "INTRO_PACK", "GAMEDAY", 
                      "PRERELEASE", "RELEASE", "FNM", "JUDGE_GIFT", "ARENA_LEAGUE", 
                      "PLAYER_REWARDS", "MEDIA_INSERT", "INSTORE", "CONVENTION", 
                      "SET_PROMO", "COMMANDER", "BRAWLER", "COMPANION", 
                      "DUELCOMMANDER", "OATHBREAKER", "PARTNER", "GAMECHANGER", 
                      "RESERVED", "NEW", "OLD", "NONFOIL", "FOIL", "ETCHED", 
                      "GLOSSY", "HIRES", "DIGITAL", "ALCHEMY", "REBALANCED", 
                      "SPOTLIGHT", "SCRYFALLPREVIEW", "REPRINT", "FF7", 
                      "FF", "NEWINPAUPER", "DATESTAMPED", "ADVENTURE", "ARENAID", 
                      "ARTISTMISPRINT", "ARTSERIES", "AUGMENTATION", "BACK", 
                      "BEGINNERBOX", "BORDERLESS", "BRAWLCOMMANDER", "CARDMARKET", 
                      "CI", "CLASS", "COLORSHIFTED", "CONTENTWARNING", "COVERED", 
                      "DOUBLESIDED", "ENGLISHART", "ETB", "ETCH", "EXTENDED", 
                      "EXTRA", "FBB", "FIRSTPRINT", "FLAVORNAME", "FULLART", 
                      "FWB", "ILLUSTRATION", "FF1", "FF10", "FF11", "FF12", 
                      "FF13", "FF14", "FF15", "FF16", "FF2", "FF3", "FF4", 
                      "FF5", "FF6", "INTROPACK", "FF8", "FF9", "FFI", "FFII", 
                      "FFIII", "FFIV", "FFIX", "FFV", "FFVI", "FFVII", "FFVIII", 
                      "FFX", "FFXI", "FFXII", "FFXIII", "FFXIV", "FFXV", 
                      "FFXVI", "FINALFANTASY", "INVITATIONAL", "LIGHTS", 
                      "LOCALIZEDNAME", "MASTERPIECE", "MTGOID", "MULTIVERSE", 
                      "ONLYPRINT", "OVERSIZED", "PAPERART", "PHYREXIA", 
                      "PLANAR", "PLANESWALKERDECK", "PRINTEDTEXT", "RELATED", 
                      "REVERSIBLE", "SHOWCASE", "SPELLBOOK", "SPIKEY", "SPLITMANA", 
                      "STAMPED", "STARTERCOLLECTION", "STARTERDECK", "STORY", 
                      "TCGPLAYER", "TEXTLESS", "TOKEN", "TOMBSTONE", "TRANSLUCENT", 
                      "VARIATION", "ALTERNATE", "AMPERSAND", "ARCHENEMY", 
                      "ARCHIVAL", "ARENALEAGUE", "BOB", "BOOSTERFUN", "BOX", 
                      "BOXTOPPER", "BRAWLDECK", "BUNDLE", "BURSTFOIL", "CHOCOBOTRACKFOIL", 
                      "CHRIMBY", "COMMANDERPARTY", "COMMANDERPROMO", "CONCEPT", 
                      "CONFETTIFOIL", "CONJUREONLY", "COSMICFOIL", "CUTE", 
                      "DEN", "DOUBLEEXPOSURE", "DOUBLERAINBOW", "DRACULASERIES", 
                      "DRAFTINNOVATION", "DRAFTWEEKEND", "DUELDECK", "DUELS", 
                      "ESCAPED", "EVENT", "FINKEL", "FIRSTPLACEFOIL", "FIXED", 
                      "FRAMEODDITY", "FROMTHEVAULT", "FULLTEXT", "FUTURESHIFTED", 
                      "GALAXYFOIL", "GARY", "GATEWAY", "GILDED", "GODZILLASERIES", 
                      "HALOFOIL", "HEADLINER", "HORIZ", "IMAGEQA", "IMAGINE", 
                      "JPWALKER", "JUDGEGIFT", "JUMPSTART", "LISTWHITE", 
                      "LOCALIZEDIMAGE", "LOSTLEGENDS", "MAGICSPOTLIGHT", 
                      "MASTERS", "MB2", "MEDIAINSERT", "MEMORABILIA", "METAL", 
                      "MISPRINT", "MOM", "MOONLITLAND", "MULTIPLAYER", "NEONINK", 
                      "OILSLICK", "OPENHOUSE", "PIKULA", "PLANECHASE", "PLASTIC", 
                      "PLAYERREWARDS", "PLAYPROMO", "PORTAL", "PORTRAIT", 
                      "POSTER", "PREMIERESHOP", "PREMIUMDECK", "PROMOPACK", 
                      "RAINBOWFOIL", "RAISEDFOIL", "RESALE", "RIPPLEFOIL", 
                      "SCANNEEDED", "SCENE", "SCHINESEALTART", "SCROLL", 
                      "SERIALIZED", "SETPROMO", "SINGULARITYFOIL", "SLDBONUS", 
                      "SOURCEMATERIAL", "STARTER", "STEPANDCOMPLEAT", "STORECHAMPIONSHIP", 
                      "TEXTURED", "THEMEPACK", "THICK", "TIMESHIFTED", "TOURNEY", 
                      "TREASURECHEST", "TRON", "UNSET", "USELESS", "VANGUARD", 
                      "VAULT", "VERT", "WANTED", "WIZARDSPLAYNETWORK", "ABNORMAL", 
                      "BASELINE", "BATTLELAND", "BELZENLOK", "BICYCLELAND", 
                      "BIKELAND", "BONDLAND", "BOUNCELAND", "CANLAND", "CANOPYLAND", 
                      "CHECKLAND", "CORE", "CREATURELAND", "CYCLELAND", 
                      "DUAL", "EXPANSION", "FASTLAND", "FETCHLAND", "FILTERLAND", 
                      "FINALFANTASY1", "FINALFANTASY10", "FINALFANTASY11", 
                      "FINALFANTASY12", "FINALFANTASY13", "FINALFANTASY14", 
                      "FINALFANTASY15", "FINALFANTASY16", "FINALFANTASY2", 
                      "FINALFANTASY3", "FINALFANTASY4", "FINALFANTASY5", 
                      "FINALFANTASY6", "FINALFANTASY7", "FINALFANTASY8", 
                      "FINALFANTASY9", "FINALFANTASYI", "FINALFANTASYII", 
                      "FINALFANTASYIII", "FINALFANTASYIV", "FINALFANTASYIX", 
                      "FINALFANTASYV", "FINALFANTASYVI", "FINALFANTASYVII", 
                      "FINALFANTASYVIII", "FINALFANTASYX", "FINALFANTASYXI", 
                      "FINALFANTASYXII", "FINALFANTASYXIII", "FINALFANTASYXIV", 
                      "FINALFANTASYXV", "FINALFANTASYXVI", "FIRSTPRINTING", 
                      "FMB1", "GAINLAND", "HALO", "KAROO", "MB1", "NONDEFAULT", 
                      "NONTRADITIONAL", "NORMAL", "ODDFRAME", "PAGL", "PAINLAND", 
                      "PATHWAY", "PCTB", "PHED", "PLACEHOLDERIMAGE", "PLAYTEST", 
                      "SCRYLAND", "SETEXTENSION", "SHADOWLAND", "SHOCKLAND", 
                      "SLOWLAND", "SNARL", "STORAGELAND", "SURVEILLAND", 
                      "TANGOLAND", "TRADITIONAL", "TRICYCLELAND", "TRIKELAND", 
                      "TRILAND", "TRIOME", "TYPICAL", "UPSIDEDOWN", "UPSIDEDOWNBACK", 
                      "STANDARD", "FUTURE", "TIMELESS", "GLADIATOR", "PIONEER", 
                      "MODERN", "LEGACY", "PAUPER", "VINTAGE", "STANDARDBRAWL", 
                      "BRAWL", "PAUPERCOMMANDER", "DUEL", "OLDSCHOOL", "PREMODERN", 
                      "PREDH", "PAPER", "MTGO", "ARENA", "COMMON", "UNCOMMON", 
                      "RARE", "SPECIAL", "MYTHIC", "BONUS", "EVEN", "ODD", 
                      "A", "ART", "ATAG", "ARTTAG", "B", "BLOCK", "BORDER", 
                      "C", "CN", "NUMBER_KEY", "CUBE", "DATE", "DEVOTION", 
                      "E", "EDITION", "FO", "FULLORACLE", "FT", "FLAVOR", 
                      "FUNCTION", "OTAG", "ORACLETAG", "ID", "IDENTITY", 
                      "ILLUSTRATIONS", "IN", "KEYWORD", "KW", "LANG", "LANGUAGE", 
                      "LOY", "LOYALTY", "M", "MANA", "N", "O", "ORACLE", 
                      "PAPERPRINTS", "PAPERSETS", "POW", "PT", "POWTOU", 
                      "PRODUCES", "R", "U", "S", "SETS", "STAMP", "ST", 
                      "T", "TYPE", "TOU", "CHEAPEST", "WM", "WATERMARK", 
                      "YEAR", "NUMBER", "QUOTED_TEXT", "REGEX", "COLOR_SET", 
                      "WORD", "BARE_VALUE", "WS" ]

    RULE_start = 0
    RULE_topExpr = 1
    RULE_topAndExpr = 2
    RULE_topFactor = 3
    RULE_topGroup = 4
    RULE_topTerm = 5
    RULE_parenExpr = 6
    RULE_parenAndExpr = 7
    RULE_parenFactor = 8
    RULE_parenGroup = 9
    RULE_parenTerm = 10
    RULE_topAtom = 11
    RULE_displayAtom = 12
    RULE_parenAtom = 13
    RULE_nonDisplayAtom = 14
    RULE_exactName = 15
    RULE_uniqueTerm = 16
    RULE_uniqueKey = 17
    RULE_uniqueValue = 18
    RULE_displayTerm = 19
    RULE_displayValue = 20
    RULE_orderTerm = 21
    RULE_orderValue = 22
    RULE_directionTerm = 23
    RULE_directionValue = 24
    RULE_preferTerm = 25
    RULE_preferValue = 26
    RULE_includeTerm = 27
    RULE_isTerm = 28
    RULE_notTerm = 29
    RULE_isValue = 30
    RULE_formatTerm = 31
    RULE_bannedTerm = 32
    RULE_restrictedTerm = 33
    RULE_formatValue = 34
    RULE_gameTerm = 35
    RULE_gameValueToken = 36
    RULE_colorTerm = 37
    RULE_colorValue = 38
    RULE_rarityTerm = 39
    RULE_rarityValue = 40
    RULE_mvTerm = 41
    RULE_genericTerm = 42
    RULE_genericKey = 43
    RULE_compOp = 44
    RULE_genericValue = 45
    RULE_quotedText = 46
    RULE_regex = 47
    RULE_word = 48
    RULE_bareValue = 49

    ruleNames =  [ "start", "topExpr", "topAndExpr", "topFactor", "topGroup", 
                   "topTerm", "parenExpr", "parenAndExpr", "parenFactor", 
                   "parenGroup", "parenTerm", "topAtom", "displayAtom", 
                   "parenAtom", "nonDisplayAtom", "exactName", "uniqueTerm", 
                   "uniqueKey", "uniqueValue", "displayTerm", "displayValue", 
                   "orderTerm", "orderValue", "directionTerm", "directionValue", 
                   "preferTerm", "preferValue", "includeTerm", "isTerm", 
                   "notTerm", "isValue", "formatTerm", "bannedTerm", "restrictedTerm", 
                   "formatValue", "gameTerm", "gameValueToken", "colorTerm", 
                   "colorValue", "rarityTerm", "rarityValue", "mvTerm", 
                   "genericTerm", "genericKey", "compOp", "genericValue", 
                   "quotedText", "regex", "word", "bareValue" ]

    EOF = Token.EOF
    LPAREN=1
    RPAREN=2
    NEG=3
    BANG=4
    COLON=5
    NEQ=6
    GTE=7
    LTE=8
    EQ=9
    GT=10
    LT=11
    OR=12
    UNIQUE=13
    DISPLAY=14
    ORDER=15
    DIRECTION=16
    PREFER=17
    INCLUDE=18
    IS=19
    NOT=20
    F=21
    FORMAT=22
    BANNED=23
    RESTRICTED=24
    GAME=25
    RARITY=26
    MV=27
    MANAVALUE=28
    CARDS=29
    PRINTS=30
    GRID=31
    CHECKLIST=32
    FULL=33
    TEXT=34
    ASC=35
    DESC=36
    EXTRAS=37
    ARTIST=38
    ARTISTS=39
    CMC=40
    POWER=41
    TOUGHNESS=42
    SET=43
    NAME=44
    USD=45
    TIX=46
    EUR=47
    COLOR=48
    WHITE=49
    BLUE=50
    BLACK=51
    RED=52
    GREEN=53
    COLORLESS=54
    MULTICOLOR=55
    AZORIUS=56
    DIMIR=57
    RAKDOS=58
    GRUUL=59
    SELESNYA=60
    ORZHOV=61
    IZZET=62
    GOLGARI=63
    BOROS=64
    SIMIC=65
    BANT=66
    ESPER=67
    GRIXIS=68
    JUND=69
    NAYA=70
    ABZAN=71
    JESKAI=72
    SULTAI=73
    MARDU=74
    TEMUR=75
    QUANDRIX=76
    PRISMARI=77
    WITHERBLOOM=78
    LOREHOLD=79
    SILVERQUILL=80
    CHAOS=81
    AGGRESSION=82
    ALTRUISM=83
    GROWTH=84
    ARTIFICE=85
    RELEASED=86
    SPOILED=87
    EDHREC=88
    PENNY=89
    REVIEW=90
    OLDEST=91
    NEWEST=92
    USD_LOW=93
    USD_HIGH=94
    TIX_LOW=95
    TIX_HIGH=96
    EUR_LOW=97
    EUR_HIGH=98
    PROMO=99
    DEFAULT=100
    ATYPICAL=101
    UNIVERSESBEYOND=102
    UB=103
    NOTUNIVERSESBEYOND=104
    NOTUB=105
    INDICATOR=106
    HYBRID=107
    PHYREXIAN=108
    SPLIT=109
    FLIP=110
    TRANSFORM=111
    TDFC=112
    MELD=113
    MELDPART=114
    MELDRESULT=115
    LEVELER=116
    DFC=117
    MDFC=118
    SPELL=119
    PERMANENT=120
    HISTORIC=121
    PARTY=122
    OUTLAW=123
    MODAL=124
    VANILLA=125
    FRENCHVANILLA=126
    BEAR=127
    MANLAND=128
    FUNNY=129
    BOOSTER=130
    PLANESWALKER_DECK=131
    LEAGUE=132
    BUYABOX=133
    GIFTBOX=134
    INTRO_PACK=135
    GAMEDAY=136
    PRERELEASE=137
    RELEASE=138
    FNM=139
    JUDGE_GIFT=140
    ARENA_LEAGUE=141
    PLAYER_REWARDS=142
    MEDIA_INSERT=143
    INSTORE=144
    CONVENTION=145
    SET_PROMO=146
    COMMANDER=147
    BRAWLER=148
    COMPANION=149
    DUELCOMMANDER=150
    OATHBREAKER=151
    PARTNER=152
    GAMECHANGER=153
    RESERVED=154
    NEW=155
    OLD=156
    NONFOIL=157
    FOIL=158
    ETCHED=159
    GLOSSY=160
    HIRES=161
    DIGITAL=162
    ALCHEMY=163
    REBALANCED=164
    SPOTLIGHT=165
    SCRYFALLPREVIEW=166
    REPRINT=167
    FF7=168
    FF=169
    NEWINPAUPER=170
    DATESTAMPED=171
    ADVENTURE=172
    ARENAID=173
    ARTISTMISPRINT=174
    ARTSERIES=175
    AUGMENTATION=176
    BACK=177
    BEGINNERBOX=178
    BORDERLESS=179
    BRAWLCOMMANDER=180
    CARDMARKET=181
    CI=182
    CLASS=183
    COLORSHIFTED=184
    CONTENTWARNING=185
    COVERED=186
    DOUBLESIDED=187
    ENGLISHART=188
    ETB=189
    ETCH=190
    EXTENDED=191
    EXTRA=192
    FBB=193
    FIRSTPRINT=194
    FLAVORNAME=195
    FULLART=196
    FWB=197
    ILLUSTRATION=198
    FF1=199
    FF10=200
    FF11=201
    FF12=202
    FF13=203
    FF14=204
    FF15=205
    FF16=206
    FF2=207
    FF3=208
    FF4=209
    FF5=210
    FF6=211
    INTROPACK=212
    FF8=213
    FF9=214
    FFI=215
    FFII=216
    FFIII=217
    FFIV=218
    FFIX=219
    FFV=220
    FFVI=221
    FFVII=222
    FFVIII=223
    FFX=224
    FFXI=225
    FFXII=226
    FFXIII=227
    FFXIV=228
    FFXV=229
    FFXVI=230
    FINALFANTASY=231
    INVITATIONAL=232
    LIGHTS=233
    LOCALIZEDNAME=234
    MASTERPIECE=235
    MTGOID=236
    MULTIVERSE=237
    ONLYPRINT=238
    OVERSIZED=239
    PAPERART=240
    PHYREXIA=241
    PLANAR=242
    PLANESWALKERDECK=243
    PRINTEDTEXT=244
    RELATED=245
    REVERSIBLE=246
    SHOWCASE=247
    SPELLBOOK=248
    SPIKEY=249
    SPLITMANA=250
    STAMPED=251
    STARTERCOLLECTION=252
    STARTERDECK=253
    STORY=254
    TCGPLAYER=255
    TEXTLESS=256
    TOKEN=257
    TOMBSTONE=258
    TRANSLUCENT=259
    VARIATION=260
    ALTERNATE=261
    AMPERSAND=262
    ARCHENEMY=263
    ARCHIVAL=264
    ARENALEAGUE=265
    BOB=266
    BOOSTERFUN=267
    BOX=268
    BOXTOPPER=269
    BRAWLDECK=270
    BUNDLE=271
    BURSTFOIL=272
    CHOCOBOTRACKFOIL=273
    CHRIMBY=274
    COMMANDERPARTY=275
    COMMANDERPROMO=276
    CONCEPT=277
    CONFETTIFOIL=278
    CONJUREONLY=279
    COSMICFOIL=280
    CUTE=281
    DEN=282
    DOUBLEEXPOSURE=283
    DOUBLERAINBOW=284
    DRACULASERIES=285
    DRAFTINNOVATION=286
    DRAFTWEEKEND=287
    DUELDECK=288
    DUELS=289
    ESCAPED=290
    EVENT=291
    FINKEL=292
    FIRSTPLACEFOIL=293
    FIXED=294
    FRAMEODDITY=295
    FROMTHEVAULT=296
    FULLTEXT=297
    FUTURESHIFTED=298
    GALAXYFOIL=299
    GARY=300
    GATEWAY=301
    GILDED=302
    GODZILLASERIES=303
    HALOFOIL=304
    HEADLINER=305
    HORIZ=306
    IMAGEQA=307
    IMAGINE=308
    JPWALKER=309
    JUDGEGIFT=310
    JUMPSTART=311
    LISTWHITE=312
    LOCALIZEDIMAGE=313
    LOSTLEGENDS=314
    MAGICSPOTLIGHT=315
    MASTERS=316
    MB2=317
    MEDIAINSERT=318
    MEMORABILIA=319
    METAL=320
    MISPRINT=321
    MOM=322
    MOONLITLAND=323
    MULTIPLAYER=324
    NEONINK=325
    OILSLICK=326
    OPENHOUSE=327
    PIKULA=328
    PLANECHASE=329
    PLASTIC=330
    PLAYERREWARDS=331
    PLAYPROMO=332
    PORTAL=333
    PORTRAIT=334
    POSTER=335
    PREMIERESHOP=336
    PREMIUMDECK=337
    PROMOPACK=338
    RAINBOWFOIL=339
    RAISEDFOIL=340
    RESALE=341
    RIPPLEFOIL=342
    SCANNEEDED=343
    SCENE=344
    SCHINESEALTART=345
    SCROLL=346
    SERIALIZED=347
    SETPROMO=348
    SINGULARITYFOIL=349
    SLDBONUS=350
    SOURCEMATERIAL=351
    STARTER=352
    STEPANDCOMPLEAT=353
    STORECHAMPIONSHIP=354
    TEXTURED=355
    THEMEPACK=356
    THICK=357
    TIMESHIFTED=358
    TOURNEY=359
    TREASURECHEST=360
    TRON=361
    UNSET=362
    USELESS=363
    VANGUARD=364
    VAULT=365
    VERT=366
    WANTED=367
    WIZARDSPLAYNETWORK=368
    ABNORMAL=369
    BASELINE=370
    BATTLELAND=371
    BELZENLOK=372
    BICYCLELAND=373
    BIKELAND=374
    BONDLAND=375
    BOUNCELAND=376
    CANLAND=377
    CANOPYLAND=378
    CHECKLAND=379
    CORE=380
    CREATURELAND=381
    CYCLELAND=382
    DUAL=383
    EXPANSION=384
    FASTLAND=385
    FETCHLAND=386
    FILTERLAND=387
    FINALFANTASY1=388
    FINALFANTASY10=389
    FINALFANTASY11=390
    FINALFANTASY12=391
    FINALFANTASY13=392
    FINALFANTASY14=393
    FINALFANTASY15=394
    FINALFANTASY16=395
    FINALFANTASY2=396
    FINALFANTASY3=397
    FINALFANTASY4=398
    FINALFANTASY5=399
    FINALFANTASY6=400
    FINALFANTASY7=401
    FINALFANTASY8=402
    FINALFANTASY9=403
    FINALFANTASYI=404
    FINALFANTASYII=405
    FINALFANTASYIII=406
    FINALFANTASYIV=407
    FINALFANTASYIX=408
    FINALFANTASYV=409
    FINALFANTASYVI=410
    FINALFANTASYVII=411
    FINALFANTASYVIII=412
    FINALFANTASYX=413
    FINALFANTASYXI=414
    FINALFANTASYXII=415
    FINALFANTASYXIII=416
    FINALFANTASYXIV=417
    FINALFANTASYXV=418
    FINALFANTASYXVI=419
    FIRSTPRINTING=420
    FMB1=421
    GAINLAND=422
    HALO=423
    KAROO=424
    MB1=425
    NONDEFAULT=426
    NONTRADITIONAL=427
    NORMAL=428
    ODDFRAME=429
    PAGL=430
    PAINLAND=431
    PATHWAY=432
    PCTB=433
    PHED=434
    PLACEHOLDERIMAGE=435
    PLAYTEST=436
    SCRYLAND=437
    SETEXTENSION=438
    SHADOWLAND=439
    SHOCKLAND=440
    SLOWLAND=441
    SNARL=442
    STORAGELAND=443
    SURVEILLAND=444
    TANGOLAND=445
    TRADITIONAL=446
    TRICYCLELAND=447
    TRIKELAND=448
    TRILAND=449
    TRIOME=450
    TYPICAL=451
    UPSIDEDOWN=452
    UPSIDEDOWNBACK=453
    STANDARD=454
    FUTURE=455
    TIMELESS=456
    GLADIATOR=457
    PIONEER=458
    MODERN=459
    LEGACY=460
    PAUPER=461
    VINTAGE=462
    STANDARDBRAWL=463
    BRAWL=464
    PAUPERCOMMANDER=465
    DUEL=466
    OLDSCHOOL=467
    PREMODERN=468
    PREDH=469
    PAPER=470
    MTGO=471
    ARENA=472
    COMMON=473
    UNCOMMON=474
    RARE=475
    SPECIAL=476
    MYTHIC=477
    BONUS=478
    EVEN=479
    ODD=480
    A=481
    ART=482
    ATAG=483
    ARTTAG=484
    B=485
    BLOCK=486
    BORDER=487
    C=488
    CN=489
    NUMBER_KEY=490
    CUBE=491
    DATE=492
    DEVOTION=493
    E=494
    EDITION=495
    FO=496
    FULLORACLE=497
    FT=498
    FLAVOR=499
    FUNCTION=500
    OTAG=501
    ORACLETAG=502
    ID=503
    IDENTITY=504
    ILLUSTRATIONS=505
    IN=506
    KEYWORD=507
    KW=508
    LANG=509
    LANGUAGE=510
    LOY=511
    LOYALTY=512
    M=513
    MANA=514
    N=515
    O=516
    ORACLE=517
    PAPERPRINTS=518
    PAPERSETS=519
    POW=520
    PT=521
    POWTOU=522
    PRODUCES=523
    R=524
    U=525
    S=526
    SETS=527
    STAMP=528
    ST=529
    T=530
    TYPE=531
    TOU=532
    CHEAPEST=533
    WM=534
    WATERMARK=535
    YEAR=536
    NUMBER=537
    QUOTED_TEXT=538
    REGEX=539
    COLOR_SET=540
    WORD=541
    BARE_VALUE=542
    WS=543

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def topExpr(self):
            return self.getTypedRuleContext(ScryfallQueryParser.TopExprContext,0)


        def EOF(self):
            return self.getToken(ScryfallQueryParser.EOF, 0)

        def getRuleIndex(self):
            return ScryfallQueryParser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStart" ):
                return visitor.visitStart(self)
            else:
                return visitor.visitChildren(self)




    def start(self):

        localctx = ScryfallQueryParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.topExpr()
            self.state = 101
            self.match(ScryfallQueryParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TopExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def topAndExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ScryfallQueryParser.TopAndExprContext)
            else:
                return self.getTypedRuleContext(ScryfallQueryParser.TopAndExprContext,i)


        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(ScryfallQueryParser.OR)
            else:
                return self.getToken(ScryfallQueryParser.OR, i)

        def getRuleIndex(self):
            return ScryfallQueryParser.RULE_topExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTopExpr" ):
                listener.enterTopExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTopExpr" ):
                listener.exitTopExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTopExpr" ):
                return visitor.visitTopExpr(self)
            else:
                return visitor.visitChildren(self)




    def topExpr(self):

        localctx = ScryfallQueryParser.TopExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_topExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self.topAndExpr()
            self.state = 108
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==12:
                self.state = 104
                self.match(ScryfallQueryParser.OR)
                self.state = 105
                self.topAndExpr()
                self.state = 110
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TopAndExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def topFactor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ScryfallQueryParser.TopFactorContext)
            else:
                return self.getTypedRuleContext(ScryfallQueryParser.TopFactorContext,i)


        def getRuleIndex(self):
            return ScryfallQueryParser.RULE_topAndExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTopAndExpr" ):
                listener.enterTopAndExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTopAndExpr" ):
                listener.exitTopAndExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTopAndExpr" ):
                return visitor.visitTopAndExpr(self)
            else:
                return visitor.visitChildren(self)




    def topAndExpr(self):

        localctx = ScryfallQueryParser.TopAndExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_topAndExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 111
                self.topFactor()
                self.state = 114 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 561577174491162) != 0) or _la==155 or ((((_la - 481)) & ~0x3f) == 0 and ((1 << (_la - 481)) & 1945537446838009855) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TopFactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def topGroup(self):
            return self.getTypedRuleContext(ScryfallQueryParser.TopGroupContext,0)


        def topTerm(self):
            return self.getTypedRuleContext(ScryfallQueryParser.TopTermContext,0)


        def getRuleIndex(self):
            return ScryfallQueryParser.RULE_topFactor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTopFactor" ):
                listener.enterTopFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTopFactor" ):
                listener.exitTopFactor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTopFactor" ):
                return visitor.visitTopFactor(self)
            else:
                return visitor.visitChildren(self)




    def topFactor(self):

        localctx = ScryfallQueryParser.TopFactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_topFactor)
        try:
            self.state = 118
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 116
                self.topGroup()
                pass
            elif token in [3, 4, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 30, 38, 39, 41, 42, 43, 44, 45, 46, 47, 48, 155, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 538, 540, 541]:
                self.enterOuterAlt(localctx, 2)
                self.state = 117
                self.topTerm()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TopGroupContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(ScryfallQueryParser.LPAREN, 0)

        def parenExpr(self):
            return self.getTypedRuleContext(ScryfallQueryParser.ParenExprContext,0)


        def RPAREN(self):
            return self.getToken(ScryfallQueryParser.RPAREN, 0)

        def getRuleIndex(self):
            return ScryfallQueryParser.RULE_topGroup

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTopGroup" ):
                listener.enterTopGroup(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTopGroup" ):
                listener.exitTopGroup(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTopGroup" ):
                return visitor.visitTopGroup(self)
            else:
                return visitor.visitChildren(self)




    def topGroup(self):

        localctx = ScryfallQueryParser.TopGroupContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_topGroup)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self.match(ScryfallQueryParser.LPAREN)
            self.state = 121
            self.parenExpr()
            self.state = 122
            self.match(ScryfallQueryParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TopTermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def topAtom(self):
            return self.getTypedRuleContext(ScryfallQueryParser.TopAtomContext,0)


        def NEG(self):
            return self.getToken(ScryfallQueryParser.NEG, 0)

        def getRuleIndex(self):
            return ScryfallQueryParser.RULE_topTerm

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTopTerm" ):
                listener.enterTopTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTopTerm" ):
                listener.exitTopTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTopTerm" ):
                return visitor.visitTopTerm(self)
            else:
                return visitor.visitChildren(self)




    def topTerm(self):

        localctx = ScryfallQueryParser.TopTermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_topTerm)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 124
                self.match(ScryfallQueryParser.NEG)


            self.state = 127
            self.topAtom()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParenExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parenAndExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ScryfallQueryParser.ParenAndExprContext)
            else:
                return self.getTypedRuleContext(ScryfallQueryParser.ParenAndExprContext,i)


        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(ScryfallQueryParser.OR)
            else:
                return self.getToken(ScryfallQueryParser.OR, i)

        def getRuleIndex(self):
            return ScryfallQueryParser.RULE_parenExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenExpr" ):
                listener.enterParenExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenExpr" ):
                listener.exitParenExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenExpr" ):
                return visitor.visitParenExpr(self)
            else:
                return visitor.visitChildren(self)




    def parenExpr(self):

        localctx = ScryfallQueryParser.ParenExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_parenExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self.parenAndExpr()
            self.state = 134
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==12:
                self.state = 130
                self.match(ScryfallQueryParser.OR)
                self.state = 131
                self.parenAndExpr()
                self.state = 136
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParenAndExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parenFactor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ScryfallQueryParser.ParenFactorContext)
            else:
                return self.getTypedRuleContext(ScryfallQueryParser.ParenFactorContext,i)


        def getRuleIndex(self):
            return ScryfallQueryParser.RULE_parenAndExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenAndExpr" ):
                listener.enterParenAndExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenAndExpr" ):
                listener.exitParenAndExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenAndExpr" ):
                return visitor.visitParenAndExpr(self)
            else:
                return visitor.visitChildren(self)




    def parenAndExpr(self):

        localctx = ScryfallQueryParser.ParenAndExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_parenAndExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 137
                self.parenFactor()
                self.state = 140 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 561577174237210) != 0) or _la==155 or ((((_la - 481)) & ~0x3f) == 0 and ((1 << (_la - 481)) & 1945537446838009855) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParenFactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parenGroup(self):
            return self.getTypedRuleContext(ScryfallQueryParser.ParenGroupContext,0)


        def parenTerm(self):
            return self.getTypedRuleContext(ScryfallQueryParser.ParenTermContext,0)


        def getRuleIndex(self):
            return ScryfallQueryParser.RULE_parenFactor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenFactor" ):
                listener.enterParenFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenFactor" ):
                listener.exitParenFactor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenFactor" ):
                return visitor.visitParenFactor(self)
            else:
                return visitor.visitChildren(self)




    def parenFactor(self):

        localctx = ScryfallQueryParser.ParenFactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_parenFactor)
        try:
            self.state = 144
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 142
                self.parenGroup()
                pass
            elif token in [3, 4, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 30, 38, 39, 41, 42, 43, 44, 45, 46, 47, 48, 155, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 538, 540, 541]:
                self.enterOuterAlt(localctx, 2)
                self.state = 143
                self.parenTerm()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParenGroupContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(ScryfallQueryParser.LPAREN, 0)

        def parenExpr(self):
            return self.getTypedRuleContext(ScryfallQueryParser.ParenExprContext,0)


        def RPAREN(self):
            return self.getToken(ScryfallQueryParser.RPAREN, 0)

        def getRuleIndex(self):
            return ScryfallQueryParser.RULE_parenGroup

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenGroup" ):
                listener.enterParenGroup(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenGroup" ):
                listener.exitParenGroup(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenGroup" ):
                return visitor.visitParenGroup(self)
            else:
                return visitor.visitChildren(self)




    def parenGroup(self):

        localctx = ScryfallQueryParser.ParenGroupContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_parenGroup)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self.match(ScryfallQueryParser.LPAREN)
            self.state = 147
            self.parenExpr()
            self.state = 148
            self.match(ScryfallQueryParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParenTermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parenAtom(self):
            return self.getTypedRuleContext(ScryfallQueryParser.ParenAtomContext,0)


        def NEG(self):
            return self.getToken(ScryfallQueryParser.NEG, 0)

        def getRuleIndex(self):
            return ScryfallQueryParser.RULE_parenTerm

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenTerm" ):
                listener.enterParenTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenTerm" ):
                listener.exitParenTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenTerm" ):
                return visitor.visitParenTerm(self)
            else:
                return visitor.visitChildren(self)




    def parenTerm(self):

        localctx = ScryfallQueryParser.ParenTermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_parenTerm)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 150
                self.match(ScryfallQueryParser.NEG)


            self.state = 153
            self.parenAtom()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TopAtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def displayAtom(self):
            return self.getTypedRuleContext(ScryfallQueryParser.DisplayAtomContext,0)


        def nonDisplayAtom(self):
            return self.getTypedRuleContext(ScryfallQueryParser.NonDisplayAtomContext,0)


        def getRuleIndex(self):
            return ScryfallQueryParser.RULE_topAtom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTopAtom" ):
                listener.enterTopAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTopAtom" ):
                listener.exitTopAtom(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTopAtom" ):
                return visitor.visitTopAtom(self)
            else:
                return visitor.visitChildren(self)




    def topAtom(self):

        localctx = ScryfallQueryParser.TopAtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_topAtom)
        try:
            self.state = 157
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13, 14, 15, 16, 17]:
                self.enterOuterAlt(localctx, 1)
                self.state = 155
                self.displayAtom()
                pass
            elif token in [4, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 30, 38, 39, 41, 42, 43, 44, 45, 46, 47, 48, 155, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 538, 540, 541]:
                self.enterOuterAlt(localctx, 2)
                self.state = 156
                self.nonDisplayAtom()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DisplayAtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def uniqueTerm(self):
            return self.getTypedRuleContext(ScryfallQueryParser.UniqueTermContext,0)


        def displayTerm(self):
            return self.getTypedRuleContext(ScryfallQueryParser.DisplayTermContext,0)


        def orderTerm(self):
            return self.getTypedRuleContext(ScryfallQueryParser.OrderTermContext,0)


        def directionTerm(self):
            return self.getTypedRuleContext(ScryfallQueryParser.DirectionTermContext,0)


        def preferTerm(self):
            return self.getTypedRuleContext(ScryfallQueryParser.PreferTermContext,0)


        def getRuleIndex(self):
            return ScryfallQueryParser.RULE_displayAtom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDisplayAtom" ):
                listener.enterDisplayAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDisplayAtom" ):
                listener.exitDisplayAtom(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDisplayAtom" ):
                return visitor.visitDisplayAtom(self)
            else:
                return visitor.visitChildren(self)




    def displayAtom(self):

        localctx = ScryfallQueryParser.DisplayAtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_displayAtom)
        try:
            self.state = 164
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13]:
                self.enterOuterAlt(localctx, 1)
                self.state = 159
                self.uniqueTerm()
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 2)
                self.state = 160
                self.displayTerm()
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 3)
                self.state = 161
                self.orderTerm()
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 4)
                self.state = 162
                self.directionTerm()
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 5)
                self.state = 163
                self.preferTerm()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParenAtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def nonDisplayAtom(self):
            return self.getTypedRuleContext(ScryfallQueryParser.NonDisplayAtomContext,0)


        def getRuleIndex(self):
            return ScryfallQueryParser.RULE_parenAtom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenAtom" ):
                listener.enterParenAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenAtom" ):
                listener.exitParenAtom(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenAtom" ):
                return visitor.visitParenAtom(self)
            else:
                return visitor.visitChildren(self)




    def parenAtom(self):

        localctx = ScryfallQueryParser.ParenAtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_parenAtom)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self.nonDisplayAtom()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NonDisplayAtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exactName(self):
            return self.getTypedRuleContext(ScryfallQueryParser.ExactNameContext,0)


        def includeTerm(self):
            return self.getTypedRuleContext(ScryfallQueryParser.IncludeTermContext,0)


        def isTerm(self):
            return self.getTypedRuleContext(ScryfallQueryParser.IsTermContext,0)


        def notTerm(self):
            return self.getTypedRuleContext(ScryfallQueryParser.NotTermContext,0)


        def formatTerm(self):
            return self.getTypedRuleContext(ScryfallQueryParser.FormatTermContext,0)


        def bannedTerm(self):
            return self.getTypedRuleContext(ScryfallQueryParser.BannedTermContext,0)


        def restrictedTerm(self):
            return self.getTypedRuleContext(ScryfallQueryParser.RestrictedTermContext,0)


        def gameTerm(self):
            return self.getTypedRuleContext(ScryfallQueryParser.GameTermContext,0)


        def rarityTerm(self):
            return self.getTypedRuleContext(ScryfallQueryParser.RarityTermContext,0)


        def mvTerm(self):
            return self.getTypedRuleContext(ScryfallQueryParser.MvTermContext,0)


        def colorTerm(self):
            return self.getTypedRuleContext(ScryfallQueryParser.ColorTermContext,0)


        def genericTerm(self):
            return self.getTypedRuleContext(ScryfallQueryParser.GenericTermContext,0)


        def quotedText(self):
            return self.getTypedRuleContext(ScryfallQueryParser.QuotedTextContext,0)


        def word(self):
            return self.getTypedRuleContext(ScryfallQueryParser.WordContext,0)


        def getRuleIndex(self):
            return ScryfallQueryParser.RULE_nonDisplayAtom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNonDisplayAtom" ):
                listener.enterNonDisplayAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNonDisplayAtom" ):
                listener.exitNonDisplayAtom(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNonDisplayAtom" ):
                return visitor.visitNonDisplayAtom(self)
            else:
                return visitor.visitChildren(self)




    def nonDisplayAtom(self):

        localctx = ScryfallQueryParser.NonDisplayAtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_nonDisplayAtom)
        try:
            self.state = 182
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 168
                self.exactName()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 169
                self.includeTerm()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 170
                self.isTerm()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 171
                self.notTerm()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 172
                self.formatTerm()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 173
                self.bannedTerm()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 174
                self.restrictedTerm()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 175
                self.gameTerm()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 176
                self.rarityTerm()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 177
                self.mvTerm()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 178
                self.colorTerm()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 179
                self.genericTerm()
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 180
                self.quotedText()
                pass

            elif la_ == 14:
                self.enterOuterAlt(localctx, 14)
                self.state = 181
                self.word()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExactNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BANG(self):
            return self.getToken(ScryfallQueryParser.BANG, 0)

        def quotedText(self):
            return self.getTypedRuleContext(ScryfallQueryParser.QuotedTextContext,0)


        def word(self):
            return self.getTypedRuleContext(ScryfallQueryParser.WordContext,0)


        def getRuleIndex(self):
            return ScryfallQueryParser.RULE_exactName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExactName" ):
                listener.enterExactName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExactName" ):
                listener.exitExactName(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExactName" ):
                return visitor.visitExactName(self)
            else:
                return visitor.visitChildren(self)




    def exactName(self):

        localctx = ScryfallQueryParser.ExactNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_exactName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self.match(ScryfallQueryParser.BANG)
            self.state = 187
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [538]:
                self.state = 185
                self.quotedText()
                pass
            elif token in [540, 541]:
                self.state = 186
                self.word()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UniqueTermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def uniqueKey(self):
            return self.getTypedRuleContext(ScryfallQueryParser.UniqueKeyContext,0)


        def COLON(self):
            return self.getToken(ScryfallQueryParser.COLON, 0)

        def uniqueValue(self):
            return self.getTypedRuleContext(ScryfallQueryParser.UniqueValueContext,0)


        def getRuleIndex(self):
            return ScryfallQueryParser.RULE_uniqueTerm

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUniqueTerm" ):
                listener.enterUniqueTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUniqueTerm" ):
                listener.exitUniqueTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUniqueTerm" ):
                return visitor.visitUniqueTerm(self)
            else:
                return visitor.visitChildren(self)




    def uniqueTerm(self):

        localctx = ScryfallQueryParser.UniqueTermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_uniqueTerm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
            self.uniqueKey()
            self.state = 190
            self.match(ScryfallQueryParser.COLON)
            self.state = 191
            self.uniqueValue()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UniqueKeyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def UNIQUE(self):
            return self.getToken(ScryfallQueryParser.UNIQUE, 0)

        def getRuleIndex(self):
            return ScryfallQueryParser.RULE_uniqueKey

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUniqueKey" ):
                listener.enterUniqueKey(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUniqueKey" ):
                listener.exitUniqueKey(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUniqueKey" ):
                return visitor.visitUniqueKey(self)
            else:
                return visitor.visitChildren(self)




    def uniqueKey(self):

        localctx = ScryfallQueryParser.UniqueKeyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_uniqueKey)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
            self.match(ScryfallQueryParser.UNIQUE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UniqueValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CARDS(self):
            return self.getToken(ScryfallQueryParser.CARDS, 0)

        def PRINTS(self):
            return self.getToken(ScryfallQueryParser.PRINTS, 0)

        def ART(self):
            return self.getToken(ScryfallQueryParser.ART, 0)

        def getRuleIndex(self):
            return ScryfallQueryParser.RULE_uniqueValue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUniqueValue" ):
                listener.enterUniqueValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUniqueValue" ):
                listener.exitUniqueValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUniqueValue" ):
                return visitor.visitUniqueValue(self)
            else:
                return visitor.visitChildren(self)




    def uniqueValue(self):

        localctx = ScryfallQueryParser.UniqueValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_uniqueValue)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
            _la = self._input.LA(1)
            if not(_la==29 or _la==30 or _la==482):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DisplayTermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DISPLAY(self):
            return self.getToken(ScryfallQueryParser.DISPLAY, 0)

        def COLON(self):
            return self.getToken(ScryfallQueryParser.COLON, 0)

        def displayValue(self):
            return self.getTypedRuleContext(ScryfallQueryParser.DisplayValueContext,0)


        def getRuleIndex(self):
            return ScryfallQueryParser.RULE_displayTerm

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDisplayTerm" ):
                listener.enterDisplayTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDisplayTerm" ):
                listener.exitDisplayTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDisplayTerm" ):
                return visitor.visitDisplayTerm(self)
            else:
                return visitor.visitChildren(self)




    def displayTerm(self):

        localctx = ScryfallQueryParser.DisplayTermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_displayTerm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
            self.match(ScryfallQueryParser.DISPLAY)
            self.state = 198
            self.match(ScryfallQueryParser.COLON)
            self.state = 199
            self.displayValue()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DisplayValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GRID(self):
            return self.getToken(ScryfallQueryParser.GRID, 0)

        def CHECKLIST(self):
            return self.getToken(ScryfallQueryParser.CHECKLIST, 0)

        def FULL(self):
            return self.getToken(ScryfallQueryParser.FULL, 0)

        def TEXT(self):
            return self.getToken(ScryfallQueryParser.TEXT, 0)

        def getRuleIndex(self):
            return ScryfallQueryParser.RULE_displayValue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDisplayValue" ):
                listener.enterDisplayValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDisplayValue" ):
                listener.exitDisplayValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDisplayValue" ):
                return visitor.visitDisplayValue(self)
            else:
                return visitor.visitChildren(self)




    def displayValue(self):

        localctx = ScryfallQueryParser.DisplayValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_displayValue)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 201
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 32212254720) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OrderTermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ORDER(self):
            return self.getToken(ScryfallQueryParser.ORDER, 0)

        def COLON(self):
            return self.getToken(ScryfallQueryParser.COLON, 0)

        def orderValue(self):
            return self.getTypedRuleContext(ScryfallQueryParser.OrderValueContext,0)


        def getRuleIndex(self):
            return ScryfallQueryParser.RULE_orderTerm

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOrderTerm" ):
                listener.enterOrderTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOrderTerm" ):
                listener.exitOrderTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOrderTerm" ):
                return visitor.visitOrderTerm(self)
            else:
                return visitor.visitChildren(self)




    def orderTerm(self):

        localctx = ScryfallQueryParser.OrderTermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_orderTerm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
            self.match(ScryfallQueryParser.ORDER)
            self.state = 204
            self.match(ScryfallQueryParser.COLON)
            self.state = 205
            self.orderValue()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OrderValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARTIST(self):
            return self.getToken(ScryfallQueryParser.ARTIST, 0)

        def CMC(self):
            return self.getToken(ScryfallQueryParser.CMC, 0)

        def POWER(self):
            return self.getToken(ScryfallQueryParser.POWER, 0)

        def TOUGHNESS(self):
            return self.getToken(ScryfallQueryParser.TOUGHNESS, 0)

        def SET(self):
            return self.getToken(ScryfallQueryParser.SET, 0)

        def NAME(self):
            return self.getToken(ScryfallQueryParser.NAME, 0)

        def USD(self):
            return self.getToken(ScryfallQueryParser.USD, 0)

        def TIX(self):
            return self.getToken(ScryfallQueryParser.TIX, 0)

        def EUR(self):
            return self.getToken(ScryfallQueryParser.EUR, 0)

        def RARITY(self):
            return self.getToken(ScryfallQueryParser.RARITY, 0)

        def COLOR(self):
            return self.getToken(ScryfallQueryParser.COLOR, 0)

        def RELEASED(self):
            return self.getToken(ScryfallQueryParser.RELEASED, 0)

        def SPOILED(self):
            return self.getToken(ScryfallQueryParser.SPOILED, 0)

        def EDHREC(self):
            return self.getToken(ScryfallQueryParser.EDHREC, 0)

        def PENNY(self):
            return self.getToken(ScryfallQueryParser.PENNY, 0)

        def REVIEW(self):
            return self.getToken(ScryfallQueryParser.REVIEW, 0)

        def getRuleIndex(self):
            return ScryfallQueryParser.RULE_orderValue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOrderValue" ):
                listener.enterOrderValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOrderValue" ):
                listener.exitOrderValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOrderValue" ):
                return visitor.visitOrderValue(self)
            else:
                return visitor.visitChildren(self)




    def orderValue(self):

        localctx = ScryfallQueryParser.OrderValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_orderValue)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 562125386809344) != 0) or ((((_la - 86)) & ~0x3f) == 0 and ((1 << (_la - 86)) & 31) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DirectionTermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DIRECTION(self):
            return self.getToken(ScryfallQueryParser.DIRECTION, 0)

        def COLON(self):
            return self.getToken(ScryfallQueryParser.COLON, 0)

        def directionValue(self):
            return self.getTypedRuleContext(ScryfallQueryParser.DirectionValueContext,0)


        def getRuleIndex(self):
            return ScryfallQueryParser.RULE_directionTerm

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDirectionTerm" ):
                listener.enterDirectionTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDirectionTerm" ):
                listener.exitDirectionTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDirectionTerm" ):
                return visitor.visitDirectionTerm(self)
            else:
                return visitor.visitChildren(self)




    def directionTerm(self):

        localctx = ScryfallQueryParser.DirectionTermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_directionTerm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
            self.match(ScryfallQueryParser.DIRECTION)
            self.state = 210
            self.match(ScryfallQueryParser.COLON)
            self.state = 211
            self.directionValue()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DirectionValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASC(self):
            return self.getToken(ScryfallQueryParser.ASC, 0)

        def DESC(self):
            return self.getToken(ScryfallQueryParser.DESC, 0)

        def getRuleIndex(self):
            return ScryfallQueryParser.RULE_directionValue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDirectionValue" ):
                listener.enterDirectionValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDirectionValue" ):
                listener.exitDirectionValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDirectionValue" ):
                return visitor.visitDirectionValue(self)
            else:
                return visitor.visitChildren(self)




    def directionValue(self):

        localctx = ScryfallQueryParser.DirectionValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_directionValue)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            _la = self._input.LA(1)
            if not(_la==35 or _la==36):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PreferTermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PREFER(self):
            return self.getToken(ScryfallQueryParser.PREFER, 0)

        def COLON(self):
            return self.getToken(ScryfallQueryParser.COLON, 0)

        def preferValue(self):
            return self.getTypedRuleContext(ScryfallQueryParser.PreferValueContext,0)


        def getRuleIndex(self):
            return ScryfallQueryParser.RULE_preferTerm

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPreferTerm" ):
                listener.enterPreferTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPreferTerm" ):
                listener.exitPreferTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPreferTerm" ):
                return visitor.visitPreferTerm(self)
            else:
                return visitor.visitChildren(self)




    def preferTerm(self):

        localctx = ScryfallQueryParser.PreferTermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_preferTerm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 215
            self.match(ScryfallQueryParser.PREFER)
            self.state = 216
            self.match(ScryfallQueryParser.COLON)
            self.state = 217
            self.preferValue()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PreferValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OLDEST(self):
            return self.getToken(ScryfallQueryParser.OLDEST, 0)

        def NEWEST(self):
            return self.getToken(ScryfallQueryParser.NEWEST, 0)

        def USD_LOW(self):
            return self.getToken(ScryfallQueryParser.USD_LOW, 0)

        def USD_HIGH(self):
            return self.getToken(ScryfallQueryParser.USD_HIGH, 0)

        def TIX_LOW(self):
            return self.getToken(ScryfallQueryParser.TIX_LOW, 0)

        def TIX_HIGH(self):
            return self.getToken(ScryfallQueryParser.TIX_HIGH, 0)

        def EUR_LOW(self):
            return self.getToken(ScryfallQueryParser.EUR_LOW, 0)

        def EUR_HIGH(self):
            return self.getToken(ScryfallQueryParser.EUR_HIGH, 0)

        def PROMO(self):
            return self.getToken(ScryfallQueryParser.PROMO, 0)

        def DEFAULT(self):
            return self.getToken(ScryfallQueryParser.DEFAULT, 0)

        def ATYPICAL(self):
            return self.getToken(ScryfallQueryParser.ATYPICAL, 0)

        def UNIVERSESBEYOND(self):
            return self.getToken(ScryfallQueryParser.UNIVERSESBEYOND, 0)

        def UB(self):
            return self.getToken(ScryfallQueryParser.UB, 0)

        def NOTUNIVERSESBEYOND(self):
            return self.getToken(ScryfallQueryParser.NOTUNIVERSESBEYOND, 0)

        def NOTUB(self):
            return self.getToken(ScryfallQueryParser.NOTUB, 0)

        def getRuleIndex(self):
            return ScryfallQueryParser.RULE_preferValue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPreferValue" ):
                listener.enterPreferValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPreferValue" ):
                listener.exitPreferValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPreferValue" ):
                return visitor.visitPreferValue(self)
            else:
                return visitor.visitChildren(self)




    def preferValue(self):

        localctx = ScryfallQueryParser.PreferValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_preferValue)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
            _la = self._input.LA(1)
            if not(((((_la - 91)) & ~0x3f) == 0 and ((1 << (_la - 91)) & 32767) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IncludeTermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INCLUDE(self):
            return self.getToken(ScryfallQueryParser.INCLUDE, 0)

        def COLON(self):
            return self.getToken(ScryfallQueryParser.COLON, 0)

        def EXTRAS(self):
            return self.getToken(ScryfallQueryParser.EXTRAS, 0)

        def getRuleIndex(self):
            return ScryfallQueryParser.RULE_includeTerm

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIncludeTerm" ):
                listener.enterIncludeTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIncludeTerm" ):
                listener.exitIncludeTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIncludeTerm" ):
                return visitor.visitIncludeTerm(self)
            else:
                return visitor.visitChildren(self)




    def includeTerm(self):

        localctx = ScryfallQueryParser.IncludeTermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_includeTerm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 221
            self.match(ScryfallQueryParser.INCLUDE)
            self.state = 222
            self.match(ScryfallQueryParser.COLON)
            self.state = 223
            self.match(ScryfallQueryParser.EXTRAS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IsTermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IS(self):
            return self.getToken(ScryfallQueryParser.IS, 0)

        def COLON(self):
            return self.getToken(ScryfallQueryParser.COLON, 0)

        def isValue(self):
            return self.getTypedRuleContext(ScryfallQueryParser.IsValueContext,0)


        def getRuleIndex(self):
            return ScryfallQueryParser.RULE_isTerm

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIsTerm" ):
                listener.enterIsTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIsTerm" ):
                listener.exitIsTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIsTerm" ):
                return visitor.visitIsTerm(self)
            else:
                return visitor.visitChildren(self)




    def isTerm(self):

        localctx = ScryfallQueryParser.IsTermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_isTerm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 225
            self.match(ScryfallQueryParser.IS)
            self.state = 226
            self.match(ScryfallQueryParser.COLON)
            self.state = 227
            self.isValue()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NotTermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(ScryfallQueryParser.NOT, 0)

        def COLON(self):
            return self.getToken(ScryfallQueryParser.COLON, 0)

        def isValue(self):
            return self.getTypedRuleContext(ScryfallQueryParser.IsValueContext,0)


        def getRuleIndex(self):
            return ScryfallQueryParser.RULE_notTerm

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNotTerm" ):
                listener.enterNotTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNotTerm" ):
                listener.exitNotTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNotTerm" ):
                return visitor.visitNotTerm(self)
            else:
                return visitor.visitChildren(self)




    def notTerm(self):

        localctx = ScryfallQueryParser.NotTermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_notTerm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
            self.match(ScryfallQueryParser.NOT)
            self.state = 230
            self.match(ScryfallQueryParser.COLON)
            self.state = 231
            self.isValue()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IsValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ABNORMAL(self):
            return self.getToken(ScryfallQueryParser.ABNORMAL, 0)

        def ADVENTURE(self):
            return self.getToken(ScryfallQueryParser.ADVENTURE, 0)

        def ALCHEMY(self):
            return self.getToken(ScryfallQueryParser.ALCHEMY, 0)

        def ALTERNATE(self):
            return self.getToken(ScryfallQueryParser.ALTERNATE, 0)

        def AMPERSAND(self):
            return self.getToken(ScryfallQueryParser.AMPERSAND, 0)

        def ARCHENEMY(self):
            return self.getToken(ScryfallQueryParser.ARCHENEMY, 0)

        def ARCHIVAL(self):
            return self.getToken(ScryfallQueryParser.ARCHIVAL, 0)

        def ARENA_LEAGUE(self):
            return self.getToken(ScryfallQueryParser.ARENA_LEAGUE, 0)

        def ARENAID(self):
            return self.getToken(ScryfallQueryParser.ARENAID, 0)

        def ARENALEAGUE(self):
            return self.getToken(ScryfallQueryParser.ARENALEAGUE, 0)

        def ARTIST(self):
            return self.getToken(ScryfallQueryParser.ARTIST, 0)

        def ARTISTMISPRINT(self):
            return self.getToken(ScryfallQueryParser.ARTISTMISPRINT, 0)

        def ARTSERIES(self):
            return self.getToken(ScryfallQueryParser.ARTSERIES, 0)

        def ATYPICAL(self):
            return self.getToken(ScryfallQueryParser.ATYPICAL, 0)

        def AUGMENTATION(self):
            return self.getToken(ScryfallQueryParser.AUGMENTATION, 0)

        def BACK(self):
            return self.getToken(ScryfallQueryParser.BACK, 0)

        def BASELINE(self):
            return self.getToken(ScryfallQueryParser.BASELINE, 0)

        def BATTLELAND(self):
            return self.getToken(ScryfallQueryParser.BATTLELAND, 0)

        def BEAR(self):
            return self.getToken(ScryfallQueryParser.BEAR, 0)

        def BEGINNERBOX(self):
            return self.getToken(ScryfallQueryParser.BEGINNERBOX, 0)

        def BELZENLOK(self):
            return self.getToken(ScryfallQueryParser.BELZENLOK, 0)

        def BICYCLELAND(self):
            return self.getToken(ScryfallQueryParser.BICYCLELAND, 0)

        def BIKELAND(self):
            return self.getToken(ScryfallQueryParser.BIKELAND, 0)

        def BOB(self):
            return self.getToken(ScryfallQueryParser.BOB, 0)

        def BONDLAND(self):
            return self.getToken(ScryfallQueryParser.BONDLAND, 0)

        def BOOSTER(self):
            return self.getToken(ScryfallQueryParser.BOOSTER, 0)

        def BOOSTERFUN(self):
            return self.getToken(ScryfallQueryParser.BOOSTERFUN, 0)

        def BORDERLESS(self):
            return self.getToken(ScryfallQueryParser.BORDERLESS, 0)

        def BOUNCELAND(self):
            return self.getToken(ScryfallQueryParser.BOUNCELAND, 0)

        def BOX(self):
            return self.getToken(ScryfallQueryParser.BOX, 0)

        def BOXTOPPER(self):
            return self.getToken(ScryfallQueryParser.BOXTOPPER, 0)

        def BRAWLCOMMANDER(self):
            return self.getToken(ScryfallQueryParser.BRAWLCOMMANDER, 0)

        def BRAWLDECK(self):
            return self.getToken(ScryfallQueryParser.BRAWLDECK, 0)

        def BRAWLER(self):
            return self.getToken(ScryfallQueryParser.BRAWLER, 0)

        def BUNDLE(self):
            return self.getToken(ScryfallQueryParser.BUNDLE, 0)

        def BURSTFOIL(self):
            return self.getToken(ScryfallQueryParser.BURSTFOIL, 0)

        def BUYABOX(self):
            return self.getToken(ScryfallQueryParser.BUYABOX, 0)

        def CANLAND(self):
            return self.getToken(ScryfallQueryParser.CANLAND, 0)

        def CANOPYLAND(self):
            return self.getToken(ScryfallQueryParser.CANOPYLAND, 0)

        def CARDMARKET(self):
            return self.getToken(ScryfallQueryParser.CARDMARKET, 0)

        def CHECKLAND(self):
            return self.getToken(ScryfallQueryParser.CHECKLAND, 0)

        def CHOCOBOTRACKFOIL(self):
            return self.getToken(ScryfallQueryParser.CHOCOBOTRACKFOIL, 0)

        def CHRIMBY(self):
            return self.getToken(ScryfallQueryParser.CHRIMBY, 0)

        def CI(self):
            return self.getToken(ScryfallQueryParser.CI, 0)

        def CLASS(self):
            return self.getToken(ScryfallQueryParser.CLASS, 0)

        def COLORSHIFTED(self):
            return self.getToken(ScryfallQueryParser.COLORSHIFTED, 0)

        def COMMANDER(self):
            return self.getToken(ScryfallQueryParser.COMMANDER, 0)

        def COMMANDERPARTY(self):
            return self.getToken(ScryfallQueryParser.COMMANDERPARTY, 0)

        def COMMANDERPROMO(self):
            return self.getToken(ScryfallQueryParser.COMMANDERPROMO, 0)

        def COMPANION(self):
            return self.getToken(ScryfallQueryParser.COMPANION, 0)

        def CONCEPT(self):
            return self.getToken(ScryfallQueryParser.CONCEPT, 0)

        def CONFETTIFOIL(self):
            return self.getToken(ScryfallQueryParser.CONFETTIFOIL, 0)

        def CONJUREONLY(self):
            return self.getToken(ScryfallQueryParser.CONJUREONLY, 0)

        def CONTENTWARNING(self):
            return self.getToken(ScryfallQueryParser.CONTENTWARNING, 0)

        def CONVENTION(self):
            return self.getToken(ScryfallQueryParser.CONVENTION, 0)

        def CORE(self):
            return self.getToken(ScryfallQueryParser.CORE, 0)

        def COSMICFOIL(self):
            return self.getToken(ScryfallQueryParser.COSMICFOIL, 0)

        def COVERED(self):
            return self.getToken(ScryfallQueryParser.COVERED, 0)

        def CREATURELAND(self):
            return self.getToken(ScryfallQueryParser.CREATURELAND, 0)

        def CUTE(self):
            return self.getToken(ScryfallQueryParser.CUTE, 0)

        def CYCLELAND(self):
            return self.getToken(ScryfallQueryParser.CYCLELAND, 0)

        def DATESTAMPED(self):
            return self.getToken(ScryfallQueryParser.DATESTAMPED, 0)

        def DEFAULT(self):
            return self.getToken(ScryfallQueryParser.DEFAULT, 0)

        def DEN(self):
            return self.getToken(ScryfallQueryParser.DEN, 0)

        def DFC(self):
            return self.getToken(ScryfallQueryParser.DFC, 0)

        def DIGITAL(self):
            return self.getToken(ScryfallQueryParser.DIGITAL, 0)

        def DOUBLEEXPOSURE(self):
            return self.getToken(ScryfallQueryParser.DOUBLEEXPOSURE, 0)

        def DOUBLERAINBOW(self):
            return self.getToken(ScryfallQueryParser.DOUBLERAINBOW, 0)

        def DOUBLESIDED(self):
            return self.getToken(ScryfallQueryParser.DOUBLESIDED, 0)

        def DRACULASERIES(self):
            return self.getToken(ScryfallQueryParser.DRACULASERIES, 0)

        def DRAFTINNOVATION(self):
            return self.getToken(ScryfallQueryParser.DRAFTINNOVATION, 0)

        def DRAFTWEEKEND(self):
            return self.getToken(ScryfallQueryParser.DRAFTWEEKEND, 0)

        def DUAL(self):
            return self.getToken(ScryfallQueryParser.DUAL, 0)

        def DUELCOMMANDER(self):
            return self.getToken(ScryfallQueryParser.DUELCOMMANDER, 0)

        def DUELDECK(self):
            return self.getToken(ScryfallQueryParser.DUELDECK, 0)

        def DUELS(self):
            return self.getToken(ScryfallQueryParser.DUELS, 0)

        def ENGLISHART(self):
            return self.getToken(ScryfallQueryParser.ENGLISHART, 0)

        def ESCAPED(self):
            return self.getToken(ScryfallQueryParser.ESCAPED, 0)

        def ETB(self):
            return self.getToken(ScryfallQueryParser.ETB, 0)

        def ETCH(self):
            return self.getToken(ScryfallQueryParser.ETCH, 0)

        def ETCHED(self):
            return self.getToken(ScryfallQueryParser.ETCHED, 0)

        def EVENT(self):
            return self.getToken(ScryfallQueryParser.EVENT, 0)

        def EXPANSION(self):
            return self.getToken(ScryfallQueryParser.EXPANSION, 0)

        def EXTENDED(self):
            return self.getToken(ScryfallQueryParser.EXTENDED, 0)

        def EXTRA(self):
            return self.getToken(ScryfallQueryParser.EXTRA, 0)

        def FASTLAND(self):
            return self.getToken(ScryfallQueryParser.FASTLAND, 0)

        def FBB(self):
            return self.getToken(ScryfallQueryParser.FBB, 0)

        def FETCHLAND(self):
            return self.getToken(ScryfallQueryParser.FETCHLAND, 0)

        def FF(self):
            return self.getToken(ScryfallQueryParser.FF, 0)

        def FF1(self):
            return self.getToken(ScryfallQueryParser.FF1, 0)

        def FF10(self):
            return self.getToken(ScryfallQueryParser.FF10, 0)

        def FF11(self):
            return self.getToken(ScryfallQueryParser.FF11, 0)

        def FF12(self):
            return self.getToken(ScryfallQueryParser.FF12, 0)

        def FF13(self):
            return self.getToken(ScryfallQueryParser.FF13, 0)

        def FF14(self):
            return self.getToken(ScryfallQueryParser.FF14, 0)

        def FF15(self):
            return self.getToken(ScryfallQueryParser.FF15, 0)

        def FF16(self):
            return self.getToken(ScryfallQueryParser.FF16, 0)

        def FF2(self):
            return self.getToken(ScryfallQueryParser.FF2, 0)

        def FF3(self):
            return self.getToken(ScryfallQueryParser.FF3, 0)

        def FF4(self):
            return self.getToken(ScryfallQueryParser.FF4, 0)

        def FF5(self):
            return self.getToken(ScryfallQueryParser.FF5, 0)

        def FF6(self):
            return self.getToken(ScryfallQueryParser.FF6, 0)

        def FF7(self):
            return self.getToken(ScryfallQueryParser.FF7, 0)

        def FF8(self):
            return self.getToken(ScryfallQueryParser.FF8, 0)

        def FF9(self):
            return self.getToken(ScryfallQueryParser.FF9, 0)

        def FFI(self):
            return self.getToken(ScryfallQueryParser.FFI, 0)

        def FFII(self):
            return self.getToken(ScryfallQueryParser.FFII, 0)

        def FFIII(self):
            return self.getToken(ScryfallQueryParser.FFIII, 0)

        def FFIV(self):
            return self.getToken(ScryfallQueryParser.FFIV, 0)

        def FFIX(self):
            return self.getToken(ScryfallQueryParser.FFIX, 0)

        def FFV(self):
            return self.getToken(ScryfallQueryParser.FFV, 0)

        def FFVI(self):
            return self.getToken(ScryfallQueryParser.FFVI, 0)

        def FFVII(self):
            return self.getToken(ScryfallQueryParser.FFVII, 0)

        def FFVIII(self):
            return self.getToken(ScryfallQueryParser.FFVIII, 0)

        def FFX(self):
            return self.getToken(ScryfallQueryParser.FFX, 0)

        def FFXI(self):
            return self.getToken(ScryfallQueryParser.FFXI, 0)

        def FFXII(self):
            return self.getToken(ScryfallQueryParser.FFXII, 0)

        def FFXIII(self):
            return self.getToken(ScryfallQueryParser.FFXIII, 0)

        def FFXIV(self):
            return self.getToken(ScryfallQueryParser.FFXIV, 0)

        def FFXV(self):
            return self.getToken(ScryfallQueryParser.FFXV, 0)

        def FFXVI(self):
            return self.getToken(ScryfallQueryParser.FFXVI, 0)

        def FILTERLAND(self):
            return self.getToken(ScryfallQueryParser.FILTERLAND, 0)

        def FINALFANTASY(self):
            return self.getToken(ScryfallQueryParser.FINALFANTASY, 0)

        def FINALFANTASY1(self):
            return self.getToken(ScryfallQueryParser.FINALFANTASY1, 0)

        def FINALFANTASY10(self):
            return self.getToken(ScryfallQueryParser.FINALFANTASY10, 0)

        def FINALFANTASY11(self):
            return self.getToken(ScryfallQueryParser.FINALFANTASY11, 0)

        def FINALFANTASY12(self):
            return self.getToken(ScryfallQueryParser.FINALFANTASY12, 0)

        def FINALFANTASY13(self):
            return self.getToken(ScryfallQueryParser.FINALFANTASY13, 0)

        def FINALFANTASY14(self):
            return self.getToken(ScryfallQueryParser.FINALFANTASY14, 0)

        def FINALFANTASY15(self):
            return self.getToken(ScryfallQueryParser.FINALFANTASY15, 0)

        def FINALFANTASY16(self):
            return self.getToken(ScryfallQueryParser.FINALFANTASY16, 0)

        def FINALFANTASY2(self):
            return self.getToken(ScryfallQueryParser.FINALFANTASY2, 0)

        def FINALFANTASY3(self):
            return self.getToken(ScryfallQueryParser.FINALFANTASY3, 0)

        def FINALFANTASY4(self):
            return self.getToken(ScryfallQueryParser.FINALFANTASY4, 0)

        def FINALFANTASY5(self):
            return self.getToken(ScryfallQueryParser.FINALFANTASY5, 0)

        def FINALFANTASY6(self):
            return self.getToken(ScryfallQueryParser.FINALFANTASY6, 0)

        def FINALFANTASY7(self):
            return self.getToken(ScryfallQueryParser.FINALFANTASY7, 0)

        def FINALFANTASY8(self):
            return self.getToken(ScryfallQueryParser.FINALFANTASY8, 0)

        def FINALFANTASY9(self):
            return self.getToken(ScryfallQueryParser.FINALFANTASY9, 0)

        def FINALFANTASYI(self):
            return self.getToken(ScryfallQueryParser.FINALFANTASYI, 0)

        def FINALFANTASYII(self):
            return self.getToken(ScryfallQueryParser.FINALFANTASYII, 0)

        def FINALFANTASYIII(self):
            return self.getToken(ScryfallQueryParser.FINALFANTASYIII, 0)

        def FINALFANTASYIV(self):
            return self.getToken(ScryfallQueryParser.FINALFANTASYIV, 0)

        def FINALFANTASYIX(self):
            return self.getToken(ScryfallQueryParser.FINALFANTASYIX, 0)

        def FINALFANTASYV(self):
            return self.getToken(ScryfallQueryParser.FINALFANTASYV, 0)

        def FINALFANTASYVI(self):
            return self.getToken(ScryfallQueryParser.FINALFANTASYVI, 0)

        def FINALFANTASYVII(self):
            return self.getToken(ScryfallQueryParser.FINALFANTASYVII, 0)

        def FINALFANTASYVIII(self):
            return self.getToken(ScryfallQueryParser.FINALFANTASYVIII, 0)

        def FINALFANTASYX(self):
            return self.getToken(ScryfallQueryParser.FINALFANTASYX, 0)

        def FINALFANTASYXI(self):
            return self.getToken(ScryfallQueryParser.FINALFANTASYXI, 0)

        def FINALFANTASYXII(self):
            return self.getToken(ScryfallQueryParser.FINALFANTASYXII, 0)

        def FINALFANTASYXIII(self):
            return self.getToken(ScryfallQueryParser.FINALFANTASYXIII, 0)

        def FINALFANTASYXIV(self):
            return self.getToken(ScryfallQueryParser.FINALFANTASYXIV, 0)

        def FINALFANTASYXV(self):
            return self.getToken(ScryfallQueryParser.FINALFANTASYXV, 0)

        def FINALFANTASYXVI(self):
            return self.getToken(ScryfallQueryParser.FINALFANTASYXVI, 0)

        def FINKEL(self):
            return self.getToken(ScryfallQueryParser.FINKEL, 0)

        def FIRSTPLACEFOIL(self):
            return self.getToken(ScryfallQueryParser.FIRSTPLACEFOIL, 0)

        def FIRSTPRINT(self):
            return self.getToken(ScryfallQueryParser.FIRSTPRINT, 0)

        def FIRSTPRINTING(self):
            return self.getToken(ScryfallQueryParser.FIRSTPRINTING, 0)

        def FIXED(self):
            return self.getToken(ScryfallQueryParser.FIXED, 0)

        def FLAVOR(self):
            return self.getToken(ScryfallQueryParser.FLAVOR, 0)

        def FLAVORNAME(self):
            return self.getToken(ScryfallQueryParser.FLAVORNAME, 0)

        def FLIP(self):
            return self.getToken(ScryfallQueryParser.FLIP, 0)

        def FMB1(self):
            return self.getToken(ScryfallQueryParser.FMB1, 0)

        def FNM(self):
            return self.getToken(ScryfallQueryParser.FNM, 0)

        def FOIL(self):
            return self.getToken(ScryfallQueryParser.FOIL, 0)

        def FRAMEODDITY(self):
            return self.getToken(ScryfallQueryParser.FRAMEODDITY, 0)

        def FRENCHVANILLA(self):
            return self.getToken(ScryfallQueryParser.FRENCHVANILLA, 0)

        def FROMTHEVAULT(self):
            return self.getToken(ScryfallQueryParser.FROMTHEVAULT, 0)

        def FULLART(self):
            return self.getToken(ScryfallQueryParser.FULLART, 0)

        def FULLTEXT(self):
            return self.getToken(ScryfallQueryParser.FULLTEXT, 0)

        def FUNNY(self):
            return self.getToken(ScryfallQueryParser.FUNNY, 0)

        def FUTURE(self):
            return self.getToken(ScryfallQueryParser.FUTURE, 0)

        def FUTURESHIFTED(self):
            return self.getToken(ScryfallQueryParser.FUTURESHIFTED, 0)

        def FWB(self):
            return self.getToken(ScryfallQueryParser.FWB, 0)

        def GAINLAND(self):
            return self.getToken(ScryfallQueryParser.GAINLAND, 0)

        def GALAXYFOIL(self):
            return self.getToken(ScryfallQueryParser.GALAXYFOIL, 0)

        def GAMECHANGER(self):
            return self.getToken(ScryfallQueryParser.GAMECHANGER, 0)

        def GAMEDAY(self):
            return self.getToken(ScryfallQueryParser.GAMEDAY, 0)

        def GARY(self):
            return self.getToken(ScryfallQueryParser.GARY, 0)

        def GATEWAY(self):
            return self.getToken(ScryfallQueryParser.GATEWAY, 0)

        def GIFTBOX(self):
            return self.getToken(ScryfallQueryParser.GIFTBOX, 0)

        def GILDED(self):
            return self.getToken(ScryfallQueryParser.GILDED, 0)

        def GLOSSY(self):
            return self.getToken(ScryfallQueryParser.GLOSSY, 0)

        def GODZILLASERIES(self):
            return self.getToken(ScryfallQueryParser.GODZILLASERIES, 0)

        def HALO(self):
            return self.getToken(ScryfallQueryParser.HALO, 0)

        def HALOFOIL(self):
            return self.getToken(ScryfallQueryParser.HALOFOIL, 0)

        def HEADLINER(self):
            return self.getToken(ScryfallQueryParser.HEADLINER, 0)

        def HIRES(self):
            return self.getToken(ScryfallQueryParser.HIRES, 0)

        def HISTORIC(self):
            return self.getToken(ScryfallQueryParser.HISTORIC, 0)

        def HORIZ(self):
            return self.getToken(ScryfallQueryParser.HORIZ, 0)

        def HYBRID(self):
            return self.getToken(ScryfallQueryParser.HYBRID, 0)

        def ILLUSTRATION(self):
            return self.getToken(ScryfallQueryParser.ILLUSTRATION, 0)

        def IMAGEQA(self):
            return self.getToken(ScryfallQueryParser.IMAGEQA, 0)

        def IMAGINE(self):
            return self.getToken(ScryfallQueryParser.IMAGINE, 0)

        def INDICATOR(self):
            return self.getToken(ScryfallQueryParser.INDICATOR, 0)

        def INSTORE(self):
            return self.getToken(ScryfallQueryParser.INSTORE, 0)

        def INTRO_PACK(self):
            return self.getToken(ScryfallQueryParser.INTRO_PACK, 0)

        def INTROPACK(self):
            return self.getToken(ScryfallQueryParser.INTROPACK, 0)

        def INVITATIONAL(self):
            return self.getToken(ScryfallQueryParser.INVITATIONAL, 0)

        def JPWALKER(self):
            return self.getToken(ScryfallQueryParser.JPWALKER, 0)

        def JUDGE_GIFT(self):
            return self.getToken(ScryfallQueryParser.JUDGE_GIFT, 0)

        def JUDGEGIFT(self):
            return self.getToken(ScryfallQueryParser.JUDGEGIFT, 0)

        def JUMPSTART(self):
            return self.getToken(ScryfallQueryParser.JUMPSTART, 0)

        def KAROO(self):
            return self.getToken(ScryfallQueryParser.KAROO, 0)

        def LEAGUE(self):
            return self.getToken(ScryfallQueryParser.LEAGUE, 0)

        def LEVELER(self):
            return self.getToken(ScryfallQueryParser.LEVELER, 0)

        def LIGHTS(self):
            return self.getToken(ScryfallQueryParser.LIGHTS, 0)

        def LISTWHITE(self):
            return self.getToken(ScryfallQueryParser.LISTWHITE, 0)

        def LOCALIZEDIMAGE(self):
            return self.getToken(ScryfallQueryParser.LOCALIZEDIMAGE, 0)

        def LOCALIZEDNAME(self):
            return self.getToken(ScryfallQueryParser.LOCALIZEDNAME, 0)

        def LOSTLEGENDS(self):
            return self.getToken(ScryfallQueryParser.LOSTLEGENDS, 0)

        def MAGICSPOTLIGHT(self):
            return self.getToken(ScryfallQueryParser.MAGICSPOTLIGHT, 0)

        def MANLAND(self):
            return self.getToken(ScryfallQueryParser.MANLAND, 0)

        def MASTERPIECE(self):
            return self.getToken(ScryfallQueryParser.MASTERPIECE, 0)

        def MASTERS(self):
            return self.getToken(ScryfallQueryParser.MASTERS, 0)

        def MB1(self):
            return self.getToken(ScryfallQueryParser.MB1, 0)

        def MB2(self):
            return self.getToken(ScryfallQueryParser.MB2, 0)

        def MDFC(self):
            return self.getToken(ScryfallQueryParser.MDFC, 0)

        def MEDIA_INSERT(self):
            return self.getToken(ScryfallQueryParser.MEDIA_INSERT, 0)

        def MEDIAINSERT(self):
            return self.getToken(ScryfallQueryParser.MEDIAINSERT, 0)

        def MELD(self):
            return self.getToken(ScryfallQueryParser.MELD, 0)

        def MELDPART(self):
            return self.getToken(ScryfallQueryParser.MELDPART, 0)

        def MELDRESULT(self):
            return self.getToken(ScryfallQueryParser.MELDRESULT, 0)

        def MEMORABILIA(self):
            return self.getToken(ScryfallQueryParser.MEMORABILIA, 0)

        def METAL(self):
            return self.getToken(ScryfallQueryParser.METAL, 0)

        def MISPRINT(self):
            return self.getToken(ScryfallQueryParser.MISPRINT, 0)

        def MODAL(self):
            return self.getToken(ScryfallQueryParser.MODAL, 0)

        def MODERN(self):
            return self.getToken(ScryfallQueryParser.MODERN, 0)

        def MOM(self):
            return self.getToken(ScryfallQueryParser.MOM, 0)

        def MOONLITLAND(self):
            return self.getToken(ScryfallQueryParser.MOONLITLAND, 0)

        def MTGOID(self):
            return self.getToken(ScryfallQueryParser.MTGOID, 0)

        def MULTIPLAYER(self):
            return self.getToken(ScryfallQueryParser.MULTIPLAYER, 0)

        def MULTIVERSE(self):
            return self.getToken(ScryfallQueryParser.MULTIVERSE, 0)

        def NEONINK(self):
            return self.getToken(ScryfallQueryParser.NEONINK, 0)

        def NEW(self):
            return self.getToken(ScryfallQueryParser.NEW, 0)

        def NEWINPAUPER(self):
            return self.getToken(ScryfallQueryParser.NEWINPAUPER, 0)

        def NONDEFAULT(self):
            return self.getToken(ScryfallQueryParser.NONDEFAULT, 0)

        def NONFOIL(self):
            return self.getToken(ScryfallQueryParser.NONFOIL, 0)

        def NONTRADITIONAL(self):
            return self.getToken(ScryfallQueryParser.NONTRADITIONAL, 0)

        def NORMAL(self):
            return self.getToken(ScryfallQueryParser.NORMAL, 0)

        def NOTUNIVERSESBEYOND(self):
            return self.getToken(ScryfallQueryParser.NOTUNIVERSESBEYOND, 0)

        def OATHBREAKER(self):
            return self.getToken(ScryfallQueryParser.OATHBREAKER, 0)

        def ODDFRAME(self):
            return self.getToken(ScryfallQueryParser.ODDFRAME, 0)

        def OILSLICK(self):
            return self.getToken(ScryfallQueryParser.OILSLICK, 0)

        def OLD(self):
            return self.getToken(ScryfallQueryParser.OLD, 0)

        def ONLYPRINT(self):
            return self.getToken(ScryfallQueryParser.ONLYPRINT, 0)

        def OPENHOUSE(self):
            return self.getToken(ScryfallQueryParser.OPENHOUSE, 0)

        def OUTLAW(self):
            return self.getToken(ScryfallQueryParser.OUTLAW, 0)

        def OVERSIZED(self):
            return self.getToken(ScryfallQueryParser.OVERSIZED, 0)

        def PAGL(self):
            return self.getToken(ScryfallQueryParser.PAGL, 0)

        def PAINLAND(self):
            return self.getToken(ScryfallQueryParser.PAINLAND, 0)

        def PAPERART(self):
            return self.getToken(ScryfallQueryParser.PAPERART, 0)

        def PARTNER(self):
            return self.getToken(ScryfallQueryParser.PARTNER, 0)

        def PARTY(self):
            return self.getToken(ScryfallQueryParser.PARTY, 0)

        def PATHWAY(self):
            return self.getToken(ScryfallQueryParser.PATHWAY, 0)

        def PAUPERCOMMANDER(self):
            return self.getToken(ScryfallQueryParser.PAUPERCOMMANDER, 0)

        def PCTB(self):
            return self.getToken(ScryfallQueryParser.PCTB, 0)

        def PERMANENT(self):
            return self.getToken(ScryfallQueryParser.PERMANENT, 0)

        def PHED(self):
            return self.getToken(ScryfallQueryParser.PHED, 0)

        def PHYREXIA(self):
            return self.getToken(ScryfallQueryParser.PHYREXIA, 0)

        def PHYREXIAN(self):
            return self.getToken(ScryfallQueryParser.PHYREXIAN, 0)

        def PIKULA(self):
            return self.getToken(ScryfallQueryParser.PIKULA, 0)

        def PLACEHOLDERIMAGE(self):
            return self.getToken(ScryfallQueryParser.PLACEHOLDERIMAGE, 0)

        def PLANAR(self):
            return self.getToken(ScryfallQueryParser.PLANAR, 0)

        def PLANECHASE(self):
            return self.getToken(ScryfallQueryParser.PLANECHASE, 0)

        def PLANESWALKER_DECK(self):
            return self.getToken(ScryfallQueryParser.PLANESWALKER_DECK, 0)

        def PLANESWALKERDECK(self):
            return self.getToken(ScryfallQueryParser.PLANESWALKERDECK, 0)

        def PLASTIC(self):
            return self.getToken(ScryfallQueryParser.PLASTIC, 0)

        def PLAYER_REWARDS(self):
            return self.getToken(ScryfallQueryParser.PLAYER_REWARDS, 0)

        def PLAYERREWARDS(self):
            return self.getToken(ScryfallQueryParser.PLAYERREWARDS, 0)

        def PLAYPROMO(self):
            return self.getToken(ScryfallQueryParser.PLAYPROMO, 0)

        def PLAYTEST(self):
            return self.getToken(ScryfallQueryParser.PLAYTEST, 0)

        def PORTAL(self):
            return self.getToken(ScryfallQueryParser.PORTAL, 0)

        def PORTRAIT(self):
            return self.getToken(ScryfallQueryParser.PORTRAIT, 0)

        def POSTER(self):
            return self.getToken(ScryfallQueryParser.POSTER, 0)

        def PREMIERESHOP(self):
            return self.getToken(ScryfallQueryParser.PREMIERESHOP, 0)

        def PREMIUMDECK(self):
            return self.getToken(ScryfallQueryParser.PREMIUMDECK, 0)

        def PRERELEASE(self):
            return self.getToken(ScryfallQueryParser.PRERELEASE, 0)

        def PRINTEDTEXT(self):
            return self.getToken(ScryfallQueryParser.PRINTEDTEXT, 0)

        def PROMO(self):
            return self.getToken(ScryfallQueryParser.PROMO, 0)

        def PROMOPACK(self):
            return self.getToken(ScryfallQueryParser.PROMOPACK, 0)

        def RAINBOWFOIL(self):
            return self.getToken(ScryfallQueryParser.RAINBOWFOIL, 0)

        def RAISEDFOIL(self):
            return self.getToken(ScryfallQueryParser.RAISEDFOIL, 0)

        def REBALANCED(self):
            return self.getToken(ScryfallQueryParser.REBALANCED, 0)

        def RELATED(self):
            return self.getToken(ScryfallQueryParser.RELATED, 0)

        def RELEASE(self):
            return self.getToken(ScryfallQueryParser.RELEASE, 0)

        def REPRINT(self):
            return self.getToken(ScryfallQueryParser.REPRINT, 0)

        def RESALE(self):
            return self.getToken(ScryfallQueryParser.RESALE, 0)

        def RESERVED(self):
            return self.getToken(ScryfallQueryParser.RESERVED, 0)

        def REVERSIBLE(self):
            return self.getToken(ScryfallQueryParser.REVERSIBLE, 0)

        def RIPPLEFOIL(self):
            return self.getToken(ScryfallQueryParser.RIPPLEFOIL, 0)

        def SCANNEEDED(self):
            return self.getToken(ScryfallQueryParser.SCANNEEDED, 0)

        def SCENE(self):
            return self.getToken(ScryfallQueryParser.SCENE, 0)

        def SCHINESEALTART(self):
            return self.getToken(ScryfallQueryParser.SCHINESEALTART, 0)

        def SCROLL(self):
            return self.getToken(ScryfallQueryParser.SCROLL, 0)

        def SCRYFALLPREVIEW(self):
            return self.getToken(ScryfallQueryParser.SCRYFALLPREVIEW, 0)

        def SCRYLAND(self):
            return self.getToken(ScryfallQueryParser.SCRYLAND, 0)

        def SERIALIZED(self):
            return self.getToken(ScryfallQueryParser.SERIALIZED, 0)

        def SET_PROMO(self):
            return self.getToken(ScryfallQueryParser.SET_PROMO, 0)

        def SETEXTENSION(self):
            return self.getToken(ScryfallQueryParser.SETEXTENSION, 0)

        def SETPROMO(self):
            return self.getToken(ScryfallQueryParser.SETPROMO, 0)

        def SHADOWLAND(self):
            return self.getToken(ScryfallQueryParser.SHADOWLAND, 0)

        def SHOCKLAND(self):
            return self.getToken(ScryfallQueryParser.SHOCKLAND, 0)

        def SHOWCASE(self):
            return self.getToken(ScryfallQueryParser.SHOWCASE, 0)

        def SINGULARITYFOIL(self):
            return self.getToken(ScryfallQueryParser.SINGULARITYFOIL, 0)

        def SLDBONUS(self):
            return self.getToken(ScryfallQueryParser.SLDBONUS, 0)

        def SLOWLAND(self):
            return self.getToken(ScryfallQueryParser.SLOWLAND, 0)

        def SNARL(self):
            return self.getToken(ScryfallQueryParser.SNARL, 0)

        def SOURCEMATERIAL(self):
            return self.getToken(ScryfallQueryParser.SOURCEMATERIAL, 0)

        def SPELL(self):
            return self.getToken(ScryfallQueryParser.SPELL, 0)

        def SPELLBOOK(self):
            return self.getToken(ScryfallQueryParser.SPELLBOOK, 0)

        def SPIKEY(self):
            return self.getToken(ScryfallQueryParser.SPIKEY, 0)

        def SPLIT(self):
            return self.getToken(ScryfallQueryParser.SPLIT, 0)

        def SPLITMANA(self):
            return self.getToken(ScryfallQueryParser.SPLITMANA, 0)

        def SPOTLIGHT(self):
            return self.getToken(ScryfallQueryParser.SPOTLIGHT, 0)

        def STAMP(self):
            return self.getToken(ScryfallQueryParser.STAMP, 0)

        def STAMPED(self):
            return self.getToken(ScryfallQueryParser.STAMPED, 0)

        def STARTER(self):
            return self.getToken(ScryfallQueryParser.STARTER, 0)

        def STARTERCOLLECTION(self):
            return self.getToken(ScryfallQueryParser.STARTERCOLLECTION, 0)

        def STARTERDECK(self):
            return self.getToken(ScryfallQueryParser.STARTERDECK, 0)

        def STEPANDCOMPLEAT(self):
            return self.getToken(ScryfallQueryParser.STEPANDCOMPLEAT, 0)

        def STORAGELAND(self):
            return self.getToken(ScryfallQueryParser.STORAGELAND, 0)

        def STORECHAMPIONSHIP(self):
            return self.getToken(ScryfallQueryParser.STORECHAMPIONSHIP, 0)

        def STORY(self):
            return self.getToken(ScryfallQueryParser.STORY, 0)

        def SURVEILLAND(self):
            return self.getToken(ScryfallQueryParser.SURVEILLAND, 0)

        def TANGOLAND(self):
            return self.getToken(ScryfallQueryParser.TANGOLAND, 0)

        def TCGPLAYER(self):
            return self.getToken(ScryfallQueryParser.TCGPLAYER, 0)

        def TDFC(self):
            return self.getToken(ScryfallQueryParser.TDFC, 0)

        def TEXTLESS(self):
            return self.getToken(ScryfallQueryParser.TEXTLESS, 0)

        def TEXTURED(self):
            return self.getToken(ScryfallQueryParser.TEXTURED, 0)

        def THEMEPACK(self):
            return self.getToken(ScryfallQueryParser.THEMEPACK, 0)

        def THICK(self):
            return self.getToken(ScryfallQueryParser.THICK, 0)

        def TIMESHIFTED(self):
            return self.getToken(ScryfallQueryParser.TIMESHIFTED, 0)

        def TOKEN(self):
            return self.getToken(ScryfallQueryParser.TOKEN, 0)

        def TOMBSTONE(self):
            return self.getToken(ScryfallQueryParser.TOMBSTONE, 0)

        def TOURNEY(self):
            return self.getToken(ScryfallQueryParser.TOURNEY, 0)

        def TRADITIONAL(self):
            return self.getToken(ScryfallQueryParser.TRADITIONAL, 0)

        def TRANSFORM(self):
            return self.getToken(ScryfallQueryParser.TRANSFORM, 0)

        def TRANSLUCENT(self):
            return self.getToken(ScryfallQueryParser.TRANSLUCENT, 0)

        def TREASURECHEST(self):
            return self.getToken(ScryfallQueryParser.TREASURECHEST, 0)

        def TRICYCLELAND(self):
            return self.getToken(ScryfallQueryParser.TRICYCLELAND, 0)

        def TRIKELAND(self):
            return self.getToken(ScryfallQueryParser.TRIKELAND, 0)

        def TRILAND(self):
            return self.getToken(ScryfallQueryParser.TRILAND, 0)

        def TRIOME(self):
            return self.getToken(ScryfallQueryParser.TRIOME, 0)

        def TRON(self):
            return self.getToken(ScryfallQueryParser.TRON, 0)

        def TYPICAL(self):
            return self.getToken(ScryfallQueryParser.TYPICAL, 0)

        def UB(self):
            return self.getToken(ScryfallQueryParser.UB, 0)

        def UNIQUE(self):
            return self.getToken(ScryfallQueryParser.UNIQUE, 0)

        def UNIVERSESBEYOND(self):
            return self.getToken(ScryfallQueryParser.UNIVERSESBEYOND, 0)

        def UNSET(self):
            return self.getToken(ScryfallQueryParser.UNSET, 0)

        def UPSIDEDOWN(self):
            return self.getToken(ScryfallQueryParser.UPSIDEDOWN, 0)

        def UPSIDEDOWNBACK(self):
            return self.getToken(ScryfallQueryParser.UPSIDEDOWNBACK, 0)

        def USELESS(self):
            return self.getToken(ScryfallQueryParser.USELESS, 0)

        def VANGUARD(self):
            return self.getToken(ScryfallQueryParser.VANGUARD, 0)

        def VANILLA(self):
            return self.getToken(ScryfallQueryParser.VANILLA, 0)

        def VARIATION(self):
            return self.getToken(ScryfallQueryParser.VARIATION, 0)

        def VAULT(self):
            return self.getToken(ScryfallQueryParser.VAULT, 0)

        def VERT(self):
            return self.getToken(ScryfallQueryParser.VERT, 0)

        def WANTED(self):
            return self.getToken(ScryfallQueryParser.WANTED, 0)

        def WATERMARK(self):
            return self.getToken(ScryfallQueryParser.WATERMARK, 0)

        def WIZARDSPLAYNETWORK(self):
            return self.getToken(ScryfallQueryParser.WIZARDSPLAYNETWORK, 0)

        def getRuleIndex(self):
            return ScryfallQueryParser.RULE_isValue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIsValue" ):
                listener.enterIsValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIsValue" ):
                listener.exitIsValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIsValue" ):
                return visitor.visitIsValue(self)
            else:
                return visitor.visitChildren(self)




    def isValue(self):

        localctx = ScryfallQueryParser.IsValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_isValue)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 233
            _la = self._input.LA(1)
            if not(_la==13 or _la==38 or ((((_la - 99)) & ~0x3f) == 0 and ((1 << (_la - 99)) & -65) != 0) or ((((_la - 163)) & ~0x3f) == 0 and ((1 << (_la - 163)) & -1) != 0) or ((((_la - 227)) & ~0x3f) == 0 and ((1 << (_la - 227)) & -1) != 0) or ((((_la - 291)) & ~0x3f) == 0 and ((1 << (_la - 291)) & -1) != 0) or ((((_la - 355)) & ~0x3f) == 0 and ((1 << (_la - 355)) & -1) != 0) or ((((_la - 419)) & ~0x3f) == 0 and ((1 << (_la - 419)) & 71571335020543) != 0) or ((((_la - 499)) & ~0x3f) == 0 and ((1 << (_la - 499)) & 69256347649) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FormatTermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COLON(self):
            return self.getToken(ScryfallQueryParser.COLON, 0)

        def formatValue(self):
            return self.getTypedRuleContext(ScryfallQueryParser.FormatValueContext,0)


        def F(self):
            return self.getToken(ScryfallQueryParser.F, 0)

        def FORMAT(self):
            return self.getToken(ScryfallQueryParser.FORMAT, 0)

        def getRuleIndex(self):
            return ScryfallQueryParser.RULE_formatTerm

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFormatTerm" ):
                listener.enterFormatTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFormatTerm" ):
                listener.exitFormatTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFormatTerm" ):
                return visitor.visitFormatTerm(self)
            else:
                return visitor.visitChildren(self)




    def formatTerm(self):

        localctx = ScryfallQueryParser.FormatTermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_formatTerm)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 235
            _la = self._input.LA(1)
            if not(_la==21 or _la==22):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 236
            self.match(ScryfallQueryParser.COLON)
            self.state = 237
            self.formatValue()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BannedTermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BANNED(self):
            return self.getToken(ScryfallQueryParser.BANNED, 0)

        def COLON(self):
            return self.getToken(ScryfallQueryParser.COLON, 0)

        def formatValue(self):
            return self.getTypedRuleContext(ScryfallQueryParser.FormatValueContext,0)


        def getRuleIndex(self):
            return ScryfallQueryParser.RULE_bannedTerm

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBannedTerm" ):
                listener.enterBannedTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBannedTerm" ):
                listener.exitBannedTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBannedTerm" ):
                return visitor.visitBannedTerm(self)
            else:
                return visitor.visitChildren(self)




    def bannedTerm(self):

        localctx = ScryfallQueryParser.BannedTermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_bannedTerm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            self.match(ScryfallQueryParser.BANNED)
            self.state = 240
            self.match(ScryfallQueryParser.COLON)
            self.state = 241
            self.formatValue()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RestrictedTermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RESTRICTED(self):
            return self.getToken(ScryfallQueryParser.RESTRICTED, 0)

        def COLON(self):
            return self.getToken(ScryfallQueryParser.COLON, 0)

        def formatValue(self):
            return self.getTypedRuleContext(ScryfallQueryParser.FormatValueContext,0)


        def getRuleIndex(self):
            return ScryfallQueryParser.RULE_restrictedTerm

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRestrictedTerm" ):
                listener.enterRestrictedTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRestrictedTerm" ):
                listener.exitRestrictedTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRestrictedTerm" ):
                return visitor.visitRestrictedTerm(self)
            else:
                return visitor.visitChildren(self)




    def restrictedTerm(self):

        localctx = ScryfallQueryParser.RestrictedTermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_restrictedTerm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 243
            self.match(ScryfallQueryParser.RESTRICTED)
            self.state = 244
            self.match(ScryfallQueryParser.COLON)
            self.state = 245
            self.formatValue()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FormatValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STANDARD(self):
            return self.getToken(ScryfallQueryParser.STANDARD, 0)

        def FUTURE(self):
            return self.getToken(ScryfallQueryParser.FUTURE, 0)

        def HISTORIC(self):
            return self.getToken(ScryfallQueryParser.HISTORIC, 0)

        def TIMELESS(self):
            return self.getToken(ScryfallQueryParser.TIMELESS, 0)

        def GLADIATOR(self):
            return self.getToken(ScryfallQueryParser.GLADIATOR, 0)

        def PIONEER(self):
            return self.getToken(ScryfallQueryParser.PIONEER, 0)

        def MODERN(self):
            return self.getToken(ScryfallQueryParser.MODERN, 0)

        def LEGACY(self):
            return self.getToken(ScryfallQueryParser.LEGACY, 0)

        def PAUPER(self):
            return self.getToken(ScryfallQueryParser.PAUPER, 0)

        def VINTAGE(self):
            return self.getToken(ScryfallQueryParser.VINTAGE, 0)

        def PENNY(self):
            return self.getToken(ScryfallQueryParser.PENNY, 0)

        def COMMANDER(self):
            return self.getToken(ScryfallQueryParser.COMMANDER, 0)

        def OATHBREAKER(self):
            return self.getToken(ScryfallQueryParser.OATHBREAKER, 0)

        def STANDARDBRAWL(self):
            return self.getToken(ScryfallQueryParser.STANDARDBRAWL, 0)

        def BRAWL(self):
            return self.getToken(ScryfallQueryParser.BRAWL, 0)

        def ALCHEMY(self):
            return self.getToken(ScryfallQueryParser.ALCHEMY, 0)

        def PAUPERCOMMANDER(self):
            return self.getToken(ScryfallQueryParser.PAUPERCOMMANDER, 0)

        def DUEL(self):
            return self.getToken(ScryfallQueryParser.DUEL, 0)

        def OLDSCHOOL(self):
            return self.getToken(ScryfallQueryParser.OLDSCHOOL, 0)

        def PREMODERN(self):
            return self.getToken(ScryfallQueryParser.PREMODERN, 0)

        def PREDH(self):
            return self.getToken(ScryfallQueryParser.PREDH, 0)

        def getRuleIndex(self):
            return ScryfallQueryParser.RULE_formatValue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFormatValue" ):
                listener.enterFormatValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFormatValue" ):
                listener.exitFormatValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFormatValue" ):
                return visitor.visitFormatValue(self)
            else:
                return visitor.visitChildren(self)




    def formatValue(self):

        localctx = ScryfallQueryParser.FormatValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_formatValue)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 247
            _la = self._input.LA(1)
            if not(((((_la - 89)) & ~0x3f) == 0 and ((1 << (_la - 89)) & 4899916398874066945) != 0) or _la==163 or ((((_la - 454)) & ~0x3f) == 0 and ((1 << (_la - 454)) & 65535) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GameTermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GAME(self):
            return self.getToken(ScryfallQueryParser.GAME, 0)

        def COLON(self):
            return self.getToken(ScryfallQueryParser.COLON, 0)

        def PAPER(self):
            return self.getToken(ScryfallQueryParser.PAPER, 0)

        def MTGO(self):
            return self.getToken(ScryfallQueryParser.MTGO, 0)

        def ARENA(self):
            return self.getToken(ScryfallQueryParser.ARENA, 0)

        def getRuleIndex(self):
            return ScryfallQueryParser.RULE_gameTerm

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGameTerm" ):
                listener.enterGameTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGameTerm" ):
                listener.exitGameTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGameTerm" ):
                return visitor.visitGameTerm(self)
            else:
                return visitor.visitChildren(self)




    def gameTerm(self):

        localctx = ScryfallQueryParser.GameTermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_gameTerm)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 249
            self.match(ScryfallQueryParser.GAME)
            self.state = 250
            self.match(ScryfallQueryParser.COLON)
            self.state = 251
            _la = self._input.LA(1)
            if not(((((_la - 470)) & ~0x3f) == 0 and ((1 << (_la - 470)) & 7) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GameValueTokenContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PAPER(self):
            return self.getToken(ScryfallQueryParser.PAPER, 0)

        def MTGO(self):
            return self.getToken(ScryfallQueryParser.MTGO, 0)

        def ARENA(self):
            return self.getToken(ScryfallQueryParser.ARENA, 0)

        def getRuleIndex(self):
            return ScryfallQueryParser.RULE_gameValueToken

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGameValueToken" ):
                listener.enterGameValueToken(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGameValueToken" ):
                listener.exitGameValueToken(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGameValueToken" ):
                return visitor.visitGameValueToken(self)
            else:
                return visitor.visitChildren(self)




    def gameValueToken(self):

        localctx = ScryfallQueryParser.GameValueTokenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_gameValueToken)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 253
            _la = self._input.LA(1)
            if not(((((_la - 470)) & ~0x3f) == 0 and ((1 << (_la - 470)) & 7) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ColorTermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def compOp(self):
            return self.getTypedRuleContext(ScryfallQueryParser.CompOpContext,0)


        def colorValue(self):
            return self.getTypedRuleContext(ScryfallQueryParser.ColorValueContext,0)


        def C(self):
            return self.getToken(ScryfallQueryParser.C, 0)

        def COLOR(self):
            return self.getToken(ScryfallQueryParser.COLOR, 0)

        def getRuleIndex(self):
            return ScryfallQueryParser.RULE_colorTerm

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColorTerm" ):
                listener.enterColorTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColorTerm" ):
                listener.exitColorTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitColorTerm" ):
                return visitor.visitColorTerm(self)
            else:
                return visitor.visitChildren(self)




    def colorTerm(self):

        localctx = ScryfallQueryParser.ColorTermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_colorTerm)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 255
            _la = self._input.LA(1)
            if not(_la==48 or _la==488):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 256
            self.compOp()
            self.state = 257
            self.colorValue()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ColorValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(ScryfallQueryParser.NUMBER, 0)

        def C(self):
            return self.getToken(ScryfallQueryParser.C, 0)

        def M(self):
            return self.getToken(ScryfallQueryParser.M, 0)

        def U(self):
            return self.getToken(ScryfallQueryParser.U, 0)

        def B(self):
            return self.getToken(ScryfallQueryParser.B, 0)

        def R(self):
            return self.getToken(ScryfallQueryParser.R, 0)

        def COLOR_SET(self):
            return self.getToken(ScryfallQueryParser.COLOR_SET, 0)

        def WHITE(self):
            return self.getToken(ScryfallQueryParser.WHITE, 0)

        def BLUE(self):
            return self.getToken(ScryfallQueryParser.BLUE, 0)

        def BLACK(self):
            return self.getToken(ScryfallQueryParser.BLACK, 0)

        def RED(self):
            return self.getToken(ScryfallQueryParser.RED, 0)

        def GREEN(self):
            return self.getToken(ScryfallQueryParser.GREEN, 0)

        def COLORLESS(self):
            return self.getToken(ScryfallQueryParser.COLORLESS, 0)

        def MULTICOLOR(self):
            return self.getToken(ScryfallQueryParser.MULTICOLOR, 0)

        def UB(self):
            return self.getToken(ScryfallQueryParser.UB, 0)

        def AZORIUS(self):
            return self.getToken(ScryfallQueryParser.AZORIUS, 0)

        def DIMIR(self):
            return self.getToken(ScryfallQueryParser.DIMIR, 0)

        def RAKDOS(self):
            return self.getToken(ScryfallQueryParser.RAKDOS, 0)

        def GRUUL(self):
            return self.getToken(ScryfallQueryParser.GRUUL, 0)

        def SELESNYA(self):
            return self.getToken(ScryfallQueryParser.SELESNYA, 0)

        def ORZHOV(self):
            return self.getToken(ScryfallQueryParser.ORZHOV, 0)

        def IZZET(self):
            return self.getToken(ScryfallQueryParser.IZZET, 0)

        def GOLGARI(self):
            return self.getToken(ScryfallQueryParser.GOLGARI, 0)

        def BOROS(self):
            return self.getToken(ScryfallQueryParser.BOROS, 0)

        def SIMIC(self):
            return self.getToken(ScryfallQueryParser.SIMIC, 0)

        def BANT(self):
            return self.getToken(ScryfallQueryParser.BANT, 0)

        def ESPER(self):
            return self.getToken(ScryfallQueryParser.ESPER, 0)

        def GRIXIS(self):
            return self.getToken(ScryfallQueryParser.GRIXIS, 0)

        def JUND(self):
            return self.getToken(ScryfallQueryParser.JUND, 0)

        def NAYA(self):
            return self.getToken(ScryfallQueryParser.NAYA, 0)

        def ABZAN(self):
            return self.getToken(ScryfallQueryParser.ABZAN, 0)

        def JESKAI(self):
            return self.getToken(ScryfallQueryParser.JESKAI, 0)

        def SULTAI(self):
            return self.getToken(ScryfallQueryParser.SULTAI, 0)

        def MARDU(self):
            return self.getToken(ScryfallQueryParser.MARDU, 0)

        def TEMUR(self):
            return self.getToken(ScryfallQueryParser.TEMUR, 0)

        def QUANDRIX(self):
            return self.getToken(ScryfallQueryParser.QUANDRIX, 0)

        def PRISMARI(self):
            return self.getToken(ScryfallQueryParser.PRISMARI, 0)

        def WITHERBLOOM(self):
            return self.getToken(ScryfallQueryParser.WITHERBLOOM, 0)

        def LOREHOLD(self):
            return self.getToken(ScryfallQueryParser.LOREHOLD, 0)

        def SILVERQUILL(self):
            return self.getToken(ScryfallQueryParser.SILVERQUILL, 0)

        def CHAOS(self):
            return self.getToken(ScryfallQueryParser.CHAOS, 0)

        def AGGRESSION(self):
            return self.getToken(ScryfallQueryParser.AGGRESSION, 0)

        def ALTRUISM(self):
            return self.getToken(ScryfallQueryParser.ALTRUISM, 0)

        def GROWTH(self):
            return self.getToken(ScryfallQueryParser.GROWTH, 0)

        def ARTIFICE(self):
            return self.getToken(ScryfallQueryParser.ARTIFICE, 0)

        def getRuleIndex(self):
            return ScryfallQueryParser.RULE_colorValue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColorValue" ):
                listener.enterColorValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColorValue" ):
                listener.exitColorValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitColorValue" ):
                return visitor.visitColorValue(self)
            else:
                return visitor.visitChildren(self)




    def colorValue(self):

        localctx = ScryfallQueryParser.ColorValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_colorValue)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 259
            _la = self._input.LA(1)
            if not(((((_la - 49)) & ~0x3f) == 0 and ((1 << (_la - 49)) & 18014535948435455) != 0) or ((((_la - 485)) & ~0x3f) == 0 and ((1 << (_la - 485)) & 40534046182211593) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RarityTermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def compOp(self):
            return self.getTypedRuleContext(ScryfallQueryParser.CompOpContext,0)


        def rarityValue(self):
            return self.getTypedRuleContext(ScryfallQueryParser.RarityValueContext,0)


        def R(self):
            return self.getToken(ScryfallQueryParser.R, 0)

        def RARITY(self):
            return self.getToken(ScryfallQueryParser.RARITY, 0)

        def IN(self):
            return self.getToken(ScryfallQueryParser.IN, 0)

        def getRuleIndex(self):
            return ScryfallQueryParser.RULE_rarityTerm

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRarityTerm" ):
                listener.enterRarityTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRarityTerm" ):
                listener.exitRarityTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRarityTerm" ):
                return visitor.visitRarityTerm(self)
            else:
                return visitor.visitChildren(self)




    def rarityTerm(self):

        localctx = ScryfallQueryParser.RarityTermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_rarityTerm)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 261
            _la = self._input.LA(1)
            if not(_la==26 or _la==506 or _la==524):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 262
            self.compOp()
            self.state = 263
            self.rarityValue()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RarityValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMON(self):
            return self.getToken(ScryfallQueryParser.COMMON, 0)

        def UNCOMMON(self):
            return self.getToken(ScryfallQueryParser.UNCOMMON, 0)

        def RARE(self):
            return self.getToken(ScryfallQueryParser.RARE, 0)

        def SPECIAL(self):
            return self.getToken(ScryfallQueryParser.SPECIAL, 0)

        def MYTHIC(self):
            return self.getToken(ScryfallQueryParser.MYTHIC, 0)

        def BONUS(self):
            return self.getToken(ScryfallQueryParser.BONUS, 0)

        def C(self):
            return self.getToken(ScryfallQueryParser.C, 0)

        def U(self):
            return self.getToken(ScryfallQueryParser.U, 0)

        def R(self):
            return self.getToken(ScryfallQueryParser.R, 0)

        def M(self):
            return self.getToken(ScryfallQueryParser.M, 0)

        def B(self):
            return self.getToken(ScryfallQueryParser.B, 0)

        def getRuleIndex(self):
            return ScryfallQueryParser.RULE_rarityValue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRarityValue" ):
                listener.enterRarityValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRarityValue" ):
                listener.exitRarityValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRarityValue" ):
                return visitor.visitRarityValue(self)
            else:
                return visitor.visitChildren(self)




    def rarityValue(self):

        localctx = ScryfallQueryParser.RarityValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_rarityValue)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 265
            _la = self._input.LA(1)
            if not(((((_la - 473)) & ~0x3f) == 0 and ((1 << (_la - 473)) & 6756498952720447) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MvTermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def compOp(self):
            return self.getTypedRuleContext(ScryfallQueryParser.CompOpContext,0)


        def MV(self):
            return self.getToken(ScryfallQueryParser.MV, 0)

        def MANAVALUE(self):
            return self.getToken(ScryfallQueryParser.MANAVALUE, 0)

        def EVEN(self):
            return self.getToken(ScryfallQueryParser.EVEN, 0)

        def ODD(self):
            return self.getToken(ScryfallQueryParser.ODD, 0)

        def NUMBER(self):
            return self.getToken(ScryfallQueryParser.NUMBER, 0)

        def getRuleIndex(self):
            return ScryfallQueryParser.RULE_mvTerm

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMvTerm" ):
                listener.enterMvTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMvTerm" ):
                listener.exitMvTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMvTerm" ):
                return visitor.visitMvTerm(self)
            else:
                return visitor.visitChildren(self)




    def mvTerm(self):

        localctx = ScryfallQueryParser.MvTermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_mvTerm)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 267
            _la = self._input.LA(1)
            if not(_la==27 or _la==28):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 268
            self.compOp()
            self.state = 269
            _la = self._input.LA(1)
            if not(((((_la - 479)) & ~0x3f) == 0 and ((1 << (_la - 479)) & 288230376151711747) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GenericTermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def genericKey(self):
            return self.getTypedRuleContext(ScryfallQueryParser.GenericKeyContext,0)


        def compOp(self):
            return self.getTypedRuleContext(ScryfallQueryParser.CompOpContext,0)


        def genericValue(self):
            return self.getTypedRuleContext(ScryfallQueryParser.GenericValueContext,0)


        def getRuleIndex(self):
            return ScryfallQueryParser.RULE_genericTerm

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGenericTerm" ):
                listener.enterGenericTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGenericTerm" ):
                listener.exitGenericTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGenericTerm" ):
                return visitor.visitGenericTerm(self)
            else:
                return visitor.visitChildren(self)




    def genericTerm(self):

        localctx = ScryfallQueryParser.GenericTermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_genericTerm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 271
            self.genericKey()
            self.state = 272
            self.compOp()
            self.state = 273
            self.genericValue()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GenericKeyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def A(self):
            return self.getToken(ScryfallQueryParser.A, 0)

        def ARTIST(self):
            return self.getToken(ScryfallQueryParser.ARTIST, 0)

        def ARTISTS(self):
            return self.getToken(ScryfallQueryParser.ARTISTS, 0)

        def ART(self):
            return self.getToken(ScryfallQueryParser.ART, 0)

        def ATAG(self):
            return self.getToken(ScryfallQueryParser.ATAG, 0)

        def ARTTAG(self):
            return self.getToken(ScryfallQueryParser.ARTTAG, 0)

        def B(self):
            return self.getToken(ScryfallQueryParser.B, 0)

        def BLOCK(self):
            return self.getToken(ScryfallQueryParser.BLOCK, 0)

        def BORDER(self):
            return self.getToken(ScryfallQueryParser.BORDER, 0)

        def CN(self):
            return self.getToken(ScryfallQueryParser.CN, 0)

        def NUMBER_KEY(self):
            return self.getToken(ScryfallQueryParser.NUMBER_KEY, 0)

        def CUBE(self):
            return self.getToken(ScryfallQueryParser.CUBE, 0)

        def DATE(self):
            return self.getToken(ScryfallQueryParser.DATE, 0)

        def DEVOTION(self):
            return self.getToken(ScryfallQueryParser.DEVOTION, 0)

        def E(self):
            return self.getToken(ScryfallQueryParser.E, 0)

        def EDITION(self):
            return self.getToken(ScryfallQueryParser.EDITION, 0)

        def FO(self):
            return self.getToken(ScryfallQueryParser.FO, 0)

        def FULLORACLE(self):
            return self.getToken(ScryfallQueryParser.FULLORACLE, 0)

        def FT(self):
            return self.getToken(ScryfallQueryParser.FT, 0)

        def FLAVOR(self):
            return self.getToken(ScryfallQueryParser.FLAVOR, 0)

        def FUNCTION(self):
            return self.getToken(ScryfallQueryParser.FUNCTION, 0)

        def OTAG(self):
            return self.getToken(ScryfallQueryParser.OTAG, 0)

        def ORACLETAG(self):
            return self.getToken(ScryfallQueryParser.ORACLETAG, 0)

        def ID(self):
            return self.getToken(ScryfallQueryParser.ID, 0)

        def IDENTITY(self):
            return self.getToken(ScryfallQueryParser.IDENTITY, 0)

        def ILLUSTRATIONS(self):
            return self.getToken(ScryfallQueryParser.ILLUSTRATIONS, 0)

        def IN(self):
            return self.getToken(ScryfallQueryParser.IN, 0)

        def KEYWORD(self):
            return self.getToken(ScryfallQueryParser.KEYWORD, 0)

        def KW(self):
            return self.getToken(ScryfallQueryParser.KW, 0)

        def LANG(self):
            return self.getToken(ScryfallQueryParser.LANG, 0)

        def LANGUAGE(self):
            return self.getToken(ScryfallQueryParser.LANGUAGE, 0)

        def LOY(self):
            return self.getToken(ScryfallQueryParser.LOY, 0)

        def LOYALTY(self):
            return self.getToken(ScryfallQueryParser.LOYALTY, 0)

        def M(self):
            return self.getToken(ScryfallQueryParser.M, 0)

        def MANA(self):
            return self.getToken(ScryfallQueryParser.MANA, 0)

        def N(self):
            return self.getToken(ScryfallQueryParser.N, 0)

        def NAME(self):
            return self.getToken(ScryfallQueryParser.NAME, 0)

        def NEW(self):
            return self.getToken(ScryfallQueryParser.NEW, 0)

        def O(self):
            return self.getToken(ScryfallQueryParser.O, 0)

        def ORACLE(self):
            return self.getToken(ScryfallQueryParser.ORACLE, 0)

        def PAPERPRINTS(self):
            return self.getToken(ScryfallQueryParser.PAPERPRINTS, 0)

        def PAPERSETS(self):
            return self.getToken(ScryfallQueryParser.PAPERSETS, 0)

        def POW(self):
            return self.getToken(ScryfallQueryParser.POW, 0)

        def POWER(self):
            return self.getToken(ScryfallQueryParser.POWER, 0)

        def PT(self):
            return self.getToken(ScryfallQueryParser.PT, 0)

        def POWTOU(self):
            return self.getToken(ScryfallQueryParser.POWTOU, 0)

        def PRINTS(self):
            return self.getToken(ScryfallQueryParser.PRINTS, 0)

        def PRODUCES(self):
            return self.getToken(ScryfallQueryParser.PRODUCES, 0)

        def R(self):
            return self.getToken(ScryfallQueryParser.R, 0)

        def RARITY(self):
            return self.getToken(ScryfallQueryParser.RARITY, 0)

        def S(self):
            return self.getToken(ScryfallQueryParser.S, 0)

        def SET(self):
            return self.getToken(ScryfallQueryParser.SET, 0)

        def SETS(self):
            return self.getToken(ScryfallQueryParser.SETS, 0)

        def STAMP(self):
            return self.getToken(ScryfallQueryParser.STAMP, 0)

        def ST(self):
            return self.getToken(ScryfallQueryParser.ST, 0)

        def GAME(self):
            return self.getToken(ScryfallQueryParser.GAME, 0)

        def T(self):
            return self.getToken(ScryfallQueryParser.T, 0)

        def TYPE(self):
            return self.getToken(ScryfallQueryParser.TYPE, 0)

        def TOU(self):
            return self.getToken(ScryfallQueryParser.TOU, 0)

        def TOUGHNESS(self):
            return self.getToken(ScryfallQueryParser.TOUGHNESS, 0)

        def USD(self):
            return self.getToken(ScryfallQueryParser.USD, 0)

        def EUR(self):
            return self.getToken(ScryfallQueryParser.EUR, 0)

        def TIX(self):
            return self.getToken(ScryfallQueryParser.TIX, 0)

        def CHEAPEST(self):
            return self.getToken(ScryfallQueryParser.CHEAPEST, 0)

        def WM(self):
            return self.getToken(ScryfallQueryParser.WM, 0)

        def WATERMARK(self):
            return self.getToken(ScryfallQueryParser.WATERMARK, 0)

        def YEAR(self):
            return self.getToken(ScryfallQueryParser.YEAR, 0)

        def getRuleIndex(self):
            return ScryfallQueryParser.RULE_genericKey

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGenericKey" ):
                listener.enterGenericKey(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGenericKey" ):
                listener.exitGenericKey(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGenericKey" ):
                return visitor.visitGenericKey(self)
            else:
                return visitor.visitChildren(self)




    def genericKey(self):

        localctx = ScryfallQueryParser.GenericKeyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_genericKey)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 275
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 280101761581056) != 0) or _la==155 or ((((_la - 481)) & ~0x3f) == 0 and ((1 << (_la - 481)) & 72040001851883391) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CompOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COLON(self):
            return self.getToken(ScryfallQueryParser.COLON, 0)

        def NEQ(self):
            return self.getToken(ScryfallQueryParser.NEQ, 0)

        def GTE(self):
            return self.getToken(ScryfallQueryParser.GTE, 0)

        def LTE(self):
            return self.getToken(ScryfallQueryParser.LTE, 0)

        def EQ(self):
            return self.getToken(ScryfallQueryParser.EQ, 0)

        def GT(self):
            return self.getToken(ScryfallQueryParser.GT, 0)

        def LT(self):
            return self.getToken(ScryfallQueryParser.LT, 0)

        def getRuleIndex(self):
            return ScryfallQueryParser.RULE_compOp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompOp" ):
                listener.enterCompOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompOp" ):
                listener.exitCompOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompOp" ):
                return visitor.visitCompOp(self)
            else:
                return visitor.visitChildren(self)




    def compOp(self):

        localctx = ScryfallQueryParser.CompOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_compOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 277
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4064) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GenericValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def regex(self):
            return self.getTypedRuleContext(ScryfallQueryParser.RegexContext,0)


        def quotedText(self):
            return self.getTypedRuleContext(ScryfallQueryParser.QuotedTextContext,0)


        def bareValue(self):
            return self.getTypedRuleContext(ScryfallQueryParser.BareValueContext,0)


        def word(self):
            return self.getTypedRuleContext(ScryfallQueryParser.WordContext,0)


        def genericKey(self):
            return self.getTypedRuleContext(ScryfallQueryParser.GenericKeyContext,0)


        def rarityValue(self):
            return self.getTypedRuleContext(ScryfallQueryParser.RarityValueContext,0)


        def formatValue(self):
            return self.getTypedRuleContext(ScryfallQueryParser.FormatValueContext,0)


        def isValue(self):
            return self.getTypedRuleContext(ScryfallQueryParser.IsValueContext,0)


        def orderValue(self):
            return self.getTypedRuleContext(ScryfallQueryParser.OrderValueContext,0)


        def preferValue(self):
            return self.getTypedRuleContext(ScryfallQueryParser.PreferValueContext,0)


        def directionValue(self):
            return self.getTypedRuleContext(ScryfallQueryParser.DirectionValueContext,0)


        def uniqueValue(self):
            return self.getTypedRuleContext(ScryfallQueryParser.UniqueValueContext,0)


        def displayValue(self):
            return self.getTypedRuleContext(ScryfallQueryParser.DisplayValueContext,0)


        def gameValueToken(self):
            return self.getTypedRuleContext(ScryfallQueryParser.GameValueTokenContext,0)


        def getRuleIndex(self):
            return ScryfallQueryParser.RULE_genericValue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGenericValue" ):
                listener.enterGenericValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGenericValue" ):
                listener.exitGenericValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGenericValue" ):
                return visitor.visitGenericValue(self)
            else:
                return visitor.visitChildren(self)




    def genericValue(self):

        localctx = ScryfallQueryParser.GenericValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_genericValue)
        try:
            self.state = 293
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 279
                self.regex()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 280
                self.quotedText()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 281
                self.bareValue()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 282
                self.word()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 283
                self.genericKey()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 284
                self.rarityValue()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 285
                self.formatValue()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 286
                self.isValue()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 287
                self.orderValue()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 288
                self.preferValue()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 289
                self.directionValue()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 290
                self.uniqueValue()
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 291
                self.displayValue()
                pass

            elif la_ == 14:
                self.enterOuterAlt(localctx, 14)
                self.state = 292
                self.gameValueToken()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QuotedTextContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def QUOTED_TEXT(self):
            return self.getToken(ScryfallQueryParser.QUOTED_TEXT, 0)

        def getRuleIndex(self):
            return ScryfallQueryParser.RULE_quotedText

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuotedText" ):
                listener.enterQuotedText(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuotedText" ):
                listener.exitQuotedText(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQuotedText" ):
                return visitor.visitQuotedText(self)
            else:
                return visitor.visitChildren(self)




    def quotedText(self):

        localctx = ScryfallQueryParser.QuotedTextContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_quotedText)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 295
            self.match(ScryfallQueryParser.QUOTED_TEXT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RegexContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def REGEX(self):
            return self.getToken(ScryfallQueryParser.REGEX, 0)

        def getRuleIndex(self):
            return ScryfallQueryParser.RULE_regex

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRegex" ):
                listener.enterRegex(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRegex" ):
                listener.exitRegex(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRegex" ):
                return visitor.visitRegex(self)
            else:
                return visitor.visitChildren(self)




    def regex(self):

        localctx = ScryfallQueryParser.RegexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_regex)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 297
            self.match(ScryfallQueryParser.REGEX)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WordContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WORD(self):
            return self.getToken(ScryfallQueryParser.WORD, 0)

        def COLOR_SET(self):
            return self.getToken(ScryfallQueryParser.COLOR_SET, 0)

        def getRuleIndex(self):
            return ScryfallQueryParser.RULE_word

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWord" ):
                listener.enterWord(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWord" ):
                listener.exitWord(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWord" ):
                return visitor.visitWord(self)
            else:
                return visitor.visitChildren(self)




    def word(self):

        localctx = ScryfallQueryParser.WordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_word)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 299
            _la = self._input.LA(1)
            if not(_la==540 or _la==541):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BareValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BARE_VALUE(self):
            return self.getToken(ScryfallQueryParser.BARE_VALUE, 0)

        def COLOR_SET(self):
            return self.getToken(ScryfallQueryParser.COLOR_SET, 0)

        def getRuleIndex(self):
            return ScryfallQueryParser.RULE_bareValue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBareValue" ):
                listener.enterBareValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBareValue" ):
                listener.exitBareValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBareValue" ):
                return visitor.visitBareValue(self)
            else:
                return visitor.visitChildren(self)




    def bareValue(self):

        localctx = ScryfallQueryParser.BareValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_bareValue)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 301
            _la = self._input.LA(1)
            if not(_la==540 or _la==542):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





