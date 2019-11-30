# !/usr/bin/python3.6
Python 3.6.8 (default, Aug 20 2019, 17:12:48) 
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.'
>>> #
# Eduardo Alexis Valencia Dorantes
# python 3.5.3
# 20/09/2019 26/09/2019
#
#
>>> # Numeros
>>> # Se agrego la operacion
>>> 2+2
4
>>> # Se agrego la operacion
>>> 50 - 5*6
20
>>> # Se agrego la operacion
>>> (50 - 5*6) / 4
5.0
>>> # Se agrego la operacion
>>> 8/5
1.6
>>> # Se agrego la operacion
>>> 17 / 3
5.666666666666667
>>> # Se agrego la operacion
>>> 17 // 3
5
>>> # Se agrego la operacion
>>> 17 % 3
2
>>> # Se agrego la operacion
>>> 5 * 3 + 2
17
>>> # Se agrego la operacion
>>> 5 ** 2
25
>>> # Se agrego la operacion
>>> 2 ** 7
128
>>> # Se agrego la operacion
>>> 9 ** 0.5
3.0
>>> # Se agrego la operacion
>>> 2 ** 1/2
1.0
>>> # Se agrego la operacion
>>> 2 ** (1/2)
1.4142135623730951
>>> # Se agrego
>>> ancho = 20
>>> # Se agrego
>>> alto = 5 * 9
>>> # Se agrego la operacion
>>> ancho * alto
900
>>> # Se agrego
>>> n
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    n
NameError: name 'n' is not defined
>>> # Se agrego
>>> # Se agrego la operacion
>>> 4 * 3.75 - 1
14.0
>>> # Se agrego
>>> iva = 16/100
>>> # Se agrego
>>> precio = 120.5
>>> # Se agrego la operacion
>>> precio * iva
19.28
>>> # Se agrego la operacion
>>> precio + _
139.78
>>> # Se agrego la operacion
>>> round(_, 2)
139.78
>>> # Cadenas
>>> # Se agrego
>>> 'una cadena'
'una cadena'
>>> # Se agrego
>>> 'La comilla simple \''
"La comilla simple '"
>>> # Se agrego
>>> 'La comilla simple \''
"La comilla simple '"
>>> # Se agrego
>>> "\"Si,\" afirmo"
'"Si," afirmo'
>>> # Se agrego
>>> '"Si," afirmo'
'"Si," afirmo'
>>> # Se agrego
>>> "Si," afirmo"
SyntaxError: invalid syntax
>>> 'La comilla simple \''
"La comilla simple '"
>>> # Se agrego
>>> "\"Si,\" afirmo"
'"Si," afirmo'
>>> # Se agrego
>>> print("\"Si,\" afirmo")
"Si," afirmo
>>> # Se agrego
>>> c = 'Primera linea.\nSegunda linea.'
>>> # Se agrego
>>> c
'Primera linea.\nSegunda linea.'
>>> # Se agrego
>>> print(c)
Primera linea.
Segunda linea.
>>> # Se agrego
>>> len(c)
29
>>> # Se agrego
>>> print('Una ruta en Windows C:\algun\nombre')
Una ruta en Windows C:lgun
ombre
>>> # Se agrego
>>> print(r'Una ruta en Windows C:\algun\nombre')
Una ruta en Windows C:\algun\nombre
>>> # Se agrego
>>> print("""\
Uso: ssh [OPCIONES] <usuario>@<servidor>
     -v                 muestra informacion adiciona de la conexion
     -p puerto          Puerto para la conexion segura, 22 es el prederterminado
""")
Uso: ssh [OPCIONES] <usuario>@<servidor>
     -v                 muestra informacion adiciona de la conexion
     -p puerto          Puerto para la conexion segura, 22 es el prederterminado

>>> # Se agrego
>>> 2 * 'goya ' + 'cachun'
'goya goya cachun'
>>> # Se agrego
>>> 'Py' 'thon'
'Python'
>>> # Se agrego
>>> text = ('Escribe varias cadenas dentro del par'entesis '
	    
SyntaxError: invalid syntax
>>> text = ('Escribe varias cadenas dentro del par'entesis '
	    
SyntaxError: invalid syntax
>>> text = ('Escribe varias cadenas dentro del par'entesis '
	    
SyntaxError: invalid syntax
>>> text = ('Escribe varias cadenas dentro del par'entesis '
	    
SyntaxError: invalid syntax
>>> text
	    
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    text
NameError: name 'text' is not defined
>>> # Se agrego
	    
>>> prefijo = 'Py'
	    
>>> # Se agrego
	    
>>> prefijo = 'thon'
	    
>>> # Se agrego
	    
>>> ('un' * 3) 'ium'
	    
SyntaxError: invalid syntax
>>> # Se agrego
	    
>>> prefijo + 'thon'
	    
'thonthon'
>>> # Se agrego
	    
>>> nombre = "Ada"
	    
>>> apellido = "Lovelace"
	    
>>> # Se agrego
	    
>>> print(nombre.upper())
	    
ADA
>>> # Se agrego
	    
>>> print(nombre.lower())
	    
ada
>>> # Se agrego
	    
>>> print(nombre.isalnum())
	    
True
>>> # Se agrego
	    
>>> print(nombre.isalpha())
	    
True
>>> # Se agrego
	    
>>> print(nombre.islower())
	    
False
>>> # Se agrego
	    
>>> print(nombre.isnumeric())
	    
False
>>> # Se agrego
	    
>>> print(nombre.isspace())
	    
False
>>> # Se agrego
	    
>>> print(nombre.istitle())
	    
True
>>> # Se agrego
	    
>>> asignatura = "Taller De Herramientas Computacionales"
	    
>>> # Se agrego
	    
>>> print(asignatura.istitle())
	    
True
>>> # Se agrego
	    
>>> print(asignatura.isupper())
	    
False
>>> # Se agrego
	    
>>> numero = "1024"
	    
>>> # Se agrego
	    
>>> vocales = "aeiou"
	    
>>> # Se agrego
	    
>>> print(numero.isnumeric())
	    
True
>>> # Se agrego
	    
>>> print(numero.isnumeric())
	    
True
>>> 
	    
>>> # Se agrego
	    
>>> print(vocales.isnumeric())
	    
False
>>> # Se agrego
	    
>>> pelicula = "2001: UNA MENTE BRILLANTE"
	    
>>> # Se agrego
	    
>>> libro = "Cinco Ecuaciones Que Cambiaron Al Mundo
	    
SyntaxError: EOL while scanning string literal
>>> libro = "Cinco Ecuaciones Que CAmbiaron Al Mundo"
	    
>>> # Se agrego
	    
>>> poema = "nadie en oro se convertirá:"
	    
>>> # Se agrego
	    
>>> print(pelicula.islower())
	    
False
>>> print(pelicula.isupper())
	    
True
>>> # Se agrego
	    
>>> print(libro.istitle())
	    
False
>>> print(libro.istitle())
	    
False
>>> print(libro.isupper())
	    
False
>>> # Se agrego
	    
>>> print(poema.istitle())
	    
False
>>> print(poema.islower())
	    
True
>>> # Se agrego
	    
>>> cadena = "linux es un kernel."
	    
>>> # Se agrego
	    
>>> " ".join(cadena)
	    
'l i n u x   e s   u n   k e r n e l .'
>>> # Se agrego
	    
>>> print(cadena)
	    
linux es un kernel.
>>> print(" ".join(cadena))
	    
l i n u x   e s   u n   k e r n e l .
>>> # Se agrego
	    
>>> print(" ".join(reversed(cadena)))
	    
. l e n r e k   n u   s e   x u n i l
>>> # Se agrego
	    
>>> # https://docs.python.org/3/tutorial/introduction.html#strings
	    
>>> # Se agrego
	    
>>> # https://www.digitalocean.com/community/tutorials/an-introduction-to-string-functions-in-python-3
	    
>>> 
