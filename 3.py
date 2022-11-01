def strcount(s1, s2):
    counter = 0
    a = len(s1)
    b = len(s2)
    if b >= a:
        print('qqq')
        for i in range(b-a+1):
            c = s2[i:a+i:]
            print(c)
            if c == s1:
                counter = counter + 1
    return counter