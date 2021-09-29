

def pattern(n, m, flag):

    if n == m and flag is False:
        print(m)
        return
    elif m - 5 > 0:
        print(m)
        pattern(n, m - 5, True)
    elif m - 5 < 0:
        print(m)
        pattern(n, m - 5, False)
    else:
        print(m)
        pattern(n, m + 5, False)

pattern(16, 16, True)