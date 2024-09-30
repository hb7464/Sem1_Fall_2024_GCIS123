def skip3():
    c = 0
    while True:
        c=c+1
        if c > 30:
            break
        elif c%3 == 0:
            continue
        else:
            print(c)
skip3()