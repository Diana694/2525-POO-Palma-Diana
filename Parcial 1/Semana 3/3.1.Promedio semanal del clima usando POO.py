# Programa para calcular el promedio semanal del clima usando POO en Python

class ClimaSemanal:
    def _init_(self):
        self.temperaturas = []

    def ingresar_temperaturas(self):
        for i in range(7):
            temp = float(input(f"Ingrese la temperatura del día {i+1}: "))
            self.temperaturas.append(temp)

    def calcular_promedio(self):
        total = sum(self.temperaturas)
        return total / len(self.temperaturas)

def main():
    print("=== Programa de promedio semanal de temperaturas (POO) ===")
    clima = ClimaSemanal()
    clima.ingresar_temperaturas()
    promedio = clima.calcular_promedio()
    print(f"El promedio semanal de temperatura es: {promedio:.2f} °C")

if _name_ == "_main_":
    main()