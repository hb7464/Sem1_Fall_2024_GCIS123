def summing_with_loop(num):
    total = 0
    for i in range(1,num+1):
        total += i
    return total

def summing_with_recursion(num):
    if num == 1:
        return 1
    else:
        return num + summing_with_recursion(num-1)

def main():
    num = 5 
    result_loop = summing_with_loop(num)
    result_recur = summing_with_recursion(num)
    print(result_loop)
    print(result_recur)    

if __name__ == '__main__':
    main()