from tkinter import *  # импортируем tkinter


class Calculator:  # класс калькулятор
    def __init__(self):   # создание окна и объектов
        self.window = Tk()  # создаем окно
        self.window.title("Калькулятор")  # задаем имя
        self.window.geometry('600x450')  # задаем размер поля
        self.window.resizable(width=False, height=False)  # статическое положение поля

        lbl1 = Label(self.window, text='Калькулятор:')
        lbl1.grid(column=0, row=0)  # размещаем надпись

        self.lbl = Label(self.window)
        self.lbl.grid(column=0, row=2)

        self.field = Entry()  # создание поля ввода
        self.field.grid(column=0, row=1)  # размещаем поле ввода

        self.btn = Button(self.window, width=10, height=1, text="Посчитать")  # создание кнопки, задаем ее размеры
        self.btn.config(command=lambda b=self.btn: self.calculate())  # привязываем функцию к кнопке
        self.btn.grid(column=1, row=1)  # размещаем кнопку

    def calculate(self):  # метод, которые вычисляет пример
        primer = eval(self.field.get())  # считает примнер
        self.lbl["text"] = str(primer)   # записываем

    def run(self):
        self.window.mainloop()  # запускаем Tk()


if __name__ == "__main__":
    calc = Calculator()  # объект класса Calculator()
    calc.run()  # запускаем метод run()





