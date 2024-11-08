def tictactoe():
    
    try:

        board = [['-','-','-'],['-','-','-'],['-','-','-']]
        c = 2
        Full = True
        
        while '-' in board[0] or '-' in board[1] or '-' in board[2]:

            printboard(board)
            print(f'Turn {c//2}')

            if c%2 == 0:
                char = 'X'
                print("It is X's turn")
    
            else:
                char = 'O'
                print("It is O's turn")

            row = int(input("Which row do you want to play in: ")) - 1
            col = int(input("Which column do you want to play in: ")) - 1

            if board[row][col] == '-':
                board[row][col] = char
                c+=1

            else:
                print("Can't play there, that is a filled square \n Try again.")
                continue

            if False == checker(board,char):
                Full = False
                break

        if Full == True:
            print('No one won :(')
        
        print('Game Over!')
        input()

    except:
       
        print('ERROR! You entered something that broke the game')

def checker(board,char):

    if board[0][0] == board[1][1] == board[2][2] != '-':
        printboard(board)
        print(f'{char} wins!')
        return False
    
    elif board[0][2] == board[1][1] == board[2][1] != '-':
        printboard(board)
        print(f'{char} wins!')
        return False
    
    for i in range(3):
    
        if board[i][0] == board[i][1] == board[i][2] != '-':
            printboard(board)
            print(f'{char} wins!')
            return False
    
        elif board[0][i] == board[1][i] == board[2][i] != '-':
            print(f'{char} wins!')
            printboard(board)
            return False

    return True

def printboard(board):
    for row in board:
        for col in row:
            print(f'|{col}|',end = '\n---------')

def main():

    tictactoe()

if __name__ == '__main__':
    main()