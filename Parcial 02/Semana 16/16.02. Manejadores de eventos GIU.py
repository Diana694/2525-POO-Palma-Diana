import tkinter as tk
from tkinter import messagebox

class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas")
        self.root.geometry("400x400")
        self.root.configure(bg="#f0f0f0")

        # Campo de entrada
        self.task_entry = tk.Entry(root, width=30, font=("Arial", 12))
        self.task_entry.pack(pady=10)
        self.task_entry.focus()

        # Botones
        btn_frame = tk.Frame(root, bg="#f0f0f0")
        btn_frame.pack()

        self.add_btn = tk.Button(btn_frame, text="Añadir Tarea", command=self.add_task)
        self.add_btn.grid(row=0, column=0, padx=5)

        self.complete_btn = tk.Button(btn_frame, text="Marcar como Completada", command=self.complete_task)
        self.complete_btn.grid(row=0, column=1, padx=5)

        self.delete_btn = tk.Button(btn_frame, text="Eliminar Tarea", command=self.delete_task)
        self.delete_btn.grid(row=0, column=2, padx=5)

        # Lista de tareas
        self.task_listbox = tk.Listbox(root, width=50, height=15, selectmode=tk.SINGLE, font=("Arial", 11))
        self.task_listbox.pack(pady=10)

        # Diccionario para seguimiento del estado de tareas
        self.tasks = {}

        # Vinculación de atajos
        self.root.bind("<Return>", lambda event: self.add_task())
        self.root.bind("<c>", lambda event: self.complete_task())
        self.root.bind("<d>", lambda event: self.delete_task())
        self.root.bind("<Delete>", lambda event: self.delete_task())
        self.root.bind("<Escape>", lambda event: self.root.quit())

    def add_task(self):
        task_text = self.task_entry.get().strip()
        if task_text:
            if task_text not in self.tasks:
                self.tasks[task_text] = False  # False = pendiente
                self.task_listbox.insert(tk.END, task_text)
                self.task_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Duplicado", "La tarea ya existe.")
        else:
            messagebox.showwarning("Entrada vacía", "Por favor escribe una tarea.")

    def complete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            task_text = self.task_listbox.get(selected_index)

            if not self.tasks[task_text]:
                self.tasks[task_text] = True
                self.task_listbox.delete(selected_index)
                self.task_listbox.insert(selected_index, task_text + " ✔️")
            else:
                messagebox.showinfo("Información", "La tarea ya está completada.")
        except IndexError:
            messagebox.showwarning("Ninguna tarea seleccionada", "Selecciona una tarea para completarla.")

    def delete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            task_text = self.task_listbox.get(selected_index).replace(" ✔️", "")
            del self.tasks[task_text]
            self.task_listbox.delete(selected_index)
        except IndexError:
            messagebox.showwarning("Ninguna tarea seleccionada", "Selecciona una tarea para eliminarla.")

# Ejecutar la app
if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()
