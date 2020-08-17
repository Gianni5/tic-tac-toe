def print_board(board):
    print('   |   |   ')
    print(' ' + str(board[7]) + ' | ' + str(board[8]) + ' | ' + str(board[9]))
    print('   |   |   ')
    print('-------------')
    print(' ' + str(board[4]) + ' | ' + str(board[5]) + ' | ' + str(board[6]))
    print('   |   |   ')
    print('-------------')
    print(' ' + str(board[1]) + ' | ' + str(board[2]) + ' | ' + str(board[3]))
    print('   |   |   ')


if __name__ == "__main__":
    board = [0] * 10
    print_board(board)
