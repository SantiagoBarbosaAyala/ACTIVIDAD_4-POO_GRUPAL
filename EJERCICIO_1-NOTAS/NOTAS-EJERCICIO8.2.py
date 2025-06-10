# Para vizualizar la interfaz se debe ejecutar sin depurar (Run Without Debugging) o ejecutar archivo Python (Run Python File) 

import tkinter as tk
from tkinter import messagebox
import math

class Notas:

    def __init__(self):
        self.listaNotas = [0.0] * 5 
    def calcularPromedio(self):
        suma = sum(self.listaNotas)
        return suma / len(self.listaNotas)
    def calcularDesviacion(self):
        prom = self.calcularPromedio()
        suma = 0
        for nota in self.listaNotas:
            suma += (nota - prom) ** 2
        return math.sqrt(suma / len(self.listaNotas))
    def calcularMenor(self):
        return min(self.listaNotas)
    def calcularMayor(self):
        return max(self.listaNotas)

class VentanaPrincipal(tk.Tk):
  
    def __init__(self):
        super().__init__()
        self.title("Ejercicio Notas")
        self.geometry("280x380")
        self.resizable(False, False)
        self.configure(bg="lightgray")

        self.inicio()

    def inicio(self):
    # NOTAS
        self.label_nota1 = tk.Label(self, text="Nota 1:", bg="lightgray", relief="flat", anchor="w")
        self.label_nota1.place(x=20, y=20, width=80, height=23)
        self.campo_nota1 = tk.Entry(self)
        self.campo_nota1.place(x=105, y=20, width=135, height=23)
        self.label_nota2 = tk.Label(self, text="Nota 2:", bg="lightgray", relief="flat", anchor="w")
        self.label_nota2.place(x=20, y=50, width=80, height=23)
        self.campo_nota2 = tk.Entry(self)
        self.campo_nota2.place(x=105, y=50, width=135, height=23)
        self.label_nota3 = tk.Label(self, text="Nota 3:", bg="lightgray", relief="flat", anchor="w")
        self.label_nota3.place(x=20, y=80, width=80, height=23)
        self.campo_nota3 = tk.Entry(self)
        self.campo_nota3.place(x=105, y=80, width=135, height=23)
        self.label_nota4 = tk.Label(self, text="Nota 4:", bg="lightgray", relief="flat", anchor="w")
        self.label_nota4.place(x=20, y=110, width=80, height=23)
        self.campo_nota4 = tk.Entry(self)
        self.campo_nota4.place(x=105, y=110, width=135, height=23)
        self.label_nota5 = tk.Label(self, text="Nota 5:", bg="lightgray", relief="flat", anchor="w")
        self.label_nota5.place(x=20, y=140, width=80, height=23)
        self.campo_nota5 = tk.Entry(self)
        self.campo_nota5.place(x=105, y=140, width=135, height=23)
    # BOTONES
        self.btn_calcular = tk.Button(self, text="Calcular", command=self.calcular, bg="#cbd6e6")
        self.btn_calcular.place(x=20, y=175, width=100, height=23)
        self.btn_limpiar = tk.Button(self, text="Limpiar", command=self.limpiar, bg="#cbd6e6")
        self.btn_limpiar.place(x=125, y=175, width=80, height=23)
    # RESULTADOS
        self.label_promedio = tk.Label(self, text="Promedio = ", bg="lightgray", relief="flat", anchor="w")
        self.label_promedio.place(x=20, y=210, width=220, height=23)
        self.label_desviacion = tk.Label(self, text="Desviación estándar = ", bg="lightgray", relief="flat", anchor="w")
        self.label_desviacion.place(x=20, y=240, width=220, height=23)
        self.label_mayor = tk.Label(self, text="Valor mayor = ", bg="lightgray", relief="flat", anchor="w")
        self.label_mayor.place(x=20, y=270, width=220, height=23)
        self.label_menor = tk.Label(self, text="Valor menor = ", bg="lightgray", relief="flat", anchor="w")
        self.label_menor.place(x=20, y=300, width=220, height=23)

    def calcular(self):
        try:
            notas = Notas()
            notas.listaNotas[0] = float(self.campo_nota1.get())
            notas.listaNotas[1] = float(self.campo_nota2.get())
            notas.listaNotas[2] = float(self.campo_nota3.get())
            notas.listaNotas[3] = float(self.campo_nota4.get())
            notas.listaNotas[4] = float(self.campo_nota5.get())

            promedio = notas.calcularPromedio()
            desviacion = notas.calcularDesviacion()
            mayor = notas.calcularMayor()
            menor = notas.calcularMenor()

            self.label_promedio.config(text=f"Promedio = {promedio:.2f}")
            self.label_desviacion.config(text=f"Desviación estándar = {desviacion:.2f}")
            self.label_mayor.config(text=f"Valor mayor = {mayor:.1f}")
            self.label_menor.config(text=f"Valor menor = {menor:.1f}")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores numéricos en todos los espacios de notas.")

    def limpiar(self):
        self.campo_nota1.delete(0, tk.END)
        self.campo_nota2.delete(0, tk.END)
        self.campo_nota3.delete(0, tk.END)
        self.campo_nota4.delete(0, tk.END)
        self.campo_nota5.delete(0, tk.END)
        self.label_promedio.config(text="Promedio = ")
        self.label_desviacion.config(text="Desviación estándar = ")
        self.label_mayor.config(text="Valor mayor = ")
        self.label_menor.config(text="Valor menor = ")

if __name__ == "__main__":
    app = VentanaPrincipal()
    app.mainloop()