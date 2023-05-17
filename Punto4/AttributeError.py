#Realizar un ejercicio por cada tipo de excepción.

#Ejemplo de AttributeError

class MiClase:
    def __init__(self, nombre):
        self.nombre = nombre

objeto = MiClase("Yency")
try:
    print(objeto.edad)
except AttributeError:
    print("Error: el atributo 'edad' no existe en el objeto")


