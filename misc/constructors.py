class Card:

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.name = str(self.rank) + ' of ' + str(self.suit) + 's'
        self.short = str(self.suit)[0] + str(self.rank)  

    pass

def main():

    a_card1 = Card(5,'Heart')
    a_card2 = Card(10,'Spade')


    print(f'Name: {a_card1.name} \nRank: {a_card1.rank} \nSuit: {a_card1.suit} \nShorthand: {a_card1.short}')
    print(f'Name: {a_card2.name} \nRank: {a_card2.rank} \nSuit: {a_card2.suit} \nShorthand: {a_card2.short}')

if __name__ == '__main__':
    main()