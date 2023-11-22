# Generated from lc.g4 by ANTLR 4.12.0
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,6,60,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,1,0,1,0,1,1,1,1,1,2,1,2,1,3,1,3,3,3,28,8,3,
        1,3,1,3,1,3,5,3,33,8,3,10,3,12,3,36,9,3,1,4,1,4,1,4,1,4,1,4,1,4,
        1,4,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,7,1,7,1,8,4,8,55,8,8,11,8,12,8,
        56,1,8,1,8,0,0,9,1,0,3,0,5,0,7,1,9,2,11,3,13,4,15,5,17,6,1,0,3,1,
        0,48,57,2,0,65,90,97,122,3,0,9,10,13,13,32,32,61,0,7,1,0,0,0,0,9,
        1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,1,19,
        1,0,0,0,3,21,1,0,0,0,5,23,1,0,0,0,7,27,1,0,0,0,9,37,1,0,0,0,11,44,
        1,0,0,0,13,49,1,0,0,0,15,51,1,0,0,0,17,54,1,0,0,0,19,20,7,0,0,0,
        20,2,1,0,0,0,21,22,7,1,0,0,22,4,1,0,0,0,23,24,5,95,0,0,24,6,1,0,
        0,0,25,28,3,3,1,0,26,28,3,5,2,0,27,25,1,0,0,0,27,26,1,0,0,0,28,34,
        1,0,0,0,29,33,3,3,1,0,30,33,3,1,0,0,31,33,3,5,2,0,32,29,1,0,0,0,
        32,30,1,0,0,0,32,31,1,0,0,0,33,36,1,0,0,0,34,32,1,0,0,0,34,35,1,
        0,0,0,35,8,1,0,0,0,36,34,1,0,0,0,37,38,5,83,0,0,38,39,5,69,0,0,39,
        40,5,76,0,0,40,41,5,69,0,0,41,42,5,67,0,0,42,43,5,84,0,0,43,10,1,
        0,0,0,44,45,5,70,0,0,45,46,5,82,0,0,46,47,5,79,0,0,47,48,5,77,0,
        0,48,12,1,0,0,0,49,50,5,42,0,0,50,14,1,0,0,0,51,52,5,59,0,0,52,16,
        1,0,0,0,53,55,7,2,0,0,54,53,1,0,0,0,55,56,1,0,0,0,56,54,1,0,0,0,
        56,57,1,0,0,0,57,58,1,0,0,0,58,59,6,8,0,0,59,18,1,0,0,0,5,0,27,32,
        34,56,1,6,0,0
    ]

class lcLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    ID = 1
    SELECT = 2
    FROM = 3
    STAR = 4
    SEMICOLON = 5
    WS = 6

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'SELECT'", "'FROM'", "'*'", "';'" ]

    symbolicNames = [ "<INVALID>",
            "ID", "SELECT", "FROM", "STAR", "SEMICOLON", "WS" ]

    ruleNames = [ "DIGIT", "LETTER", "UNDERSCORE", "ID", "SELECT", "FROM", 
                  "STAR", "SEMICOLON", "WS" ]

    grammarFileName = "lc.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.12.0")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


