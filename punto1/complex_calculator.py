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
    tree = parser.start()

    visitor = myVisitor()
    result = visitor.visit(tree)
    #print(result)
    if (result[1]) >=  0 :
        sig = " + "
    else :
        sig = " "
    result = (str (round((result[1]), 2)) + sig + str(round((result[1]), 2)) + 'j')
    print("El resultado de la operación es:", result)

if __name__ == '__main__':
    main()
