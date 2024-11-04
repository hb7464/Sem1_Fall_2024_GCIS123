def quicksort(arr):
    print(f'arr{arr}')
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr.pop(len(arr)//2)
        print(pivot)
    
    more = []
    less = []
    for item in arr:
        if item > pivot:
            more.append(item)
        else:
            less.append(item)
    return quicksort(less) + [pivot] + quicksort(more)

def main():
    import time as t
    L = [2,3,52,8,9,11,31,5,6,7]
    print(L)
    star = t.perf_counter()
    print(quicksort(L))
    end = t.perf_counter()
    print(end-star)

if __name__ == '__main__':
    main()