import random


def print_domino_snake(s):
    if len(s) > 6:
        print(f'{s[0]}{s[1]}{s[2]}...{s[-3]}{s[-2]}{s[-1]}')
    else:
        print(''.join([str(i) for i in s]))


def is_draw(domino_snake):
    left_number = domino_snake[0][0]
    right_number = domino_snake[-1][1]
    left_counter = 0
    right_counter = 0
    for p in domino_snake:
        for v in p:
            if v == left_number:
                left_counter += 1
            if v == right_number:
                right_counter += 1
    return left_counter == 8 and right_counter == 8


def player_choice(player_pieces, stock_pieces, domino_snake):
    size = len(player_pieces)
    print("It's your turn to make a move. Enter your command.")
    s = input()
    while True:
        if s.isnumeric() and -size <= int(s) <= size:
            break
        print("Invalid input. Please try again.")
        s = input()
    choice = int(s)
    if choice == 0 and len(stock_pieces) > 0:
        player_pieces.append(stock_pieces.pop())
    elif choice > 0:
        domino_snake.append(player_pieces.pop(choice - 1))
    elif choice < 0:
        domino_snake.insert(0, player_pieces.pop(abs(choice) - 1))

    if len(player_pieces) == 0:
        return "Status: The game is over. You won!"
    return ""
    

def cpu_choice(computer_pieces, stock_pieces, domino_snake):
    size = len(computer_pieces)
    print("Computer is about to make a move. Press Enter to continue...")
    input()
    choice = random.randint(-size, size)
    if choice == 0 and len(stock_pieces) > 0:
        computer_pieces.append(stock_pieces.pop())
    elif choice > 0:
        domino_snake.append(computer_pieces.pop(choice - 1))
    elif choice < 0:
        domino_snake.insert(0, computer_pieces.pop(abs(choice) - 1))

    if len(computer_pieces) == 0:
        return "Status: The game is over. The computer won!"
    return ""
    

pieces = [[a, b] for a in range(7) for b in range(a, 7)]

repeat = True
while repeat:
    random.shuffle(pieces)
    repeat = all([i[0] != i [1] for i in pieces[14:]])
stock_pieces = pieces[:14]
computer_pieces = pieces[14:21]
player_pieces = pieces[21:]

index = -1
max = -1
for i, p  in enumerate(pieces[14:]):
    if p[0] == p[1] and p[0] > max:
        index = i
        max = p[0]

player = {'pieces': player_pieces, 'choice': player_choice}
computer = {'pieces': computer_pieces, 'choice': cpu_choice}
players = [player, computer]
domino_snake = [ pieces[index + 14] ]
if index < 7:
    computer_pieces.pop(index)
    first_player = 0
else:
    player_pieces.pop(index - 7)
    first_player = 1


status = ""
while True:
    print("=" * 70)
    print(f'Stock size: {len(stock_pieces)}')
    print(f'Computer pieces: {len(computer_pieces)}')
    print("")
    print_domino_snake(domino_snake)
    print("")
    print('Your pieces:')
    print('\n'.join([f'{i + 1}:{p}' for i, p in enumerate(player_pieces)]))
    print("")
    if status != "":
        print(status)
        break
    player = players[first_player]
    status = player['choice'](player['pieces'], stock_pieces, domino_snake)
    if is_draw(domino_snake):
        status = "Status: The game is over. It's a draw!" if status == "" else status
    first_player = (first_player + 1) % 2