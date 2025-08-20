# Sistema de Gestión de Inventarios Mejorado
# Autor: [Tu Nombre]
# Fecha: [Fecha Actual]
# Descripción: Este programa permite gestionar un inventario de productos utilizando archivos de texto
# para guardar y recuperar datos. Incluye manejo de excepciones para lectura y escritura de archivos.

import os

# Clase Producto: representa un producto con código, nombre y cantidad
class Producto:
    def __init__(self, codigo, nombre, cantidad):
        self.codigo = codigo
        self.nombre = nombre
        self.cantidad = cantidad

    def __str__(self):
        return f"{self.codigo},{self.nombre},{self.cantidad}"

    @staticmethod
    def desde_linea(linea):
        """
        Convierte una línea del archivo en un objeto Producto.
        """
        try:
            codigo, nombre, cantidad = linea.strip().split(',')
            return Producto(codigo, nombre, int(cantidad))
        except ValueError:
            print("⚠️ Línea inválida en el archivo. Se omitirá.")
            return None

# Clase Inventario: maneja la lógica del inventario y el archivo
class Inventario:
    def __init__(self, archivo='inventario.txt'):
        self.archivo = archivo
        self.productos = {}
        self.cargar_desde_archivo()

    def cargar_desde_archivo(self):
        """
        Carga los productos desde el archivo al iniciar el programa.
        """
        try:
            with open(self.archivo, 'r', encoding='utf-8') as f:
                for linea in f:
                    producto = Producto.desde_linea(linea)
                    if producto:
                        self.productos[producto.codigo] = producto
            print("✅ Inventario cargado correctamente.")
        except FileNotFoundError:
            print("📂 Archivo no encontrado. Se creará uno nuevo al guardar.")
        except PermissionError:
            print("⛔ Error de permisos al leer el archivo.")
        except Exception as e:
            print(f"⚠️ Error inesperado al cargar: {e}")

    def guardar_en_archivo(self):
        """
        Guarda todos los productos actuales en el archivo.
        """
        try:
            with open(self.archivo, 'w', encoding='utf-8') as f:
                for producto in self.productos.values():
                    f.write(str(producto) + '\n')
            print("💾 Cambios guardados en el archivo correctamente.")
        except PermissionError:
            print("⛔ No tienes permiso para escribir en el archivo.")
        except Exception as e:
            print(f"⚠️ Error al guardar el archivo: {e}")

    def agregar_producto(self, codigo, nombre, cantidad):
        if codigo in self.productos:
            print("⚠️ El producto ya existe. Usa la opción de actualizar.")
            return
        self.productos[codigo] = Producto(codigo, nombre, cantidad)
        self.guardar_en_archivo()
        print("✅ Producto agregado correctamente.")

    def actualizar_producto(self, codigo, cantidad):
        if codigo not in self.productos:
            print("❌ Producto no encontrado.")
            return
        self.productos[codigo].cantidad = cantidad
        self.guardar_en_archivo()
        print("✅ Producto actualizado correctamente.")

    def eliminar_producto(self, codigo):
        if codigo in self.productos:
            del self.productos[codigo]
            self.guardar_en_archivo()
            print("🗑️ Producto eliminado correctamente.")
        else:
            print("❌ Producto no encontrado.")

    def mostrar_inventario(self):
        if not self.productos:
            print("📭 El inventario está vacío.")
        else:
            print("\n📦 Inventario actual:")
            for p in self.productos.values():
                print(f" - Código: {p.codigo}, Nombre: {p.nombre}, Cantidad: {p.cantidad}")

# Menú interactivo para el usuario
def menu():
    inventario = Inventario()

    while True:
        print("\n========= MENÚ DE INVENTARIO =========")
        print("1. Ver inventario")
        print("2. Agregar producto")
        print("3. Actualizar producto")
        print("4. Eliminar producto")
        print("5. Salir")
        print("======================================")

        opcion = input("Seleccione una opción (1-5): ")

        if opcion == '1':
            inventario.mostrar_inventario()
        elif opcion == '2':
            codigo = input("Ingrese el código del producto: ").strip()
            nombre = input("Ingrese el nombre del producto: ").strip()
            try:
                cantidad = int(input("Ingrese la cantidad: "))
                inventario.agregar_producto(codigo, nombre, cantidad)
            except ValueError:
                print("⚠️ Error: La cantidad debe ser un número entero.")
        elif opcion == '3':
            codigo = input("Ingrese el código del producto a actualizar: ").strip()
            try:
                cantidad = int(input("Ingrese la nueva cantidad: "))
                inventario.actualizar_producto(codigo, cantidad)
            except ValueError:
                print("⚠️ Error: La cantidad debe ser un número entero.")
        elif opcion == '4':
            codigo = input("Ingrese el código del producto a eliminar: ").strip()
            inventario.eliminar_producto(codigo)
        elif opcion == '5':
            print("👋 Saliendo del sistema. ¡Hasta pronto!")
            break
        else:
            print("❌ Opción inválida. Intente nuevamente.")

# Punto de entrada del programa
if __name__ == "__main__":
    menu()
