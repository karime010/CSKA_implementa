import tkinter as tk

ventana = tk.Tk()
ventana.title("Cruz Silva Karime Arisbel")
ventana.geometry("400x500")
ventana.configure(bg="pink")

pantalla = tk.Entry(ventana, font=("Arial", 15), borderwidth=3, relief="solid", justify="right")
pantalla.insert(0, "0")         
pantalla.config(state='readonly')
pantalla.pack(padx=10, pady=10, fill="both") 

# FUNCIONES DEL PIZARRÓN

def concatenar(valor):
    pantalla.config(state='normal')
    if pantalla.get() == "0":
        pantalla.delete(0, tk.END)
        pantalla.insert(0, str(valor))
    else:
        pantalla.insert(tk.END, str(valor))
    pantalla.config(state='readonly')

def dar_punto():
    pantalla.config(state='normal')
    if pantalla.get().find(".") == -1:
        pantalla.insert(tk.END, ".")
    pantalla.config(state='readonly')

def limpia_todo():
    pantalla.config(state='normal')
    pantalla.delete(0, tk.END)
    pantalla.insert(0, "0")
    pantalla.config(state='readonly')

def quita():
    pantalla.config(state='normal')
    texto = pantalla.get()
    texto = texto[0:len(texto)-1]
    pantalla.delete(0, tk.END)
    pantalla.insert(0, texto if texto else "0")
    pantalla.config(state='readonly')

def cambia_signo():
    pantalla.config(state='normal')
    ui = float(pantalla.get()) * -1
    pantalla.delete(0, tk.END)
    pantalla.insert(0, str(ui))
    pantalla.config(state='readonly')

def igual():
    pantalla.config(state='normal')
    try:
        resultado = eval(pantalla.get().replace("X", "*"))
        pantalla.delete(0, tk.END)
        pantalla.insert(0, str(resultado))
    except:
        pantalla.delete(0, tk.END)
        pantalla.insert(0, "Error")
    pantalla.config(state='readonly')

# BOTONES

marco_botones = tk.Frame(ventana, bg="white")
marco_botones.pack(padx=10, pady=10)

botones = [
    ("C", 0, 0, limpia_todo),
    ("←", 0, 1, quita),
    ("±", 0, 2, cambia_signo),
    ("/", 0, 3, lambda: concatenar("/")),

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

ventana.mainloop()
