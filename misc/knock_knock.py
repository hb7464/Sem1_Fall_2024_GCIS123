"""In the last class (and your homework!) you wrote lots of
functions that used the built-in print() and input()
functions. Refresh your memory by writing a function that
tells your favorite knock-knock joke!
4
● Create a new Python module in a file named "knock_knock.py"
and define a function named "joke".
○ Use the built-in input() function to prompt the user, e.g.
input("Knock-knock:")
○ Print the user's response to your prompts. You do not need to validate
their response to see if it is correct.
○ Use the print() function for the punchline.
● Define a main function that calls your joke function at least twice.
● Run your program to verify that it works correctly.
○ Don't forget to call main!
"""

def joke():
    knock_knock = input("Knock knock: ")
    print(knock_knock)
    part2 = input("ya: ")
    print(part2)
    print("yahoo.com")

def main():
    joke()
    joke()

main()



'''
import random
kkjokes = [["Diane","I'm Diane to come in, open the door."],["Omelet","Omelet myself in."],["Juicy","Juicy the look on your face? Ridiculous."],["Doris","Doris locked, why do you think I'm knocking?"]]
for i in range(2):
    a=random.randint(0,3)
    L = kkjokes[a]
    knock_knock = input("Knock knock: ")
    print(knock_knock)
    p2= L[0] + ": "
    part2 = input(p2)
    print(part2)
    print(L[1])
'''