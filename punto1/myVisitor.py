from ComplexOperationsVisitor import ComplexOperationsVisitor
from ComplexOperationsParser import ComplexOperationsParser
class myVisitor(ComplexOperationsVisitor):
    def __init__(self):
        self.result = None

    def visitOperar(self, ctx):
        #print("a")
        left = self.visit(ctx.complexNumber(0))
        #print(left)
        right = self.visit(ctx.complexNumber(1))
        #print(right)
        op = ctx.op.type
        #print("chao")
        if op == ComplexOperationsParser.ADD:
            self.result = (left[0] + right[0], left[1] + right[1])
            #print(self.result)
            return self.result
        elif op == ComplexOperationsParser.SUB:
            self.result = (left[0] - right[0], left[1] - right[1])
            #print(self.result)
            return self.result
        elif op == ComplexOperationsParser.MUL:
            self.result = ((left[0] * right[0]) - (left[1] * right[1]), (left[0] * right[1]) + (left[1] * right[0]))
            #print(self.result)
            return self.result
        elif op == ComplexOperationsParser.DIV:
            denominator = right[0]**2 + right[1]**2
            self.result = ((left[0] * right[0] + left[1] * right[1]) / denominator, (left[1] * right[0] - left[0] * right[1]) / denominator)
            #print(self.result)
            return self.result

    def visitDefComplex(self, ctx):
        #print("a")
        real = self.visit(ctx.realPart())
        imaginary = self.visit(ctx.imaginaryPart())
        sign = 1 if ctx.op.type == ComplexOperationsParser.ADD else -1
        return (real, sign * imaginary)
    
    def visitPrint(self, ctx): 
        #print("ajsndk")
        #print("sjdn fksdbbfkjhdns")
        val = self.visit(ctx.operation())
        #print(val)
        return val
    
    def visitReal(self, ctx):  # visitReal
        return int (ctx.NUMBER().getText())

    def visitImg(self, ctx):  # visitImg
        return int( ctx.NUMBER().getText())

    
   