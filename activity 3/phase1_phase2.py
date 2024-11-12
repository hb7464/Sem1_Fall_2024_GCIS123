'''
Mohammed Nagla's Repository link - 
Hishaam's Repository link - https://github.com/hb7464/hb7464 
Munzir's Repository link - https://github.com/munzir1910/GCIS123 
'''

def generate_sorted_data(size):
    #Generates an array of size random integers between 1 and 100 and sorts it using insertion sort.

    import random

    mydata = [random.randint(1, 100) for _ in range(size)]

    # Insertion sort implementation
    for i in range(1, len(mydata)):
        nagla = mydata[i]
        n = i - 1
        while n >= 0 and nagla < mydata[n]:
            mydata[n + 1] = mydata[n]
            n -= 1
        mydata[n + 1] = nagla

    return mydata

def main():

    '''The main function to call the function to generate and array a
    nd sort it with time complexity'''

    import time

    size = int(input("Enter the number of elements you want: "))
    
    start = time.perf_counter()
    Arr = generate_sorted_data(size)
    end = time.perf_counter()

    print(f'The sorted array: {Arr} \nTime Taken to generate and sort: {end-start}')

if __name__ == '__main__':
    main()