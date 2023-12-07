# Generated from lc.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .lcParser import lcParser
else:
    from lcParser import lcParser

# This class defines a complete generic visitor for a parse tree produced by lcParser.

class lcVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by lcParser#root.
    def visitRoot(self, ctx:lcParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lcParser#plot.
    def visitPlot(self, ctx:lcParser.PlotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lcParser#assignation.
    def visitAssignation(self, ctx:lcParser.AssignationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lcParser#select.
    def visitSelect(self, ctx:lcParser.SelectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lcParser#innerJoinList.
    def visitInnerJoinList(self, ctx:lcParser.InnerJoinListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lcParser#innerJoin.
    def visitInnerJoin(self, ctx:lcParser.InnerJoinContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lcParser#columnList.
    def visitColumnList(self, ctx:lcParser.ColumnListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lcParser#column.
    def visitColumn(self, ctx:lcParser.ColumnContext):
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


    # Visit a parse tree produced by lcParser#orderingList.
    def visitOrderingList(self, ctx:lcParser.OrderingListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lcParser#order.
    def visitOrder(self, ctx:lcParser.OrderContext):
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



del lcParser