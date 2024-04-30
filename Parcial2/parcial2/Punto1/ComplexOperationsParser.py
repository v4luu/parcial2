# Generated from ComplexOperations.g4 by ANTLR 4.13.1
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
        4,1,10,36,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,4,
        0,14,8,0,11,0,12,0,15,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,
        3,1,3,1,3,1,4,1,4,1,5,1,5,1,5,1,5,0,0,6,0,2,4,6,8,10,0,2,1,0,4,7,
        1,0,4,5,30,0,13,1,0,0,0,2,17,1,0,0,0,4,20,1,0,0,0,6,24,1,0,0,0,8,
        30,1,0,0,0,10,32,1,0,0,0,12,14,3,2,1,0,13,12,1,0,0,0,14,15,1,0,0,
        0,15,13,1,0,0,0,15,16,1,0,0,0,16,1,1,0,0,0,17,18,3,4,2,0,18,19,5,
        9,0,0,19,3,1,0,0,0,20,21,3,6,3,0,21,22,7,0,0,0,22,23,3,6,3,0,23,
        5,1,0,0,0,24,25,5,1,0,0,25,26,3,8,4,0,26,27,7,1,0,0,27,28,3,10,5,
        0,28,29,5,2,0,0,29,7,1,0,0,0,30,31,5,8,0,0,31,9,1,0,0,0,32,33,5,
        8,0,0,33,34,5,3,0,0,34,11,1,0,0,0,1,15
    ]

class ComplexOperationsParser ( Parser ):

    grammarFileName = "ComplexOperations.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'i'", "'+'", "'-'", "'*'", 
                     "'/'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "ADD", "SUB", "MUL", "DIV", "NUMBER", "NEWLINE", "WS" ]

    RULE_prog = 0
    RULE_start = 1
    RULE_operation = 2
    RULE_complexNumber = 3
    RULE_realPart = 4
    RULE_imaginaryPart = 5

    ruleNames =  [ "prog", "start", "operation", "complexNumber", "realPart", 
                   "imaginaryPart" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    ADD=4
    SUB=5
    MUL=6
    DIV=7
    NUMBER=8
    NEWLINE=9
    WS=10

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def start(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ComplexOperationsParser.StartContext)
            else:
                return self.getTypedRuleContext(ComplexOperationsParser.StartContext,i)


        def getRuleIndex(self):
            return ComplexOperationsParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = ComplexOperationsParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 12
                self.start()
                self.state = 15 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==1):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ComplexOperationsParser.RULE_start

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class PrintContext(StartContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ComplexOperationsParser.StartContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def operation(self):
            return self.getTypedRuleContext(ComplexOperationsParser.OperationContext,0)

        def NEWLINE(self):
            return self.getToken(ComplexOperationsParser.NEWLINE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrint" ):
                listener.enterPrint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrint" ):
                listener.exitPrint(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrint" ):
                return visitor.visitPrint(self)
            else:
                return visitor.visitChildren(self)



    def start(self):

        localctx = ComplexOperationsParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_start)
        try:
            localctx = ComplexOperationsParser.PrintContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 17
            self.operation()
            self.state = 18
            self.match(ComplexOperationsParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ComplexOperationsParser.RULE_operation

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class OperarContext(OperationContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ComplexOperationsParser.OperationContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def complexNumber(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ComplexOperationsParser.ComplexNumberContext)
            else:
                return self.getTypedRuleContext(ComplexOperationsParser.ComplexNumberContext,i)

        def ADD(self):
            return self.getToken(ComplexOperationsParser.ADD, 0)
        def SUB(self):
            return self.getToken(ComplexOperationsParser.SUB, 0)
        def MUL(self):
            return self.getToken(ComplexOperationsParser.MUL, 0)
        def DIV(self):
            return self.getToken(ComplexOperationsParser.DIV, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperar" ):
                listener.enterOperar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperar" ):
                listener.exitOperar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperar" ):
                return visitor.visitOperar(self)
            else:
                return visitor.visitChildren(self)



    def operation(self):

        localctx = ComplexOperationsParser.OperationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_operation)
        self._la = 0 # Token type
        try:
            localctx = ComplexOperationsParser.OperarContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            self.complexNumber()
            self.state = 21
            localctx.op = self._input.LT(1)
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 240) != 0)):
                localctx.op = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 22
            self.complexNumber()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComplexNumberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ComplexOperationsParser.RULE_complexNumber

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class DefComplexContext(ComplexNumberContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ComplexOperationsParser.ComplexNumberContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def realPart(self):
            return self.getTypedRuleContext(ComplexOperationsParser.RealPartContext,0)

        def imaginaryPart(self):
            return self.getTypedRuleContext(ComplexOperationsParser.ImaginaryPartContext,0)

        def ADD(self):
            return self.getToken(ComplexOperationsParser.ADD, 0)
        def SUB(self):
            return self.getToken(ComplexOperationsParser.SUB, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefComplex" ):
                listener.enterDefComplex(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefComplex" ):
                listener.exitDefComplex(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefComplex" ):
                return visitor.visitDefComplex(self)
            else:
                return visitor.visitChildren(self)



    def complexNumber(self):

        localctx = ComplexOperationsParser.ComplexNumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_complexNumber)
        self._la = 0 # Token type
        try:
            localctx = ComplexOperationsParser.DefComplexContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.match(ComplexOperationsParser.T__0)
            self.state = 25
            self.realPart()
            self.state = 26
            localctx.op = self._input.LT(1)
            _la = self._input.LA(1)
            if not(_la==4 or _la==5):
                localctx.op = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 27
            self.imaginaryPart()
            self.state = 28
            self.match(ComplexOperationsParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RealPartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ComplexOperationsParser.RULE_realPart

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class RealContext(RealPartContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ComplexOperationsParser.RealPartContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(ComplexOperationsParser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReal" ):
                listener.enterReal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReal" ):
                listener.exitReal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReal" ):
                return visitor.visitReal(self)
            else:
                return visitor.visitChildren(self)



    def realPart(self):

        localctx = ComplexOperationsParser.RealPartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_realPart)
        try:
            localctx = ComplexOperationsParser.RealContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.match(ComplexOperationsParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImaginaryPartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ComplexOperationsParser.RULE_imaginaryPart

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ImgContext(ImaginaryPartContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ComplexOperationsParser.ImaginaryPartContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(ComplexOperationsParser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImg" ):
                listener.enterImg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImg" ):
                listener.exitImg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImg" ):
                return visitor.visitImg(self)
            else:
                return visitor.visitChildren(self)



    def imaginaryPart(self):

        localctx = ComplexOperationsParser.ImaginaryPartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_imaginaryPart)
        try:
            localctx = ComplexOperationsParser.ImgContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.match(ComplexOperationsParser.NUMBER)
            self.state = 33
            self.match(ComplexOperationsParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





