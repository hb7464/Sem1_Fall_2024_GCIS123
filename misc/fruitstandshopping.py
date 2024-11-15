class Fruit:
    Type = ''
    price = ''

    def creator(Fruit):
        Fruit.Type = input("Enter fruit type: ")
        Fruit.price = float(input("Enter fruit price: "))
        print()
   
    def printvalues(Fruit):
        print(f'Fruit Type: {Fruit.Type} \nFruit Price: {Fruit.price} \n')

def createfruits():

    fruit1 = Fruit()
    fruit1.creator()
    fruit2 = Fruit()
    fruit2.creator()
    fruit3 = Fruit()
    fruit3.creator()

    return {fruit1.Type:fruit1.price,fruit2.Type:fruit2.price,fruit3.Type:fruit3.price}

def main():
    
    d = createfruits()
    
    basket = []
    while True:

        inp = input("Enter name of fruit to add to the basket or Nothing to stop: ")
        
        if inp == 'Nothing':
            break
        
        elif inp in d:
            basket.append([inp,d[inp]])

        else:
            print("Fruit stand doesn't sell that")

    print(basket)

if __name__ == '__main__':
    main()
            