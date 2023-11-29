# Generated from lc.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .lcParser import lcParser
else:
    from lcParser import lcParser

# This class defines a complete generic visitor for a parse tree produced by lcParser.

class lcVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by lcParser#select.
    def visitSelect(self, ctx:lcParser.SelectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lcParser#columnList.
    def visitColumnList(self, ctx:lcParser.ColumnListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lcParser#column.
    def visitColumn(self, ctx:lcParser.ColumnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lcParser#constraintList.
    def visitConstraintList(self, ctx:lcParser.ConstraintListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lcParser#constraint.
    def visitConstraint(self, ctx:lcParser.ConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lcParser#conditionList.
    def visitConditionList(self, ctx:lcParser.ConditionListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lcParser#Equals.
    def visitEquals(self, ctx:lcParser.EqualsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lcParser#Minor.
    def visitMinor(self, ctx:lcParser.MinorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lcParser#NotEquals.
    def visitNotEquals(self, ctx:lcParser.NotEqualsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lcParser#NotMinor.
    def visitNotMinor(self, ctx:lcParser.NotMinorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lcParser#Div.
    def visitDiv(self, ctx:lcParser.DivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lcParser#Identifier.
    def visitIdentifier(self, ctx:lcParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lcParser#Mult.
    def visitMult(self, ctx:lcParser.MultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lcParser#Subst.
    def visitSubst(self, ctx:lcParser.SubstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lcParser#Sum.
    def visitSum(self, ctx:lcParser.SumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lcParser#Phar.
    def visitPhar(self, ctx:lcParser.PharContext):
        return self.visitChildren(ctx)



del lcParser