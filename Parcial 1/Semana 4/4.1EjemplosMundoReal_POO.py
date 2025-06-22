# hotel.py

# Clase Cliente representa a una persona que quiere reservar
class Cliente:
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula

    def __str__(self):
        return f"Cliente: {self.nombre}, Cédula: {self.cedula}"


# Clase Habitacion representa una habitación del hotel
class Habitacion:
    def __init__(self, numero, tipo, precio):
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.esta_reservada = False

    def reservar(self):
        if not self.esta_reservada:
            self.esta_reservada = True
            print(f"Habitación {self.numero} ha sido reservada.")
        else:
            print(f"Habitación {self.numero} ya está reservada.")

    def __str__(self):
        estado = "Reservada" if self.esta_reservada else "Disponible"
        return f"Habitación {self.numero} - {self.tipo} - ${self.precio} - {estado}"


# Clase Reserva representa una reserva realizada por un cliente
class Reserva:
    def __init__(self, cliente, habitacion):
        self.cliente = cliente
        self.habitacion = habitacion

    def confirmar_reserva(self):
        if not self.habitacion.esta_reservada:
            self.habitacion.reservar()
            print(f"Reserva confirmada para {self.cliente.nombre}")
        else:
            print("No se pudo confirmar la reserva. Habitación ocupada.")

    def __str__(self):
        return f"{self.cliente.nombre} reservó la habitación {self.habitacion.numero}"


# Ejemplo de uso
if __name__ == "__main__":
    # Crear clientes
    cliente1 = Cliente("Juan Pérez", "0102030405")
    cliente2 = Cliente("Ana Gómez", "0506070809")

    # Crear habitaciones
    habitacion1 = Habitacion(101, "Individual", 50)
    habitacion2 = Habitacion(102, "Doble", 80)

    # Mostrar estado de habitaciones
    print(habitacion1)
    print(habitacion2)

    # Realizar reservas
    reserva1 = Reserva(cliente1, habitacion1)
    reserva1.confirmar_reserva()

    reserva2 = Reserva(cliente2, habitacion1)  # Esta ya está reservada
    reserva2.confirmar_reserva()

    # Estado final
    print(habitacion1)
