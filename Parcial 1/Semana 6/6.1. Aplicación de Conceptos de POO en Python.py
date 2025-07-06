# zoo.py

# Clase base: Animal
class Animal:
    def __init__(self, nombre, edad):
        self._nombre = nombre            # Atributo encapsulado
        self._edad = edad                # Atributo encapsulado

    def hacer_sonido(self):
        return "El animal hace un sonido"

    def informacion(self):
        return f"Nombre: {self._nombre}, Edad: {self._edad} años"

# Clase derivada: Perro (hereda de Animal)
class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)
        self._raza = raza                # Atributo encapsulado

    # Polimorfismo: sobrescribimos el método hacer_sonido
    def hacer_sonido(self):
        return "Guau Guau!"

    def informacion(self):
        # Polimorfismo: mismo método, diferente comportamiento
        base_info = super().informacion()
        return f"{base_info}, Raza: {self._raza}"

# Clase derivada: Gato (hereda de Animal)
class Gato(Animal):
    def __init__(self, nombre, edad, color):
        super().__init__(nombre, edad)
        self._color = color              # Atributo encapsulado

    def hacer_sonido(self):
        return "Miau!"

    def informacion(self):
        base_info = super().informacion()
        return f"{base_info}, Color: {self._color}"

# Crear instancias de las clases
perro1 = Perro("Fido", 3, "Labrador")
gato1 = Gato("Michi", 2, "Blanco")

# Mostrar información y sonido
print(perro1.informacion())
print("Sonido del perro:", perro1.hacer_sonido())

print(gato1.informacion())
print("Sonido del gato:", gato1.hacer_sonido())

# Polimorfismo en acción: misma interfaz, diferentes comportamientos
animales = [perro1, gato1]
for animal in animales:
    print(f"{animal._nombre} dice: {animal.hacer_sonido()}")
