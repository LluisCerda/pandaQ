# Generated from lc.g4 by ANTLR 4.12.0
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
        4,1,6,9,2,0,7,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,0,0,1,0,0,0,7,0,2,1,
        0,0,0,2,3,5,2,0,0,3,4,5,4,0,0,4,5,5,3,0,0,5,6,5,1,0,0,6,7,5,5,0,
        0,7,1,1,0,0,0,0
    ]

class lcParser ( Parser ):

    grammarFileName = "lc.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'SELECT'", "'FROM'", "'*'", 
                     "';'" ]

    symbolicNames = [ "<INVALID>", "ID", "SELECT", "FROM", "STAR", "SEMICOLON", 
                      "WS" ]

    RULE_sql_query = 0

    ruleNames =  [ "sql_query" ]

    EOF = Token.EOF
    ID=1
    SELECT=2
    FROM=3
    STAR=4
    SEMICOLON=5
    WS=6

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.12.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class Sql_queryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SELECT(self):
            return self.getToken(lcParser.SELECT, 0)

        def STAR(self):
            return self.getToken(lcParser.STAR, 0)

        def FROM(self):
            return self.getToken(lcParser.FROM, 0)

        def ID(self):
            return self.getToken(lcParser.ID, 0)

        def SEMICOLON(self):
            return self.getToken(lcParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return lcParser.RULE_sql_query

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSql_query" ):
                return visitor.visitSql_query(self)
            else:
                return visitor.visitChildren(self)




    def sql_query(self):

        localctx = lcParser.Sql_queryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_sql_query)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2
            self.match(lcParser.SELECT)
            self.state = 3
            self.match(lcParser.STAR)
            self.state = 4
            self.match(lcParser.FROM)
            self.state = 5
            self.match(lcParser.ID)
            self.state = 6
            self.match(lcParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





