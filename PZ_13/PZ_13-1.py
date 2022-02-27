# В последовательности из N чисел (N-четное) во второй её половине найти сумму элементов больших 10

import random

n = int(input("Введите число: "))
list1 = [random.randint(-10, 20) for x in range(n)]
print(list1)

l2 = int(len(list1) / 2)
list2 = [list1[i] for i in range(l2, (len(list1)))]
print(list2)

list3 = [n for n in list2 if n > 10]
print(sum(list3))
