from oop import Animal

"""
Liskov Substitution Principle

Animal es la super clase de gato, tambien imlementaremos una clase perro con esta Super clase
Con esto obligamos a implementar una función que tienen en comun: leg_count

"""


class CatSolid(Animal):
    name = "lanita"
    breed = "angora"
    age = 1
    """"
    Dependency Inversion Principle
    
    Si esta clase ocupa otra clase para solucionar problemas, podemos iyectar la segunda clase mediante el constructor.
    
    Esto sirve mucho a la hora de hacer unit testing, ya que mediante mock puedes tener acceso a toda la cobertura de funciones de esta clase.
    Ej: Necesito probar una clase catService, este hace uso de un catModel para llamar a la base de datos.
    Sin inyeccion de dependencias al momento de testear: 
    Tienes acceso solo a las funciones de catService. Solo tendras cobertura para suponer que hace la funcion de catService con catModel, no un control total.
    
    Con Inyeccion de dependencias:
    Puedes crear un mock de catModel eliminando la necesidad de una base de datos, luego pasarlo en el constructor de catService.
    
    Con esto tienes cobertura total de catService y catModel, mediante el mock vas a poder a interactuar con catModel.
    Saber si una funcion fue llamada y devolver valores, completando la cobertura de cualquier funcion de catService
    que necesite a catModel. 
    """""

    def __init__(self, cat_gun):
        self.cat_gun = cat_gun

    def meow(self):
        print(
            f"meow soy {self.name}, un gato creado con OOP y los principios solid, voy a ocupar mi gatopistola que alguien me regalo")
