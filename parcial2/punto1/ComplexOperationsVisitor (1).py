# Generated from ComplexOperations.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ComplexOperationsParser import ComplexOperationsParser
else:
    from ComplexOperationsParser import ComplexOperationsParser

# This class defines a complete generic visitor for a parse tree produced by ComplexOperationsParser.

class ComplexOperationsVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ComplexOperationsParser#start.
    def visitStart(self, ctx:ComplexOperationsParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ComplexOperationsParser#operation.
    def visitOperation(self, ctx:ComplexOperationsParser.OperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ComplexOperationsParser#complexNumber.
    def visitComplexNumber(self, ctx:ComplexOperationsParser.ComplexNumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ComplexOperationsParser#realPart.
    def visitRealPart(self, ctx:ComplexOperationsParser.RealPartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ComplexOperationsParser#imaginaryPart.
    def visitImaginaryPart(self, ctx:ComplexOperationsParser.ImaginaryPartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ComplexOperationsParser#operator.
    def visitOperator(self, ctx:ComplexOperationsParser.OperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ComplexOperationsParser#sign.
    def visitSign(self, ctx:ComplexOperationsParser.SignContext):
        return self.visitChildren(ctx)



del ComplexOperationsParser