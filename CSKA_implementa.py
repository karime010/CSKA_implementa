import tkinter as tk

ventana = tk.Tk()
ventana.title("Cruz Silva Karime Arisbel")
ventana.geometry("400x500")
ventana.configure(bg="pink")

def concatenar(valor):
    pantalla.config(state='normal')
    actual = pantalla.get()
    if actual == "0":
        pantalla.delete(0, tk.END)
        pantalla.insert(0, str(valor))
    else:
        pantalla.insert(tk.END, str(valor))
    pantalla.config(state='readonly')

pantalla = tk.Entry(ventana, font=("Arial", 15), borderwidth=3, relief="solid", justify="right")
pantalla.insert(0, "0")         
pantalla.config(state='readonly')
pantalla.pack(padx=10, pady=10, fill="both") 




marco_botones = tk.Frame(ventana, bg="white")
marco_botones.pack(padx=10, pady=10)

botones = [
    ("7", 0, 0), ("8", 0, 1), ("9", 0, 2), ("/", 0, 3),
    ("4", 1, 0), ("5", 1, 1), ("6", 1, 2), ("-", 1, 3),
    ("1", 2, 0), ("2", 2, 1), ("3", 2, 2), ("+", 2, 3),
    ("0", 3, 0), (".", 3, 1), ("=", 3, 2), ("X", 3, 3),
]

for (texto, fila, col) in botones:
    tk.Button(marco_botones, text=texto, font=("Arial", 13), width=6, height=2,
              bg="white", relief="ridge", 
              command=lambda val=texto: concatenar(val)).grid(row=fila, column=col, padx=5, pady=5)
ventana.mainloop()
