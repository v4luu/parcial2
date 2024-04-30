// ComplexOperations.g4

grammar ComplexOperations;

prog:   start+ ;

start: operation NEWLINE   						# Print;

operation: complexNumber op=('+'|'-'|'*'|'/') complexNumber 	# Operar;
complexNumber: '(' realPart op=('+'|'-') imaginaryPart ')' 	# DefComplex;

realPart: NUMBER						# real;
imaginaryPart: NUMBER 'i' 					# img;

ADD: '+' ; 
SUB: '-' ;
MUL: '*' ;
DIV: '/' ;

NUMBER: [0-9]+;
NEWLINE:'\r'? '\n' ;     // return newlines to parser (is end-statement signal)
WS  :   [ \t]+ -> skip ;

