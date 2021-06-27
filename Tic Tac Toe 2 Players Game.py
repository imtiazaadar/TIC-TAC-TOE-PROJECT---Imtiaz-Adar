# Imtiaz Adar
# Tic Tac Toe Project
# Language Used : Python
# Date : 26/6/2021
# Email : imtiaz-adar@hotmail.com, imtiazadarofficial@gmail.com


# ------------------------------- TIC TAC TOE 2 PLAYERS GAME ----------------------------------------


board = [[' ',' ',' '], [' ',' ',' '], [' ',' ',' ']]
champ = ''
winner = False


# Game Board
def game_board():

    print('\t               -----------------------------')
    print('\t               |         |       |         |')
    print(f'\t               |    {board[0][0]}    |   {board[0][1]}   |    {board[0][2]}    |')
    print('\t               | ________|_______|________ |')
    print('\t               |         |       |         |')
    print(f'\t               |    {board[1][0]}    |   {board[1][1]}   |    {board[1][2]}    |')
    print('\t               | ________|_______|________ |')
    print('\t               |         |       |         |')
    print(f'\t               |    {board[2][0]}    |   {board[2][1]}   |    {board[2][2]}    |')
    print('\t               |         |       |         |')
    print('\t               -----------------------------')
    print()
    print()
    print()


# Check Winner
def check_winner(board):

    if ((board[0][0] == 'X' and board[0][1] == 'X' and board[0][2] == 'X') or (board[1][0] == 'X' and board[1][1] == 'X' and board[1][2] == 'X')
        or (board[2][0] == 'X' and board[2][1] == 'X' and board[2][2] == 'X') or (board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X')
        or (board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == 'X') or (board[0][0] == 'X' and board[1][0] == 'X' and board[2][0] == 'X')
        or (board[0][1] == 'X' and board[1][1] == 'X' and board[2][1] == 'X') or (board[0][2] == 'X' and board[1][2] == 'X' and board[2][2] == 'X')):
        winner = True

    elif ((board[0][0] == 'O' and board[0][1] == 'O' and board[0][2] == 'O') or (board[1][0] == 'O' and board[1][1] == 'O' and board[1][2] == 'O')
        or (board[2][0] == 'O' and board[2][1] == 'O' and board[2][2] == 'O') or (board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O')
        or (board[0][2] == 'O' and board[1][1] == 'O' and board[2][0] == 'O') or (board[0][0] == 'O' and board[1][0] == 'O' and board[2][0] == 'O')
        or (board[0][1] == 'O' and board[1][1] == 'O' and board[2][1] == 'O') or (board[0][2] == 'O' and board[1][2] == 'O' and board[2][2] == 'O')):
        winner = True

    else:
        winner = False

    return winner


# Main
def main():

    status = True
    while status:
        print('\n            ------------WELCOME TO TIC-TAC-TOE------------')
        print('\n                         MADE BY IMTIAZ ADAR')
        print()
        print()
        p1 = input("PLAYER 1'S NAME : ")
        p2 = input("PLAYER 2'S NAME : ")
        print()

        count = 0
        c = 0
        i = 1

        while i <= 9:

            count += 1
            c += 1
            if c % 2 != 0:
                player = p1
            elif c % 2 == 0:
                player = p2

            print(f"{player.upper()}'S TURN")
            print()
            choice = int(input(f'TYPE POSITION [ 1 - 9 ] : '))
            print()

            # if position == 1
            if choice == 1:
                if board[0][0] == ' ' and count % 2 != 0:
                    board[0][0] = 'X'
                elif board[0][0] == ' ' and count % 2 == 0:
                    board[0][0] = 'O'
                elif board[0][0] == 'X' or board[0][0] == 'O':
                    i = i - 1
                    count -= 1
                    c -= 1

            # if position == 2
            elif choice == 2:
                if board[0][1] == ' ' and count % 2 != 0:
                    board[0][1] = 'X'
                elif board[0][1] == ' ' and count % 2 == 0:
                    board[0][1] = 'O'
                elif board[0][1] == 'X' or board[0][1] == 'O':
                    i = i - 1
                    count -= 1
                    c -= 1

            # if position == 3
            elif choice == 3:
                if board[0][2] == ' ' and count % 2 != 0:
                    board[0][2] = 'X'
                elif board[0][2] == ' ' and count % 2 == 0:
                    board[0][2] = 'O'
                elif board[0][2] == 'X' or board[0][2] == 'O':
                    i = i - 1
                    count -= 1
                    c -= 1

            # if position == 4
            elif choice == 4:
                if board[1][0] == ' ' and count % 2 != 0:
                    board[1][0] = 'X'
                elif board[1][0] == ' ' and count % 2 == 0:
                    board[1][0] = 'O'
                elif board[1][0] == 'X' or board[1][0] == 'O':
                    i = i - 1
                    count -= 1
                    c -= 1

            # if position == 5
            elif choice == 5:
                if board[1][1] == ' ' and count % 2 != 0:
                    board[1][1] = 'X'
                elif board[1][1] == ' ' and count % 2 == 0:
                    board[1][1] = 'O'
                elif board[1][1] == 'X' or board[1][1] == 'O':
                    i = i - 1
                    count -= 1
                    c -= 1
            # if position == 6
            elif choice == 6:
                if board[1][2] == ' ' and count % 2 != 0:
                    board[1][2] = 'X'
                elif board[1][2] == ' ' and count % 2 == 0:
                    board[1][2] = 'O'
                elif board[1][2] == 'X' or board[1][2] == 'O':
                    i = i - 1
                    count -= 1
                    c -= 1

            # if position == 7
            elif choice == 7:
                if board[2][0] == ' ' and count % 2 != 0:
                    board[2][0] = 'X'
                elif board[2][0] == ' ' and count % 2 == 0:
                    board[2][0] = 'O'
                elif board[2][0] == 'X' or board[2][0] == 'O':
                    i = i - 1
                    count -= 1
                    c -= 1

            # if position == 8
            elif choice == 8:
                if board[2][1] == ' ' and count % 2 != 0:
                    board[2][1] = 'X'
                elif board[2][1] == ' ' and count % 2 == 0:
                    board[2][1] = 'O'
                elif board[2][1] == 'X' or board[2][1] == 'O':
                    i = i - 1
                    count -= 1
                    c -= 1

            # if position == 9
            elif choice == 9:
                if board[2][2] == ' ' and count % 2 != 0:
                    board[2][2] = 'X'
                elif board[2][2] == ' ' and count % 2 == 0:
                    board[2][2] = 'O'
                elif board[2][2] == 'X' or board[2][2] == 'O':
                    i = i - 1
                    count -= 1
                    c -= 1

            # else again player have to type position
            else:
                i -= 1
                count -= 1
                c -= 1
            i += 1

            # after every input Game Board will be printed
            game_board()

            # after every input board will be checked if someone win or not within the last turn
            won = check_winner(board)

            if won == True and count <= 9:
                print(f'CONGRATULATIONS ! {player.upper()} HAS WON THE MATCH !')
                break
            elif count == 9 and winner == False:
                print('GOOD LUCK NEXT TIME ! MATCH HAS DRAWN !')

        print()
        print()
        print('-------TYPE [[ OK ]] TO PLAY AGAIN OR, [[ EXIT ]] TO CLOSE THE GAME-------\n')
        play_again_or_not = input()
        if play_again_or_not == 'EXIT':
            status = False
        elif play_again_or_not == 'OK':
            status = True
        else:
            status = False
        print()
        print()
        board[0][0] = board[0][1] = board[0][2] = board[1][0] = board[1][1] = board[1][2] = board[2][0] = board[2][1] = board[2][2] = ' '


# Driver File
if __name__ == '__main__':
    main()
