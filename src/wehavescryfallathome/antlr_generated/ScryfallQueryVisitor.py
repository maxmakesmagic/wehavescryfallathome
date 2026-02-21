# Generated from grammar/ScryfallQuery.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ScryfallQueryParser import ScryfallQueryParser
else:
    from ScryfallQueryParser import ScryfallQueryParser

# This class defines a complete generic visitor for a parse tree produced by ScryfallQueryParser.

class ScryfallQueryVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ScryfallQueryParser#start.
    def visitStart(self, ctx:ScryfallQueryParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScryfallQueryParser#topExpr.
    def visitTopExpr(self, ctx:ScryfallQueryParser.TopExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScryfallQueryParser#topAndExpr.
    def visitTopAndExpr(self, ctx:ScryfallQueryParser.TopAndExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScryfallQueryParser#topFactor.
    def visitTopFactor(self, ctx:ScryfallQueryParser.TopFactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScryfallQueryParser#topGroup.
    def visitTopGroup(self, ctx:ScryfallQueryParser.TopGroupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScryfallQueryParser#topTerm.
    def visitTopTerm(self, ctx:ScryfallQueryParser.TopTermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScryfallQueryParser#parenExpr.
    def visitParenExpr(self, ctx:ScryfallQueryParser.ParenExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScryfallQueryParser#parenAndExpr.
    def visitParenAndExpr(self, ctx:ScryfallQueryParser.ParenAndExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScryfallQueryParser#parenFactor.
    def visitParenFactor(self, ctx:ScryfallQueryParser.ParenFactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScryfallQueryParser#parenGroup.
    def visitParenGroup(self, ctx:ScryfallQueryParser.ParenGroupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScryfallQueryParser#parenTerm.
    def visitParenTerm(self, ctx:ScryfallQueryParser.ParenTermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScryfallQueryParser#topAtom.
    def visitTopAtom(self, ctx:ScryfallQueryParser.TopAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScryfallQueryParser#displayAtom.
    def visitDisplayAtom(self, ctx:ScryfallQueryParser.DisplayAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScryfallQueryParser#parenAtom.
    def visitParenAtom(self, ctx:ScryfallQueryParser.ParenAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScryfallQueryParser#nonDisplayAtom.
    def visitNonDisplayAtom(self, ctx:ScryfallQueryParser.NonDisplayAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScryfallQueryParser#exactName.
    def visitExactName(self, ctx:ScryfallQueryParser.ExactNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScryfallQueryParser#uniqueTerm.
    def visitUniqueTerm(self, ctx:ScryfallQueryParser.UniqueTermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScryfallQueryParser#uniqueKey.
    def visitUniqueKey(self, ctx:ScryfallQueryParser.UniqueKeyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScryfallQueryParser#uniqueValue.
    def visitUniqueValue(self, ctx:ScryfallQueryParser.UniqueValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScryfallQueryParser#displayTerm.
    def visitDisplayTerm(self, ctx:ScryfallQueryParser.DisplayTermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScryfallQueryParser#displayValue.
    def visitDisplayValue(self, ctx:ScryfallQueryParser.DisplayValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScryfallQueryParser#orderTerm.
    def visitOrderTerm(self, ctx:ScryfallQueryParser.OrderTermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScryfallQueryParser#orderValue.
    def visitOrderValue(self, ctx:ScryfallQueryParser.OrderValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScryfallQueryParser#directionTerm.
    def visitDirectionTerm(self, ctx:ScryfallQueryParser.DirectionTermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScryfallQueryParser#directionValue.
    def visitDirectionValue(self, ctx:ScryfallQueryParser.DirectionValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScryfallQueryParser#preferTerm.
    def visitPreferTerm(self, ctx:ScryfallQueryParser.PreferTermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScryfallQueryParser#preferValue.
    def visitPreferValue(self, ctx:ScryfallQueryParser.PreferValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScryfallQueryParser#includeTerm.
    def visitIncludeTerm(self, ctx:ScryfallQueryParser.IncludeTermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScryfallQueryParser#isTerm.
    def visitIsTerm(self, ctx:ScryfallQueryParser.IsTermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScryfallQueryParser#notTerm.
    def visitNotTerm(self, ctx:ScryfallQueryParser.NotTermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScryfallQueryParser#isValue.
    def visitIsValue(self, ctx:ScryfallQueryParser.IsValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScryfallQueryParser#formatTerm.
    def visitFormatTerm(self, ctx:ScryfallQueryParser.FormatTermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScryfallQueryParser#bannedTerm.
    def visitBannedTerm(self, ctx:ScryfallQueryParser.BannedTermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScryfallQueryParser#restrictedTerm.
    def visitRestrictedTerm(self, ctx:ScryfallQueryParser.RestrictedTermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScryfallQueryParser#formatValue.
    def visitFormatValue(self, ctx:ScryfallQueryParser.FormatValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScryfallQueryParser#gameTerm.
    def visitGameTerm(self, ctx:ScryfallQueryParser.GameTermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScryfallQueryParser#gameValueToken.
    def visitGameValueToken(self, ctx:ScryfallQueryParser.GameValueTokenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScryfallQueryParser#inTerm.
    def visitInTerm(self, ctx:ScryfallQueryParser.InTermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScryfallQueryParser#identityTerm.
    def visitIdentityTerm(self, ctx:ScryfallQueryParser.IdentityTermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScryfallQueryParser#identityValue.
    def visitIdentityValue(self, ctx:ScryfallQueryParser.IdentityValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScryfallQueryParser#colorTerm.
    def visitColorTerm(self, ctx:ScryfallQueryParser.ColorTermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScryfallQueryParser#colorValue.
    def visitColorValue(self, ctx:ScryfallQueryParser.ColorValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScryfallQueryParser#borderTerm.
    def visitBorderTerm(self, ctx:ScryfallQueryParser.BorderTermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScryfallQueryParser#borderValue.
    def visitBorderValue(self, ctx:ScryfallQueryParser.BorderValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScryfallQueryParser#frameTerm.
    def visitFrameTerm(self, ctx:ScryfallQueryParser.FrameTermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScryfallQueryParser#frameValue.
    def visitFrameValue(self, ctx:ScryfallQueryParser.FrameValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScryfallQueryParser#languageTerm.
    def visitLanguageTerm(self, ctx:ScryfallQueryParser.LanguageTermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScryfallQueryParser#languageValue.
    def visitLanguageValue(self, ctx:ScryfallQueryParser.LanguageValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScryfallQueryParser#stampTerm.
    def visitStampTerm(self, ctx:ScryfallQueryParser.StampTermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScryfallQueryParser#stampValue.
    def visitStampValue(self, ctx:ScryfallQueryParser.StampValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScryfallQueryParser#rarityTerm.
    def visitRarityTerm(self, ctx:ScryfallQueryParser.RarityTermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScryfallQueryParser#rarityValue.
    def visitRarityValue(self, ctx:ScryfallQueryParser.RarityValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScryfallQueryParser#powerTerm.
    def visitPowerTerm(self, ctx:ScryfallQueryParser.PowerTermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScryfallQueryParser#powerValue.
    def visitPowerValue(self, ctx:ScryfallQueryParser.PowerValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScryfallQueryParser#toughnessTerm.
    def visitToughnessTerm(self, ctx:ScryfallQueryParser.ToughnessTermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScryfallQueryParser#toughnessValue.
    def visitToughnessValue(self, ctx:ScryfallQueryParser.ToughnessValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScryfallQueryParser#mvTerm.
    def visitMvTerm(self, ctx:ScryfallQueryParser.MvTermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScryfallQueryParser#manaTerm.
    def visitManaTerm(self, ctx:ScryfallQueryParser.ManaTermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScryfallQueryParser#manaValue.
    def visitManaValue(self, ctx:ScryfallQueryParser.ManaValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScryfallQueryParser#manaValuePart.
    def visitManaValuePart(self, ctx:ScryfallQueryParser.ManaValuePartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScryfallQueryParser#cnTerm.
    def visitCnTerm(self, ctx:ScryfallQueryParser.CnTermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScryfallQueryParser#cnValue.
    def visitCnValue(self, ctx:ScryfallQueryParser.CnValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScryfallQueryParser#genericTerm.
    def visitGenericTerm(self, ctx:ScryfallQueryParser.GenericTermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScryfallQueryParser#genericKey.
    def visitGenericKey(self, ctx:ScryfallQueryParser.GenericKeyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScryfallQueryParser#compOp.
    def visitCompOp(self, ctx:ScryfallQueryParser.CompOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScryfallQueryParser#genericValue.
    def visitGenericValue(self, ctx:ScryfallQueryParser.GenericValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScryfallQueryParser#quotedText.
    def visitQuotedText(self, ctx:ScryfallQueryParser.QuotedTextContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScryfallQueryParser#regex.
    def visitRegex(self, ctx:ScryfallQueryParser.RegexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScryfallQueryParser#word.
    def visitWord(self, ctx:ScryfallQueryParser.WordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScryfallQueryParser#bareValue.
    def visitBareValue(self, ctx:ScryfallQueryParser.BareValueContext):
        return self.visitChildren(ctx)



del ScryfallQueryParser