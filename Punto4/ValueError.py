#Realizar un ejercicio por cada tipo de excepción.

#Ejemplo ValueError

try:
    edad = int(input("Ingrese su edad: "))
except ValueError:
    print("Error: El valor ingresado no es un número válido")
