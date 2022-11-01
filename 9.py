import pandas as pd
import numpy as np
def dtframe(fileCsv):
    sumPh100 = 0
    sumR = 0
    countR = 0
    use = pd.read_csv(fileCsv)
    a = {'number_of_student' : use.shape[0]}
    m = list(use['Математика'])
    ph = list(use['Физика'])
    r = list(use['Русский язык'])
    a['mean_math'] = sum(m)/a['number_of_student']

    for i in range(a['number_of_student']):
        if ph[i] == 100:
            sumR = sumR + r[i]
            countR = countR + 1
    a['mean_russian'] = sumR/countR


    a['sorted_russian'] = pd.DataFrame(use.sort_values(by='Русский язык', ascending=False))

    a['number_7'] = 0

    for i in range(a['number_of_student']):
        if (ph[i] == m[i]) and (ph[i] == r[i]):
            a['number_7'] = a['number_7'] + 1

    for i in range(a['number_of_student']-100, a['number_of_student']):
        sumPh100 = sumPh100 + ph[i]
    a['mean_physics'] = sumPh100 / 100

    a['sum'] = use[["Математика", "Русский язык", "Физика"]].apply(lambda x: x.sum(), axis=1)

    a['max'] = max(a['sum'])
    return (a)
