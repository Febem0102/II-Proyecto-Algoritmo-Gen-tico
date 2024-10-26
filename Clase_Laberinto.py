import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class Laberinto:
    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.matriz = [[None for _ in range(columnas)] for _ in range(filas)]
        self.items = {
            "azúcar": "azucar.png",
            "vino": "vino.png",
            "veneno": "veneno.png",
            "roca": "roca.png"
        }

    def actualizar_estado(self, fila, columna, item):
        """Actualiza la celda del laberinto con el ítem correspondiente."""
        self.matriz[fila][columna] = item

class InterfazLaberinto:
    def __init__(self, root):
        self.root = root
        self.root.title("Configuración del Laberinto")
        self.laberinto = None
        self.filas = tk.IntVar(value=5)
        self.columnas = tk.IntVar(value=5)

        # Ventana inicial para elegir el tamaño de la matriz
        self.setup_size_selection()

    def setup_size_selection(self):
        """Configura la ventana inicial para seleccionar el tamaño de la matriz."""
        label_filas = ttk.Label(self.root, text="Filas:")
        label_filas.grid(row=0, column=0, padx=5, pady=5)
        spin_filas = ttk.Spinbox(self.root, from_=3, to=10, textvariable=self.filas, width=5)
        spin_filas.grid(row=0, column=1, padx=5, pady=5)

        label_columnas = ttk.Label(self.root, text="Columnas:")
        label_columnas.grid(row=1, column=0, padx=5, pady=5)
        spin_columnas = ttk.Spinbox(self.root, from_=3, to=10, textvariable=self.columnas, width=5)
        spin_columnas.grid(row=1, column=1, padx=5, pady=5)

        btn_crear = ttk.Button(self.root, text="Crear Laberinto", command=self.crear_laberinto)
        btn_crear.grid(row=2, column=0, columnspan=2, pady=10)

    def crear_laberinto(self):
        """Crea el laberinto y abre la ventana principal."""
        self.laberinto = Laberinto(self.filas.get(), self.columnas.get())
        self.mostrar_laberinto()

    def mostrar_laberinto(self):
        """Muestra la interfaz principal del laberinto y sus ítems."""
        for widget in self.root.winfo_children():
            widget.destroy()  # Limpiar la ventana para la interfaz principal

        self.celdas = []
        self.panel_items = tk.Frame(self.root)
        self.panel_items.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

        # Crear el grid del laberinto
        for i in range(self.laberinto.filas):
            fila = []
            for j in range(self.laberinto.columnas):
                celda = tk.Label(self.root, width=4, height=2, relief="solid", borderwidth=1)
                celda.grid(row=i, column=j, padx=1, pady=1)
                celda.bind("<Button-1>", lambda e, x=i, y=j: self.soltar_item(x, y))  # Cambiado a Button-1 para clic
                fila.append(celda)
            self.celdas.append(fila)

        # Cargar las imágenes de los ítems
        self.cargar_imagenes_items()

    def cargar_imagenes_items(self):
        """Carga las imágenes de los ítems en la barra inferior y las configura para arrastrar."""
        self.imagenes = {}
        self.item_actual = None  # Almacena el ítem que se está arrastrando

        for i, (nombre, archivo) in enumerate(self.laberinto.items.items()):
            img = Image.open(archivo).resize((30, 30))  # Ajusta el tamaño de la imagen
            img_tk = ImageTk.PhotoImage(img)
            self.imagenes[nombre] = img_tk

            label = tk.Label(self.panel_items, image=img_tk, text=nombre)
            label.grid(row=0, column=i, padx=5)
            label.bind("<ButtonPress-1>", lambda e, item=nombre: self.iniciar_arrastre(e, item))

    def iniciar_arrastre(self, event, item):
        """Inicia el proceso de arrastre de un ítem."""
        self.item_actual = item  # Guardamos el ítem que se está arrastrando

    def soltar_item(self, fila, columna):
        """Coloca el ítem en la celda seleccionada."""
        if self.item_actual:  # Verifica si hay un ítem arrastrando
            celda = self.celdas[fila][columna]
            img = self.imagenes[self.item_actual]
            celda.config(image=img)
            self.laberinto.actualizar_estado(fila, columna, self.item_actual)
            # No reiniciamos self.item_actual aquí para permitir múltiples arrastres.



