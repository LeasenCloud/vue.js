# Python prmite el tipado dinamico
'''
El tipado dinamico es que una misma variable puede
contener diferentes tipos de datos a lo largo
del programa
'''
print("Hola mundo\n")
print("hola la")

# - operadores aritmeticos
num1 = 10
num2 = 3
resultado = num1 / num2
print(resultado)  # Nos dara 3.3333333
resultado = num1 // num2
print(resultado)  # Nos dara 3. Division entera
resultado = num1 % num2
print(resultado)  # Nos dara 1. Nos da el resto de la division(modulo)
resultado = num1 ** num2
print(resultado)  # Nos dara 35 es decir 2 elevado a 5
# (exponencial o elevado a una potencia)
# La prioridad de los operadores aritmeticos es:  (), **, *, /, %, +, -

# - operadores relacionales. Se ejecutan despues de los aritmeticos
# < > <= >= != ==
resultado = 10 < 2
print(resultado)
resultado = 10 != 20
print(resultado)
resultado = num1+num2 > 30
print(resultado)

# - operadores logicos
# AND (multiplicacion logica - conjuncion). OR (suma logica - disyuncion). NOT
# En progarmacion TRUE tiene como valor 1
# En progarmacion TRUE tiene como valor 0
# La prioridad es:  NOT, AND, OR
a = 10
b = 12
c = 13
d = 10
resultado = ((a > b) or (a < c)) and ((a == c) or (a >= b))
print(resultado)

# Prioridad de los operadores en genera:
# ()
# **
# *,/,modulo,not
# +,-,and
# >,<,==,>=,<=,!=,or

a = 10
b = 15
c = 20

resultado = not((a > b) or (b < c))
print(resultado)

# - operadores de asignacion. Ayudan a ahorrar codigo
# antes hay que declarar la variable y asignarle un valor
a = 0
a = a + 5  # suma normal
# o
a += 5  # suma en asignacion
a **= 2  # potencia en asignacion

# Salidas de datos por consola:
nombre = "Alejandro"
edad = 34
print(nombre)
print("Hola ", nombre, " tienes ", edad, "de edad.")
print("Hola {} tienes {} de edad".format(nombre, edad))
# print(f"Hola {nombre}")  # Esto es para la version 3 de python

# Entrada de datos por consola:
nombre_entrada = input("Digite su nombre: ")
print("Hola {}". format(nombre_entrada))
print("Hola {}". format(nombre_entrada+5))
# Lo correcto al utilizar numeros es pasar la funcion a entero
edad_entrada = int(input("Digite su edad: "))
print("Hola {}". format(edad_entrada+10))

# Funciones integradas:
# str --> cadena - float --> flotante - bin --> binario - hex --> hexadecimal
n = bin(10)  # El binario del entero 10
print('binario de "10"', n)
str = str(10.98)  # Convertimos numeros en cadena
print("cadena de '10.98'", str)
# hexadecimal
n = hex(10)  # El hexadecimal del entero 10
print("hexadecimal de 10", n)
# Binario a entero
n = int("0b1010", base=2)
print("entero de un binario:  0b1010", n)
# Hexadecimal a entero:
n = int("0xa", base=16)
print("Hexadecimal a entero", n)
# entero a hexadecimal a entero:
n = hex(10)
print("entero 10 a hexadecimal", n)
# Valor absoluto:
n = abs(-8)
print("absoluto:", n)
# redondeo:
n = round(5.4)
print("redondeo", n)
n = round(5.6)
print("redondeo", n)
# Contador letras y numeros:
n = len("Alejandro111")
print("Contador de Alejandro111", n)
