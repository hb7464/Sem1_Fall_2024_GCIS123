def search():
    s = input("Enter the word to be searched: ")
    with open(r"C:\Users\hisha\gcis123\hb7464\misc\tl.txt") as f:
        c=0
        ch=0
        for line in f:
            c+=1
            a = line.split()
            for i in a:
                if s==i:
                    print(f"Word found in line {c}")
                    ch+=1
        if ch == 0:
            print("Word not found")

def main():
    search()

if __name__ == '__main__':
    main()