board = [" " for i in range(9)]


def print_board():
    row1 = "| {} | {} | {} |".format(board[0], board[1], board[2])
    row2 = "| {} | {} | {} |".format(board[3], board[4], board[5])
    row3 = "| {} | {} | {} |".format(board[6], board[7], board[8])

    print()
    print(row3)
    print(row2)
    print(row1)
    print()


def check_icon(player):
    if player == 1:
        return "X"
    else:
        return "O"


def player_move(player):
    print("Your turn player {}".format(player))

    icon = check_icon(player)

    while True:
        choice = int(input("Enter your move (1-9):\n").strip()) - 1
        if not choice in range(9):
            print("Please input a valid number.")
            print()
            continue
        if board[choice] == " ":
            board[choice] = icon
            break
        else:
            print("The space is taken!")
            print()

    print_board()
    if is_victory(icon):
        print("{} Wins! Congratulations!".format(icon))
        quit()


def is_victory(icon):
    return (board[0] == icon and board[1] == icon and board[2] == icon) or \
        (board[3] == icon and board[4] == icon and board[5] == icon) or \
        (board[6] == icon and board[7] == icon and board[8] == icon) or \
        (board[0] == icon and board[3] == icon and board[6] == icon) or \
        (board[1] == icon and board[4] == icon and board[7] == icon) or \
        (board[2] == icon and board[5] == icon and board[8] == icon) or \
        (board[0] == icon and board[4] == icon and board[8] == icon) or \
        (board[6] == icon and board[4] == icon and board[2] == icon)


def is_draw():
    return not " " in board


def game():
    print_board()
    for x in range(9):
        player_move(x % 2 + 1)
    is_draw()


game()
