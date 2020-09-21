# Em construção
from tkinter import *
from time import sleep


# Função para selecionar o texto que estiver dentro da caixa de texto das horas
def horas_entry_callback(event):
    horas_entry.selection_range(0, END)


# Função para selecionar o texto que estiver dentro da caixa de texto dos minutos
def minutos_entry_callback(event):
    minutos_entry.selection_range(0, END)


# Função para selecionar o texto que estiver dentro da caixa de texto dos segundos
def segundos_entry_callback(event):
    segundos_entry.selection_range(0, END)


# Função do timer
def timer():
    global timer_label
    global stop_btn
    horas = int(horas_entry.get())
    minutos = int(minutos_entry.get())
    segundos = int(segundos_entry.get())

    while horas > 0 or minutos > 0 or segundos > 0:
        timer_label.destroy()
        stop_btn.destroy()
        timer_label = Label(root, text=f"{horas} : {minutos} : {segundos}", font=("Helvetica", 40))
        timer_label.pack()
        timer_label.update()
        stop_btn = Button(root, text="STOP", height=2, width=20)
        stop_btn.pack()
        stop_btn.update()
        if segundos > 0:
            segundos -= 1
        elif segundos == 0:
            if minutos > 0:
                minutos -= 1
                segundos = 59
            if minutos == 0:
                if horas > 0:
                    horas -= 1
                    minutos = 59
                    segundos = 59
        sleep(1)


# Main
root = Tk()
root.title("Timerzada")
root.geometry("500x500+200+200")

timer_label = Label(root)
stop_btn = Button(root)

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
start_btn = Button(frame, text="START", height=2, width=20, command=timer)
start_btn.grid(row=3, column=0, columnspan=3, padx=20, pady=20)

root.mainloop()
