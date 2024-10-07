import random

'''A collection of examples of 
raising errors 
'''

def guessing_game():
    
    '''A function designed to ask the user to guess a number
    and has checks to ensure the user has entered a valid 
    number as per the requirements
    '''
    
    try:
    
        answer = random.randint(1,10)       #Getting a random number from 1-10 and storing it
        num = int(input("Please enter a number between 1 and 10: "))
        
        if num < 1 or num > 10:             #Checking if the user entered a number outside the range
            raise ValueError
        
        elif num == answer:
            print("Congrats you guess right!")
        
        else:
            print(f"Unlucky, incorrect guess, the correct answer was {answer}")
        
    except ValueError:
        print("Invalid Input.")

def password_func():

    '''A function to let the user set a 
    password with the required parameters'''

    try:
        
        c = 0
        passwd = input("Enter a password between 10-20 characters long: ")

        if len(passwd) < 10 or len(passwd) > 20:
            raise ValueError

        else:
            confirm_passwd = input("Please confirm your password: ")
            c+=1

        if passwd != confirm_passwd:
            raise ValueError
        
        else:
            return passwd
        

    except ValueError:
        if c == 0:
            print("Invalid password entered.")
    
        else:
            print("Passwords do not match.")

def division():

    # A function to accept two numbers and divide them
    
    try:
        
        num1 = int(input("Enter the numerator: "))
        num2 = int(input("Enter the denominator: "))
        
        if num2 == 0:
            raise ZeroDivisionError
        
        print('The quotient is',num1/num2)
    
    except ValueError:
        print("Invalid Input.")
    
    except ZeroDivisionError:
        print("You cannot put the denominator as 0.")

def main():
    guessing_game()


if __name__ == '__main__':
    main()