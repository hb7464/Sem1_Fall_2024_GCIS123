def listcomp():
    return [x for x in range(50)if x%3 == 0 or x%5==0]

def main():
    LIST = listcomp()
    print(LIST)

if __name__ == '__main__':
    main()