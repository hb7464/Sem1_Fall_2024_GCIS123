'''#Phase 1
def generate_sorted_data_with_linear(size):

    import random as rdm
    import arrays
    
    #Array generation

    Arr = arrays.Array(size)
    for i in range(size):
        Arr[i] = rdm.randint(1,100)

    #Array sorting
    
    for i in range(1,len(Arr)):
        
        j = i
        while j > 0 and Arr[j] < Arr[j-1]:
            Arr[j], Arr[j-1] = Arr[j-1], Arr[j]
            j-=1
        
    return Arr

#Phase 2
def binary_search(sorted_array, target):

    top = len(sorted_array) - 1 
    bot = 0
    mid = (top+bot)//2 

    while True:

        if target == sorted_array[mid]:
            return f'Index is {mid}'
        
        elif top < bot:
            return None
        
        elif target > sorted_array[mid]:
            bot = mid + 1
            mid = mid


        elif target < sorted_array[mid]:
            top = mid - 1
            mid = mid 
'''
#Phase 3

def generate_sorted_array_with_merge(size):

    import random as rdm
    import arrays
    
    #Array generation

    # Arr = arrays.Array(size)
    L=[]
    for i in range(size):
        L.append(rdm.randint(1,100))
        # Arr[i] = rdm.randint(1,100)
    
    return mergesort(L)

def mergesort(arr):

    if arr is None:
        return None

    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])

    return merge(left,right)

def merge(left,right):

    import array

    sorted_arr = []
    i = j = 0

    while i < len(left) and j < len(right):

        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i+=1
        
        else:
            sorted_arr.append(right[j])
            j+=1

    sorted_arr += left[i:]
    sorted_arr += right[j:]
    return array.array('i',sorted_arr)

def main():
    Arr = generate_sorted_array_with_merge(10)
    print(Arr)

if __name__ == '__main__':
    main()