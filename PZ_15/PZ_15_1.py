# В матрице найти среднее арифметическое положительных чисел

import random
M = 3
matrix = [[random.randint(-2, 2) for j in range(M)] for i in range(M)]
print(*matrix, sep='\n')
h = []
for i in matrix:
    for t in i:
        if t in i:
            if t > 0:
                h.append(t)
print('среднее арифметическое положительных элементов равно:', sum(h) / len(h))
