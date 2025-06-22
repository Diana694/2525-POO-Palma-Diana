# Programa para calcular el promedio semanal del clima usando programación tradicional

def ingresar_temperaturas():
    temperaturas = []
    for i in range(7):
        temp = float(input(f"Ingrese la temperatura del día {i+1}: "))
        temperaturas.append(temp)
    return temperaturas

def calcular_promedio(temperaturas):
    total = sum(temperaturas)
    promedio = total / len(temperaturas)
    return promedio

def main():
    print("=== Programa de promedio semanal de temperaturas ===")
    temps = ingresar_temperaturas()
    promedio_semanal = calcular_promedio(temps)
    print(f"El promedio semanal de temperatura es: {promedio_semanal:.2f} °C")

if _name_ == "_main_":
    main()