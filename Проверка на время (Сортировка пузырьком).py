import datetime

from random import randint

a1 = []
for i in range(1, 101):
    a1.append(i)
a2 = []
for i in range(1, 10001):
    a2.append(i)
a3 = []
for i in range(100, 0, -1):
    a3.append(i)
a4 = []
for i in range(10000, 0, -1):
    a4.append(i)
a5 = []
for i in range(100):
    t = randint(1, 100)
    a5.append(t)
a6= []
for i in range(10000):
    t = randint(1, 100)
    a6.append(t)
a7 = []
for i in range(100):
    t = randint(1, 10000)
    a7.append(t)
a8 = []
for i in range(10000):
    t = randint(1, 10000)
    a8.append(t)


def bubble_sort(a):
    n = len(a)
    unordered = True
    while unordered:
        unordered = False
        for j in range(n - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                unordered = True
        n -= 1


start = datetime.datetime.now()
bubble_sort(a1)
finish = datetime.datetime.now()
print("Массив 1:")
print('Время работы: ' + str(finish - start))
print()

start = datetime.datetime.now()
bubble_sort(a2)
finish = datetime.datetime.now()
print("Массив 2:")
print('Время работы: ' + str(finish - start))
print()

start = datetime.datetime.now()
bubble_sort(a3)
finish = datetime.datetime.now()
print("Массив 3:")
print('Время работы: ' + str(finish - start))
print()

start = datetime.datetime.now()
bubble_sort(a4)
finish = datetime.datetime.now()
print("Массив 4:")
print('Время работы: ' + str(finish - start))
print()

start = datetime.datetime.now()
bubble_sort(a5)
finish = datetime.datetime.now()
print("Массив 5:")
print('Время работы: ' + str(finish - start))
print()

start = datetime.datetime.now()
bubble_sort(a6)
finish = datetime.datetime.now()
print("Массив 6:")
print('Время работы: ' + str(finish - start))
print()

start = datetime.datetime.now()
bubble_sort(a7)
finish = datetime.datetime.now()
print("Массив 7:")
print('Время работы: ' + str(finish - start))
print()

start = datetime.datetime.now()
bubble_sort(a8)
finish = datetime.datetime.now()
print("Массив 8:")
print('Время работы: ' + str(finish - start))
print()

