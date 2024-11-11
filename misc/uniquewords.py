def uniquewords(filename):
    UniqueWords = {1}
    with open(filename) as file:
        for line in file:
            wordlist = line.split()
            for word in wordlist:
                UniqueWords.add(word.lower())
    
    print(f'Alice in wonderland has {len(UniqueWords)-1} unique words in it.')
    print(UniqueWords)

def main():
    filename = input("Enter file name: ")
    uniquewords(filename)

if __name__ == '__main__':
    main()