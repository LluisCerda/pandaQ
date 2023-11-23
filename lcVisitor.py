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



del lcParser