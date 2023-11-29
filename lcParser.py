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
        4,1,22,134,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,
        0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,
        0,1,0,1,0,1,0,1,0,3,0,51,8,0,1,1,1,1,1,1,1,1,5,1,57,8,1,10,1,12,
        1,60,9,1,3,1,62,8,1,1,2,1,2,1,2,1,2,1,2,3,2,69,8,2,1,3,1,3,1,3,5,
        3,74,8,3,10,3,12,3,77,9,3,1,4,1,4,1,4,1,4,3,4,83,8,4,1,5,1,5,1,5,
        5,5,88,8,5,10,5,12,5,91,9,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,
        1,6,1,6,1,6,1,6,1,6,3,6,107,8,6,1,7,1,7,1,7,1,7,1,7,1,7,3,7,115,
        8,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,5,7,129,8,7,
        10,7,12,7,132,9,7,1,7,0,1,14,8,0,2,4,6,8,10,12,14,0,0,142,0,50,1,
        0,0,0,2,61,1,0,0,0,4,68,1,0,0,0,6,70,1,0,0,0,8,82,1,0,0,0,10,84,
        1,0,0,0,12,106,1,0,0,0,14,114,1,0,0,0,16,17,5,15,0,0,17,18,3,2,1,
        0,18,19,5,16,0,0,19,20,5,21,0,0,20,21,5,1,0,0,21,51,1,0,0,0,22,23,
        5,15,0,0,23,24,3,2,1,0,24,25,5,16,0,0,25,26,5,21,0,0,26,27,5,17,
        0,0,27,28,5,18,0,0,28,29,3,6,3,0,29,30,5,1,0,0,30,51,1,0,0,0,31,
        32,5,15,0,0,32,33,3,2,1,0,33,34,5,16,0,0,34,35,5,21,0,0,35,36,5,
        19,0,0,36,37,3,10,5,0,37,38,5,1,0,0,38,51,1,0,0,0,39,40,5,15,0,0,
        40,41,3,2,1,0,41,42,5,16,0,0,42,43,5,21,0,0,43,44,5,19,0,0,44,45,
        3,10,5,0,45,46,5,17,0,0,46,47,5,18,0,0,47,48,3,6,3,0,48,49,5,1,0,
        0,49,51,1,0,0,0,50,16,1,0,0,0,50,22,1,0,0,0,50,31,1,0,0,0,50,39,
        1,0,0,0,51,1,1,0,0,0,52,62,5,2,0,0,53,58,3,4,2,0,54,55,5,3,0,0,55,
        57,3,4,2,0,56,54,1,0,0,0,57,60,1,0,0,0,58,56,1,0,0,0,58,59,1,0,0,
        0,59,62,1,0,0,0,60,58,1,0,0,0,61,52,1,0,0,0,61,53,1,0,0,0,62,3,1,
        0,0,0,63,69,5,21,0,0,64,65,3,14,7,0,65,66,5,4,0,0,66,67,5,21,0,0,
        67,69,1,0,0,0,68,63,1,0,0,0,68,64,1,0,0,0,69,5,1,0,0,0,70,75,3,8,
        4,0,71,72,5,3,0,0,72,74,3,8,4,0,73,71,1,0,0,0,74,77,1,0,0,0,75,73,
        1,0,0,0,75,76,1,0,0,0,76,7,1,0,0,0,77,75,1,0,0,0,78,79,5,21,0,0,
        79,83,5,5,0,0,80,81,5,21,0,0,81,83,5,6,0,0,82,78,1,0,0,0,82,80,1,
        0,0,0,83,9,1,0,0,0,84,89,3,12,6,0,85,86,5,7,0,0,86,88,3,12,6,0,87,
        85,1,0,0,0,88,91,1,0,0,0,89,87,1,0,0,0,89,90,1,0,0,0,90,11,1,0,0,
        0,91,89,1,0,0,0,92,93,5,21,0,0,93,94,5,8,0,0,94,107,5,21,0,0,95,
        96,5,21,0,0,96,97,5,9,0,0,97,107,5,21,0,0,98,99,5,20,0,0,99,100,
        5,21,0,0,100,101,5,8,0,0,101,107,5,21,0,0,102,103,5,20,0,0,103,104,
        5,21,0,0,104,105,5,9,0,0,105,107,5,21,0,0,106,92,1,0,0,0,106,95,
        1,0,0,0,106,98,1,0,0,0,106,102,1,0,0,0,107,13,1,0,0,0,108,109,6,
        7,-1,0,109,115,5,21,0,0,110,111,5,13,0,0,111,112,3,14,7,0,112,113,
        5,14,0,0,113,115,1,0,0,0,114,108,1,0,0,0,114,110,1,0,0,0,115,130,
        1,0,0,0,116,117,10,5,0,0,117,118,5,2,0,0,118,129,5,21,0,0,119,120,
        10,4,0,0,120,121,5,10,0,0,121,129,5,21,0,0,122,123,10,3,0,0,123,
        124,5,11,0,0,124,129,5,21,0,0,125,126,10,2,0,0,126,127,5,12,0,0,
        127,129,5,21,0,0,128,116,1,0,0,0,128,119,1,0,0,0,128,122,1,0,0,0,
        128,125,1,0,0,0,129,132,1,0,0,0,130,128,1,0,0,0,130,131,1,0,0,0,
        131,15,1,0,0,0,132,130,1,0,0,0,11,50,58,61,68,75,82,89,106,114,128,
        130
    ]

class lcParser ( Parser ):

    grammarFileName = "lc.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'*'", "','", "'as'", "'asc'", 
                     "'desc'", "'and'", "'='", "'<'", "'+'", "'-'", "'/'", 
                     "'('", "')'", "'select'", "'from'", "'order'", "'by'", 
                     "'where'", "'not'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "SELECT", "FROM", 
                      "ORDER", "BY", "WHERE", "NOT", "ID", "Spaces" ]

    RULE_select = 0
    RULE_columnList = 1
    RULE_column = 2
    RULE_constraintList = 3
    RULE_constraint = 4
    RULE_conditionList = 5
    RULE_condition = 6
    RULE_expression = 7

    ruleNames =  [ "select", "columnList", "column", "constraintList", "constraint", 
                   "conditionList", "condition", "expression" ]

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
    SELECT=15
    FROM=16
    ORDER=17
    BY=18
    WHERE=19
    NOT=20
    ID=21
    Spaces=22

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
            self.state = 50
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 16
                self.match(lcParser.SELECT)
                self.state = 17
                self.columnList()
                self.state = 18
                self.match(lcParser.FROM)
                self.state = 19
                self.match(lcParser.ID)
                self.state = 20
                self.match(lcParser.T__0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 22
                self.match(lcParser.SELECT)
                self.state = 23
                self.columnList()
                self.state = 24
                self.match(lcParser.FROM)
                self.state = 25
                self.match(lcParser.ID)
                self.state = 26
                self.match(lcParser.ORDER)
                self.state = 27
                self.match(lcParser.BY)
                self.state = 28
                self.constraintList()
                self.state = 29
                self.match(lcParser.T__0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 31
                self.match(lcParser.SELECT)
                self.state = 32
                self.columnList()
                self.state = 33
                self.match(lcParser.FROM)
                self.state = 34
                self.match(lcParser.ID)
                self.state = 35
                self.match(lcParser.WHERE)
                self.state = 36
                self.conditionList()
                self.state = 37
                self.match(lcParser.T__0)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 39
                self.match(lcParser.SELECT)
                self.state = 40
                self.columnList()
                self.state = 41
                self.match(lcParser.FROM)
                self.state = 42
                self.match(lcParser.ID)
                self.state = 43
                self.match(lcParser.WHERE)
                self.state = 44
                self.conditionList()
                self.state = 45
                self.match(lcParser.ORDER)
                self.state = 46
                self.match(lcParser.BY)
                self.state = 47
                self.constraintList()
                self.state = 48
                self.match(lcParser.T__0)
                pass


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
        self.enterRule(localctx, 2, self.RULE_columnList)
        self._la = 0 # Token type
        try:
            self.state = 61
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 52
                self.match(lcParser.T__1)
                pass
            elif token in [13, 21]:
                self.enterOuterAlt(localctx, 2)
                self.state = 53
                self.column()
                self.state = 58
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==3:
                    self.state = 54
                    self.match(lcParser.T__2)
                    self.state = 55
                    self.column()
                    self.state = 60
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
        self.enterRule(localctx, 4, self.RULE_column)
        try:
            self.state = 68
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 63
                self.match(lcParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 64
                self.expression(0)
                self.state = 65
                self.match(lcParser.T__3)
                self.state = 66
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
        self.enterRule(localctx, 6, self.RULE_constraintList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.constraint()
            self.state = 75
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 71
                self.match(lcParser.T__2)
                self.state = 72
                self.constraint()
                self.state = 77
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
        self.enterRule(localctx, 8, self.RULE_constraint)
        try:
            self.state = 82
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 78
                self.match(lcParser.ID)
                self.state = 79
                self.match(lcParser.T__4)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 80
                self.match(lcParser.ID)
                self.state = 81
                self.match(lcParser.T__5)
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
        self.enterRule(localctx, 10, self.RULE_conditionList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.condition()
            self.state = 89
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7:
                self.state = 85
                self.match(lcParser.T__6)
                self.state = 86
                self.condition()
                self.state = 91
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
        self.enterRule(localctx, 12, self.RULE_condition)
        try:
            self.state = 106
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                localctx = lcParser.EqualsContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 92
                self.match(lcParser.ID)
                self.state = 93
                self.match(lcParser.T__7)
                self.state = 94
                self.match(lcParser.ID)
                pass

            elif la_ == 2:
                localctx = lcParser.MinorContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 95
                self.match(lcParser.ID)
                self.state = 96
                self.match(lcParser.T__8)
                self.state = 97
                self.match(lcParser.ID)
                pass

            elif la_ == 3:
                localctx = lcParser.NotEqualsContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 98
                self.match(lcParser.NOT)
                self.state = 99
                self.match(lcParser.ID)
                self.state = 100
                self.match(lcParser.T__7)
                self.state = 101
                self.match(lcParser.ID)
                pass

            elif la_ == 4:
                localctx = lcParser.NotMinorContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 102
                self.match(lcParser.NOT)
                self.state = 103
                self.match(lcParser.ID)
                self.state = 104
                self.match(lcParser.T__8)
                self.state = 105
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
        _startState = 14
        self.enterRecursionRule(localctx, 14, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [21]:
                localctx = lcParser.IdentifierContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 109
                self.match(lcParser.ID)
                pass
            elif token in [13]:
                localctx = lcParser.PharContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 110
                self.match(lcParser.T__12)
                self.state = 111
                self.expression(0)
                self.state = 112
                self.match(lcParser.T__13)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 130
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 128
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
                    if la_ == 1:
                        localctx = lcParser.MultContext(self, lcParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 116
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 117
                        self.match(lcParser.T__1)
                        self.state = 118
                        self.match(lcParser.ID)
                        pass

                    elif la_ == 2:
                        localctx = lcParser.SumContext(self, lcParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 119
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 120
                        self.match(lcParser.T__9)
                        self.state = 121
                        self.match(lcParser.ID)
                        pass

                    elif la_ == 3:
                        localctx = lcParser.SubstContext(self, lcParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 122
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 123
                        self.match(lcParser.T__10)
                        self.state = 124
                        self.match(lcParser.ID)
                        pass

                    elif la_ == 4:
                        localctx = lcParser.DivContext(self, lcParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 125
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 126
                        self.match(lcParser.T__11)
                        self.state = 127
                        self.match(lcParser.ID)
                        pass

             
                self.state = 132
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

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
        self._predicates[7] = self.expression_sempred
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
         




