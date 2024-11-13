def names():
    Dict = {}
    for i in range(3):
        family_names = input("Enter first name, middle name and last name: ")

        ar = family_names.split()
        Dict[ar[0][0]] = ar[0]
        for i in ar[1:]:
            Dict[ar[0][0]] += ' '+i

    print(Dict)

def main():
    names()

if __name__ == '__main__':
    main()