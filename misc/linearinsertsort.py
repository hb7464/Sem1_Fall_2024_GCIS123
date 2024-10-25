def insertsort(L):
    
    for i in range(1, len(L)):
        
        j = i
        while L[j-1] > L[j] and j > 0:
            L[j-1], L[j] = L[j], L[j-1]
            j-=1

    return L

def main():
    L = [2,34,6,12,4,5,7]
    end_list = insertsort(L)
    print(f"Sorted List: {end_list}")

if __name__ == '__main__':
    main()