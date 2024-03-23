from tkinter import *

root = Tk()  # создаем окно
canvas = Canvas(root)  # создаем поверхность
canvas.create_line(15, 25, 200, 25)  # рисуем
canvas.create_line(300, 35, 300, 200, dash=(4, 2))  # рисуем
canvas.create_line(55, 85, 155, 85, 105, 180, 55, 85)  # рисуем
canvas.grid(column=0, row=0)  # размещаем поверхность
root.mainloop()
