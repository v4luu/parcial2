# parcial2
Parcial 2 

Asignación: Lenguajes de programación y transducción

Docente: Joaquin F. Sánchez

Trabajo: Parcial Lenguajes de programación - Segundo corte

Grupo 02

Integrantes del grupo: Valentina Andrade - Mateo Patiño - Nicolás Ramírez

Pasos para la ejecución por punto (en consola):

-Descargar los archivos de la carpeta comprimida.  
-Descomprimir la carpeta.  
-Abrir la línea de consola de la carpeta que contenga el archivo, si se desea realizar modificaciones en la gramatica o ingresar una distinta, ingrese al .txt del respectivo punto y hacer los cambios que se requieran   
-Ejecutar con los comandos especificados en cada punto.    
-Para todos los puntos el nombre del archivo input es input.txt     
    
*Punto 1:   
Para este tener en cuenta que siempre se seguira la estructura de (Real Operacion Imaginario), por lo tanto si no hay parte Real esta debera ser expresada como un 0, lo mismo para el caso de los imaginarios donde sera entonces 0i.
     
Comandos punto 1:    
$ antlr4 -Dlanguage=Python3 -visitor ComplexOperations.g4 -> aplicar si se hacen cambios en la gramatica     
$ python3 complex_calculator.py   
     
*Punto 2:    
-Aplicación de una funcion:   
La funcion seleccionada para este punto fue map, donde el input esperado para esta funcion sera de la forma:   
>map(funcion, lista)
Donde funcion sera definida con la estructura de una funcion lambda luego de los dos puntos. Ejemplos:     
>x+9
>x*2   
>len(x)   
>x[0]
>x.capitalize()
Y lista sera cualquier lista de strings, floats o ints
     
-Aplicación de funcion para Filtrar:   
La funcion seleccionada para este punto fue filter, donde el input esperado para esta funcion sera de la forma:   
>filter(funcion, lista)
Donde funcion sera definida siempre con una sentencia condicional donde se tenga a x como variable iteradora. Ejemplos:    
>x % 2 == 0    
>len(x) > 5       
>x > 5
Y lista sera cualquier lista de strings, floats o ints
    
Comandos punto 2:     
$ antlr4 -Dlanguage=Python3 -visitor function.g4 -> aplicar si se hacen cambios en la gramatica     
$ python3 main.py    
          
*Punto 3:    
Para el caso de este punto se uso la tabla proporcionada en Segundo_Parcial_LP.pdf, siendo asi que se tomaron las transformaciones de manera literal, los input aceptados son unicamente los siguientes, en donde se devolvera la forma para solucionar la funcion mediante transformada de fourier:    
>f(x) = {(1, t <= a/2),(0, t <= a/2)}     
>f(x) = {(1, t <= 2),(0, t <= 2)}     
>sign(t) = {(1, t > 0),(-1, t < 0)}     
>u(t) = {(1, t > 0),(0, t < 0)}     
>d(t)    
>cos(2 t)     
>sin(123 t)     
>SUM( inf, n = -inf , d(t  -n 14 ))       
     
Comandos punto 3:    
$ antlr4 -Dlanguage=Python3 -visitor fourier.g4 -> aplicar si se hacen cambios en la gramatica     
$ python3 main.py 
