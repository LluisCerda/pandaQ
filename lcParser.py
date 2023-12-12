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
        4,1,30,161,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        1,0,1,0,1,0,3,0,32,8,0,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,3,1,3,1,
        3,1,3,1,3,3,3,47,8,3,1,3,1,3,3,3,51,8,3,1,3,3,3,54,8,3,1,3,1,3,1,
        3,3,3,59,8,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,5,5,72,
        8,5,10,5,12,5,75,9,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,
        1,7,5,7,89,8,7,10,7,12,7,92,9,7,3,7,94,8,7,1,8,1,8,1,8,1,8,1,8,3,
        8,101,8,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,
        9,1,9,5,9,118,8,9,10,9,12,9,121,9,9,1,10,1,10,1,10,5,10,126,8,10,
        10,10,12,10,129,9,10,1,11,1,11,1,11,1,11,3,11,135,8,11,1,12,1,12,
        1,12,5,12,140,8,12,10,12,12,12,143,9,12,1,13,1,13,1,13,1,13,1,13,
        1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,3,13,159,8,13,1,13,
        0,1,18,14,0,2,4,6,8,10,12,14,16,18,20,22,24,26,0,0,166,0,31,1,0,
        0,0,2,33,1,0,0,0,4,37,1,0,0,0,6,41,1,0,0,0,8,62,1,0,0,0,10,69,1,
        0,0,0,12,76,1,0,0,0,14,93,1,0,0,0,16,100,1,0,0,0,18,102,1,0,0,0,
        20,122,1,0,0,0,22,134,1,0,0,0,24,136,1,0,0,0,26,158,1,0,0,0,28,32,
        3,4,2,0,29,32,3,6,3,0,30,32,3,2,1,0,31,28,1,0,0,0,31,29,1,0,0,0,
        31,30,1,0,0,0,32,1,1,0,0,0,33,34,5,26,0,0,34,35,5,28,0,0,35,36,5,
        1,0,0,36,3,1,0,0,0,37,38,5,28,0,0,38,39,5,2,0,0,39,40,3,6,3,0,40,
        5,1,0,0,0,41,42,5,17,0,0,42,43,3,14,7,0,43,44,5,18,0,0,44,46,5,28,
        0,0,45,47,3,10,5,0,46,45,1,0,0,0,46,47,1,0,0,0,47,50,1,0,0,0,48,
        49,5,21,0,0,49,51,3,24,12,0,50,48,1,0,0,0,50,51,1,0,0,0,51,53,1,
        0,0,0,52,54,3,8,4,0,53,52,1,0,0,0,53,54,1,0,0,0,54,58,1,0,0,0,55,
        56,5,19,0,0,56,57,5,20,0,0,57,59,3,20,10,0,58,55,1,0,0,0,58,59,1,
        0,0,0,59,60,1,0,0,0,60,61,5,1,0,0,61,7,1,0,0,0,62,63,5,21,0,0,63,
        64,5,28,0,0,64,65,5,27,0,0,65,66,5,3,0,0,66,67,3,6,3,0,67,68,5,4,
        0,0,68,9,1,0,0,0,69,73,3,12,6,0,70,72,3,12,6,0,71,70,1,0,0,0,72,
        75,1,0,0,0,73,71,1,0,0,0,73,74,1,0,0,0,74,11,1,0,0,0,75,73,1,0,0,
        0,76,77,5,23,0,0,77,78,5,24,0,0,78,79,5,28,0,0,79,80,5,25,0,0,80,
        81,5,28,0,0,81,82,5,5,0,0,82,83,5,28,0,0,83,13,1,0,0,0,84,94,5,6,
        0,0,85,90,3,16,8,0,86,87,5,7,0,0,87,89,3,16,8,0,88,86,1,0,0,0,89,
        92,1,0,0,0,90,88,1,0,0,0,90,91,1,0,0,0,91,94,1,0,0,0,92,90,1,0,0,
        0,93,84,1,0,0,0,93,85,1,0,0,0,94,15,1,0,0,0,95,101,5,28,0,0,96,97,
        3,18,9,0,97,98,5,8,0,0,98,99,5,28,0,0,99,101,1,0,0,0,100,95,1,0,
        0,0,100,96,1,0,0,0,101,17,1,0,0,0,102,103,6,9,-1,0,103,104,5,28,
        0,0,104,119,1,0,0,0,105,106,10,4,0,0,106,107,5,6,0,0,107,118,5,29,
        0,0,108,109,10,3,0,0,109,110,5,9,0,0,110,118,5,29,0,0,111,112,10,
        2,0,0,112,113,5,10,0,0,113,118,5,29,0,0,114,115,10,1,0,0,115,116,
        5,11,0,0,116,118,5,29,0,0,117,105,1,0,0,0,117,108,1,0,0,0,117,111,
        1,0,0,0,117,114,1,0,0,0,118,121,1,0,0,0,119,117,1,0,0,0,119,120,
        1,0,0,0,120,19,1,0,0,0,121,119,1,0,0,0,122,127,3,22,11,0,123,124,
        5,7,0,0,124,126,3,22,11,0,125,123,1,0,0,0,126,129,1,0,0,0,127,125,
        1,0,0,0,127,128,1,0,0,0,128,21,1,0,0,0,129,127,1,0,0,0,130,131,5,
        28,0,0,131,135,5,12,0,0,132,133,5,28,0,0,133,135,5,13,0,0,134,130,
        1,0,0,0,134,132,1,0,0,0,135,23,1,0,0,0,136,141,3,26,13,0,137,138,
        5,14,0,0,138,140,3,26,13,0,139,137,1,0,0,0,140,143,1,0,0,0,141,139,
        1,0,0,0,141,142,1,0,0,0,142,25,1,0,0,0,143,141,1,0,0,0,144,145,5,
        28,0,0,145,146,5,5,0,0,146,159,5,28,0,0,147,148,5,28,0,0,148,149,
        5,15,0,0,149,159,5,28,0,0,150,151,5,22,0,0,151,152,5,28,0,0,152,
        153,5,5,0,0,153,159,5,28,0,0,154,155,5,22,0,0,155,156,5,28,0,0,156,
        157,5,15,0,0,157,159,5,28,0,0,158,144,1,0,0,0,158,147,1,0,0,0,158,
        150,1,0,0,0,158,154,1,0,0,0,159,27,1,0,0,0,15,31,46,50,53,58,73,
        90,93,100,117,119,127,134,141,158
    ]

class lcParser ( Parser ):

    grammarFileName = "lc.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "':='", "'('", "')'", "'='", "'*'", 
                     "','", "'as'", "'+'", "'-'", "'/'", "'asc'", "'desc'", 
                     "'and'", "'<'", "<INVALID>", "'select'", "'from'", 
                     "'order'", "'by'", "'where'", "'not'", "'inner'", "'join'", 
                     "'on'", "'plot'", "'in'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "Spaces", "SELECT", "FROM", "ORDER", "BY", "WHERE", 
                      "NOT", "INNER", "JOIN", "ON", "PLOT", "IN", "ID", 
                      "NUM", "DIGIT" ]

    RULE_root = 0
    RULE_plot = 1
    RULE_assignation = 2
    RULE_select = 3
    RULE_subQuery = 4
    RULE_innerJoinList = 5
    RULE_innerJoin = 6
    RULE_columnList = 7
    RULE_column = 8
    RULE_expression = 9
    RULE_orderingList = 10
    RULE_order = 11
    RULE_conditionList = 12
    RULE_condition = 13

    ruleNames =  [ "root", "plot", "assignation", "select", "subQuery", 
                   "innerJoinList", "innerJoin", "columnList", "column", 
                   "expression", "orderingList", "order", "conditionList", 
                   "condition" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    Spaces=16
    SELECT=17
    FROM=18
    ORDER=19
    BY=20
    WHERE=21
    NOT=22
    INNER=23
    JOIN=24
    ON=25
    PLOT=26
    IN=27
    ID=28
    NUM=29
    DIGIT=30

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class RootContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignation(self):
            return self.getTypedRuleContext(lcParser.AssignationContext,0)


        def select(self):
            return self.getTypedRuleContext(lcParser.SelectContext,0)


        def plot(self):
            return self.getTypedRuleContext(lcParser.PlotContext,0)


        def getRuleIndex(self):
            return lcParser.RULE_root

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRoot" ):
                return visitor.visitRoot(self)
            else:
                return visitor.visitChildren(self)




    def root(self):

        localctx = lcParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        try:
            self.state = 31
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [28]:
                self.enterOuterAlt(localctx, 1)
                self.state = 28
                self.assignation()
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 2)
                self.state = 29
                self.select()
                pass
            elif token in [26]:
                self.enterOuterAlt(localctx, 3)
                self.state = 30
                self.plot()
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


    class PlotContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PLOT(self):
            return self.getToken(lcParser.PLOT, 0)

        def ID(self):
            return self.getToken(lcParser.ID, 0)

        def getRuleIndex(self):
            return lcParser.RULE_plot

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPlot" ):
                return visitor.visitPlot(self)
            else:
                return visitor.visitChildren(self)




    def plot(self):

        localctx = lcParser.PlotContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_plot)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self.match(lcParser.PLOT)
            self.state = 34
            self.match(lcParser.ID)
            self.state = 35
            self.match(lcParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(lcParser.ID, 0)

        def select(self):
            return self.getTypedRuleContext(lcParser.SelectContext,0)


        def getRuleIndex(self):
            return lcParser.RULE_assignation

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignation" ):
                return visitor.visitAssignation(self)
            else:
                return visitor.visitChildren(self)




    def assignation(self):

        localctx = lcParser.AssignationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assignation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.match(lcParser.ID)
            self.state = 38
            self.match(lcParser.T__1)
            self.state = 39
            self.select()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


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

        def innerJoinList(self):
            return self.getTypedRuleContext(lcParser.InnerJoinListContext,0)


        def WHERE(self):
            return self.getToken(lcParser.WHERE, 0)

        def conditionList(self):
            return self.getTypedRuleContext(lcParser.ConditionListContext,0)


        def subQuery(self):
            return self.getTypedRuleContext(lcParser.SubQueryContext,0)


        def ORDER(self):
            return self.getToken(lcParser.ORDER, 0)

        def BY(self):
            return self.getToken(lcParser.BY, 0)

        def orderingList(self):
            return self.getTypedRuleContext(lcParser.OrderingListContext,0)


        def getRuleIndex(self):
            return lcParser.RULE_select

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSelect" ):
                return visitor.visitSelect(self)
            else:
                return visitor.visitChildren(self)




    def select(self):

        localctx = lcParser.SelectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_select)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self.match(lcParser.SELECT)
            self.state = 42
            self.columnList()
            self.state = 43
            self.match(lcParser.FROM)
            self.state = 44
            self.match(lcParser.ID)
            self.state = 46
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==23:
                self.state = 45
                self.innerJoinList()


            self.state = 50
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 48
                self.match(lcParser.WHERE)
                self.state = 49
                self.conditionList()


            self.state = 53
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==21:
                self.state = 52
                self.subQuery()


            self.state = 58
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==19:
                self.state = 55
                self.match(lcParser.ORDER)
                self.state = 56
                self.match(lcParser.BY)
                self.state = 57
                self.orderingList()


            self.state = 60
            self.match(lcParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubQueryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHERE(self):
            return self.getToken(lcParser.WHERE, 0)

        def ID(self):
            return self.getToken(lcParser.ID, 0)

        def IN(self):
            return self.getToken(lcParser.IN, 0)

        def select(self):
            return self.getTypedRuleContext(lcParser.SelectContext,0)


        def getRuleIndex(self):
            return lcParser.RULE_subQuery

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubQuery" ):
                return visitor.visitSubQuery(self)
            else:
                return visitor.visitChildren(self)




    def subQuery(self):

        localctx = lcParser.SubQueryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_subQuery)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self.match(lcParser.WHERE)
            self.state = 63
            self.match(lcParser.ID)
            self.state = 64
            self.match(lcParser.IN)
            self.state = 65
            self.match(lcParser.T__2)
            self.state = 66
            self.select()
            self.state = 67
            self.match(lcParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InnerJoinListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def innerJoin(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lcParser.InnerJoinContext)
            else:
                return self.getTypedRuleContext(lcParser.InnerJoinContext,i)


        def getRuleIndex(self):
            return lcParser.RULE_innerJoinList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInnerJoinList" ):
                return visitor.visitInnerJoinList(self)
            else:
                return visitor.visitChildren(self)




    def innerJoinList(self):

        localctx = lcParser.InnerJoinListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_innerJoinList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.innerJoin()
            self.state = 73
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==23:
                self.state = 70
                self.innerJoin()
                self.state = 75
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InnerJoinContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INNER(self):
            return self.getToken(lcParser.INNER, 0)

        def JOIN(self):
            return self.getToken(lcParser.JOIN, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(lcParser.ID)
            else:
                return self.getToken(lcParser.ID, i)

        def ON(self):
            return self.getToken(lcParser.ON, 0)

        def getRuleIndex(self):
            return lcParser.RULE_innerJoin

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInnerJoin" ):
                return visitor.visitInnerJoin(self)
            else:
                return visitor.visitChildren(self)




    def innerJoin(self):

        localctx = lcParser.InnerJoinContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_innerJoin)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.match(lcParser.INNER)
            self.state = 77
            self.match(lcParser.JOIN)
            self.state = 78
            self.match(lcParser.ID)
            self.state = 79
            self.match(lcParser.ON)
            self.state = 80
            self.match(lcParser.ID)
            self.state = 81
            self.match(lcParser.T__4)
            self.state = 82
            self.match(lcParser.ID)
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

        def column(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lcParser.ColumnContext)
            else:
                return self.getTypedRuleContext(lcParser.ColumnContext,i)


        def getRuleIndex(self):
            return lcParser.RULE_columnList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitColumnList" ):
                return visitor.visitColumnList(self)
            else:
                return visitor.visitChildren(self)




    def columnList(self):

        localctx = lcParser.ColumnListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_columnList)
        self._la = 0 # Token type
        try:
            self.state = 93
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 84
                self.match(lcParser.T__5)
                pass
            elif token in [28]:
                self.enterOuterAlt(localctx, 2)
                self.state = 85
                self.column()
                self.state = 90
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==7:
                    self.state = 86
                    self.match(lcParser.T__6)
                    self.state = 87
                    self.column()
                    self.state = 92
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


    class ColumnContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(lcParser.ID, 0)

        def expression(self):
            return self.getTypedRuleContext(lcParser.ExpressionContext,0)


        def getRuleIndex(self):
            return lcParser.RULE_column

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitColumn" ):
                return visitor.visitColumn(self)
            else:
                return visitor.visitChildren(self)




    def column(self):

        localctx = lcParser.ColumnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_column)
        try:
            self.state = 100
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 95
                self.match(lcParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 96
                self.expression(0)
                self.state = 97
                self.match(lcParser.T__7)
                self.state = 98
                self.match(lcParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return lcParser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class DivContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a lcParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(lcParser.ExpressionContext,0)

        def NUM(self):
            return self.getToken(lcParser.NUM, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDiv" ):
                return visitor.visitDiv(self)
            else:
                return visitor.visitChildren(self)


    class IdentifierContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a lcParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(lcParser.ID, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifier" ):
                return visitor.visitIdentifier(self)
            else:
                return visitor.visitChildren(self)


    class MultContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a lcParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(lcParser.ExpressionContext,0)

        def NUM(self):
            return self.getToken(lcParser.NUM, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMult" ):
                return visitor.visitMult(self)
            else:
                return visitor.visitChildren(self)


    class SubstContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a lcParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(lcParser.ExpressionContext,0)

        def NUM(self):
            return self.getToken(lcParser.NUM, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubst" ):
                return visitor.visitSubst(self)
            else:
                return visitor.visitChildren(self)


    class SumContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a lcParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(lcParser.ExpressionContext,0)

        def NUM(self):
            return self.getToken(lcParser.NUM, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSum" ):
                return visitor.visitSum(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = lcParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 18
        self.enterRecursionRule(localctx, 18, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = lcParser.IdentifierContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 103
            self.match(lcParser.ID)
            self._ctx.stop = self._input.LT(-1)
            self.state = 119
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 117
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
                    if la_ == 1:
                        localctx = lcParser.MultContext(self, lcParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 105
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 106
                        self.match(lcParser.T__5)
                        self.state = 107
                        self.match(lcParser.NUM)
                        pass

                    elif la_ == 2:
                        localctx = lcParser.SumContext(self, lcParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 108
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 109
                        self.match(lcParser.T__8)
                        self.state = 110
                        self.match(lcParser.NUM)
                        pass

                    elif la_ == 3:
                        localctx = lcParser.SubstContext(self, lcParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 111
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 112
                        self.match(lcParser.T__9)
                        self.state = 113
                        self.match(lcParser.NUM)
                        pass

                    elif la_ == 4:
                        localctx = lcParser.DivContext(self, lcParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 114
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 115
                        self.match(lcParser.T__10)
                        self.state = 116
                        self.match(lcParser.NUM)
                        pass

             
                self.state = 121
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class OrderingListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def order(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lcParser.OrderContext)
            else:
                return self.getTypedRuleContext(lcParser.OrderContext,i)


        def getRuleIndex(self):
            return lcParser.RULE_orderingList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOrderingList" ):
                return visitor.visitOrderingList(self)
            else:
                return visitor.visitChildren(self)




    def orderingList(self):

        localctx = lcParser.OrderingListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_orderingList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.order()
            self.state = 127
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7:
                self.state = 123
                self.match(lcParser.T__6)
                self.state = 124
                self.order()
                self.state = 129
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OrderContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(lcParser.ID, 0)

        def getRuleIndex(self):
            return lcParser.RULE_order

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOrder" ):
                return visitor.visitOrder(self)
            else:
                return visitor.visitChildren(self)




    def order(self):

        localctx = lcParser.OrderContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_order)
        try:
            self.state = 134
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 130
                self.match(lcParser.ID)
                self.state = 131
                self.match(lcParser.T__11)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 132
                self.match(lcParser.ID)
                self.state = 133
                self.match(lcParser.T__12)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def condition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lcParser.ConditionContext)
            else:
                return self.getTypedRuleContext(lcParser.ConditionContext,i)


        def getRuleIndex(self):
            return lcParser.RULE_conditionList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConditionList" ):
                return visitor.visitConditionList(self)
            else:
                return visitor.visitChildren(self)




    def conditionList(self):

        localctx = lcParser.ConditionListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_conditionList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self.condition()
            self.state = 141
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==14:
                self.state = 137
                self.match(lcParser.T__13)
                self.state = 138
                self.condition()
                self.state = 143
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return lcParser.RULE_condition

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class EqualsContext(ConditionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a lcParser.ConditionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(lcParser.ID)
            else:
                return self.getToken(lcParser.ID, i)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEquals" ):
                return visitor.visitEquals(self)
            else:
                return visitor.visitChildren(self)


    class MinorContext(ConditionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a lcParser.ConditionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(lcParser.ID)
            else:
                return self.getToken(lcParser.ID, i)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMinor" ):
                return visitor.visitMinor(self)
            else:
                return visitor.visitChildren(self)


    class NotMinorContext(ConditionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a lcParser.ConditionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(lcParser.NOT, 0)
        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(lcParser.ID)
            else:
                return self.getToken(lcParser.ID, i)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNotMinor" ):
                return visitor.visitNotMinor(self)
            else:
                return visitor.visitChildren(self)


    class NotEqualsContext(ConditionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a lcParser.ConditionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(lcParser.NOT, 0)
        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(lcParser.ID)
            else:
                return self.getToken(lcParser.ID, i)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNotEquals" ):
                return visitor.visitNotEquals(self)
            else:
                return visitor.visitChildren(self)



    def condition(self):

        localctx = lcParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_condition)
        try:
            self.state = 158
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                localctx = lcParser.EqualsContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 144
                self.match(lcParser.ID)
                self.state = 145
                self.match(lcParser.T__4)
                self.state = 146
                self.match(lcParser.ID)
                pass

            elif la_ == 2:
                localctx = lcParser.MinorContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 147
                self.match(lcParser.ID)
                self.state = 148
                self.match(lcParser.T__14)
                self.state = 149
                self.match(lcParser.ID)
                pass

            elif la_ == 3:
                localctx = lcParser.NotEqualsContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 150
                self.match(lcParser.NOT)
                self.state = 151
                self.match(lcParser.ID)
                self.state = 152
                self.match(lcParser.T__4)
                self.state = 153
                self.match(lcParser.ID)
                pass

            elif la_ == 4:
                localctx = lcParser.NotMinorContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 154
                self.match(lcParser.NOT)
                self.state = 155
                self.match(lcParser.ID)
                self.state = 156
                self.match(lcParser.T__14)
                self.state = 157
                self.match(lcParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[9] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 1)
         




