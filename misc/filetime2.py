def countlines():
    with open(r"hb7464\misc\tl.txt") as f:
        c = 0
        for lines in f:
            c+=1
        print(c)
def countword():
    with open(r"hb7464\misc\tl.txt") as f:
        c = 0
        for lines in f:
            c+=len(lines.split())
        print(c)

def countchar():
    with open(r"hb7464\misc\tl.txt") as f:
        c = 0
        for lines in f:
            c+= len(lines)
        print(c)

def main():
    countlines()
    countword()
    countchar()
    
if __name__=='__main__':
    main()
