#Realizar un ejercicio por cada tipo de excepción.

#Ejemplo de ZeroDivisionError

numero1 = 10
numero2 = 0
try:
    resultado = numero1 / numero2
except ZeroDivisionError:
    print("Error: división por cero")
