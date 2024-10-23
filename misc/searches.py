def linear_search(arr,val):
    for i in range(len(arr)):
        if arr[i] == val:
            return i
        
    else:
        return None

def main():
    arr = [10,23,555,333,22323,12]
    print(linear_search(arr,333))
    print(linear_search(arr,2))
    print(linear_search(arr,23))
    print(linear_search(arr,555))

if __name__ == '__main__':
    main()