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
    status = 'player'
    computer_pieces.pop(index)
else:
    status = 'computer'
    player_pieces.pop(index - 7)

print(f'Stock pieces: {stock_pieces}')
print(f'Computer pieces: {computer_pieces}')
print(f'Player pieces: {player_pieces}')
print(f'Domino snake: {domino_snake}')
print(f'Status: {status}')
