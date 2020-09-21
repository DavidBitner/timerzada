from tkinter import *
from time import *


def horas_entry_callback(event):
    horas_entry.selection_range(0, END)


def minutos_entry_callback(event):
    minutos_entry.selection_range(0, END)


def segundos_entry_callback(event):
    segundos_entry.selection_range(0, END)


# Main
root = Tk()
root.title("Timerzada")
root.geometry("500x500+200+200")

# Frame
frame = LabelFrame(root, padx=5, pady=5)
frame.pack(padx=40, pady=40)

# Titulo do programa
titulo_label = Label(frame, text="TIMERZADA", font=("Helvetica", 20))
titulo_label.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# Campos do timer
horas_entry = Entry(frame, font=("Helvetica", 40), width=2)
minutos_entry = Entry(frame, font=("Helvetica", 40), width=2)
segundos_entry = Entry(frame, font=("Helvetica", 40), width=2)
horas_entry.grid(row=1, column=0, padx=10, pady=3)
minutos_entry.grid(row=1, column=1, padx=10, pady=3)
segundos_entry.grid(row=1, column=2, padx=10, pady=3)
horas_entry.insert(0, "00")
minutos_entry.insert(0, "00")
segundos_entry.insert(0, "00")

# Código para selecionar o que estiver dentro do campo assim que for clickado
horas_entry.bind("<FocusIn>", horas_entry_callback)
minutos_entry.bind("<FocusIn>", minutos_entry_callback)
segundos_entry.bind("<FocusIn>", segundos_entry_callback)

# Labels do timer
horas_label = Label(frame, text="Horas")
minutos_label = Label(frame, text="Minutos")
segundos_label = Label(frame, text="Segundos")
horas_label.grid(row=2, column=0)
minutos_label.grid(row=2, column=1)
segundos_label.grid(row=2, column=2)

# Botões do timer
start_btn = Button(frame, text="START", height=2, width=20)
start_btn.grid(row=3, column=0, columnspan=3, padx=20, pady=20)



root.mainloop()
