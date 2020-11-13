# Em construção
from tkinter import Entry 
from tkinter import Label
from tkinter import LabelFrame
from tkinter import Tk
from tkinter import Button
from tkinter import END
from tkinter import Radiobutton
from tkinter import W, E, IntVar


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
    global agora_label
    global despertar_label
    global stop_btn

    # Imports para o alarme
    from datetime import datetime, timedelta
    from os import system
    import pygame

    # Função do botão stop
    def stop():
        if opcao == 1:
            pygame.mixer.music.stop()
            stop_btn.destroy()
            agora_label.destroy()
            despertar_label.destroy()

    # Variaveis para o timer funcionar
    base = datetime.now()
    agora = base.strftime("%H:%M:%S")
    horas = int(horas_entry.get())
    minutos = int(minutos_entry.get())
    segundos = int(segundos_entry.get())
    tempo_adicionado = timedelta(hours=horas, minutes=minutos, seconds=segundos)
    base2 = base + tempo_adicionado
    tempo_despertar = base2.strftime("%H:%M:%S")

    # Declaração das labels do timer
    agora_label.destroy()
    despertar_label.destroy()
    agora_label = Label(frame, text=agora, font=("Helvetica", 15))
    despertar_label = Label(frame, text=tempo_despertar, font=("Helvetica", 15))

    # Posicionamento das labels do timer
    agora_label.grid(row=5, column=0, columnspan=3)
    despertar_label.grid(row=6, column=0, columnspan=3)

    # Função para o alarme funcionar
    while base < base2:
        base = datetime.now()
        agora = base.strftime("%H:%M:%S")
        agora_label.grid_forget()
        agora_label = Label(frame, text=agora, font=("Helvetica", 15))
        agora_label.grid(row=5, column=0, columnspan=3)
        agora_label.update()

    # Código para tocar o alarme
    if base >= base2:
        # Botão para parar o alarme
        stop_btn.destroy()
        stop_btn = Button(frame, text="STOP", height=2, width=20, command=stop)
        stop_btn.grid(row=4, column=0, columnspan=3, padx=20, pady=20)
        opcao = v.get()

        if opcao == 1:
            mp3 = "toques/Feint - The Things Weve Seen.mp3"
            pygame.mixer.init()
            pygame.mixer.music.load(mp3)
            pygame.mixer.music.play()
        elif opcao == 2:
            system("shutdown /s /t 1")
        elif opcao == 3:
            pass


# Main
root = Tk()
root.title("Timerzada")
root.geometry("500x500+200+200")

# Frame
frame = LabelFrame(root, padx=5, pady=5)
frame.pack(padx=40, pady=40)

# Declaração das labels para uso depois de ativar o timer
agora_label = Label(frame)
despertar_label = Label(frame)
stop_btn = Button(frame)

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

# Opções do timer
v = IntVar()
radio1 = Radiobutton(frame, text="Despertar", variable=v, value=1, anchor=W)
radio2 = Radiobutton(frame, text="Desligar", variable=v, value=2, anchor=W)
radio3 = Radiobutton(frame, text="Placeholder", variable=v, value=3, anchor=W)
radio1.grid(row=3, column=0, sticky=W + E)
radio2.grid(row=3, column=1, sticky=W + E)
radio3.grid(row=3, column=2, sticky=W + E)

# Botões do timer
start_btn = Button(frame, text="START", height=2, width=20, command=timer)
start_btn.grid(row=4, column=0, columnspan=3, padx=20, pady=20)

root.mainloop()
