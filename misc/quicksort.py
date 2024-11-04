def quicksort(arr):
    print(f'arr{arr}')
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr.pop()
    
    more = []
    less = []
    for item in arr:
        if item > pivot:
            more.append(item)
        else:
            less.append(item)
    return quicksort(less) + [pivot] + quicksort(more)

def main():
    L = [2,3,52,8,9,11,31,5,6,7]
    print(L)
    print(quicksort(L))

if __name__ == '__main__':
    main()