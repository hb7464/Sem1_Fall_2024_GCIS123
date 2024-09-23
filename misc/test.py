'''
import random

s = input("Enter a sentence with no punctuation: ")

for i in range(10):

    # s= 'This is a string of characters and if it creates a coherent sentence thats cool'

    L=s.split()
    a=len(L)
    b=''
    c=a - 1

    for j in range(a):

        d=random.randint(0,c)
        c-=1
        b+= ' '
        b+=L.pop(d)

    print(b)
'''

a = input("Whats your name? \n")
print("Hi ",a,"!",sep='')   