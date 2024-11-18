class animal:
    # Class level variables
    feature = 'furry'
    tail = 'medium'

    def __init__(self,Name,Age):
        self.Name = Name
        self.Age = Age

    def animalsound(self,sound):
        self.sound = sound
        print(f'{self.Name} makes the sound {self.sound}')

def main():

    cat = animal('cat',3)
    cat.animalsound('meow')
    print(cat.sound)
    cat.sound = 'dem'
    print(cat.sound)
    print(cat.feature,cat.tail)


if __name__ == '__main__':
    main()