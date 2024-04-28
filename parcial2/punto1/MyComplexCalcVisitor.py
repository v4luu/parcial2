from ComplexCalcParser import ComplexCalcParser
from ComplexCalcParser import ComplexCalcParser

class MyComplexCalcVisitor(ComplexCalcParser):
    def visitStart(self, ctx:ComplexCalcParser.StartContext):
        return self.visit(ctx.expr())

    def visitComplex(self, ctx:ComplexCalcParser.ComplexContext):
        real_part = int(ctx.realPart().getText())
        imag_part = int(ctx.imaginaryPart().getText().replace('i', 'j'))
        if ctx.sign() and ctx.sign().getText() == '-':
            imag_part = -imag_part
        return complex(real_part, imag_part)

    def visitExpr(self, ctx:ComplexCalcParser.ExprContext):
        if ctx.complexNumber():
            return self.visit(ctx.complexNumber())
        if ctx.op:
            left = self.visit(ctx.expr(0))
            right = self.visit(ctx.expr(1))
            if ctx.op.type == ComplexCalcParser.ADD:
                return left + right
            elif ctx.op.type == ComplexCalcParser.SUB:
                return left - right
                
from LabeledExprVisitor import LabeledExprVisitor

class MyVisitor1(LabeledExprVisitor):
    def __init__(self):
        self.memory = {}

    def visitAssign(self, ctx):
        name = ctx.ID().getText()
        value = self.visit(ctx.expr())
        self.memory[name] = value
        return value

    def visitPrintExpr(self, ctx):
        value = self.visit(ctx.expr())
        print(value)
        return 0
