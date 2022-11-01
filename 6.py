import math

def angle(a, b):
    sp = 0
    l = 0
    if len(a) == len(b):
        for i in range(len(a)):
            sp = sp + a[i]*b[i]
            l = l + a[i]**2 + b[i]**2
        return (math.degrees(math.acos(sp/l**0.5)))
    else:
        return 'Разная размерность векторов'