# Generated from lc.g4 by ANTLR 4.13.1
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
        4,1,7,22,2,0,7,0,2,1,7,1,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,
        5,1,15,8,1,10,1,12,1,18,9,1,3,1,20,8,1,1,1,0,0,2,0,2,0,0,21,0,4,
        1,0,0,0,2,19,1,0,0,0,4,5,5,4,0,0,5,6,3,2,1,0,6,7,5,5,0,0,7,8,5,6,
        0,0,8,9,5,1,0,0,9,1,1,0,0,0,10,20,5,2,0,0,11,16,5,6,0,0,12,13,5,
        3,0,0,13,15,5,6,0,0,14,12,1,0,0,0,15,18,1,0,0,0,16,14,1,0,0,0,16,
        17,1,0,0,0,17,20,1,0,0,0,18,16,1,0,0,0,19,10,1,0,0,0,19,11,1,0,0,
        0,20,3,1,0,0,0,2,16,19
    ]

class lcParser ( Parser ):

    grammarFileName = "lc.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'*'", "','", "'select'", "'from'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "SELECT", "FROM", "ID", "SPACES" ]

    RULE_select = 0
    RULE_columnList = 1

    ruleNames =  [ "select", "columnList" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    SELECT=4
    FROM=5
    ID=6
    SPACES=7

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class SelectContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SELECT(self):
            return self.getToken(lcParser.SELECT, 0)

        def columnList(self):
            return self.getTypedRuleContext(lcParser.ColumnListContext,0)


        def FROM(self):
            return self.getToken(lcParser.FROM, 0)

        def ID(self):
            return self.getToken(lcParser.ID, 0)

        def getRuleIndex(self):
            return lcParser.RULE_select

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSelect" ):
                return visitor.visitSelect(self)
            else:
                return visitor.visitChildren(self)




    def select(self):

        localctx = lcParser.SelectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_select)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 4
            self.match(lcParser.SELECT)
            self.state = 5
            self.columnList()
            self.state = 6
            self.match(lcParser.FROM)
            self.state = 7
            self.match(lcParser.ID)
            self.state = 8
            self.match(lcParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ColumnListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(lcParser.ID)
            else:
                return self.getToken(lcParser.ID, i)

        def getRuleIndex(self):
            return lcParser.RULE_columnList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitColumnList" ):
                return visitor.visitColumnList(self)
            else:
                return visitor.visitChildren(self)




    def columnList(self):

        localctx = lcParser.ColumnListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_columnList)
        self._la = 0 # Token type
        try:
            self.state = 19
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 10
                self.match(lcParser.T__1)
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 11
                self.match(lcParser.ID)
                self.state = 16
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==3:
                    self.state = 12
                    self.match(lcParser.T__2)
                    self.state = 13
                    self.match(lcParser.ID)
                    self.state = 18
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

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





