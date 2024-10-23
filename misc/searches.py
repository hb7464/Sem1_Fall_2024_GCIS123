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
    import random
    arr=[]
    for i in range(10):
        arr.append(random.randint(1,10))
    print(linear_search(arr,random.randint(1,10)))
    print(linear_search(arr,random.randint(1,10)))
    print(linear_search(arr,random.randint(1,10)))
    print(linear_search(arr,random.randint(1,10)))
    
if __name__ == '__main__':  
    main()