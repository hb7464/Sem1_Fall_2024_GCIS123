pi = 3.14159
def circ(r):
    global pi
    c = pi * r ** 2
    return c

def main():
    r = float(input("Radius: "))
    print(circ(r))

main()