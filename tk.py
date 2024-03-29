import random
import os
from tkinter import *
from tkinter import ttk
from time import sleep




root= Tk()
root['bg'] = '#ffcf94'
root.title('Магический шар')
root.geometry("1200x900")
root.resizable(width=False, height=False)
root

#Картинка с надписью
canvas = Canvas(root, width=300, height=300)
background_image = PhotoImage(file="shar.png")
canvas.create_image( 0, 0, anchor='nw', image=background_image )
canvas.config(borderwidth=5, relief="solid", highlightbackground='purple')
canvas.create_text(150,290,text='Магический шар', fill='#A60DFC', font=('Arial', 15))
canvas.pack()



# Текст
label = Label(text=f"Привет, {os.getlogin()}. Ты можешь задать мне любой вопрос на который я могу ответить либо да либо нет", )
label.config(borderwidth=2, background='#ffcf94', font=('TimesNewRoman', 15), padx=3, pady=3  )
label.place(relx=0.5, rely=0.4, anchor='center')







#Кнопка
answers=["Бесспорно", "Предрешено", "Никаких сомнений", "Определённо да","Можешь быть уверен в этом", "Мне кажется - да", "Вероятнее всего", "Хорошие перспективы", "Знаки говорят - да", "Да", "Пока неясно, попробуй снова", "Спроси позже", "Лучше не рассказывать", "Сейчас нельзя предсказать", "Сконцентрируйся и спроси опять", "Даже не думай", "Мой ответ - нет", "По моим данным - нет", "Перспективы не очень хорошие"]

def click_button():
    global otvetik
    otvet=random.choice(answers)
    #otvetik["text"]=gif
    sleep(1)
    # изменяем текст на кнопке
    otvetik["text"] = otvet 

Button = ttk.Button(text='Получить ответ', command=click_button)
Button.place(relx=0.5, rely=0.5, anchor='center',   )

#Поле вывода
#gif = Image("loading.gif")
otvetik = Label(text='',  font=('Helvetica', 20), bg='#ffcf94')
otvetik.place(relx=0.5, rely=0.6,anchor='center')



root.mainloop()
