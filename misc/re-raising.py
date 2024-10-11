def login():
    attempts = 4
    usid = input("Enter username: ")
    passwd = input("Enter password: ")
 
    while True:

        try:
        
            if validate(usid, passwd) == True:
                break
        
        except ValueError as ve:
            attempts -=1
            
            if attempts > 0:
            
                print(f"Invalid Password: {attempts} Remaining")
            
            else:
                raise ve
            
def validate(user,pwd):
    passwd = input(f"Enter password for the user {user}: ")

    if pwd == passwd:
        print("Correct Password: Logged In")
        return True
    
    else: 
        raise ValueError("Too Many Failed Attempts")
    
def main():
    login()

if __name__ == '__main__':
    main()