import tkinter as tk
ventana = tk.Tk()
ventana.title("Cruz Silva Karime Arisbel")
ventana.geometry("400x300")
ventana.config(bg="lightpink")
instruccion = tk.Label(ventana, text="Ingresa el número de tu tarjeta:", font=("Arial", 12), bg="white")
instruccion.pack(pady=5)
entrada = tk.Entry(ventana,font=("Arial",14),width=25)
entrada.pack(pady=10)
def verificar():
    num = entrada.get() 
    if not num.isdigit():
        resultado.set("Solo se permiten números")
        return  
    if num.startswith('4') and len(num) in [13, 16]:
        tipo = "Visa"
    elif num.startswith(('51', '52', '53', '54', '55')) and len(num) == 16:
        tipo = "MasterCard"
    elif num.startswith(('34', '37')) and len(num) == 15:
        tipo = "American Express"
    else:
        tipo = "Desconocida"

    
    total = 0
    invertido = num[::-1] 
    for i, digito in enumerate(invertido):
        n = int(digito)
        if i % 2 == 1:  
            n *= 2
            if n > 9:
                n -= 9
        total += n

    
    if total % 10 == 0:
        resultado.set(f"Tarjeta válida - {tipo}")
    else:
        resultado.set("Tarjeta inválida")


boton = tk.Button(ventana, text="Verificar", command=lambda: verificar(), bg="light")
boton.pack(pady=10)
resultado = tk.StringVar()
etiqueta_resultado = tk.Label(ventana, textvariable=resultado, font=("Arial", 12), bg="lightpurple")
etiqueta_resultado.pack()

ventana.mainloop()