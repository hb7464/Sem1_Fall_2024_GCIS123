import csv
import random

random_lists = [
    [random.randint(1, 100) for _ in range(5)] for _ in range(10)
]

def writecsv():
    with open(r'testing.csv','w',newline='') as f:
        a = csv.writer(f)
        a.writerows(random_lists)

def readcsv():
     with open(r'testing.csv') as f:
        a = csv.reader(f)
        lin=0
        wrd=0
        char=0
        for i in a:
            lin+=1
            wrd+=len(i)
            for j in i:
                char+= len(j)
        print(lin)
        print(wrd)
        print(char)
def main():
    writecsv()
    readcsv()

if __name__ == '__main__':
    main()