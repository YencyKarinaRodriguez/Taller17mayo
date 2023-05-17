#Realizar un ejercicio por cada tipo de excepción.

#Ejemplo TypeError

verdura = "tomate"
precio = 500
try:
    resultado = verdura + precio
except TypeError:
    print("Error: tipos de datos incompatibles")
