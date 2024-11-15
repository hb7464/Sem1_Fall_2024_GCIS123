# write a sorting code on lists that should sort it using descending order

def sortingcode(L):
    L.sort(reverse = True)

# Using list comprehension, write all the numbers from 1 to 
# 30 that are divisble by 3 and on their right side, unit place should be no other digit than 5

def listcomp():
    return [x for x in range(1,30) if x%3 == 0 and str(x)[-1] == '5']

def main():
    L = listcomp()
    print(L)
    L.extend([1,3,56,74,3])
    print(L)
    sortingcode(L)
    print(L)

main()

if __name__ == '__main__':
    main()