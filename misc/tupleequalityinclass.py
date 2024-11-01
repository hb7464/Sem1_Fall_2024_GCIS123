def tupequal(a,b):
    if a is b:
        print("Shallow equality")
    if a == b:
        print("Deep equality")
    else:
        print("No equality")

def main():
    al = ['a',3,3.0]
    bl = ['a',3,3]

    ta = tuple(al)
    tb = tuple(bl)

    tupequal(ta,tb)

if __name__ == '__main__':
    main()