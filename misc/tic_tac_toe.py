def make_board():
    # board = [[1,2,3],[4,5,6],[7,8,9]]
    board = [['-']*3]*3
    return board

def print_board(board):

    print(f'{board[0][0]}|{board[0][1]}|{board[0][2]}', \
          f'{board[1][0]}|{board[1][1]}|{board[1][2]}',\
          f'{board[2][0]}|{board[2][1]}|{board[2][2]}',\
          sep='\n-----\n')

def make_move(board,sym):

    row = int(input("Enter a row number(1-3): ")) - 1
    col = int(input("Enter a col number(1-3): ")) - 1
    board[row][col] = sym

    print_board(board)

def main():

    board = make_board()
    print_board(board)

    print('X goes first')

    for i in range(9):

        if i%2 == 0:
            sym = 'X'
        else:
            sym = 'O'

        make_move(board,sym)

    print("Game over!")

if __name__ == '__main__':
    main()
    