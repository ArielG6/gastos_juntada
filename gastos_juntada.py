import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("División de Gastos de Juntada")
        self.root.configure(bg="#214ADB")  # Cambiar el color de fondo de la ventana
        
        self.style = ttk.Style()
        self.style.configure("RoundedButton.TButton", font=("Arial", 12), padding=6, relief="flat", background="#7121DB", foreground="#7121DB") # Cambiar el color de los botones
        self.style.map("RoundedButton.TButton",
                       background=[("active", "#3521DC")],
                       relief=[("pressed", "flat")])

        self.entries = []
        self.create_widgets()
        self.add_entry()  # Añadir el primer campo por defecto
        self.add_entry()  # Añadir el segundo campo por defecto

    def create_widgets(self): # Crear botones y labels
        self.add_button = ttk.Button(self.root, text="Agregar", command=self.add_entry, style="RoundedButton.TButton")
        self.add_button.grid(row=0, column=1, padx=10, pady=10)

        self.submit_button = ttk.Button(self.root, text="Enviar", command=self.submit, style="RoundedButton.TButton")
        self.submit_button.grid(row=0, column=2, padx=10, pady=10)

        self.name_label = tk.Label(self.root, text="Nombre", bg="#214ADB", fg="white", font=("Arial", 12))
        self.name_label.grid(row=1, column=1, padx=10, pady=10)

        self.amount_label = tk.Label(self.root, text="Monto", bg="#214ADB", fg="white", font=("Arial", 12))
        self.amount_label.grid(row=1, column=2, padx=10, pady=10)

        self.result_label = tk.Label(self.root, text="Resultado", bg="#214ADB", fg="white", font=("Arial", 12))
        self.result_label.grid(row=1, column=3, padx=10, pady=10)

    def add_entry(self): # Crear campos de ingreso de datos
        row = len(self.entries) + 2
        name_entry = tk.Entry(self.root, font=("Arial", 12), fg="grey")
        name_entry.insert(0, "Nombre...")
        name_entry.bind("<FocusIn>", lambda event: self.clear_placeholder(event, "Nombre..."))
        name_entry.bind("<FocusOut>", lambda event: self.add_placeholder(event, "Nombre..."))
        name_entry.grid(row=row, column=1, padx=10, pady=5)
        
        amount_entry = tk.Entry(self.root, font=("Arial", 12), fg="grey")
        amount_entry.insert(0, "0")
        amount_entry.bind("<FocusIn>", lambda event: self.clear_placeholder(event, "0"))
        amount_entry.bind("<FocusOut>", lambda event: self.add_placeholder(event, "0"))
        amount_entry.bind("<KeyRelease>", self.validate_number)
        amount_entry.grid(row=row, column=2, padx=10, pady=5)
        
        result_label = tk.Label(self.root, text="", bg="#214ADB", fg="white", font=("Arial", 12))
        result_label.grid(row=row, column=3, padx=10, pady=5)
        
        delete_button = ttk.Button(self.root, text="Eliminar", command=lambda: self.delete_entry(row), style="RoundedButton.TButton")
        delete_button.grid(row=row, column=0, padx=10, pady=5)
        
        self.entries.append((name_entry, amount_entry, result_label, delete_button))
    # Validar datos ingresados
    def clear_placeholder(self, event, placeholder):
        if event.widget.get() == placeholder:
            event.widget.delete(0, tk.END)
            event.widget.config(fg="#7121DB")

    def add_placeholder(self, event, placeholder):
        if event.widget.get() == "":
            event.widget.insert(0, placeholder)
            event.widget.config(fg="grey")

    def validate_number(self, event):
        if not event.widget.get().isdigit():
            event.widget.delete(0, tk.END)
            event.widget.insert(0, "0")

    def delete_entry(self, row):
        for entry in self.entries:
            if entry[3].grid_info()["row"] == row:
                entry[0].grid_forget()
                entry[1].grid_forget()
                entry[2].grid_forget()
                entry[3].grid_forget()
                self.entries.remove(entry)
                break

    def submit(self):   #Calcular gastos
        cant = len(self.entries)
        total = 0.0
        for name_entry, amount_entry, result_label, _ in self.entries:
            total += float(amount_entry.get())
        promedio = total/cant

        for name_entry, amount_entry, result_label, _ in self.entries:
            amount = round(float(amount_entry.get())-promedio,-1)
            result_label.config(text=amount)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
