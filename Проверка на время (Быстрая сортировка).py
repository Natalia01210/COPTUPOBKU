import datetime
import random
from random import choice
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


def quicksort(nums):
   if len(nums) <= 1:
       return nums
   else:
       q = random.choice(nums)
       s_nums = []
       m_nums = []
       e_nums = []
       for n in nums:
           if n < q:
               s_nums.append(n)
           elif n > q:
               m_nums.append(n)
           else:
               e_nums.append(n)
       return quicksort(s_nums) + e_nums + quicksort(m_nums)


start = datetime.datetime.now()
quicksort(a1)
finish = datetime.datetime.now()
print("Массив 1:")
print('Время работы: ' + str(finish - start))
print()

start = datetime.datetime.now()
quicksort(a2)
finish = datetime.datetime.now()
print("Массив 2:")
print('Время работы: ' + str(finish - start))
print()

start = datetime.datetime.now()
quicksort(a3)
finish = datetime.datetime.now()
print("Массив 3:")
print('Время работы: ' + str(finish - start))
print()

start = datetime.datetime.now()
quicksort(a4)
finish = datetime.datetime.now()
print("Массив 4:")
print('Время работы: ' + str(finish - start))
print()

start = datetime.datetime.now()
quicksort(a5)
finish = datetime.datetime.now()
print("Массив 5:")
print('Время работы: ' + str(finish - start))
print()

start = datetime.datetime.now()
quicksort(a6)
finish = datetime.datetime.now()
print("Массив 6:")
print('Время работы: ' + str(finish - start))
print()

start = datetime.datetime.now()
quicksort(a7)
finish = datetime.datetime.now()
print("Массив 7:")
print('Время работы: ' + str(finish - start))
print()

start = datetime.datetime.now()
quicksort(a8)
finish = datetime.datetime.now()
print("Массив 8:")
print('Время работы: ' + str(finish - start))
print()
