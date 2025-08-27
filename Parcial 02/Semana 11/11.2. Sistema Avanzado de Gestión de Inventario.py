import json
import os


class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def to_dict(self):
        return {
            'id_producto': self.id_producto,
            'nombre': self.nombre,
            'cantidad': self.cantidad,
            'precio': self.precio
        }

    @staticmethod
    def from_dict(data):
        return Producto(
            id_producto=data['id_producto'],
            nombre=data['nombre'],
            cantidad=data['cantidad'],
            precio=data['precio']
        )

    def __str__(self):
        return f"[{self.id_producto}] {self.nombre} - Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"


class Inventario:
    def __init__(self):
        self.productos = {}  # Diccionario: clave = ID, valor = Producto

    def agregar_producto(self, producto):
        if producto.id_producto in self.productos:
            print("⚠️ Ya existe un producto con ese ID.")
        else:
            self.productos[producto.id_producto] = producto
            print("✅ Producto agregado correctamente.")

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            print("✅ Producto eliminado.")
        else:
            print("❌ Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            if cantidad is not None:
                self.productos[id_producto].cantidad = cantidad
            if precio is not None:
                self.productos[id_producto].precio = precio
            print("✅ Producto actualizado.")
        else:
            print("❌ Producto no encontrado.")

    def buscar_por_nombre(self, nombre):
        resultados = [p for p in self.productos.values() if p.nombre.lower() == nombre.lower()]
        if resultados:
            for p in resultados:
                print(p)
        else:
            print("❌ No se encontraron productos con ese nombre.")

    def mostrar_todos(self):
        if not self.productos:
            print("📭 El inventario está vacío.")
        else:
            for p in self.productos.values():
                print(p)

    def guardar_en_archivo(self, nombre_archivo):
        with open(nombre_archivo, 'w') as f:
            json.dump([p.to_dict() for p in self.productos.values()], f, indent=4)
        print("💾 Inventario guardado en archivo.")

    def cargar_desde_archivo(self, nombre_archivo):
        if not os.path.exists(nombre_archivo):
            print("📁 Archivo no encontrado. Creando inventario con datos de ejemplo.")
            self.agregar_datos_de_ejemplo()
            return
        try:
            with open(nombre_archivo, 'r') as f:
                data = json.load(f)
                for item in data:
                    producto = Producto.from_dict(item)
                    self.productos[producto.id_producto] = producto
            print("📂 Inventario cargado desde archivo.")
        except json.JSONDecodeError:
            print("❌ El archivo de inventario está dañado o vacío.")

    def agregar_datos_de_ejemplo(self):
        productos_ejemplo = [
            Producto("P001", "Laptop Lenovo", 10, 799.99),
            Producto("P002", "Mouse Logitech", 25, 19.99),
            Producto("P003", "Teclado Redragon", 15, 45.50),
            Producto("P004", "Monitor Samsung", 8, 159.99),
            Producto("P005", "Disco SSD 1TB", 12, 99.90),
        ]
        for p in productos_ejemplo:
            self.agregar_producto(p)


def mostrar_menu():
    print("""
📦 MENÚ DE INVENTARIO:
1. Agregar producto
2. Eliminar producto
3. Actualizar producto
4. Buscar producto por nombre
5. Mostrar todos los productos
6. Guardar inventario
7. Cargar inventario
8. Salir
""")


def main():
    inventario = Inventario()
    archivo = "inventario.json"
    inventario.cargar_desde_archivo(archivo)

    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == '1':
            id_producto = input("ID del producto: ")
            nombre = input("Nombre: ")
            try:
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))
                producto = Producto(id_producto, nombre, cantidad, precio)
                inventario.agregar_producto(producto)
            except ValueError:
                print("❌ Error: cantidad y precio deben ser números.")

        elif opcion == '2':
            id_producto = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == '3':
            id_producto = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (dejar vacío para no cambiar): ")
            precio = input("Nuevo precio (dejar vacío para no cambiar): ")
            inventario.actualizar_producto(
                id_producto,
                cantidad=int(cantidad) if cantidad else None,
                precio=float(precio) if precio else None
            )

        elif opcion == '4':
            nombre = input("Nombre del producto a buscar: ")
            inventario.buscar_por_nombre(nombre)

        elif opcion == '5':
            inventario.mostrar_todos()

        elif opcion == '6':
            inventario.guardar_en_archivo(archivo)

        elif opcion == '7':
            inventario.cargar_desde_archivo(archivo)

        elif opcion == '8':
            print("👋 Saliendo del sistema.")
            break

        else:
            print("❌ Opción inválida. Intenta de nuevo.")


if __name__ == "__main__":
    main()
