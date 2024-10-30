def mutater(a_lst, a_int):
    print(f'Mutater: {a_int} {a_lst}')
    a_int *= 5
    a_lst[0] = a_lst[0] * 5
    print(f'Mutater: {a_int} {a_lst}')

def main():
    a_int = 7
    a_lst = [7]
    print(f"Before: {a_int} {a_lst}")
    mutater(a_lst,a_int)
    print(f"After: {a_int} {a_lst}")

if __name__ == '__main__':
    main()