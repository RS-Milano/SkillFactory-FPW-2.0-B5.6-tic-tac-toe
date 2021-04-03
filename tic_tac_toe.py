import os
import time
from collections import Counter

def game_mode_selection():
    flag = input("Enter: 1 - for a two-player game\n\
       2 - for a singel game\n       0 - for exit\n")
    if flag == "1":
        return (1,)
    elif flag == "2":
        return (2, first_move_selection())
    elif flag == "0":
        return (0,)
    else:
        print("incorrect input")
        return game_mode_selection()

def first_move_selection():
    flag = input("Who will go first?: 1 - you\n\
                    2 - computer\n")
    if flag == "1":
        return 1
    elif flag == "2":
        return 2
    else:
        print("Incorrect input!")
        return first_move_selection()

def get_move():
    move = input("Enter the coordinates of the move (without space, for example: 01)\n\
First digit - row number\nSecond digit - column number\n")
    if len(move) == 2 and move[0] in "012" and move[1] in "012":
        move = tuple(map(int, list(move)))
        if game_field[move[0]][move[1]] == "-":
            return move
        else:
            print("This cell is busy!")
            return get_move()           
    else:
        print("Incorrect input!")
        return get_move()

def show_field():
    separator = "------------------------"
    print(f"\n     |  0  |  1  |  2  |\n" + separator)
    for i, line in enumerate(game_field):
        line = f"  {i}  |  {'  |  '.join(line)}  |"
        print(line + "\n" + separator)
    print()

def check_win():
    win_combinations = [[] for _ in range(8)]
    for i in range(3):
        win_combinations[0].append(game_field[0][i])
        win_combinations[1].append(game_field[1][i])
        win_combinations[2].append(game_field[2][i])
        win_combinations[3].append(game_field[i][0])
        win_combinations[4].append(game_field[i][1])
        win_combinations[5].append(game_field[i][2])
        win_combinations[6].append(game_field[i][i])
        win_combinations[7].append(game_field[2 - i][i])
    draw_counter = 0
    for i in win_combinations:
        if "-" not in i and len(set(i)) == 1:
            return "X" if "X" in i else "O"
        if "X" in i and "O" in i:
            draw_counter += 1
    if draw_counter == 8:
        return "draw"
    else:
        return "continue"

def computer_move():
    """AI rev.2"""

    if game_field[1][1] == "-":
        return (1, 1)

    lines = {(0, 0): [], (0, 1): [], (0, 2): [],
             (1, 0): [], (1, 1): [], (1, 2): [],
             (2,): [], (3,): []}
    sign = "X" if game_mode[1] == 2 else "O"
    for i in range(3):
        lines[(0, 0)].append(game_field[0][i])
        lines[(0, 1)].append(game_field[1][i])
        lines[(0, 2)].append(game_field[2][i])
        lines[(1, 0)].append(game_field[i][0])
        lines[(1, 1)].append(game_field[i][1])
        lines[(1, 2)].append(game_field[i][2])
        lines[(2,)].append(game_field[i][i])
        lines[(3,)].append(game_field[2 - i][i])
    for key, value in lines.items():
        check = Counter(value)
        if check["-"] == 1 and len(set(value)) == 2 and sign in value:
            for i in range (3):
                if key[0] == 0 and value[i] == "-":
                    return (key[1], i)
                if key[0] == 1 and value[i] == "-":
                    return (i, key[1])
                if key[0] == 2 and value[i] == "-":
                    return (i, i)
                if key[0] == 3 and value[i] == "-":
                    return (2 - i, i)
    for key, value in lines.items():
        check = Counter(value)
        if check["-"] == 1 and len(set(value)) == 2:
            for i in range (3):
                if key[0] == 0 and value[i] == "-":
                    return (key[1], i)
                if key[0] == 1 and value[i] == "-":
                    return (i, key[1])
                if key[0] == 2 and value[i] == "-":
                    return (i, i)
                if key[0] == 3 and value[i] == "-":
                    return (2 - i, i)

    corners = {(0, 0): game_field[0][0], (0, 2): game_field[0][2],
    (2, 0): game_field[2][0], (2, 2): game_field[2][2]}
    middles = {(0, 1): game_field[0][1], (1, 0): game_field[1][0],
    (1, 2): game_field[1][2], (2, 1): game_field[2][1]}
    if "-" in corners.values():
        for key, value in corners.items():
            if value == "-":
                return key
    elif "-" in middles.values():
        for key, value in middles.items():
            if value == "-":
                return key

os.system('cls' if os.name == 'nt' else 'clear')
game_field = [["-" for i in range(3)] for i in range(3)]
print("This is a tic-tac-toe game. Let's play")
game_mode = game_mode_selection()
os.system('cls' if os.name == 'nt' else 'clear')
if game_mode[0] != 0:    
    first_player = "First player" if game_mode[0] == 1 else "Your" if game_mode[1] == 1 else "Computer"
    second_player = "Second player" if game_mode[0] == 1 else "Computer" if game_mode[1] == 1 else "Your"
    for i in range(1, 10):
        print("     Playing field")
        show_field()
        if i % 2 == 1:
            print(f"{first_player} - X\n{second_player} - O\n\n{first_player} turn\n")
            if first_player == "Computer":
                move = computer_move()
                # time.sleep(1)
            else:
                move = get_move()
            game_field[move[0]][move[1]] = "X"
            win = check_win()
            os.system('cls' if os.name == 'nt' else 'clear')
            if win == "X":
                print("     Playing field")
                show_field()
                print(f"{first_player} - X\n{second_player} - O\nCongratulations! {first_player} win!\n")
                break
            elif win == "draw":
                print("     Playing field")
                show_field()
                print(f"\nDraw! Thanks!\n")
                break
        else:
            print(f"{first_player} - X\n{second_player} - O\n\n{second_player} turn\n")
            if second_player == "Computer":
                move = computer_move()
                # time.sleep(1)
            else:
                move = get_move()
            game_field[move[0]][move[1]] = "O"
            win = check_win()
            os.system('cls' if os.name == 'nt' else 'clear')
            if win == "O":
                print("     Playing field")
                show_field()
                print(f"{first_player} - X\n{second_player} - O\nCongratulations! {second_player} win!\n")
                break
            elif win == "draw":
                print("     Playing field")
                show_field()
                print(f"\nDraw! Thanks!\n")
                break