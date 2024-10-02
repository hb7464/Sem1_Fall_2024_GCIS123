def rev1(s):
    a = len(s) - 1
    s2=''
    for i in range(a,-1,-1):
        s2=s2+s[i]
    print(s2)

def rev2(s):
    a = len(s)+1
    s2=''
    for i in range(1,a):
        s2=s2+s[-i]
    print(s2)

def rev3(s):
    a = len(s)
    s2=''
    for i in range(0,a):
        s2=s[i]+s2
    print(s2)

def rev4(s):
    a = len(s)+1
    for i in range(1,a):
        print(s[-i],end='')

def main():
    s=input("Enter string: ")
    rev1(s)
    rev2(s)
    rev3(s)
    rev4(s)

if __name__ == '__main__':
    main()