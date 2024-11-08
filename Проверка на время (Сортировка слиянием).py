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


def merge(a, b):
    res = []
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            res.append(a[i])
            i += 1
        else:
           res.append(b[j])
           j += 1
    res.extend(a[i:])
    res.extend(b[j:])
    return res
def msort(a):
    if len(a) <= 1:
        return a
    k = len(a) // 2
    return merge(msort(a[:k]), msort(a[k:]))



start = datetime.datetime.now()
msort(a1)
finish = datetime.datetime.now()
print("Массив 1:")
print('Время работы: ' + str(finish - start))
print()

start = datetime.datetime.now()
msort(a2)
finish = datetime.datetime.now()
print("Массив 2:")
print('Время работы: ' + str(finish - start))
print()

start = datetime.datetime.now()
msort(a3)
finish = datetime.datetime.now()
print("Массив 3:")
print('Время работы: ' + str(finish - start))
print()

start = datetime.datetime.now()
msort(a4)
finish = datetime.datetime.now()
print("Массив 4:")
print('Время работы: ' + str(finish - start))
print()

start = datetime.datetime.now()
msort(a5)
finish = datetime.datetime.now()
print("Массив 5:")
print('Время работы: ' + str(finish - start))
print()

start = datetime.datetime.now()
msort(a6)
finish = datetime.datetime.now()
print("Массив 6:")
print('Время работы: ' + str(finish - start))
print()

start = datetime.datetime.now()
msort(a7)
finish = datetime.datetime.now()
print("Массив 7:")
print('Время работы: ' + str(finish - start))
print()

start = datetime.datetime.now()
msort(a8)
finish = datetime.datetime.now()
print("Массив 8:")
print('Время работы: ' + str(finish - start))
print()

