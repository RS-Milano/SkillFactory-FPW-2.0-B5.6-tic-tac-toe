def game_mode_selection():
    flag_1 = input("Enter: 1 - for a two-player game 2 - for a singel game 0 - for exit\n")
    if flag_1 == "1":
        return (1,)
    elif flag_1 == "2":
        flag_2 = input("Who will go first?: 1 - you 2 - computer\n")
        if flag_2 == "1":
            return (2, 1)
        elif flag_2 == "2":
            return (2, 2)
        else:
            print("incorrect input")
            return game_mode_selection()
    elif flag_1 == "0":
        return (0,)
    else:
        print("incorrect input")
        return game_mode_selection()

def get_move():
    move = input("Enter the coordinates of the move. First the line number, then the column number (for example: 01)\n")
    if len(move) == 2 and move[0] in "012" and move[1] in "012":
        move = tuple([int(move[0]), int(move[1])])
        if game_field[move[0]][move[1]] == "-":
            return move
        else:
            print("this cell is busy")
            return get_move()           
    else:
        print("incorrect input")
        return get_move()

def show_field():
    separator = "------------------------"
    print(f"\n     |  0  |  1  |  2  |\n" + separator)
    for i, line in enumerate(game_field):
        line = f"  {i}  |  {'  |  '.join(line)}  |"
        print(line + "\n" + separator)

def make_move(move, flag):
    """move - tuple of two items, each digit (0/1/2).
    flag - digit (1/2): 1 - first player ("x"), 2 - second player ("o")"""

    if flag == 1:
        game_field[move[0]][move[1]] = "x"
    elif flag == 2:
        game_field[move[0]][move[1]] = "o"

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

    for i in win_combinations:
        if "-" not in i and len(set(i)) == 1:
            return "x" if "x" in i else "o"
    
    if "-" not in game_field[0] and "-" not in game_field[1] and "-" not in game_field[2]:
        return "draw"
    else:
        return "continue"

def computer_move():
    """The coputer has vary primitive logic. Can be improved"""

    corners = {(0, 0): game_field[0][0], (0, 2): game_field[0][2],
    (2, 0): game_field[2][0], (2, 2): game_field[2][2]}
    middles = {(0, 1): game_field[0][1], (1, 0): game_field[1][0],
    (1, 2): game_field[1][2], (2, 1): game_field[2][1]}

    if game_field[1][1] == "-":
        return (1, 1)
    elif "-" in corners.values():
        for key, value in corners.items():
            if value == "-":
                return key
    elif "-" in middles.values():
        for key, value in middles.items():
            if value == "-":
                return key

game_field = [["-" for i in range(3)] for i in range(3)]
print("This is a game tic-tac-toe. Let's play")
game_mode = game_mode_selection()

# Main program logic
if not game_mode[0]:
    pass
elif game_mode[0] == 1:
    print("This is the playing field")
    while True:
        show_field()
        print("First player move")
        move = get_move()
        make_move(move, 1)
        win = check_win()
        if win in "xodraw":
            break
        show_field()
        print("Second player move")
        move = get_move()
        make_move(move, 2)
        win = check_win()
        if win in "xodraw":
            break
elif game_mode[0] == 2 and game_mode[1] == 1:
    print("This is the playing field")
    while True:
        show_field()
        print("Player move")
        move = get_move()
        make_move(move, 1)
        win = check_win()
        if win in "xodraw":
            break
        show_field()
        print("Computer move")
        move = computer_move()
        make_move(move, 2)
        win = check_win()
        if win in "xodraw":
            break
elif game_mode[0] == 2 and game_mode[1] == 2:
    print("This is the playing field")
    while True:
        show_field()
        print("Computer move")
        move = computer_move()
        make_move(move, 1)
        win = check_win()
        if win in "xodraw":
            break   
        show_field()
        print("Player move")
        move = get_move()
        make_move(move, 2)
        win = check_win()
        if win in "xodraw":
            break

# Result handler
win = check_win()
if game_mode[0] == 1:
    if win == "x":
        print("First player win")
        show_field()
    elif win == "o":
        print("Second player win")
        show_field()
    elif win == "draw":
        print("Draw")
        show_field()
elif game_mode[0] == 2 and game_mode[1] == 1:
    if win == "x":
        print("Player win")
        show_field()
    elif win == "o":
        print("Computer win")
        show_field()
    elif win == "draw":
        print("Draw")
        show_field()
elif game_mode[0] == 2 and game_mode[1] == 2:
    if win == "x":
        print("Computer win")
        show_field()
    elif win == "o":
        print("Player win")
        show_field()
    elif win == "draw":
        print("Draw")
        show_field()