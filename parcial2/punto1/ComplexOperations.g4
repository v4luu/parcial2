// ComplexOperations.g4

grammar ComplexOperations;

start: operation EOF						# Print;

operation: complexNumber op=('+'|'-'|'*'|'/') complexNumber	# Operar;
complexNumber: '(' realPart op=('+'|'-') imaginaryPart ')'	# DefComplex;

realPart: NUMBER						# real;
imaginaryPart: NUMBER 'i' 					# img;

ADD: '+' ; 
SUB: '-' ;
MUL: '*' ;
DIV: '/' ;

NUMBER: [0-9]+;
WS: [ \t\r\n]+ -> skip;
