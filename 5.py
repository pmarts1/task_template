import numpy as np

def multiplication(A, B):
    if A.shape == B.shape:
        return np.dot(A, B.T)
    else:
        return 'Размеры матриц не совпадают.'
