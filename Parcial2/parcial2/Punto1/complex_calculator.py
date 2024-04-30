# main.py

from antlr4 import *
from ComplexOperationsLexer import ComplexOperationsLexer
from ComplexOperationsParser import ComplexOperationsParser
from ComplexOperationsVisitor import ComplexOperationsVisitor
from myVisitor import myVisitor

def main():
    input_stream = FileStream('input.txt')
    lexer = ComplexOperationsLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ComplexOperationsParser(stream)
    tree = parser.prog()

    visitor = myVisitor()
    visitor.visit(tree)
    #print(result)
    

if __name__ == '__main__':
    main()
