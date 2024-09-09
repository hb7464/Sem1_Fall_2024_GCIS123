pi = 3.14159
def circ(r):
    global pi
    c = 2 * pi * r 
    return c

def area(r):
    global pi
    a = pi * r **2
    return a

def main():
    r = float(input("Radius: "))
    print(circ(r))
    print(area(r))

main()