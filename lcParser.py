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
        4,1,13,58,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,1,0,1,0,1,0,1,0,1,
        0,1,1,1,1,1,1,1,1,5,1,19,8,1,10,1,12,1,22,9,1,3,1,24,8,1,1,2,1,2,
        1,2,1,2,1,2,3,2,31,8,2,1,3,1,3,1,3,1,3,1,3,1,3,3,3,39,8,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,5,3,53,8,3,10,3,12,3,56,
        9,3,1,3,0,1,6,4,0,2,4,6,0,0,61,0,8,1,0,0,0,2,23,1,0,0,0,4,30,1,0,
        0,0,6,38,1,0,0,0,8,9,5,10,0,0,9,10,3,2,1,0,10,11,5,11,0,0,11,12,
        5,12,0,0,12,13,5,1,0,0,13,1,1,0,0,0,14,24,5,2,0,0,15,20,3,4,2,0,
        16,17,5,3,0,0,17,19,3,4,2,0,18,16,1,0,0,0,19,22,1,0,0,0,20,18,1,
        0,0,0,20,21,1,0,0,0,21,24,1,0,0,0,22,20,1,0,0,0,23,14,1,0,0,0,23,
        15,1,0,0,0,24,3,1,0,0,0,25,31,5,12,0,0,26,27,3,6,3,0,27,28,5,4,0,
        0,28,29,5,12,0,0,29,31,1,0,0,0,30,25,1,0,0,0,30,26,1,0,0,0,31,5,
        1,0,0,0,32,33,6,3,-1,0,33,39,5,12,0,0,34,35,5,8,0,0,35,36,3,6,3,
        0,36,37,5,9,0,0,37,39,1,0,0,0,38,32,1,0,0,0,38,34,1,0,0,0,39,54,
        1,0,0,0,40,41,10,5,0,0,41,42,5,2,0,0,42,53,5,12,0,0,43,44,10,4,0,
        0,44,45,5,5,0,0,45,53,5,12,0,0,46,47,10,3,0,0,47,48,5,6,0,0,48,53,
        5,12,0,0,49,50,10,2,0,0,50,51,5,7,0,0,51,53,5,12,0,0,52,40,1,0,0,
        0,52,43,1,0,0,0,52,46,1,0,0,0,52,49,1,0,0,0,53,56,1,0,0,0,54,52,
        1,0,0,0,54,55,1,0,0,0,55,7,1,0,0,0,56,54,1,0,0,0,6,20,23,30,38,52,
        54
    ]

class lcParser ( Parser ):

    grammarFileName = "lc.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'*'", "','", "'as'", "'+'", "'-'", 
                     "'/'", "'('", "')'", "'select'", "'from'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "SELECT", "FROM", "ID", 
                      "Spaces" ]

    RULE_select = 0
    RULE_columnList = 1
    RULE_column = 2
    RULE_expression = 3

    ruleNames =  [ "select", "columnList", "column", "expression" ]

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
    SELECT=10
    FROM=11
    ID=12
    Spaces=13

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
            self.state = 8
            self.match(lcParser.SELECT)
            self.state = 9
            self.columnList()
            self.state = 10
            self.match(lcParser.FROM)
            self.state = 11
            self.match(lcParser.ID)
            self.state = 12
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
            self.state = 23
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 14
                self.match(lcParser.T__1)
                pass
            elif token in [8, 12]:
                self.enterOuterAlt(localctx, 2)
                self.state = 15
                self.column()
                self.state = 20
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==3:
                    self.state = 16
                    self.match(lcParser.T__2)
                    self.state = 17
                    self.column()
                    self.state = 22
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
            self.state = 30
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 25
                self.match(lcParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 26
                self.expression(0)
                self.state = 27
                self.match(lcParser.T__3)
                self.state = 28
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
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12]:
                localctx = lcParser.IdentifierContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 33
                self.match(lcParser.ID)
                pass
            elif token in [8]:
                localctx = lcParser.PharContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 34
                self.match(lcParser.T__7)
                self.state = 35
                self.expression(0)
                self.state = 36
                self.match(lcParser.T__8)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 54
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 52
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = lcParser.MultContext(self, lcParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 40
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 41
                        self.match(lcParser.T__1)
                        self.state = 42
                        self.match(lcParser.ID)
                        pass

                    elif la_ == 2:
                        localctx = lcParser.SumContext(self, lcParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 43
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 44
                        self.match(lcParser.T__4)
                        self.state = 45
                        self.match(lcParser.ID)
                        pass

                    elif la_ == 3:
                        localctx = lcParser.SubstContext(self, lcParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 46
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 47
                        self.match(lcParser.T__5)
                        self.state = 48
                        self.match(lcParser.ID)
                        pass

                    elif la_ == 4:
                        localctx = lcParser.DivContext(self, lcParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 49
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 50
                        self.match(lcParser.T__6)
                        self.state = 51
                        self.match(lcParser.ID)
                        pass

             
                self.state = 56
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

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
        self._predicates[3] = self.expression_sempred
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
         




