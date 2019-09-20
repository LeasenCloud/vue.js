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
