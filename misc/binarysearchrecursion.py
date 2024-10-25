def binary_search(L,top,bot,val):

    L.sort()
    leng = len(L)
    mid = (top+bot)//2
    
    #print(f"{L} \n Top: {top} \n Bottom: {bot} \n Mid: {mid} \n MidValue: {L[mid]} \n Value: {val}")
   
    if L[mid] == val:
     
        return mid
    
    elif bot > top:
     
        return -1
    
    elif L[mid] < val: 
     
        bot = mid+1
        return binary_search(L,top,bot,val)

    elif L[mid] > val:
     
        top = mid - 1
        return binary_search(L,top,bot,val)
    
    elif bot > top:
     
        return -1
    
def main():

    # L = eval(input("LIST: "))
    # val = int(input("Value to be found: "))
    
    L = [0,1,2,3,4,5,6,7,8,9]
    val = 10
    top = len(L) - 1
    a=binary_search(L,top,0,val)
    
    if a == -1:
    
        print(f"{val} is not a value in the list")
    
    else:
    
        print(f"{val} was found at index {a}")
    

if __name__ == '__main__':
    main()
        