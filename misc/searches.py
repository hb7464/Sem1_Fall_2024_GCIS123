def linear_search(arr,val):
    import time
    start = time.perf_counter()
    for i in range(len(arr)):
        if arr[i] == val:
            end = time.perf_counter()
            elapsed = end - start
            return i, f'Time Elapsed: {elapsed}'
        
    else:
        end = time.perf_counter()
        elapsed = end - start
        return None,f'Time Elapsed: {elapsed}'

def main():
    arr = [10,23,555,333,22323,12]
    print(linear_search(arr,333))
    print(linear_search(arr,2))
    print(linear_search(arr,23))
    print(linear_search(arr,555))

if __name__ == '__main__':
    main()