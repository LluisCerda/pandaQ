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
        4,1,27,199,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,1,0,1,0,
        1,0,3,0,30,8,0,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,101,8,3,1,4,1,4,5,4,105,8,
        4,10,4,12,4,108,9,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,
        1,6,5,6,122,8,6,10,6,12,6,125,9,6,3,6,127,8,6,1,7,1,7,1,7,1,7,1,
        7,3,7,134,8,7,1,8,1,8,1,8,5,8,139,8,8,10,8,12,8,142,9,8,1,9,1,9,
        1,9,1,9,3,9,148,8,9,1,10,1,10,1,10,5,10,153,8,10,10,10,12,10,156,
        9,10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,
        1,11,1,11,3,11,172,8,11,1,12,1,12,1,12,1,12,1,12,1,12,3,12,180,8,
        12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,5,
        12,194,8,12,10,12,12,12,197,9,12,1,12,0,1,24,13,0,2,4,6,8,10,12,
        14,16,18,20,22,24,0,0,208,0,29,1,0,0,0,2,31,1,0,0,0,4,34,1,0,0,0,
        6,100,1,0,0,0,8,102,1,0,0,0,10,109,1,0,0,0,12,126,1,0,0,0,14,133,
        1,0,0,0,16,135,1,0,0,0,18,147,1,0,0,0,20,149,1,0,0,0,22,171,1,0,
        0,0,24,179,1,0,0,0,26,30,3,4,2,0,27,30,3,6,3,0,28,30,3,2,1,0,29,
        26,1,0,0,0,29,27,1,0,0,0,29,28,1,0,0,0,30,1,1,0,0,0,31,32,5,25,0,
        0,32,33,5,26,0,0,33,3,1,0,0,0,34,35,5,26,0,0,35,36,5,1,0,0,36,37,
        3,6,3,0,37,5,1,0,0,0,38,39,5,16,0,0,39,40,3,12,6,0,40,41,5,17,0,
        0,41,42,5,26,0,0,42,43,5,2,0,0,43,101,1,0,0,0,44,45,5,16,0,0,45,
        46,3,12,6,0,46,47,5,17,0,0,47,48,5,26,0,0,48,49,5,18,0,0,49,50,5,
        19,0,0,50,51,3,16,8,0,51,52,5,2,0,0,52,101,1,0,0,0,53,54,5,16,0,
        0,54,55,3,12,6,0,55,56,5,17,0,0,56,57,5,26,0,0,57,58,5,20,0,0,58,
        59,3,20,10,0,59,60,5,2,0,0,60,101,1,0,0,0,61,62,5,16,0,0,62,63,3,
        12,6,0,63,64,5,17,0,0,64,65,5,26,0,0,65,66,5,20,0,0,66,67,3,20,10,
        0,67,68,5,18,0,0,68,69,5,19,0,0,69,70,3,16,8,0,70,71,5,2,0,0,71,
        101,1,0,0,0,72,73,5,16,0,0,73,74,3,12,6,0,74,75,5,17,0,0,75,76,5,
        26,0,0,76,77,3,8,4,0,77,78,5,2,0,0,78,101,1,0,0,0,79,80,5,16,0,0,
        80,81,3,12,6,0,81,82,5,17,0,0,82,83,5,26,0,0,83,84,3,8,4,0,84,85,
        5,20,0,0,85,86,3,20,10,0,86,87,5,2,0,0,87,101,1,0,0,0,88,89,5,16,
        0,0,89,90,3,12,6,0,90,91,5,17,0,0,91,92,5,26,0,0,92,93,3,8,4,0,93,
        94,5,20,0,0,94,95,3,20,10,0,95,96,5,18,0,0,96,97,5,19,0,0,97,98,
        3,16,8,0,98,99,5,2,0,0,99,101,1,0,0,0,100,38,1,0,0,0,100,44,1,0,
        0,0,100,53,1,0,0,0,100,61,1,0,0,0,100,72,1,0,0,0,100,79,1,0,0,0,
        100,88,1,0,0,0,101,7,1,0,0,0,102,106,3,10,5,0,103,105,3,10,5,0,104,
        103,1,0,0,0,105,108,1,0,0,0,106,104,1,0,0,0,106,107,1,0,0,0,107,
        9,1,0,0,0,108,106,1,0,0,0,109,110,5,22,0,0,110,111,5,23,0,0,111,
        112,5,26,0,0,112,113,5,24,0,0,113,114,5,26,0,0,114,115,5,3,0,0,115,
        116,5,26,0,0,116,11,1,0,0,0,117,127,5,4,0,0,118,123,3,14,7,0,119,
        120,5,5,0,0,120,122,3,14,7,0,121,119,1,0,0,0,122,125,1,0,0,0,123,
        121,1,0,0,0,123,124,1,0,0,0,124,127,1,0,0,0,125,123,1,0,0,0,126,
        117,1,0,0,0,126,118,1,0,0,0,127,13,1,0,0,0,128,134,5,26,0,0,129,
        130,3,24,12,0,130,131,5,6,0,0,131,132,5,26,0,0,132,134,1,0,0,0,133,
        128,1,0,0,0,133,129,1,0,0,0,134,15,1,0,0,0,135,140,3,18,9,0,136,
        137,5,5,0,0,137,139,3,18,9,0,138,136,1,0,0,0,139,142,1,0,0,0,140,
        138,1,0,0,0,140,141,1,0,0,0,141,17,1,0,0,0,142,140,1,0,0,0,143,144,
        5,26,0,0,144,148,5,7,0,0,145,146,5,26,0,0,146,148,5,8,0,0,147,143,
        1,0,0,0,147,145,1,0,0,0,148,19,1,0,0,0,149,154,3,22,11,0,150,151,
        5,9,0,0,151,153,3,22,11,0,152,150,1,0,0,0,153,156,1,0,0,0,154,152,
        1,0,0,0,154,155,1,0,0,0,155,21,1,0,0,0,156,154,1,0,0,0,157,158,5,
        26,0,0,158,159,5,3,0,0,159,172,5,26,0,0,160,161,5,26,0,0,161,162,
        5,10,0,0,162,172,5,26,0,0,163,164,5,21,0,0,164,165,5,26,0,0,165,
        166,5,3,0,0,166,172,5,26,0,0,167,168,5,21,0,0,168,169,5,26,0,0,169,
        170,5,10,0,0,170,172,5,26,0,0,171,157,1,0,0,0,171,160,1,0,0,0,171,
        163,1,0,0,0,171,167,1,0,0,0,172,23,1,0,0,0,173,174,6,12,-1,0,174,
        180,5,26,0,0,175,176,5,14,0,0,176,177,3,24,12,0,177,178,5,15,0,0,
        178,180,1,0,0,0,179,173,1,0,0,0,179,175,1,0,0,0,180,195,1,0,0,0,
        181,182,10,5,0,0,182,183,5,4,0,0,183,194,5,26,0,0,184,185,10,4,0,
        0,185,186,5,11,0,0,186,194,5,26,0,0,187,188,10,3,0,0,188,189,5,12,
        0,0,189,194,5,26,0,0,190,191,10,2,0,0,191,192,5,13,0,0,192,194,5,
        26,0,0,193,181,1,0,0,0,193,184,1,0,0,0,193,187,1,0,0,0,193,190,1,
        0,0,0,194,197,1,0,0,0,195,193,1,0,0,0,195,196,1,0,0,0,196,25,1,0,
        0,0,197,195,1,0,0,0,13,29,100,106,123,126,133,140,147,154,171,179,
        193,195
    ]

class lcParser ( Parser ):

    grammarFileName = "lc.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "':='", "';'", "'='", "'*'", "','", "'as'", 
                     "'asc'", "'desc'", "'and'", "'<'", "'+'", "'-'", "'/'", 
                     "'('", "')'", "'select'", "'from'", "'order'", "'by'", 
                     "'where'", "'not'", "'inner'", "'join'", "'on'", "'plot'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "SELECT", "FROM", "ORDER", "BY", "WHERE", "NOT", "INNER", 
                      "JOIN", "ON", "PLOT", "ID", "Spaces" ]

    RULE_root = 0
    RULE_plot = 1
    RULE_assignation = 2
    RULE_select = 3
    RULE_innerJoinList = 4
    RULE_innerJoin = 5
    RULE_columnList = 6
    RULE_column = 7
    RULE_constraintList = 8
    RULE_constraint = 9
    RULE_conditionList = 10
    RULE_condition = 11
    RULE_expression = 12

    ruleNames =  [ "root", "plot", "assignation", "select", "innerJoinList", 
                   "innerJoin", "columnList", "column", "constraintList", 
                   "constraint", "conditionList", "condition", "expression" ]

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
    SELECT=16
    FROM=17
    ORDER=18
    BY=19
    WHERE=20
    NOT=21
    INNER=22
    JOIN=23
    ON=24
    PLOT=25
    ID=26
    Spaces=27

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
            self.state = 29
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [26]:
                self.enterOuterAlt(localctx, 1)
                self.state = 26
                self.assignation()
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 2)
                self.state = 27
                self.select()
                pass
            elif token in [25]:
                self.enterOuterAlt(localctx, 3)
                self.state = 28
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
            self.state = 31
            self.match(lcParser.PLOT)
            self.state = 32
            self.match(lcParser.ID)
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
            self.state = 34
            self.match(lcParser.ID)
            self.state = 35
            self.match(lcParser.T__0)
            self.state = 36
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

        def ORDER(self):
            return self.getToken(lcParser.ORDER, 0)

        def BY(self):
            return self.getToken(lcParser.BY, 0)

        def constraintList(self):
            return self.getTypedRuleContext(lcParser.ConstraintListContext,0)


        def WHERE(self):
            return self.getToken(lcParser.WHERE, 0)

        def conditionList(self):
            return self.getTypedRuleContext(lcParser.ConditionListContext,0)


        def innerJoinList(self):
            return self.getTypedRuleContext(lcParser.InnerJoinListContext,0)


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
        try:
            self.state = 100
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 38
                self.match(lcParser.SELECT)
                self.state = 39
                self.columnList()
                self.state = 40
                self.match(lcParser.FROM)
                self.state = 41
                self.match(lcParser.ID)
                self.state = 42
                self.match(lcParser.T__1)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 44
                self.match(lcParser.SELECT)
                self.state = 45
                self.columnList()
                self.state = 46
                self.match(lcParser.FROM)
                self.state = 47
                self.match(lcParser.ID)
                self.state = 48
                self.match(lcParser.ORDER)
                self.state = 49
                self.match(lcParser.BY)
                self.state = 50
                self.constraintList()
                self.state = 51
                self.match(lcParser.T__1)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 53
                self.match(lcParser.SELECT)
                self.state = 54
                self.columnList()
                self.state = 55
                self.match(lcParser.FROM)
                self.state = 56
                self.match(lcParser.ID)
                self.state = 57
                self.match(lcParser.WHERE)
                self.state = 58
                self.conditionList()
                self.state = 59
                self.match(lcParser.T__1)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 61
                self.match(lcParser.SELECT)
                self.state = 62
                self.columnList()
                self.state = 63
                self.match(lcParser.FROM)
                self.state = 64
                self.match(lcParser.ID)
                self.state = 65
                self.match(lcParser.WHERE)
                self.state = 66
                self.conditionList()
                self.state = 67
                self.match(lcParser.ORDER)
                self.state = 68
                self.match(lcParser.BY)
                self.state = 69
                self.constraintList()
                self.state = 70
                self.match(lcParser.T__1)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 72
                self.match(lcParser.SELECT)
                self.state = 73
                self.columnList()
                self.state = 74
                self.match(lcParser.FROM)
                self.state = 75
                self.match(lcParser.ID)
                self.state = 76
                self.innerJoinList()
                self.state = 77
                self.match(lcParser.T__1)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 79
                self.match(lcParser.SELECT)
                self.state = 80
                self.columnList()
                self.state = 81
                self.match(lcParser.FROM)
                self.state = 82
                self.match(lcParser.ID)
                self.state = 83
                self.innerJoinList()
                self.state = 84
                self.match(lcParser.WHERE)
                self.state = 85
                self.conditionList()
                self.state = 86
                self.match(lcParser.T__1)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 88
                self.match(lcParser.SELECT)
                self.state = 89
                self.columnList()
                self.state = 90
                self.match(lcParser.FROM)
                self.state = 91
                self.match(lcParser.ID)
                self.state = 92
                self.innerJoinList()
                self.state = 93
                self.match(lcParser.WHERE)
                self.state = 94
                self.conditionList()
                self.state = 95
                self.match(lcParser.ORDER)
                self.state = 96
                self.match(lcParser.BY)
                self.state = 97
                self.constraintList()
                self.state = 98
                self.match(lcParser.T__1)
                pass


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
        self.enterRule(localctx, 8, self.RULE_innerJoinList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.innerJoin()
            self.state = 106
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==22:
                self.state = 103
                self.innerJoin()
                self.state = 108
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
        self.enterRule(localctx, 10, self.RULE_innerJoin)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.match(lcParser.INNER)
            self.state = 110
            self.match(lcParser.JOIN)
            self.state = 111
            self.match(lcParser.ID)
            self.state = 112
            self.match(lcParser.ON)
            self.state = 113
            self.match(lcParser.ID)
            self.state = 114
            self.match(lcParser.T__2)
            self.state = 115
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
        self.enterRule(localctx, 12, self.RULE_columnList)
        self._la = 0 # Token type
        try:
            self.state = 126
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 117
                self.match(lcParser.T__3)
                pass
            elif token in [14, 26]:
                self.enterOuterAlt(localctx, 2)
                self.state = 118
                self.column()
                self.state = 123
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==5:
                    self.state = 119
                    self.match(lcParser.T__4)
                    self.state = 120
                    self.column()
                    self.state = 125
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
        self.enterRule(localctx, 14, self.RULE_column)
        try:
            self.state = 133
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 128
                self.match(lcParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 129
                self.expression(0)
                self.state = 130
                self.match(lcParser.T__5)
                self.state = 131
                self.match(lcParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstraintListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def constraint(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lcParser.ConstraintContext)
            else:
                return self.getTypedRuleContext(lcParser.ConstraintContext,i)


        def getRuleIndex(self):
            return lcParser.RULE_constraintList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstraintList" ):
                return visitor.visitConstraintList(self)
            else:
                return visitor.visitChildren(self)




    def constraintList(self):

        localctx = lcParser.ConstraintListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_constraintList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self.constraint()
            self.state = 140
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 136
                self.match(lcParser.T__4)
                self.state = 137
                self.constraint()
                self.state = 142
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstraintContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(lcParser.ID, 0)

        def getRuleIndex(self):
            return lcParser.RULE_constraint

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstraint" ):
                return visitor.visitConstraint(self)
            else:
                return visitor.visitChildren(self)




    def constraint(self):

        localctx = lcParser.ConstraintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_constraint)
        try:
            self.state = 147
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 143
                self.match(lcParser.ID)
                self.state = 144
                self.match(lcParser.T__6)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 145
                self.match(lcParser.ID)
                self.state = 146
                self.match(lcParser.T__7)
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
        self.enterRule(localctx, 20, self.RULE_conditionList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            self.condition()
            self.state = 154
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9:
                self.state = 150
                self.match(lcParser.T__8)
                self.state = 151
                self.condition()
                self.state = 156
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
        self.enterRule(localctx, 22, self.RULE_condition)
        try:
            self.state = 171
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                localctx = lcParser.EqualsContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 157
                self.match(lcParser.ID)
                self.state = 158
                self.match(lcParser.T__2)
                self.state = 159
                self.match(lcParser.ID)
                pass

            elif la_ == 2:
                localctx = lcParser.MinorContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 160
                self.match(lcParser.ID)
                self.state = 161
                self.match(lcParser.T__9)
                self.state = 162
                self.match(lcParser.ID)
                pass

            elif la_ == 3:
                localctx = lcParser.NotEqualsContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 163
                self.match(lcParser.NOT)
                self.state = 164
                self.match(lcParser.ID)
                self.state = 165
                self.match(lcParser.T__2)
                self.state = 166
                self.match(lcParser.ID)
                pass

            elif la_ == 4:
                localctx = lcParser.NotMinorContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 167
                self.match(lcParser.NOT)
                self.state = 168
                self.match(lcParser.ID)
                self.state = 169
                self.match(lcParser.T__9)
                self.state = 170
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

        def ID(self):
            return self.getToken(lcParser.ID, 0)

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

        def ID(self):
            return self.getToken(lcParser.ID, 0)

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

        def ID(self):
            return self.getToken(lcParser.ID, 0)

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

        def ID(self):
            return self.getToken(lcParser.ID, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSum" ):
                return visitor.visitSum(self)
            else:
                return visitor.visitChildren(self)


    class PharContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a lcParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(lcParser.ExpressionContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPhar" ):
                return visitor.visitPhar(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = lcParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 24
        self.enterRecursionRule(localctx, 24, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [26]:
                localctx = lcParser.IdentifierContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 174
                self.match(lcParser.ID)
                pass
            elif token in [14]:
                localctx = lcParser.PharContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 175
                self.match(lcParser.T__13)
                self.state = 176
                self.expression(0)
                self.state = 177
                self.match(lcParser.T__14)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 195
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 193
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
                    if la_ == 1:
                        localctx = lcParser.MultContext(self, lcParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 181
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 182
                        self.match(lcParser.T__3)
                        self.state = 183
                        self.match(lcParser.ID)
                        pass

                    elif la_ == 2:
                        localctx = lcParser.SumContext(self, lcParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 184
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 185
                        self.match(lcParser.T__10)
                        self.state = 186
                        self.match(lcParser.ID)
                        pass

                    elif la_ == 3:
                        localctx = lcParser.SubstContext(self, lcParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 187
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 188
                        self.match(lcParser.T__11)
                        self.state = 189
                        self.match(lcParser.ID)
                        pass

                    elif la_ == 4:
                        localctx = lcParser.DivContext(self, lcParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 190
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 191
                        self.match(lcParser.T__12)
                        self.state = 192
                        self.match(lcParser.ID)
                        pass

             
                self.state = 197
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[12] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         




