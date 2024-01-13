# Generated from pandaQ.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .pandaQParser import pandaQParser
else:
    from pandaQParser import pandaQParser

# This class defines a complete generic visitor for a parse tree produced by pandaQParser.

class pandaQVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by pandaQParser#root.
    def visitRoot(self, ctx:pandaQParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pandaQParser#plot.
    def visitPlot(self, ctx:pandaQParser.PlotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pandaQParser#assignation.
    def visitAssignation(self, ctx:pandaQParser.AssignationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pandaQParser#select.
    def visitSelect(self, ctx:pandaQParser.SelectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pandaQParser#columnList.
    def visitColumnList(self, ctx:pandaQParser.ColumnListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pandaQParser#column.
    def visitColumn(self, ctx:pandaQParser.ColumnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pandaQParser#Div.
    def visitDiv(self, ctx:pandaQParser.DivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pandaQParser#Identifier.
    def visitIdentifier(self, ctx:pandaQParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pandaQParser#Mult.
    def visitMult(self, ctx:pandaQParser.MultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pandaQParser#Subst.
    def visitSubst(self, ctx:pandaQParser.SubstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pandaQParser#Sum.
    def visitSum(self, ctx:pandaQParser.SumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pandaQParser#innerJoinList.
    def visitInnerJoinList(self, ctx:pandaQParser.InnerJoinListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pandaQParser#innerJoin.
    def visitInnerJoin(self, ctx:pandaQParser.InnerJoinContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pandaQParser#conditionList.
    def visitConditionList(self, ctx:pandaQParser.ConditionListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pandaQParser#Equals.
    def visitEquals(self, ctx:pandaQParser.EqualsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pandaQParser#Minor.
    def visitMinor(self, ctx:pandaQParser.MinorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pandaQParser#NotEquals.
    def visitNotEquals(self, ctx:pandaQParser.NotEqualsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pandaQParser#NotMinor.
    def visitNotMinor(self, ctx:pandaQParser.NotMinorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pandaQParser#subQuery.
    def visitSubQuery(self, ctx:pandaQParser.SubQueryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pandaQParser#orderingList.
    def visitOrderingList(self, ctx:pandaQParser.OrderingListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pandaQParser#order.
    def visitOrder(self, ctx:pandaQParser.OrderContext):
        return self.visitChildren(ctx)



del pandaQParser