# --------------------------------------------
# Sistema de Gestión de Biblioteca Digital v2
# --------------------------------------------

class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.detalles = (titulo, autor)  # Tupla inmutable
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        titulo, autor = self.detalles
        return f"{titulo} por {autor} | Categoría: {self.categoria} | ISBN: {self.isbn}"


class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.prestamos = []

    def __str__(self):
        return f"{self.nombre} (ID: {self.id_usuario})"


class Biblioteca:
    def __init__(self):
        self.catalogo = {}          # ISBN -> Libro
        self.usuarios = {}          # ID -> Usuario
        self.ids_registrados = set()

    # -----------------------------
    # Métodos de administración
    # -----------------------------

    def añadir_libro(self, libro):
        if libro.isbn in self.catalogo:
            print("⚠️ Este libro ya está registrado.")
        else:
            self.catalogo[libro.isbn] = libro
            print(f"✅ Libro añadido: {libro}")

    def eliminar_libro(self, isbn):
        if isbn in self.catalogo:
            eliminado = self.catalogo.pop(isbn)
            print(f"🗑️ Libro eliminado: {eliminado}")
        else:
            print("❌ No se encontró el libro con ese ISBN.")

    def registrar_usuario(self, usuario):
        if usuario.id_usuario in self.ids_registrados:
            print("⚠️ Este ID de usuario ya está registrado.")
        else:
            self.usuarios[usuario.id_usuario] = usuario
            self.ids_registrados.add(usuario.id_usuario)
            print(f"✅ Usuario registrado: {usuario}")

    def eliminar_usuario(self, id_usuario):
        if id_usuario in self.ids_registrados:
            eliminado = self.usuarios.pop(id_usuario)
            self.ids_registrados.remove(id_usuario)
            print(f"🗑️ Usuario eliminado: {eliminado}")
        else:
            print("❌ Usuario no encontrado.")

    # -----------------------------
    # Funciones de préstamo
    # -----------------------------

    def prestar(self, id_usuario, isbn):
        if id_usuario not in self.usuarios:
            print("❌ Usuario no registrado.")
            return
        if isbn not in self.catalogo:
            print("❌ Libro no disponible para préstamo.")
            return

        libro = self.catalogo.pop(isbn)
        self.usuarios[id_usuario].prestamos.append(libro)
        print(f"📚 '{libro.detalles[0]}' prestado a {self.usuarios[id_usuario].nombre}.")

    def devolver(self, id_usuario, isbn):
        usuario = self.usuarios.get(id_usuario)
        if not usuario:
            print("❌ Usuario no registrado.")
            return

        for libro in usuario.prestamos:
            if libro.isbn == isbn:
                usuario.prestamos.remove(libro)
                self.catalogo[isbn] = libro
                print(f"✅ Libro devuelto: {libro}")
                return

        print("❌ Este libro no está prestado a este usuario.")

    # -----------------------------
    # Funciones de consulta
    # -----------------------------

    def buscar(self, titulo=None, autor=None, categoria=None):
        resultados = []
        for libro in self.catalogo.values():
            t, a = libro.detalles
            if (
                (titulo and titulo.lower() in t.lower()) or
                (autor and autor.lower() in a.lower()) or
                (categoria and categoria.lower() == libro.categoria.lower())
            ):
                resultados.append(libro)

        if resultados:
            print("🔍 Resultados encontrados:")
            for libro in resultados:
                print(" -", libro)
        else:
            print("❌ No se encontraron coincidencias.")

    def mostrar_prestamos_usuario(self, id_usuario):
        usuario = self.usuarios.get(id_usuario)
        if not usuario:
            print("❌ Usuario no encontrado.")
            return

        if not usuario.prestamos:
            print(f"ℹ️ {usuario.nombre} no tiene libros prestados.")
        else:
            print(f"📚 Libros prestados a {usuario.nombre}:")
            for libro in usuario.prestamos:
                print(" -", libro)


# --------------------------------------------
# PRUEBA DEL SISTEMA
# --------------------------------------------

if __name__ == "__main__":
    biblioteca = Biblioteca()

    # Crear libros
    l1 = Libro("El Principito", "Antoine de Saint-Exupéry", "Fábula", "0001")
    l2 = Libro("Don Quijote", "Miguel de Cervantes", "Novela", "0002")
    l3 = Libro("Curso de Python", "Laura Tech", "Educativo", "0003")

    # Añadir libros
    biblioteca.añadir_libro(l1)
    biblioteca.añadir_libro(l2)
    biblioteca.añadir_libro(l3)

    print("\n--------------------------\n")

    # Crear y registrar usuarios
    u1 = Usuario("María", "U100")
    u2 = Usuario("Pedro", "U200")

    biblioteca.registrar_usuario(u1)
    biblioteca.registrar_usuario(u2)

    print("\n--------------------------\n")

    # Préstamos
    biblioteca.prestar("U100", "0001")  # María toma El Principito
    biblioteca.prestar("U200", "0002")  # Pedro toma Don Quijote

    print("\n--------------------------\n")

    # Consultar préstamos
    biblioteca.mostrar_prestamos_usuario("U100")
    biblioteca.mostrar_prestamos_usuario("U200")

    print("\n--------------------------\n")

    # Buscar por autor y categoría
    biblioteca.buscar(autor="Laura")
    biblioteca.buscar(categoria="Educativo")

    print("\n--------------------------\n")

    # Devolver libro
    biblioteca.devolver("U100", "0001")

    print("\n--------------------------\n")

    # Eliminar usuario y libro
    biblioteca.eliminar_usuario("U200")
    biblioteca.eliminar_libro("0003")

    print("\n✅ Fin del sistema de prueba")
