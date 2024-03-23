# кнопка пример

from tkinter import *  # импортируем tkinter

count = 0  # счетчик


def click_button():
    global count  # объявляем count глобальной переменой
    count += 1  # увеличиваем счетчик
    print(count)  # печатаем


root = Tk()  # создаем окно
root.geometry("100x100")  # задаем размеры
btn = Button(command=click_button, text="Кнопка")  # создаем кнопку и задаем команду
btn.grid(column=0, row=0)  # размещаем кнопку
root.mainloop()  # запускаем

