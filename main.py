import math
import pandas as pd
import matplotlib.pyplot as plt
from tabulate import tabulate

data = [0.92, 0.51, -1.05, -1.41, 1.04, -1.03, 1.55, -0.17, 0.92, 0.17, -0.49, -0.25, 1.49, -1.48, 0.4, 0.64, -0.61, 0.43, 0.13, 0.91]
data.sort()
print('Вариационный ряд:', [i for i in data])
print('Экстримальные значения (мин и макс):', data[0], data[-1])
print('Размах:', round(data[-1] - data[0], 2))
print('Математическое ожидание: ', sum(data) / len(data))
d = 0
for i in data: d += (i - sum(data) / len(data)) ** 2
print('Среднеквадратичное отклонение: ', round((d / len(data)) ** 0.5, 2))

fun = [[], [], []]
fun[0].append("x")
fun[1].append("f(x)")
fun[2].append("rate")
prev = 0
steps = -1
for i in data:
    steps += 1
    if i != data[0]:
        if i == prev:
            fun[2][-1] += 1
            continue
    fun[0].append(i)
    fun[1].append(steps / len(data))
    fun[2].append(1)
    prev = i
print('Эмперическая функция распределения: ')
print(tabulate(fun, tablefmt="grid"))

fun2 = []
for i in range(len(fun[0])):
    fun2.append([fun[0][i], fun[1][i], fun[2][i]])
fun = fun2[1:]

plt.title('Эмпирическая функция')
plt.xlabel("X")
plt.ylabel("F(x)")
for i in range(0, len(fun) - 1):
    plt.hlines(fun[i][1], fun[i][0], fun[i + 1][0])
plt.hlines(fun[-1][1], fun[-1][0], fun[-1][0])
plt.scatter("xx", "f(x)", data=pd.DataFrame(fun, columns=['xx', 'f(x)', 'rate']), marker='o', c='w', edgecolors='g')
plt.show()

plt.title("Гистограмма и полигон частотостей")
num = int(1 + math.log2(len(data)))
h = (data[-1] - data[0]) / num
blocks = []
int_row = []
for i in range(num + 1):
    blocks.append(data[0] + i * h)
    if i != 0:
        int_row.append(['[' + (str)(data[0] + (i-1) * h) + ',' + (str)(data[0] + i * h) + ')', 0, 0])
blocks_per = []
for i in range(num):
    cou = 0
    for j in data:
        if j >= blocks[i] and j < blocks[i + 1]:
           cou += 1
    int_row[i][1] = cou
    int_row[i][2] = cou/len(data)
    blocks_per.append(cou/len(data))
print('Интервальный ряд')
print(tabulate(int_row, tablefmt="grid"))

tost = []
for i in range(num + 1):
    tost.append(data[0] + i * h)
plt.stairs(blocks_per, edges=tost, fill=True)
toplot = []
for i in range(num):
    toplot.append(data[0] + h/2 + i * h)
plt.plot(toplot, blocks_per)
plt.show()