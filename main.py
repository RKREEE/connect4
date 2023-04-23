import colorama

game_over = False

board = {
    "7": {"placed": 0, "0": "#", "1": "#", "2": "#", "3": "#", "4": "#", "5": "#"},
    "6": {"placed": 0, "0": "#", "1": "#", "2": "#", "3": "#", "4": "#", "5": "#"},
    "5": {"placed": 0, "0": "#", "1": "#", "2": "#", "3": "#", "4": "#", "5": "#"},
    "4": {"placed": 0, "0": "#", "1": "#", "2": "#", "3": "#", "4": "#", "5": "#"},
    "3": {"placed": 0, "0": "#", "1": "#", "2": "#", "3": "#", "4": "#", "5": "#"},
    "2": {"placed": 0, "0": "#", "1": "#", "2": "#", "3": "#", "4": "#", "5": "#"},
    "1": {"placed": 0, "0": "#", "1": "#", "2": "#", "3": "#", "4": "#", "5": "#"}
}
turn = -1
names = [input("name 1: "), input("name 2: ")]
colours = [colorama.Fore.LIGHTRED_EX, colorama.Fore.LIGHTYELLOW_EX]

print("7654321")
for i in range(6):
    print("#######")

while not game_over:
    turn += 1
    num = False
    column = input("column: ")
    while not num: 
        try: 
            if int(column) > 7 or int(column) < 1:
                raise ValueError
            row = str(board[column]["placed"])
            board[column][row] = f"{colours[turn%2]}#{colorama.Fore.RESET}"
            board[column]["placed"] = str(int(row) + 1)
            num = True
        except ValueError:
            column = input("invalid column: ")

    output = ""
    for x in range(6):
        for y in range(7):
            output = board[str(y+1)][str(x)] + output
        output = "\n" + output
    
    output += colorama.Fore.RESET
    print(output)

    token = f"{colours[turn%2]}#{colorama.Fore.RESET}"
    connect_4 = False
    for column in board:
        for piece in board[column]:
            if piece == "placed":
                continue
            try:
                if token == board[column][piece] == board[column][str(int(piece)+1)] == board[column][str(int(piece)+2)] == board[column][str(int(piece)+3)]:
                    connect_4 = True
            except KeyError:
                pass
            
            try:
                if token == board[column][piece] == board[str(int(column)+1)][piece] == board[str(int(column)+2)][piece] == board[str(int(column)+3)][piece]:
                    connect_4 = True
            except KeyError:
                pass

            try:
                if token == board[column][piece] == board[str(int(column)+1)][str(int(piece)+1)] == board[str(int(column)+2)][str(int(piece)+2)] == board[str(int(column)+3)][str(int(piece)+3)]:
                    connect_4 = True
            except KeyError:
                pass

            try:
                if token == board[column][piece] == board[str(int(column)+1)][str(int(piece)-1)] == board[str(int(column)+2)][str(int(piece)-2)] == board[str(int(column)+3)][str(int(piece)-3)]:
                    connect_4 = True
            except KeyError:
                pass

    if connect_4:
        print(f'{colours[turn%2]}Game Over, {names[turn%2]} wins!!{colorama.Fore.RESET}')
        game_over = True

