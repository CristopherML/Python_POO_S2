class Persona:
    especie="Humano"
    
    def __init__(self, nombre, edad):
        self.nombre=nombre
        self.edad=edad
    
    def saludar(self):
        return f"Hola mi nombres es: {self.nombre} y tengo {self.edad} años"
    
    @classmethod
    def obtener_especie(cls):
        return f"Todos somos {cls.especie}"
    
    @staticmethod
    def es_mayor_de_edad(edad):
        return edad>=18
    
    persona1 = Persona("Alice",30)
    persona2 = Persona("Bob",17)
    
    print(persona1.nombre)
    print(persona2.edad)
    
    print(persona1.saludar())
     
    print(Persona.especie)
    print(persona1.especie)
    
    print(persona1.obtener_especie())
    print(Persona.es_mayor_edad(20))
    print(persona1.es_mayor_edad(16))