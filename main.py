from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox

def convert():
    sens1 = float(sens1_tf.get())
    dpi1 = int(dpi1_tf.get())
    dpi2 = int(dpi2_tf.get())
    game1 = game1_cb.get()
    game2 = game2_cb.get()
    sens2 = sens1 * dpi1 / dpi2
    if game1 == "CS:GO" and game2 == "VALORANT" :
        sens2 = sens1 / 3.18  * dpi1 / dpi2
        sens2 = round(sens2, 2)
        if sens2 :
            messagebox.showinfo('Sensetivity Converter', f'Ваша сенса {sens2} в игре {game2}')
    elif game1 == "VALORANT" and game2 == "CS:GO" :
        sens2 = sens1 * 3.18  * dpi1 / dpi2
        sens2 = round(sens2, 2)
        if sens2 :
            messagebox.showinfo('Sensetivity Converter', f'Ваша сенса {sens2} в игре {game2}')
    elif game1 == "OVERWATCH 2" and game2 == "VALORANT" :
        sens2 = sens1 / 10.6  * dpi1 / dpi2
        sens2 = round(sens2, 2)
        if sens2 :
            messagebox.showinfo('Sensetivity Converter', f'Ваша сенса {sens2} в игре {game2}')
    elif game1 == "VALORANT" and game2 == "OVERWATCH 2" :
        sens2 = sens1 * 10.6  * dpi1 / dpi2
        sens2 = round(sens2, 2)
        if sens2 :
            messagebox.showinfo('Sensetivity Converter', f'Ваша сенса {sens2} в игре {game2}')
    elif game1 == "CS:GO" and game2 == "OVERWATCH 2" :
        sens2 = sens1 / 3.33  * dpi1 / dpi2
        sens2 = round(sens2, 2)
        if sens2 :
            messagebox.showinfo('Sensetivity Converter', f'Ваша сенса {sens2} в игре {game2}')
    elif game1 == "OVERWATCH 2" and game2 == "CS:GO" :
        sens2 = sens1 * 3.33  * dpi1 / dpi2
        sens2 = round(sens2, 2)
        if sens2 :
            messagebox.showinfo('Sensetivity Converter', f'Ваша сенса {sens2} в игре {game2}')
    else:
        sens2 = sens1 * dpi1 / dpi2
        sens2 = round(sens2, 2)
        if sens2:
            messagebox.showinfo('Sensetivity Converter', f'Ваша сенса {sens2} в игре {game2}')

window = Tk()
window.title('CS:GO/VALORANT Sensitivity Converter')
window.geometry('500x350')
frame = Frame(
    window,
    padx=10,
    pady=10
)
frame.pack(expand=True)

game1_lb = Label(
    frame,
    text="Выберите игру с которой хотите сконвертировать"
)
game1_lb.grid(row=2, column=1)

game2_lb = Label(
    frame,
    text="Выберите игру в которую хотите сконвертировать"
)
game2_lb.grid(row=6, column=1)

sens1_lb = Label(
    frame,
    text="Введите вашу старую сенсу"
)
sens1_lb.grid(row=3, column=1)

dpi1_lb = Label(
    frame,
    text="Введите ваш старый dpi",
)
dpi1_lb.grid(row=4, column=1)

dpi2_lb = Label(
    frame,
    text="Введите ваш новый dpi",
)
dpi2_lb.grid(row=5, column=1)

sens1_tf = Entry(
    frame,
)
sens1_tf.grid(row=3, column=2, pady=5)

dpi1_tf = Entry(
    frame,
)
dpi1_tf.grid(row=4, column=2, pady=5)

dpi2_tf = Entry(
    frame,
)
dpi2_tf.grid(row=5, column=2, pady=5)

game1_cb = Combobox(
    frame,
    values=["CS:GO", "VALORANT", "OVERWATCH 2"]
)
game1_cb.grid(row=2, column=2, pady=5)

game2_cb = Combobox(
    frame,
    values=["CS:GO", "VALORANT", "OVERWATCH 2"]
)
game2_cb.grid(row=6, column=2, pady=5)

con_btn = Button(
    frame,
    text='Рассчитать чувствительность',
    command=convert
)
con_btn.grid(row=7, column=2)

window.mainloop()