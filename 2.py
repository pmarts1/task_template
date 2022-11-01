def is_palindrom(s):
    s = s.replace(' ', '')
    s = s.lower()
    if len(s) % 2 != 0:
        return False
    else:
        s1 = s[:int(len(s)/2):]
        s2 = s[:int(len(s)/2-1):-1]
        if s1 == s2:
            return True
        else:
            return False