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
        4,1,17,83,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,1,
        0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,3,0,28,8,0,
        1,1,1,1,1,1,1,1,5,1,34,8,1,10,1,12,1,37,9,1,3,1,39,8,1,1,2,1,2,1,
        2,1,2,1,2,3,2,46,8,2,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,3,4,56,8,4,
        1,5,1,5,1,5,1,5,1,5,1,5,3,5,64,8,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,
        5,1,5,1,5,1,5,1,5,5,5,78,8,5,10,5,12,5,81,9,5,1,5,0,1,10,6,0,2,4,
        6,8,10,0,0,86,0,27,1,0,0,0,2,38,1,0,0,0,4,45,1,0,0,0,6,47,1,0,0,
        0,8,55,1,0,0,0,10,63,1,0,0,0,12,13,5,12,0,0,13,14,3,2,1,0,14,15,
        5,13,0,0,15,16,5,16,0,0,16,17,5,1,0,0,17,28,1,0,0,0,18,19,5,12,0,
        0,19,20,3,2,1,0,20,21,5,13,0,0,21,22,5,16,0,0,22,23,5,14,0,0,23,
        24,5,15,0,0,24,25,3,6,3,0,25,26,5,1,0,0,26,28,1,0,0,0,27,12,1,0,
        0,0,27,18,1,0,0,0,28,1,1,0,0,0,29,39,5,2,0,0,30,35,3,4,2,0,31,32,
        5,3,0,0,32,34,3,4,2,0,33,31,1,0,0,0,34,37,1,0,0,0,35,33,1,0,0,0,
        35,36,1,0,0,0,36,39,1,0,0,0,37,35,1,0,0,0,38,29,1,0,0,0,38,30,1,
        0,0,0,39,3,1,0,0,0,40,46,5,16,0,0,41,42,3,10,5,0,42,43,5,4,0,0,43,
        44,5,16,0,0,44,46,1,0,0,0,45,40,1,0,0,0,45,41,1,0,0,0,46,5,1,0,0,
        0,47,48,3,8,4,0,48,49,5,3,0,0,49,50,3,8,4,0,50,7,1,0,0,0,51,52,5,
        16,0,0,52,56,5,5,0,0,53,54,5,16,0,0,54,56,5,6,0,0,55,51,1,0,0,0,
        55,53,1,0,0,0,56,9,1,0,0,0,57,58,6,5,-1,0,58,64,5,16,0,0,59,60,5,
        10,0,0,60,61,3,10,5,0,61,62,5,11,0,0,62,64,1,0,0,0,63,57,1,0,0,0,
        63,59,1,0,0,0,64,79,1,0,0,0,65,66,10,5,0,0,66,67,5,2,0,0,67,78,5,
        16,0,0,68,69,10,4,0,0,69,70,5,7,0,0,70,78,5,16,0,0,71,72,10,3,0,
        0,72,73,5,8,0,0,73,78,5,16,0,0,74,75,10,2,0,0,75,76,5,9,0,0,76,78,
        5,16,0,0,77,65,1,0,0,0,77,68,1,0,0,0,77,71,1,0,0,0,77,74,1,0,0,0,
        78,81,1,0,0,0,79,77,1,0,0,0,79,80,1,0,0,0,80,11,1,0,0,0,81,79,1,
        0,0,0,8,27,35,38,45,55,63,77,79
    ]

class lcParser ( Parser ):

    grammarFileName = "lc.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'*'", "','", "'as'", "'asc'", 
                     "'desc'", "'+'", "'-'", "'/'", "'('", "')'", "'select'", 
                     "'from'", "'order'", "'by'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "SELECT", "FROM", "ORDER", "BY", "ID", "Spaces" ]

    RULE_select = 0
    RULE_columnList = 1
    RULE_column = 2
    RULE_constraintList = 3
    RULE_constraint = 4
    RULE_expression = 5

    ruleNames =  [ "select", "columnList", "column", "constraintList", "constraint", 
                   "expression" ]

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
    SELECT=12
    FROM=13
    ORDER=14
    BY=15
    ID=16
    Spaces=17

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
            self.state = 27
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 12
                self.match(lcParser.SELECT)
                self.state = 13
                self.columnList()
                self.state = 14
                self.match(lcParser.FROM)
                self.state = 15
                self.match(lcParser.ID)
                self.state = 16
                self.match(lcParser.T__0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 18
                self.match(lcParser.SELECT)
                self.state = 19
                self.columnList()
                self.state = 20
                self.match(lcParser.FROM)
                self.state = 21
                self.match(lcParser.ID)
                self.state = 22
                self.match(lcParser.ORDER)
                self.state = 23
                self.match(lcParser.BY)
                self.state = 24
                self.constraintList()
                self.state = 25
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
            self.state = 38
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 29
                self.match(lcParser.T__1)
                pass
            elif token in [10, 16]:
                self.enterOuterAlt(localctx, 2)
                self.state = 30
                self.column()
                self.state = 35
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==3:
                    self.state = 31
                    self.match(lcParser.T__2)
                    self.state = 32
                    self.column()
                    self.state = 37
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
            self.state = 45
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 40
                self.match(lcParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 41
                self.expression(0)
                self.state = 42
                self.match(lcParser.T__3)
                self.state = 43
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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.constraint()

            self.state = 48
            self.match(lcParser.T__2)
            self.state = 49
            self.constraint()
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
            self.state = 55
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 51
                self.match(lcParser.ID)
                self.state = 52
                self.match(lcParser.T__4)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 53
                self.match(lcParser.ID)
                self.state = 54
                self.match(lcParser.T__5)
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
        _startState = 10
        self.enterRecursionRule(localctx, 10, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                localctx = lcParser.IdentifierContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 58
                self.match(lcParser.ID)
                pass
            elif token in [10]:
                localctx = lcParser.PharContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 59
                self.match(lcParser.T__9)
                self.state = 60
                self.expression(0)
                self.state = 61
                self.match(lcParser.T__10)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 79
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 77
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                    if la_ == 1:
                        localctx = lcParser.MultContext(self, lcParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 65
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 66
                        self.match(lcParser.T__1)
                        self.state = 67
                        self.match(lcParser.ID)
                        pass

                    elif la_ == 2:
                        localctx = lcParser.SumContext(self, lcParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 68
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 69
                        self.match(lcParser.T__6)
                        self.state = 70
                        self.match(lcParser.ID)
                        pass

                    elif la_ == 3:
                        localctx = lcParser.SubstContext(self, lcParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 71
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 72
                        self.match(lcParser.T__7)
                        self.state = 73
                        self.match(lcParser.ID)
                        pass

                    elif la_ == 4:
                        localctx = lcParser.DivContext(self, lcParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 74
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 75
                        self.match(lcParser.T__8)
                        self.state = 76
                        self.match(lcParser.ID)
                        pass

             
                self.state = 81
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

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
        self._predicates[5] = self.expression_sempred
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
         




