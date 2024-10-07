import csv
import random

random_lists = [
    [random.randint(1, 100) for _ in range(5)] for _ in range(10)
]

def writecsv():
    with open(r'hb7464\misc\testing.csv','w',newline='') as f:
        a = csv.writer(f)
        a.writerows(random_lists)

def readcsv():
     with open(r'hb7464\misc\testing.csv') as f:
        a = csv.reader(f)
        for i in a:
            print(i)

def main():
    writecsv()
    readcsv()

if __name__ == '__main__':
    main()