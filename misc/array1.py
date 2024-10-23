import arrays

def making_arrays():
    array1 = arrays.Array(5)
    array2 = arrays.Array(1,0)
    array3 = arrays.Array(10, "")
    array4 = arrays.Array(20,False)
    print(array1,array2,array3,array4,sep ='\n')

def for_fill():
    arr = arrays.Array(10)
    leng = len(arr)
    for i in arr:
        arr[i] = i+1
    print(arr)

def while_fill():
    arr = arrays.Array(10)
    leng = len(arr)
    c = 0
    while c < leng:
        arr[c] = c+1
        c+=1
    print(arr)
    
def rolldice():
    import random
    result = random.randint(1,6)
    print(f"The dice returned: {result}")

if __name__ == '__main__':
    main()
def main():
    # making_arrays()
    # for_fill()
    while_fill()

if __name__ == '__main__':
    main()