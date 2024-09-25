def ind(s):
    print(s)
    i=0
    while i < len(s):
        print(s[i])
        i+=1

def rev(s):
    print(s)
    re=''
    i=1
    while i <= len(s):
        print(s[-i])
        re += s[-i]
        i+=1
    print(re)
    
def main():
    s=input("Enter a string: ")
    ind(s)
    print()
    rev(s)

main()