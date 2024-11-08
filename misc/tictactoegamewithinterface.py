def grid():

    import turtle as t
    t.tracer(False)
    t.fillcolor('white')
    
    for i in range(3):
    
        t.up()
        t.goto(-75,75 - i*50)
        t.setheading(0)
        t.down()
    
        for j in range(3):
    
            t.begin_fill()
    
            for k in range(4):
                t.forward(50)
                t.right(90)
    
            t.forward(50)
            t.end_fill()
    
    t.tracer(True)

def xdraw(row,col):
    
    import turtle as t
    
    t.up()
    t.goto(-75+((col)*50),75-((row+1)*50))
    t.setheading(45)
    t.down()
    
    t.forward(50*((2)**(1/2)))
    
    t.up()
    t.goto(-75+(col*50),75-(row*50))
    t.setheading(315)
    t.down()
    
    t.forward(50*((2)**(1/2)))
    t.up()

def odraw(row,col):
    
    import turtle as t
    
    t.up()
    t.goto(-75+((col)*50),75-((row)*50))
    t.setheading(0)
    t.forward(25)
    t.down()
    
    t.setheading(180)
    t.circle(25)
    t.up()

def wincond(char):
    
    import turtle as t
    
    winmsg = char + ' wins!'
    t.goto(-0,125)
    t.write(winmsg, move=False, align='center', font = ('arial',20,'normal'))

def tictactoe():
    
    try:

        board = [[None,None,None],[None,None,None],[None,None,None]]
        c = 1
        Full = True
        
        grid()

        while None in board[0] or None in board[1] or None in board[2]:
            
            print(f'Turn {c//2}')
            for i in board:
                print(i)

            if c%2 == 1:
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

            if c%2 == 1:
                xdraw(row,col)
    
            else:
                odraw(row,col)

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

    if board[0][0] == board[1][1] == board[2][2] != None:
    
        print(f'{char} wins!')
        wincond(char)
        return False
    
    elif board[0][2] == board[1][1] == board[2][1] != None:
    
        print(f'{char} wins!')
        wincond(char)
        return False
    
    for i in range(3):
    
        if board[i][0] == board[i][1] == board[i][2] != None:
            print(f'{char} wins!')
            wincond(char)
            return False
    
        elif board[0][i] == board[1][i] == board[2][i] != None:
            print(f'{char} wins!')
            wincond(char)
            return False

    return True
    
def main():
   
    import turtle as t
   
    t.hideturtle()
    t.bgcolor('lightgrey')

    tictactoe()

if __name__ == '__main__':
    main()