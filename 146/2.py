import random

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

status = ""
domino_snake = [ pieces[index + 14] ]
if index < 7:
    status = "It's your turn to make a move. Enter your command."
    computer_pieces.pop(index)
else:
    status = 'Computer is about to make a move. Press Enter to continue...'
    player_pieces.pop(index - 7)

print("=" * 70)
print(f'Stock size: {len(stock_pieces)}')
print(f'Computer pieces: {len(computer_pieces)}')
print("")
print(f'{domino_snake[0]}')
print("")
print(f'Your pieces: {player_pieces}')
print('\n'.join([f'{i + 1}:{p}' for i, p in enumerate(player_pieces)]))
print("")
print(f'Status: {status}')