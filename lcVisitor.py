# Generated from lc.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .lcParser import lcParser
else:
    from lcParser import lcParser

# This class defines a complete generic visitor for a parse tree produced by lcParser.

class lcVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by lcParser#sql_query.
    def visitSql_query(self, ctx:lcParser.Sql_queryContext):
        return self.visitChildren(ctx)



del lcParser