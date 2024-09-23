def smfor():
    s = 0
    for i in range(1,11):
        s+=i
    print(s)

def smwhile():
    c = 1
    s = 0
    while c <= 10:
        print(c)
        s+=c
        c+=1
    print(s)

def main():
    smwhile()

main()