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


def print_grid(input):
    tokens = input.replace("_", " ")
    list = [[tokens[i * 3], tokens[i * 3 + 1], tokens[i * 3 + 2]] for i in range(3)]
    print('---------')
    for i in range(3):
        print('| ' + ' '.join(list[i]) + ' |')
    print('---------')


if __name__ == "__main__":
    tokens = input()
    print_grid(tokens)
    print(get_current_stat(tokens))