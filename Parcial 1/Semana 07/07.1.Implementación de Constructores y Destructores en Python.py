# -----------------------------------------------------
# Ejemplo 1: Clase Archivo (manejo de recursos externos)
# -----------------------------------------------------
class Archivo:
    """
    Clase que simula la apertura y cierre de un archivo para demostrar
    el uso de constructores y destructores en Python.
    """

    def __init__(self, nombre_archivo):
        """
        Constructor que abre el archivo en modo escritura.
        """
        self.nombre_archivo = nombre_archivo
        self.archivo = open(nombre_archivo, 'w')
        print(f"[INIT] Archivo '{self.nombre_archivo}' ha sido creado y abierto para escribir.")

    def escribir_linea(self, texto):
        """
        Escribe una línea de texto en el archivo.
        """
        self.archivo.write(texto + '\n')
        print(f"[WRITE] Se escribió: '{texto}' en el archivo '{self.nombre_archivo}'.")

    def __del__(self):
        """
        Destructor que cierra el archivo si está abierto.
        """
        if hasattr(self, 'archivo') and not self.archivo.closed:
            self.archivo.close()
            print(f"[DEL] Archivo '{self.nombre_archivo}' ha sido cerrado correctamente.")


# -----------------------------------------------------
# Ejemplo 2: Clase Estudiante
# -----------------------------------------------------
class Estudiante:
    """
    Clase que representa a un estudiante.
    """

    def __init__(self, nombre, edad, carrera):
        """
        Constructor que inicializa los datos del estudiante.
        """
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera
        print(f"[INIT] Estudiante '{self.nombre}' ha sido registrado.")

    def mostrar_informacion(self):
        """
        Muestra la información del estudiante.
        """
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, Carrera: {self.carrera}")

    def __del__(self):
        """
        Destructor que indica que el objeto ha sido eliminado.
        """
        print(f"[DEL] Estudiante '{self.nombre}' ha sido eliminado de la memoria.")


# -----------------------------------------------------
# Ejemplo 3: Clase CuentaBancaria
# -----------------------------------------------------
class CuentaBancaria:
    """
    Clase que simula una cuenta bancaria.
    """

    def __init__(self, titular, saldo=0.0):
        """
        Constructor que crea una cuenta con un saldo inicial.
        """
        self.titular = titular
        self.saldo = saldo
        print(f"[INIT] Cuenta creada para {self.titular} con saldo de ${self.saldo:.2f}")

    def depositar(self, cantidad):
        """
        Deposita dinero en la cuenta.
        """
        self.saldo += cantidad
        print(f"[DEPÓSITO] +${cantidad:.2f} -> Saldo actual: ${self.saldo:.2f}")

    def retirar(self, cantidad):
        """
        Retira dinero si hay saldo suficiente.
        """
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            print(f"[RETIRO] -${cantidad:.2f} -> Saldo restante: ${self.saldo:.2f}")
        else:
            print("[ERROR] Fondos insuficientes para realizar el retiro.")

    def __del__(self):
        """
        Destructor que indica el cierre de la cuenta.
        """
        print(f"[DEL] Cuenta de {self.titular} cerrada con saldo final de ${self.saldo:.2f}")


# -----------------------------------------------------
# Bloque principal del programa
# -----------------------------------------------------
if __name__ == "__main__":
    print("========== INICIO DEL PROGRAMA ==========\n")

    # Ejemplo 1: Uso de la clase Archivo
    print(">>> Ejemplo 1: Archivo")
    archivo = Archivo("salida.txt")
    archivo.escribir_linea("Primera línea en el archivo.")
    archivo.escribir_linea("Segunda línea de prueba.")
    print()

    # Ejemplo 2: Uso de la clase Estudiante
    print(">>> Ejemplo 2: Estudiante")
    estudiante = Estudiante("Luis García", 20, "Ingeniería en Sistemas")
    estudiante.mostrar_informacion()
    print()

    # Ejemplo 3: Uso de la clase CuentaBancaria
    print(">>> Ejemplo 3: CuentaBancaria")
    cuenta = CuentaBancaria("María López", 1000)
    cuenta.depositar(500)
    cuenta.retirar(300)
    cuenta.retirar(1500)  # intento fallido
    print()

    print("========== FIN DEL PROGRAMA ==========\n")
