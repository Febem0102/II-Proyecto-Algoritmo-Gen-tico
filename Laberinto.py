import tkinter as tk

# Tamaño de la matriz (personalizable)
MATRIX_SIZE = 33

class Laberinto:
    def __init__(self, window):
        self.window = window
        
        # Crear un frame para contener la cuadrícula
        self.grid_frame = tk.Frame(self.window)
        self.grid_frame.pack()

        # Crear botones que representen las celdas de la matriz
        self.buttons = []
        for i in range(MATRIX_SIZE):
            row = []
            for j in range(MATRIX_SIZE):
                btn = tk.Button(self.grid_frame, text="", width=5, height=2)
                btn.grid(row=i, column=j)  # Colocar el botón en la posición i,j
                row.append(btn)
            self.buttons.append(row)

# Crear la ventana principal
window = tk.Tk()
app = Laberinto(window)
window.mainloop()