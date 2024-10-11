import csv 

def csv_fun():
    
    #Filepath = r"C:\Users\hisha\gcis123\hb7464\misc\csv_fun.csv"
    Filepath = input(r"Enter filepath")
    
    with open(Filepath) as f:

        A = csv.reader(f)
        next(A)

        for line in A:  
            print(f"Name <{line[0]}> Address: <{line[1]}>")

def average():

    #Filepath = r"C:\Users\hisha\gcis123\hb7464\misc\csv_fun.csv"
    Filepath = input(r"Enter filepath")

    with open(Filepath) as f:
        
        A = csv.reader(f)
        c=0
        s=0
        next(A)

        for i in A:
            c+=1
            s+= float(i[-1])

        avg = s/c
        print(f"The average is {avg}")

def main():
    csv_fun()
    average()

if __name__ == '__main__':
    main()