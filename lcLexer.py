# Generated from lc.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,6,38,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,
        0,1,0,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,
        4,4,4,31,8,4,11,4,12,4,32,1,5,1,5,1,5,1,5,0,0,6,1,1,3,2,5,3,7,4,
        9,5,11,6,1,0,2,2,0,65,90,97,122,3,0,9,10,13,13,32,32,38,0,1,1,0,
        0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,
        1,13,1,0,0,0,3,15,1,0,0,0,5,17,1,0,0,0,7,24,1,0,0,0,9,30,1,0,0,0,
        11,34,1,0,0,0,13,14,5,42,0,0,14,2,1,0,0,0,15,16,5,59,0,0,16,4,1,
        0,0,0,17,18,5,115,0,0,18,19,5,101,0,0,19,20,5,108,0,0,20,21,5,101,
        0,0,21,22,5,99,0,0,22,23,5,116,0,0,23,6,1,0,0,0,24,25,5,102,0,0,
        25,26,5,114,0,0,26,27,5,111,0,0,27,28,5,109,0,0,28,8,1,0,0,0,29,
        31,7,0,0,0,30,29,1,0,0,0,31,32,1,0,0,0,32,30,1,0,0,0,32,33,1,0,0,
        0,33,10,1,0,0,0,34,35,7,1,0,0,35,36,1,0,0,0,36,37,6,5,0,0,37,12,
        1,0,0,0,2,0,32,1,6,0,0
    ]

class lcLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    SELECT = 3
    FROM = 4
    ID = 5
    SPACES = 6

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'*'", "';'", "'select'", "'from'" ]

    symbolicNames = [ "<INVALID>",
            "SELECT", "FROM", "ID", "SPACES" ]

    ruleNames = [ "T__0", "T__1", "SELECT", "FROM", "ID", "SPACES" ]

    grammarFileName = "lc.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


