# Generated from ComplexOperations.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ComplexOperationsParser import ComplexOperationsParser
else:
    from ComplexOperationsParser import ComplexOperationsParser

# This class defines a complete listener for a parse tree produced by ComplexOperationsParser.
class ComplexOperationsListener(ParseTreeListener):

    # Enter a parse tree produced by ComplexOperationsParser#Print.
    def enterPrint(self, ctx:ComplexOperationsParser.PrintContext):
        pass

    # Exit a parse tree produced by ComplexOperationsParser#Print.
    def exitPrint(self, ctx:ComplexOperationsParser.PrintContext):
        pass


    # Enter a parse tree produced by ComplexOperationsParser#Operar.
    def enterOperar(self, ctx:ComplexOperationsParser.OperarContext):
        pass

    # Exit a parse tree produced by ComplexOperationsParser#Operar.
    def exitOperar(self, ctx:ComplexOperationsParser.OperarContext):
        pass


    # Enter a parse tree produced by ComplexOperationsParser#DefComplex.
    def enterDefComplex(self, ctx:ComplexOperationsParser.DefComplexContext):
        pass

    # Exit a parse tree produced by ComplexOperationsParser#DefComplex.
    def exitDefComplex(self, ctx:ComplexOperationsParser.DefComplexContext):
        pass


    # Enter a parse tree produced by ComplexOperationsParser#real.
    def enterReal(self, ctx:ComplexOperationsParser.RealContext):
        pass

    # Exit a parse tree produced by ComplexOperationsParser#real.
    def exitReal(self, ctx:ComplexOperationsParser.RealContext):
        pass


    # Enter a parse tree produced by ComplexOperationsParser#img.
    def enterImg(self, ctx:ComplexOperationsParser.ImgContext):
        pass

    # Exit a parse tree produced by ComplexOperationsParser#img.
    def exitImg(self, ctx:ComplexOperationsParser.ImgContext):
        pass



del ComplexOperationsParser