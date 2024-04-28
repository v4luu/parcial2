# Generated from ComplexOperations.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ComplexOperationsParser import ComplexOperationsParser
else:
    from ComplexOperationsParser import ComplexOperationsParser

# This class defines a complete generic visitor for a parse tree produced by ComplexOperationsParser.

class ComplexOperationsVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ComplexOperationsParser#Print.
    def visitPrint(self, ctx:ComplexOperationsParser.PrintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ComplexOperationsParser#Operar.
    def visitOperar(self, ctx:ComplexOperationsParser.OperarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ComplexOperationsParser#DefComplex.
    def visitDefComplex(self, ctx:ComplexOperationsParser.DefComplexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ComplexOperationsParser#real.
    def visitReal(self, ctx:ComplexOperationsParser.RealContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ComplexOperationsParser#img.
    def visitImg(self, ctx:ComplexOperationsParser.ImgContext):
        return self.visitChildren(ctx)



del ComplexOperationsParser