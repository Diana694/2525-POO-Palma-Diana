import tkinter as tk
from tkinter import messagebox

class ListaDeTareasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas")

        # Lista para almacenar tareas y su estado
        self.tareas = []

        # ------------------ INTERFAZ ------------------ #

        # Campo de entrada para nuevas tareas
        self.entry_tarea = tk.Entry(root, width=40)
        self.entry_tarea.grid(row=0, column=0, padx=10, pady=10)
        self.entry_tarea.bind("<Return>", self.agregar_tarea_evento)

        # Botón para añadir tarea
        self.btn_agregar = tk.Button(root, text="Añadir Tarea", command=self.agregar_tarea)
        self.btn_agregar.grid(row=0, column=1, padx=10)

        # Listbox para mostrar las tareas
        self.listbox_tareas = tk.Listbox(root, width=50, height=10, selectmode=tk.SINGLE)
        self.listbox_tareas.grid(row=1, column=0, columnspan=2, padx=10)

        # Botón para marcar como completada
        self.btn_completar = tk.Button(root, text="Marcar como Completada", command=self.marcar_completada)
        self.btn_completar.grid(row=2, column=0, pady=10)

        # Botón para eliminar tarea
        self.btn_eliminar = tk.Button(root, text="Eliminar Tarea", command=self.eliminar_tarea)
        self.btn_eliminar.grid(row=2, column=1, pady=10)

        # Doble clic para marcar como completada
        self.listbox_tareas.bind("<Double-Button-1>", self.marcar_completada_evento)

    # ------------------ FUNCIONES ------------------ #

    def agregar_tarea_evento(self, event):
        self.agregar_tarea()

    def agregar_tarea(self):
        texto = self.entry_tarea.get().strip()
        if texto == "":
            messagebox.showwarning("Campo vacío", "Por favor, escribe una tarea.")
            return
        self.tareas.append({"texto": texto, "completada": False})
        self.actualizar_listbox()
        self.entry_tarea.delete(0, tk.END)

    def marcar_completada(self):
        seleccion = self.listbox_tareas.curselection()
        if not seleccion:
            messagebox.showinfo("Selecciona una tarea", "Selecciona una tarea para marcar como completada.")
            return
        index = seleccion[0]
        self.tareas[index]["completada"] = not self.tareas[index]["completada"]
        self.actualizar_listbox()

    def marcar_completada_evento(self, event):
        self.marcar_completada()

    def eliminar_tarea(self):
        seleccion = self.listbox_tareas.curselection()
        if not seleccion:
            messagebox.showinfo("Selecciona una tarea", "Selecciona una tarea para eliminar.")
            return
        index = seleccion[0]
        del self.tareas[index]
        self.actualizar_listbox()

    def actualizar_listbox(self):
        self.listbox_tareas.delete(0, tk.END)
        for tarea in self.tareas:
            texto = tarea["texto"]
            if tarea["completada"]:
                texto = f"[✔] {texto}"
            self.listbox_tareas.insert(tk.END, texto)

# ------------------ EJECUCIÓN ------------------ #

if __name__ == "__main__":
    root = tk.Tk()
    app = ListaDeTareasApp(root)
    root.mainloop()
