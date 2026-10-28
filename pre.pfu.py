import tkinter as tk
from pathlib import Path

FONDO = "#CED7DE"
AZUL = "#17324d"
TEXTO = "#34495e"

ventana = tk.Tk()
ventana.title("Presentación personal")
ventana.geometry("520x720")
ventana.resizable(False, False)
ventana.configure(bg=FONDO)

# Foto en la parte superior, cargada desde la carpeta de este programa.
ruta_imagen = Path(__file__).with_name("loxs.png")
foto = tk.PhotoImage(file=str(ruta_imagen))
foto = foto.subsample(6, 6)

imagen = tk.Label(ventana, image=foto, bg=FONDO)
imagen.pack(pady=(22, 10))

tk.Label(
    ventana,
    text="¡Hola! Mi nombre ",
    font=("Segoe UI", 12),
    fg=TEXTO,
    bg=FONDO,
).pack()

tk.Label(
    ventana,
    text="Luis Angel Llampaz Sullcani",
    font=("Segoe UI", 20, "bold"),
    fg=AZUL,
    bg=FONDO,
    wraplength=460,
).pack(pady=(4, 20))

# Presentamos cada dato en su propia línea.
datos = (
    ("Edad", "22 años"),
    ("Sexo", "Masculino"),
    ("Fecha de nacimiento", "23 de octubre de 2004"),
    ("Habilidades", "Las Extraordinarias"),
)

for etiqueta, valor in datos:
    tk.Label(
        ventana,
        text=f"{etiqueta}: {valor}",
        font=("Segoe UI", 12),
        fg=TEXTO,
        bg=FONDO,
    ).pack(pady=8)

boton = tk.Button(
    ventana,
    text="Cerrar",
    font=("Segoe UI", 10, "bold"),
    fg="white",
    bg=AZUL,
    activebackground="#274c6d",
    activeforeground="white",
    relief="flat",
    padx=22,
    pady=8,
    cursor="hand2",
    command=ventana.destroy,
)
boton.pack(pady=22)

ventana.mainloop()
