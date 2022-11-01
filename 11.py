import numpy as np

def th(arr, threshold, width):
    l = []
    a = arr
    b = np.array([0 for i in range(len(a))])
    for i in range(len(a)):
        if a[i] > threshold:
            b[i] = 1
            for j in range(i-int(width/2), i+int(width/2)+1):
                if j >= 0 and j < len(a):
                    if a[j] > threshold and j != i:
                        b[i] = 2;
    for i in range(len(b)):
        if b[i] == 1:
            l.append(i)
    return (l)