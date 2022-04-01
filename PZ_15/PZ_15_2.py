# В матрице элементы первого столбца возвести его в куб

import random
import np
M = 3
Matrix = [[random.randint(0, 2) for j in range(M)] for i in range(M)]
arr = np.array(Matrix)
temp = arr[:, 0]
print(*Matrix, sep='\n')
print(np.power(temp, 3))
