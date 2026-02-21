# Generated from grammar/ScryfallQuery.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ScryfallQueryParser import ScryfallQueryParser
else:
    from ScryfallQueryParser import ScryfallQueryParser

# This class defines a complete listener for a parse tree produced by ScryfallQueryParser.
class ScryfallQueryListener(ParseTreeListener):

    # Enter a parse tree produced by ScryfallQueryParser#start.
    def enterStart(self, ctx:ScryfallQueryParser.StartContext):
        pass

    # Exit a parse tree produced by ScryfallQueryParser#start.
    def exitStart(self, ctx:ScryfallQueryParser.StartContext):
        pass


    # Enter a parse tree produced by ScryfallQueryParser#topExpr.
    def enterTopExpr(self, ctx:ScryfallQueryParser.TopExprContext):
        pass

    # Exit a parse tree produced by ScryfallQueryParser#topExpr.
    def exitTopExpr(self, ctx:ScryfallQueryParser.TopExprContext):
        pass


    # Enter a parse tree produced by ScryfallQueryParser#topAndExpr.
    def enterTopAndExpr(self, ctx:ScryfallQueryParser.TopAndExprContext):
        pass

    # Exit a parse tree produced by ScryfallQueryParser#topAndExpr.
    def exitTopAndExpr(self, ctx:ScryfallQueryParser.TopAndExprContext):
        pass


    # Enter a parse tree produced by ScryfallQueryParser#topFactor.
    def enterTopFactor(self, ctx:ScryfallQueryParser.TopFactorContext):
        pass

    # Exit a parse tree produced by ScryfallQueryParser#topFactor.
    def exitTopFactor(self, ctx:ScryfallQueryParser.TopFactorContext):
        pass


    # Enter a parse tree produced by ScryfallQueryParser#topGroup.
    def enterTopGroup(self, ctx:ScryfallQueryParser.TopGroupContext):
        pass

    # Exit a parse tree produced by ScryfallQueryParser#topGroup.
    def exitTopGroup(self, ctx:ScryfallQueryParser.TopGroupContext):
        pass


    # Enter a parse tree produced by ScryfallQueryParser#topTerm.
    def enterTopTerm(self, ctx:ScryfallQueryParser.TopTermContext):
        pass

    # Exit a parse tree produced by ScryfallQueryParser#topTerm.
    def exitTopTerm(self, ctx:ScryfallQueryParser.TopTermContext):
        pass


    # Enter a parse tree produced by ScryfallQueryParser#parenExpr.
    def enterParenExpr(self, ctx:ScryfallQueryParser.ParenExprContext):
        pass

    # Exit a parse tree produced by ScryfallQueryParser#parenExpr.
    def exitParenExpr(self, ctx:ScryfallQueryParser.ParenExprContext):
        pass


    # Enter a parse tree produced by ScryfallQueryParser#parenAndExpr.
    def enterParenAndExpr(self, ctx:ScryfallQueryParser.ParenAndExprContext):
        pass

    # Exit a parse tree produced by ScryfallQueryParser#parenAndExpr.
    def exitParenAndExpr(self, ctx:ScryfallQueryParser.ParenAndExprContext):
        pass


    # Enter a parse tree produced by ScryfallQueryParser#parenFactor.
    def enterParenFactor(self, ctx:ScryfallQueryParser.ParenFactorContext):
        pass

    # Exit a parse tree produced by ScryfallQueryParser#parenFactor.
    def exitParenFactor(self, ctx:ScryfallQueryParser.ParenFactorContext):
        pass


    # Enter a parse tree produced by ScryfallQueryParser#parenGroup.
    def enterParenGroup(self, ctx:ScryfallQueryParser.ParenGroupContext):
        pass

    # Exit a parse tree produced by ScryfallQueryParser#parenGroup.
    def exitParenGroup(self, ctx:ScryfallQueryParser.ParenGroupContext):
        pass


    # Enter a parse tree produced by ScryfallQueryParser#parenTerm.
    def enterParenTerm(self, ctx:ScryfallQueryParser.ParenTermContext):
        pass

    # Exit a parse tree produced by ScryfallQueryParser#parenTerm.
    def exitParenTerm(self, ctx:ScryfallQueryParser.ParenTermContext):
        pass


    # Enter a parse tree produced by ScryfallQueryParser#topAtom.
    def enterTopAtom(self, ctx:ScryfallQueryParser.TopAtomContext):
        pass

    # Exit a parse tree produced by ScryfallQueryParser#topAtom.
    def exitTopAtom(self, ctx:ScryfallQueryParser.TopAtomContext):
        pass


    # Enter a parse tree produced by ScryfallQueryParser#displayAtom.
    def enterDisplayAtom(self, ctx:ScryfallQueryParser.DisplayAtomContext):
        pass

    # Exit a parse tree produced by ScryfallQueryParser#displayAtom.
    def exitDisplayAtom(self, ctx:ScryfallQueryParser.DisplayAtomContext):
        pass


    # Enter a parse tree produced by ScryfallQueryParser#parenAtom.
    def enterParenAtom(self, ctx:ScryfallQueryParser.ParenAtomContext):
        pass

    # Exit a parse tree produced by ScryfallQueryParser#parenAtom.
    def exitParenAtom(self, ctx:ScryfallQueryParser.ParenAtomContext):
        pass


    # Enter a parse tree produced by ScryfallQueryParser#nonDisplayAtom.
    def enterNonDisplayAtom(self, ctx:ScryfallQueryParser.NonDisplayAtomContext):
        pass

    # Exit a parse tree produced by ScryfallQueryParser#nonDisplayAtom.
    def exitNonDisplayAtom(self, ctx:ScryfallQueryParser.NonDisplayAtomContext):
        pass


    # Enter a parse tree produced by ScryfallQueryParser#exactName.
    def enterExactName(self, ctx:ScryfallQueryParser.ExactNameContext):
        pass

    # Exit a parse tree produced by ScryfallQueryParser#exactName.
    def exitExactName(self, ctx:ScryfallQueryParser.ExactNameContext):
        pass


    # Enter a parse tree produced by ScryfallQueryParser#uniqueTerm.
    def enterUniqueTerm(self, ctx:ScryfallQueryParser.UniqueTermContext):
        pass

    # Exit a parse tree produced by ScryfallQueryParser#uniqueTerm.
    def exitUniqueTerm(self, ctx:ScryfallQueryParser.UniqueTermContext):
        pass


    # Enter a parse tree produced by ScryfallQueryParser#uniqueKey.
    def enterUniqueKey(self, ctx:ScryfallQueryParser.UniqueKeyContext):
        pass

    # Exit a parse tree produced by ScryfallQueryParser#uniqueKey.
    def exitUniqueKey(self, ctx:ScryfallQueryParser.UniqueKeyContext):
        pass


    # Enter a parse tree produced by ScryfallQueryParser#uniqueValue.
    def enterUniqueValue(self, ctx:ScryfallQueryParser.UniqueValueContext):
        pass

    # Exit a parse tree produced by ScryfallQueryParser#uniqueValue.
    def exitUniqueValue(self, ctx:ScryfallQueryParser.UniqueValueContext):
        pass


    # Enter a parse tree produced by ScryfallQueryParser#displayTerm.
    def enterDisplayTerm(self, ctx:ScryfallQueryParser.DisplayTermContext):
        pass

    # Exit a parse tree produced by ScryfallQueryParser#displayTerm.
    def exitDisplayTerm(self, ctx:ScryfallQueryParser.DisplayTermContext):
        pass


    # Enter a parse tree produced by ScryfallQueryParser#displayValue.
    def enterDisplayValue(self, ctx:ScryfallQueryParser.DisplayValueContext):
        pass

    # Exit a parse tree produced by ScryfallQueryParser#displayValue.
    def exitDisplayValue(self, ctx:ScryfallQueryParser.DisplayValueContext):
        pass


    # Enter a parse tree produced by ScryfallQueryParser#orderTerm.
    def enterOrderTerm(self, ctx:ScryfallQueryParser.OrderTermContext):
        pass

    # Exit a parse tree produced by ScryfallQueryParser#orderTerm.
    def exitOrderTerm(self, ctx:ScryfallQueryParser.OrderTermContext):
        pass


    # Enter a parse tree produced by ScryfallQueryParser#orderValue.
    def enterOrderValue(self, ctx:ScryfallQueryParser.OrderValueContext):
        pass

    # Exit a parse tree produced by ScryfallQueryParser#orderValue.
    def exitOrderValue(self, ctx:ScryfallQueryParser.OrderValueContext):
        pass


    # Enter a parse tree produced by ScryfallQueryParser#directionTerm.
    def enterDirectionTerm(self, ctx:ScryfallQueryParser.DirectionTermContext):
        pass

    # Exit a parse tree produced by ScryfallQueryParser#directionTerm.
    def exitDirectionTerm(self, ctx:ScryfallQueryParser.DirectionTermContext):
        pass


    # Enter a parse tree produced by ScryfallQueryParser#directionValue.
    def enterDirectionValue(self, ctx:ScryfallQueryParser.DirectionValueContext):
        pass

    # Exit a parse tree produced by ScryfallQueryParser#directionValue.
    def exitDirectionValue(self, ctx:ScryfallQueryParser.DirectionValueContext):
        pass


    # Enter a parse tree produced by ScryfallQueryParser#preferTerm.
    def enterPreferTerm(self, ctx:ScryfallQueryParser.PreferTermContext):
        pass

    # Exit a parse tree produced by ScryfallQueryParser#preferTerm.
    def exitPreferTerm(self, ctx:ScryfallQueryParser.PreferTermContext):
        pass


    # Enter a parse tree produced by ScryfallQueryParser#preferValue.
    def enterPreferValue(self, ctx:ScryfallQueryParser.PreferValueContext):
        pass

    # Exit a parse tree produced by ScryfallQueryParser#preferValue.
    def exitPreferValue(self, ctx:ScryfallQueryParser.PreferValueContext):
        pass


    # Enter a parse tree produced by ScryfallQueryParser#includeTerm.
    def enterIncludeTerm(self, ctx:ScryfallQueryParser.IncludeTermContext):
        pass

    # Exit a parse tree produced by ScryfallQueryParser#includeTerm.
    def exitIncludeTerm(self, ctx:ScryfallQueryParser.IncludeTermContext):
        pass


    # Enter a parse tree produced by ScryfallQueryParser#isTerm.
    def enterIsTerm(self, ctx:ScryfallQueryParser.IsTermContext):
        pass

    # Exit a parse tree produced by ScryfallQueryParser#isTerm.
    def exitIsTerm(self, ctx:ScryfallQueryParser.IsTermContext):
        pass


    # Enter a parse tree produced by ScryfallQueryParser#notTerm.
    def enterNotTerm(self, ctx:ScryfallQueryParser.NotTermContext):
        pass

    # Exit a parse tree produced by ScryfallQueryParser#notTerm.
    def exitNotTerm(self, ctx:ScryfallQueryParser.NotTermContext):
        pass


    # Enter a parse tree produced by ScryfallQueryParser#isValue.
    def enterIsValue(self, ctx:ScryfallQueryParser.IsValueContext):
        pass

    # Exit a parse tree produced by ScryfallQueryParser#isValue.
    def exitIsValue(self, ctx:ScryfallQueryParser.IsValueContext):
        pass


    # Enter a parse tree produced by ScryfallQueryParser#formatTerm.
    def enterFormatTerm(self, ctx:ScryfallQueryParser.FormatTermContext):
        pass

    # Exit a parse tree produced by ScryfallQueryParser#formatTerm.
    def exitFormatTerm(self, ctx:ScryfallQueryParser.FormatTermContext):
        pass


    # Enter a parse tree produced by ScryfallQueryParser#bannedTerm.
    def enterBannedTerm(self, ctx:ScryfallQueryParser.BannedTermContext):
        pass

    # Exit a parse tree produced by ScryfallQueryParser#bannedTerm.
    def exitBannedTerm(self, ctx:ScryfallQueryParser.BannedTermContext):
        pass


    # Enter a parse tree produced by ScryfallQueryParser#restrictedTerm.
    def enterRestrictedTerm(self, ctx:ScryfallQueryParser.RestrictedTermContext):
        pass

    # Exit a parse tree produced by ScryfallQueryParser#restrictedTerm.
    def exitRestrictedTerm(self, ctx:ScryfallQueryParser.RestrictedTermContext):
        pass


    # Enter a parse tree produced by ScryfallQueryParser#formatValue.
    def enterFormatValue(self, ctx:ScryfallQueryParser.FormatValueContext):
        pass

    # Exit a parse tree produced by ScryfallQueryParser#formatValue.
    def exitFormatValue(self, ctx:ScryfallQueryParser.FormatValueContext):
        pass


    # Enter a parse tree produced by ScryfallQueryParser#gameTerm.
    def enterGameTerm(self, ctx:ScryfallQueryParser.GameTermContext):
        pass

    # Exit a parse tree produced by ScryfallQueryParser#gameTerm.
    def exitGameTerm(self, ctx:ScryfallQueryParser.GameTermContext):
        pass


    # Enter a parse tree produced by ScryfallQueryParser#gameValueToken.
    def enterGameValueToken(self, ctx:ScryfallQueryParser.GameValueTokenContext):
        pass

    # Exit a parse tree produced by ScryfallQueryParser#gameValueToken.
    def exitGameValueToken(self, ctx:ScryfallQueryParser.GameValueTokenContext):
        pass


    # Enter a parse tree produced by ScryfallQueryParser#colorTerm.
    def enterColorTerm(self, ctx:ScryfallQueryParser.ColorTermContext):
        pass

    # Exit a parse tree produced by ScryfallQueryParser#colorTerm.
    def exitColorTerm(self, ctx:ScryfallQueryParser.ColorTermContext):
        pass


    # Enter a parse tree produced by ScryfallQueryParser#colorValue.
    def enterColorValue(self, ctx:ScryfallQueryParser.ColorValueContext):
        pass

    # Exit a parse tree produced by ScryfallQueryParser#colorValue.
    def exitColorValue(self, ctx:ScryfallQueryParser.ColorValueContext):
        pass


    # Enter a parse tree produced by ScryfallQueryParser#borderTerm.
    def enterBorderTerm(self, ctx:ScryfallQueryParser.BorderTermContext):
        pass

    # Exit a parse tree produced by ScryfallQueryParser#borderTerm.
    def exitBorderTerm(self, ctx:ScryfallQueryParser.BorderTermContext):
        pass


    # Enter a parse tree produced by ScryfallQueryParser#borderValue.
    def enterBorderValue(self, ctx:ScryfallQueryParser.BorderValueContext):
        pass

    # Exit a parse tree produced by ScryfallQueryParser#borderValue.
    def exitBorderValue(self, ctx:ScryfallQueryParser.BorderValueContext):
        pass


    # Enter a parse tree produced by ScryfallQueryParser#frameTerm.
    def enterFrameTerm(self, ctx:ScryfallQueryParser.FrameTermContext):
        pass

    # Exit a parse tree produced by ScryfallQueryParser#frameTerm.
    def exitFrameTerm(self, ctx:ScryfallQueryParser.FrameTermContext):
        pass


    # Enter a parse tree produced by ScryfallQueryParser#frameValue.
    def enterFrameValue(self, ctx:ScryfallQueryParser.FrameValueContext):
        pass

    # Exit a parse tree produced by ScryfallQueryParser#frameValue.
    def exitFrameValue(self, ctx:ScryfallQueryParser.FrameValueContext):
        pass


    # Enter a parse tree produced by ScryfallQueryParser#languageTerm.
    def enterLanguageTerm(self, ctx:ScryfallQueryParser.LanguageTermContext):
        pass

    # Exit a parse tree produced by ScryfallQueryParser#languageTerm.
    def exitLanguageTerm(self, ctx:ScryfallQueryParser.LanguageTermContext):
        pass


    # Enter a parse tree produced by ScryfallQueryParser#languageValue.
    def enterLanguageValue(self, ctx:ScryfallQueryParser.LanguageValueContext):
        pass

    # Exit a parse tree produced by ScryfallQueryParser#languageValue.
    def exitLanguageValue(self, ctx:ScryfallQueryParser.LanguageValueContext):
        pass


    # Enter a parse tree produced by ScryfallQueryParser#stampTerm.
    def enterStampTerm(self, ctx:ScryfallQueryParser.StampTermContext):
        pass

    # Exit a parse tree produced by ScryfallQueryParser#stampTerm.
    def exitStampTerm(self, ctx:ScryfallQueryParser.StampTermContext):
        pass


    # Enter a parse tree produced by ScryfallQueryParser#stampValue.
    def enterStampValue(self, ctx:ScryfallQueryParser.StampValueContext):
        pass

    # Exit a parse tree produced by ScryfallQueryParser#stampValue.
    def exitStampValue(self, ctx:ScryfallQueryParser.StampValueContext):
        pass


    # Enter a parse tree produced by ScryfallQueryParser#rarityTerm.
    def enterRarityTerm(self, ctx:ScryfallQueryParser.RarityTermContext):
        pass

    # Exit a parse tree produced by ScryfallQueryParser#rarityTerm.
    def exitRarityTerm(self, ctx:ScryfallQueryParser.RarityTermContext):
        pass


    # Enter a parse tree produced by ScryfallQueryParser#rarityValue.
    def enterRarityValue(self, ctx:ScryfallQueryParser.RarityValueContext):
        pass

    # Exit a parse tree produced by ScryfallQueryParser#rarityValue.
    def exitRarityValue(self, ctx:ScryfallQueryParser.RarityValueContext):
        pass


    # Enter a parse tree produced by ScryfallQueryParser#powerTerm.
    def enterPowerTerm(self, ctx:ScryfallQueryParser.PowerTermContext):
        pass

    # Exit a parse tree produced by ScryfallQueryParser#powerTerm.
    def exitPowerTerm(self, ctx:ScryfallQueryParser.PowerTermContext):
        pass


    # Enter a parse tree produced by ScryfallQueryParser#powerValue.
    def enterPowerValue(self, ctx:ScryfallQueryParser.PowerValueContext):
        pass

    # Exit a parse tree produced by ScryfallQueryParser#powerValue.
    def exitPowerValue(self, ctx:ScryfallQueryParser.PowerValueContext):
        pass


    # Enter a parse tree produced by ScryfallQueryParser#toughnessTerm.
    def enterToughnessTerm(self, ctx:ScryfallQueryParser.ToughnessTermContext):
        pass

    # Exit a parse tree produced by ScryfallQueryParser#toughnessTerm.
    def exitToughnessTerm(self, ctx:ScryfallQueryParser.ToughnessTermContext):
        pass


    # Enter a parse tree produced by ScryfallQueryParser#toughnessValue.
    def enterToughnessValue(self, ctx:ScryfallQueryParser.ToughnessValueContext):
        pass

    # Exit a parse tree produced by ScryfallQueryParser#toughnessValue.
    def exitToughnessValue(self, ctx:ScryfallQueryParser.ToughnessValueContext):
        pass


    # Enter a parse tree produced by ScryfallQueryParser#mvTerm.
    def enterMvTerm(self, ctx:ScryfallQueryParser.MvTermContext):
        pass

    # Exit a parse tree produced by ScryfallQueryParser#mvTerm.
    def exitMvTerm(self, ctx:ScryfallQueryParser.MvTermContext):
        pass


    # Enter a parse tree produced by ScryfallQueryParser#manaTerm.
    def enterManaTerm(self, ctx:ScryfallQueryParser.ManaTermContext):
        pass

    # Exit a parse tree produced by ScryfallQueryParser#manaTerm.
    def exitManaTerm(self, ctx:ScryfallQueryParser.ManaTermContext):
        pass


    # Enter a parse tree produced by ScryfallQueryParser#manaValue.
    def enterManaValue(self, ctx:ScryfallQueryParser.ManaValueContext):
        pass

    # Exit a parse tree produced by ScryfallQueryParser#manaValue.
    def exitManaValue(self, ctx:ScryfallQueryParser.ManaValueContext):
        pass


    # Enter a parse tree produced by ScryfallQueryParser#manaValuePart.
    def enterManaValuePart(self, ctx:ScryfallQueryParser.ManaValuePartContext):
        pass

    # Exit a parse tree produced by ScryfallQueryParser#manaValuePart.
    def exitManaValuePart(self, ctx:ScryfallQueryParser.ManaValuePartContext):
        pass


    # Enter a parse tree produced by ScryfallQueryParser#genericTerm.
    def enterGenericTerm(self, ctx:ScryfallQueryParser.GenericTermContext):
        pass

    # Exit a parse tree produced by ScryfallQueryParser#genericTerm.
    def exitGenericTerm(self, ctx:ScryfallQueryParser.GenericTermContext):
        pass


    # Enter a parse tree produced by ScryfallQueryParser#genericKey.
    def enterGenericKey(self, ctx:ScryfallQueryParser.GenericKeyContext):
        pass

    # Exit a parse tree produced by ScryfallQueryParser#genericKey.
    def exitGenericKey(self, ctx:ScryfallQueryParser.GenericKeyContext):
        pass


    # Enter a parse tree produced by ScryfallQueryParser#compOp.
    def enterCompOp(self, ctx:ScryfallQueryParser.CompOpContext):
        pass

    # Exit a parse tree produced by ScryfallQueryParser#compOp.
    def exitCompOp(self, ctx:ScryfallQueryParser.CompOpContext):
        pass


    # Enter a parse tree produced by ScryfallQueryParser#genericValue.
    def enterGenericValue(self, ctx:ScryfallQueryParser.GenericValueContext):
        pass

    # Exit a parse tree produced by ScryfallQueryParser#genericValue.
    def exitGenericValue(self, ctx:ScryfallQueryParser.GenericValueContext):
        pass


    # Enter a parse tree produced by ScryfallQueryParser#quotedText.
    def enterQuotedText(self, ctx:ScryfallQueryParser.QuotedTextContext):
        pass

    # Exit a parse tree produced by ScryfallQueryParser#quotedText.
    def exitQuotedText(self, ctx:ScryfallQueryParser.QuotedTextContext):
        pass


    # Enter a parse tree produced by ScryfallQueryParser#regex.
    def enterRegex(self, ctx:ScryfallQueryParser.RegexContext):
        pass

    # Exit a parse tree produced by ScryfallQueryParser#regex.
    def exitRegex(self, ctx:ScryfallQueryParser.RegexContext):
        pass


    # Enter a parse tree produced by ScryfallQueryParser#word.
    def enterWord(self, ctx:ScryfallQueryParser.WordContext):
        pass

    # Exit a parse tree produced by ScryfallQueryParser#word.
    def exitWord(self, ctx:ScryfallQueryParser.WordContext):
        pass


    # Enter a parse tree produced by ScryfallQueryParser#bareValue.
    def enterBareValue(self, ctx:ScryfallQueryParser.BareValueContext):
        pass

    # Exit a parse tree produced by ScryfallQueryParser#bareValue.
    def exitBareValue(self, ctx:ScryfallQueryParser.BareValueContext):
        pass



del ScryfallQueryParser