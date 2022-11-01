import numpy as np

def solution(a, b):
    m = np.array(a)
    return np.linalg.solve(m, b)