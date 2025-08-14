# inventario_app.py

# ==========================
# Clase Producto
# ==========================
class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def get_id(self):
        return self.id

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"


# ==========================
# Clase Inventario
# ==========================
class Inventario:
    def __init__(self):
        self.productos = []
        self.cargar_datos_de_ejemplo()

    def cargar_datos_de_ejemplo(self):
        # Datos precargados de ejemplo
        ejemplos = [
            Producto("P001", "Laptop Lenovo", 10, 999.99),
            Producto("P002", "Mouse Logitech", 25, 19.99),
            Producto("P003", "Teclado Mecánico", 15, 49.50),
            Producto("P004", "Monitor Samsung 24''", 8, 150.00),
            Producto("P005", "Disco SSD 1TB", 12, 120.00)
        ]
        for prod in ejemplos:
            self.agregar_producto(prod, mostrar_mensaje=False)

    def agregar_producto(self, producto, mostrar_mensaje=True):
        if any(p.get_id() == producto.get_id() for p in self.productos):
            if mostrar_mensaje:
                print("⚠️ Error: Ya existe un producto con ese ID.")
            return False
        self.productos.append(producto)
        if mostrar_mensaje:
            print("✅ Producto agregado correctamente.")
        return True

    def eliminar_producto(self, id):
        for producto in self.productos:
            if producto.get_id() == id:
                self.productos.remove(producto)
                print("✅ Producto eliminado correctamente.")
                return True
        print("❌ Producto no encontrado.")
        return False

    def actualizar_producto(self, id, cantidad=None, precio=None):
        for producto in self.productos:
            if producto.get_id() == id:
                if cantidad is not None:
                    producto.set_cantidad(cantidad)
                if precio is not None:
                    producto.set_precio(precio)
                print("✅ Producto actualizado.")
                return True
        print("❌ Producto no encontrado.")
        return False

    def buscar_producto(self, nombre):
        return [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]

    def mostrar_productos(self):
        if not self.productos:
            print("ℹ️ El inventario está vacío.")
        else:
            print("\n📦 Productos en inventario:")
            for producto in self.productos:
                print(producto)


# ==========================
# Interfaz de Consola
# ==========================
def mostrar_menu():
    print("\n====== Menú de Gestión de Inventario ======")
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto por nombre")
    print("5. Mostrar todos los productos")
    print("6. Salir")

def main():
    inventario = Inventario()

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-6): ")

        if opcion == '1':
            try:
                id = input("ID del producto: ").strip()
                nombre = input("Nombre del producto: ").strip()
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))
                producto = Producto(id, nombre, cantidad, precio)
                inventario.agregar_producto(producto)
            except ValueError:
                print("❌ Error: Entrada inválida. Intenta de nuevo.")

        elif opcion == '2':
            id = input("ID del producto a eliminar: ").strip()
            inventario.eliminar_producto(id)

        elif opcion == '3':
            id = input("ID del producto a actualizar: ").strip()
            try:
                cantidad_input = input("Nueva cantidad (enter para omitir): ")
                precio_input = input("Nuevo precio (enter para omitir): ")
                cantidad = int(cantidad_input) if cantidad_input else None
                precio = float(precio_input) if precio_input else None
                inventario.actualizar_producto(id, cantidad, precio)
            except ValueError:
                print("❌ Error: Entrada inválida.")

        elif opcion == '4':
            nombre = input("Nombre del producto a buscar: ").strip()
            resultados = inventario.buscar_producto(nombre)
            if resultados:
                print("\n🔍 Resultados de búsqueda:")
                for p in resultados:
                    print(p)
            else:
                print("🔎 No se encontraron productos con ese nombre.")

        elif opcion == '5':
            inventario.mostrar_productos()

        elif opcion == '6':
            print("👋 Saliendo del sistema. ¡Hasta luego!")
            break

        else:
            print("❗ Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()

