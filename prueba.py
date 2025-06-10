import tkinter as tk

# Crear ventana
ventana = tk.Tk()
ventana.title("Cruz Silva Karime Arisbel")
ventana.geometry("400x500")
ventana.configure(bg="pink")

# Variable para mostrar la expresión arriba
expresion = tk.StringVar()
expresion.set("")

# Etiqueta para mostrar la expresión
label_expr = tk.Label(ventana, textvariable=expresion, anchor="e",
                      font=("Arial", 12), bg="pink", fg="gray")
label_expr.pack(padx=10, pady=(10, 0), fill="both")

# Pantalla principal para el resultado
pantalla = tk.Entry(ventana, font=("Arial", 15), borderwidth=3,
                    relief="solid", justify="right")
pantalla.insert(0, "0")
pantalla.config(state='readonly')
pantalla.pack(padx=10, pady=5, fill="both")

# FUNCIONES

def concatenar(valor):
    pantalla.config(state='normal')
    if pantalla.get() == "0":
        pantalla.delete(0, tk.END)
        pantalla.insert(0, str(valor))
    else:
        pantalla.insert(tk.END, str(valor))
    expresion.set(expresion.get() + str(valor))  # actualiza lo de arriba
    pantalla.config(state='readonly')

def dar_punto():
    pantalla.config(state='normal')
    if "." not in pantalla.get():
        pantalla.insert(tk.END, ".")
        expresion.set(expresion.get() + ".")
    pantalla.config(state='readonly')

def limpia_todo():
    pantalla.config(state='normal')
    pantalla.delete(0, tk.END)
    pantalla.insert(0, "0")
    pantalla.config(state='readonly')
    expresion.set("")  # limpia también la expresión de arriba

def quita():
    pantalla.config(state='normal')
    texto = pantalla.get()
    if len(texto) > 1:
        texto = texto[:-1]
    else:
        texto = "0"
    pantalla.delete(0, tk.END)
    pantalla.insert(0, texto)
    pantalla.config(state='readonly')

    # También borrar en la expresión de arriba
    expr = expresion.get()
    if expr:
        expresion.set(expr[:-1])

def igual():
    pantalla.config(state='normal')
    try:
        resultado = eval(expresion.get().replace("X", "*"))
        pantalla.delete(0, tk.END)
        pantalla.insert(0, str(resultado))
        expresion.set("")  # limpia la expresión después
    except:
        pantalla.delete(0, tk.END)
        pantalla.insert(0, "Error")
        expresion.set("")
    pantalla.config(state='readonly')

# MARCO PARA LOS BOTONES
marco_botones = tk.Frame(ventana, bg="white")
marco_botones.pack(padx=10, pady=10)

# Lista de botones (ya sin el ±)
botones = [
    ("C", 0, 0, limpia_todo),
    ("←", 0, 1, quita),
    ("/", 0, 2, lambda: concatenar("/")),

    ("7", 1, 0, lambda: concatenar("7")),
    ("8", 1, 1, lambda: concatenar("8")),
    ("9", 1, 2, lambda: concatenar("9")),
    ("X", 1, 3, lambda: concatenar("X")),

    ("4", 2, 0, lambda: concatenar("4")),
    ("5", 2, 1, lambda: concatenar("5")),
    ("6", 2, 2, lambda: concatenar("6")),
    ("-", 2, 3, lambda: concatenar("-")),

    ("1", 3, 0, lambda: concatenar("1")),
    ("2", 3, 1, lambda: concatenar("2")),
    ("3", 3, 2, lambda: concatenar("3")),
    ("+", 3, 3, lambda: concatenar("+")),

    ("0", 4, 0, lambda: concatenar("0")),
    (".", 4, 1, dar_punto),
    ("=", 4, 2, igual),
]

# Crear los botones
for texto, fila, columna, comando in botones:
    tk.Button(marco_botones, text=texto, font=("Arial", 13), width=6, height=2,
              bg="white", relief="ridge", command=comando).grid(row=fila, column=columna, padx=5, pady=5)

# Ejecutar ventana
ventana.mainloop()
