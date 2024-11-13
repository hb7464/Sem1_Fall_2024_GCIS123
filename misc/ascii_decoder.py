def decoder():
    
    Listofnumbercodestobedecoded = []
    
    try:
        
        while True:

            latestnumber = int(input("Enter the numbers: "))
            Listofnumbercodestobedecoded.append(latestnumber)

    except ValueError:
        
        result = ''
        
        for i in Listofnumbercodestobedecoded:
            result+= chr(i)
        
        print(result)

def main():
    decoder()

if __name__ == '__main__':
    main()