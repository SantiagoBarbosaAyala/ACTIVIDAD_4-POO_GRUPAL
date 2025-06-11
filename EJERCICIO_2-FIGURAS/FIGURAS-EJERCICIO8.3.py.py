import math
import tkinter as tk
from tkinter import ttk

# --- Clases de Modelo ---
class Figura:
    def volumen(self):
        raise NotImplementedError
    def superficie(self):
        raise NotImplementedError

class Cilindro(Figura):
    def __init__(self, r, h):
        self.r, self.h = r, h
    def volumen(self):
        return math.pi * self.r**2 * self.h
    def superficie(self):
        return 2*math.pi*self.r**2 + 2*math.pi*self.r*self.h

class Esfera(Figura):
    def __init__(self, r):
        self.r = r
    def volumen(self):
        return 4/3 * math.pi * self.r**3
    def superficie(self):
        return 4 * math.pi * self.r**2

class Piramide(Figura):
    def __init__(self, b, h, a):
        self.b, self.h, self.a = b, h, a
    def volumen(self):
        return (self.b**2 * self.h) / 3
    def superficie(self):
        return self.b**2 + (4*self.b*self.a)/2

# --- Función para abrir cada ventana de cálculo ---
def abrir_ventana(tipo):
    win = tk.Toplevel(root)
    win.title(tipo)
    win.resizable(False, False)
    
    # Creamos una lista de "Entry" según el tipo
    entradas = []
    if tipo == "Cilindro":
        labels = ["Radio (cms):", "Altura (cms):"]
    elif tipo == "Esfera":
        labels = ["Radio (cms):"]
    elif tipo == "Pirámide":
        labels = ["Base (cms):", "Altura (cms):", "Apotema (cms):"]
    else:
        return
    
    # Colocamos los labels y las entradas
    for i, texto in enumerate(labels):
        tk.Label(win, text=texto).grid(row=i, column=0, sticky="e", padx=5, pady=5)
        e = ttk.Entry(win)
        e.grid(row=i, column=1, padx=5, pady=5)
        entradas.append(e)
    
    # Labels de resultado (iniciales en guión)
    lbl_vol = tk.Label(win, text="Volumen (cm³): —")
    lbl_vol.grid(row=len(labels)+1, column=0, columnspan=2, sticky="w", padx=5, pady=(10,0))
    lbl_sup = tk.Label(win, text="Superficie (cm²): —")
    lbl_sup.grid(row=len(labels)+2, column=0, columnspan=2, sticky="w", padx=5, pady=(2,10))
    
    # Botón de calcular
    ttk.Button(
        win,
        text="Calcular",
        width=20,
        command=lambda: calcular(tipo, entradas, lbl_vol, lbl_sup)
    ).grid(row=len(labels), column=0, columnspan=2, pady=(10,5))

# --- Función que hace el cálculo genérico ---
def calcular(tipo, entradas, lbl_vol, lbl_sup):
    try:
        vals = [float(e.get()) for e in entradas]
        if tipo == "Cilindro":
            fig = Cilindro(*vals)
        elif tipo == "Esfera":
            fig = Esfera(*vals)
        elif tipo == "Pirámide":
            fig = Piramide(*vals)
        else:
            return
        v = fig.volumen()
        s = fig.superficie()
        lbl_vol.config(text=f"Volumen (cm³): {v:.2f}")
        lbl_sup.config(text=f"Superficie (cm²): {s:.2f}")
    except ValueError:
        lbl_vol.config(text="Volumen (cm³): ¡Error en los datos!")
        lbl_sup.config(text="Superficie (cm²): ¡Error en los datos!")

# --- Ventana Principal ---
root = tk.Tk()
root.title("Figuras")
root.resizable(False, False)

frame = ttk.Frame(root, padding=10)
frame.pack()

ttk.Button(frame, text="Cilindro",  width=15,
           command=lambda: abrir_ventana("Cilindro"))\
    .grid(row=0, column=0, padx=5)
ttk.Button(frame, text="Esfera",    width=15,
           command=lambda: abrir_ventana("Esfera"))\
    .grid(row=0, column=1, padx=5)
ttk.Button(frame, text="Pirámide",  width=15,
           command=lambda: abrir_ventana("Pirámide"))\
    .grid(row=0, column=2, padx=5)

root.mainloop()
