import tkinter as tk
import random

class JuegoAdivinar:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.config(width=300, height=300)
        self.ventana.title("Juego Adivinar Número")
        self.ventana.resizable(0, 0)

        self.numero_secreto = random.randint(1, 100)
        self.intentos = 0

        # Widgets
        self.lblTitulo1 = tk.Label(self.ventana, text="Adivina un Número", font=('Arial', 20))
        self.lblTitulo1.place(x=30, y=20)

        self.lblTitulo2 = tk.Label(self.ventana, text="Introduce un número:", font='Arial')
        self.lblTitulo2.place(x=30, y=90)

        self.txtTitulo2 = tk.Entry(self.ventana)
        self.txtTitulo2.place(x=180, y=92, width=50)

        self.btnBoton = tk.Button(self.ventana, text="Adivinar", command=self.adivinar)
        self.btnBoton.place(x=110, y=140)

        self.label_resultado = tk.Label(self.ventana, text="", fg="blue")
        self.label_resultado.place(x=30, y=200)

        self.boton_reiniciar = tk.Button(self.ventana, text="Reiniciar juego", command=self.reiniciar, state=tk.DISABLED)
        self.boton_reiniciar.place(x=100, y=240)

        self.ventana.mainloop()

    def adivinar(self):
        try:
            numero = int(self.txtTitulo2.get())
        except ValueError:
            self.label_resultado.config(text="Por favor, ingresa un número válido.")
            return

        self.intentos += 1

        if numero < self.numero_secreto:
            self.label_resultado.config(text="El número es mayor. Intenta de nuevo.")
        elif numero > self.numero_secreto:
            self.label_resultado.config(text="El número es menor. Intenta de nuevo.")
        else:
            self.label_resultado.config(text=f"¡Felicidades! Adivinaste en {self.intentos} intentos.")
            self.btnBoton.config(state=tk.DISABLED)
            self.boton_reiniciar.config(state=tk.NORMAL)

        self.txtTitulo2.delete(0, tk.END)

    def reiniciar(self):
        self.numero_secreto = random.randint(1, 100)
        self.intentos = 0
        self.label_resultado.config(text="")
        self.txtTitulo2.delete(0, tk.END)
        self.btnBoton.config(state=tk.NORMAL)
        self.boton_reiniciar.config(state=tk.DISABLED)


