import random


def draw_board(board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])


def input_player_letter():
    letter = ''
    while not (letter == 'O' or letter == 'X'):
        print('Вы выбираете X или O ?')
        letter = input().upper()

    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


def who_goes_first():
    first_step = random.randint(0, 1)
    if first_step == 0:
        return 'Человек'
    else:
        return 'Компьютер'


def make_move(board, letter, move):
    board[move] = letter


def is_winner(board, letter):
    return ((board[7] == letter and board[8] == letter and board[9] == letter) or
            (board[4] == letter and board[5] == letter and board[6] == letter) or
            (board[1] == letter and board[2] == letter and board[3] == letter) or
            (board[7] == letter and board[4] == letter and board[1] == letter) or
            (board[8] == letter and board[5] == letter and board[2] == letter) or
            (board[9] == letter and board[6] == letter and board[3] == letter) or
            (board[7] == letter and board[5] == letter and board[3] == letter) or
            (board[9] == letter and board[5] == letter and board[1] == letter))


def copy_board(board):
    copy_board = []
    for i in board:
        copy_board.append(i)
    return copy_board


def free_space(board, move):
    return board[move] == ' '


def player_move(board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not free_space(board, int(move)):
        move = input('Ваш следующий ход? (1-9): ')
    return int(move)


def choice_move_from_list(board, moves_list):
    possible_moves = []
    for i in moves_list:
        if free_space(board, i):
            possible_moves.append(i)

    if len(possible_moves) != 0:
        return random.choice(possible_moves)
    else:
        return None


def computer_move(board, comp_letter):
    if comp_letter == 'X':
        player_letter = 'O'
    else:
        player_letter = 'X'

    for i in range(1, 10):
        board_copy = copy_board(board)
        if free_space(board_copy, i):
            make_move(board_copy, comp_letter, i)
            if is_winner(board_copy, comp_letter):
                return i
    for i in range(1, 10):
        board_copy = copy_board(board)
        if free_space(board_copy, i):
            make_move(board_copy, player_letter, i)
            if is_winner(board_copy, player_letter):
                return i

    move = choice_move_from_list(board, [1, 3, 7, 9])
    if move != None:
        return move

    if free_space(board, 5):
        return 5

    return choice_move_from_list(board, [2, 4, 6, 8])


def is_board_full(board):
    for i in range(1, 10):
        if free_space(board, i):
            return False
    return True


print('Игра "Крестики-нолики"')

while True:
    # Перезагрузка игрового поля
    the_board = [' '] * 10

    player_letter, comp_letter = input_player_letter()
    turn = who_goes_first()
    print(f'{turn} ходит первым.')
    game_is_playing = True
    while game_is_playing:
        if turn == 'Человек':
            # human's turn
            draw_board(the_board)
            move = player_move(the_board)
            make_move(the_board, player_letter, move)
            if is_winner(the_board, player_letter):
                draw_board(the_board)
                print('Ура! Вы выиграли!')
                game_is_playing = False
            else:
                if is_board_full(the_board):
                    draw_board(the_board)
                    print('Ничья')
                    break
                else:
                    turn = 'Компьютер'
        else:
            # computer's turn
            move = computer_move(the_board, comp_letter)
            make_move(the_board, comp_letter, move)
            if is_winner(the_board, comp_letter):
                draw_board(the_board)
                print('Компьютер победил! Вы проиграли... :(')
                game_is_playing = False
            else:
                if is_board_full(the_board):
                    draw_board(the_board)
                    print('Ничья')
                    break
                else:
                    turn = 'Человек'

    question = input('Еще партейку? (да / нет) ')
    if not question.lower().startswith('д'):
        break


