def is_unfinished(input):
    return "_" in input


def is_possible(input):
    counter = 0
    for c in input:
        if c == "O":
            counter += 1
        elif c == "X":
            counter -= 1
    result = -2 < counter < 2
    counter = 0
    for i in range(3):
       r = 3 * i
       if input[r] == input[r + 1] == input[r + 2]:
           counter += 1
       if input[i] == input[i + 3] == input[i + 6]:
           counter += 1
    if input[0] == input[4] == input[8]:
        counter += 1
    if input[2] == input[4] == input[6]:
        counter += 1
    return result and counter < 2        


def get_winner(input):
    for i in range(3):
       r = 3 * i
       if input[r] == input[r + 1] == input[r + 2]:
           return input[r]
       if input[i] == input[i + 3] == input[i + 6]:
           return input[i]
    if input[0] == input[4] == input[8]:
        return input[0]
    if input[2] == input[4] == input[6]:
        return input[2]
    return ""        


def get_current_stat(input):
    if not is_possible(input):
        return "Impossible"
    if get_winner(input) != "":
        return f"{get_winner(input)} wins"
    if is_unfinished(input):
        return "Game not finished"
    return "Draw"


def grid_data(input):
    tokens = input.replace("_", " ")
    return [[tokens[i * 3], tokens[i * 3 + 1], tokens[i * 3 + 2]] for i in range(3)]
    
def print_grid(data):
    print('---------')
    for i in range(3):
        print('| ' + ' '.join(data[i]) + ' |')
    print('---------')


def play_turn(data):
    while True:
        tokens = input().split()
        if not all([token.isnumeric() for token in tokens]):
            print("You should enter numbers!")
            continue
        r, c = int(tokens[0]), int(tokens[1])
        if not (1 <= r <= 3 and 1 <= c <= 3):
            print("Coordinates should be from 1 to 3!")
            continue
        if data[r - 1][c - 1] != " ":
            print("This cell is occupied! Choose another one!")
            continue
        break
    data[r - 1][c - 1] = "X"
    print_grid(data)


if __name__ == "__main__":
    tokens = input()
    data = grid_data(tokens)
    print_grid(data)
    #print(get_current_stat(tokens))
    play_turn(data)