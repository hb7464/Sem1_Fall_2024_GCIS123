def addnum(x,y):
    s=x+y
    return s

def subnum(x,y):
    d=x-y
    return d

def multnum(x,y):
    p=x*y
    return p

def divnum(x,y):
    q = x/y
    return q

def main():
    a = float(input("num1: "))
    b = float(input("num2: "))
    print(addnum(a,b))
    print(subnum(a,b))
    print(multnum(a,b))
    print(divnum(a,b))

main()