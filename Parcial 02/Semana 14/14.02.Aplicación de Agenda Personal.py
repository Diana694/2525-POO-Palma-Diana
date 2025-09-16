import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
from datetime import datetime

class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")
        self.root.geometry("600x400")
        self.root.resizable(False, False)

        # ----- Frame superior (visualización de eventos) -----
        frame_eventos = tk.Frame(self.root)
        frame_eventos.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        self.tree = ttk.Treeview(frame_eventos, columns=("Fecha", "Hora", "Descripción"), show="headings", height=10)
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.column("Fecha", width=100, anchor="center")
        self.tree.column("Hora", width=80, anchor="center")
        self.tree.column("Descripción", width=380, anchor="w")
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = ttk.Scrollbar(frame_eventos, orient="vertical", command=self.tree.yview)
        scrollbar.pack(side=tk.RIGHT, fill="y")
        self.tree.configure(yscrollcommand=scrollbar.set)

        # ----- Frame central (entrada de datos) -----
        frame_entrada = tk.Frame(self.root)
        frame_entrada.pack(pady=5)

        tk.Label(frame_entrada, text="Fecha:").grid(row=0, column=0, padx=5, pady=5)
        self.entry_fecha = DateEntry(frame_entrada, date_pattern='yyyy-mm-dd', width=12)
        self.entry_fecha.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame_entrada, text="Hora (HH:MM):").grid(row=0, column=2, padx=5, pady=5)
        self.entry_hora = tk.Entry(frame_entrada, width=10)
        self.entry_hora.grid(row=0, column=3, padx=5, pady=5)

        tk.Label(frame_entrada, text="Descripción:").grid(row=1, column=0, padx=5, pady=5)
        self.entry_descripcion = tk.Entry(frame_entrada, width=50)
        self.entry_descripcion.grid(row=1, column=1, columnspan=3, padx=5, pady=5)

        # ----- Frame inferior (botones) -----
        frame_botones = tk.Frame(self.root)
        frame_botones.pack(pady=10)

        btn_agregar = tk.Button(frame_botones, text="Agregar Evento", command=self.agregar_evento, bg="#dff0d8")
        btn_agregar.grid(row=0, column=0, padx=10)

        btn_eliminar = tk.Button(frame_botones, text="Eliminar Evento Seleccionado", command=self.eliminar_evento, bg="#f2dede")
        btn_eliminar.grid(row=0, column=1, padx=10)

        btn_salir = tk.Button(frame_botones, text="Salir", command=self.root.quit, bg="#d9edf7")
        btn_salir.grid(row=0, column=2, padx=10)

    def agregar_evento(self):
        fecha = self.entry_fecha.get()
        hora = self.entry_hora.get().strip()
        descripcion = self.entry_descripcion.get().strip()

        if not (hora and descripcion):
            messagebox.showwarning("Campos incompletos", "Por favor, completa todos los campos.")
            return

        try:
            datetime.strptime(hora, "%H:%M")  # Validación de formato de hora
        except ValueError:
            messagebox.showerror("Formato de hora incorrecto", "Por favor, usa el formato HH:MM (24 horas).")
            return

        self.tree.insert("", "end", values=(fecha, hora, descripcion))
        self.entry_hora.delete(0, tk.END)
        self.entry_descripcion.delete(0, tk.END)

    def eliminar_evento(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showinfo("Selecciona un evento", "Debes seleccionar un evento para eliminarlo.")
            return

        confirm = messagebox.askyesno("Confirmar eliminación", "¿Estás seguro de que deseas eliminar el evento seleccionado?")
        if confirm:
            self.tree.delete(selected_item)

# ----- Ejecutar la aplicación -----
if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()

