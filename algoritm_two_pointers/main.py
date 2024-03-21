# Жадный алгоритм
data = [1, 5, 8, 9, 10, 34, 78, 45, 56]  # массив
data = sorted(data)  # сортируем список

k = 57  # сумма чисел должна быть больше этого числа

minim = len(data)  # минимальное кол-во элементов сумма, которых больше числа k

for i in range(len(data)):
    s = 0  # сумма
    for j in range(i, len(data)):
        s += data[i]  # высчитываем сумму
        # print(j)
        if j - i + 1 > minim:
            minim = j - i + 1
print(s)  # выводим сумму
