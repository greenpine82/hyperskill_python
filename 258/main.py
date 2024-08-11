import random


def number_of_pencils():
    text = input('How many pencils would you like to use:')
    while True:   
        if not text.isnumeric():
            text = input('The number of pencils should be numeric')
            continue
        if (number := int(text)) <= 0:
            text = input('The number of pencils should be positive')
            continue
        return number


def first_player(names):
    player_name = input(f'Who will be the first ({names[0]}, {names[1]}):')
    while not player_name in names:
        player_name = input(f"Choose between '{names[0]}' and '{names[1]}'")
    return names.index(player_name)


def cpu_choice(number):
    cpu_input = 0
    is_winning = number % 4 != 1
    if is_winning:
        cpu_input = (number - 1) % 4
    else:
        while (cpu_input := random.randint(1, 3)) > number:
            pass

    print(cpu_input)
    return int(cpu_input)


def user_choice(number):
    user_input = input()
    while True:
        if user_input not in ['1', '2', '3']:
            user_input = input("Possible values: '1', '2' or '3'")
            continue
        if int(user_input) > number:
            user_input = input("Too many pencils were taken")
            continue
        return int(user_input)


def start_game(players, pencils):
    i = first_player([players[0]['name'], players[1]['name']])
    while(pencils > 0):
        player = players[i]
        print('|' * pencils)
        print(f"{player['name']}'s turn!")
        pencils -= player['choice'](pencils)
        i = (i + 1) % 2
    print(f"{players[i]['name']} won!")


if __name__ == "__main__":
    cpu  = {'name':  'Jack', 'choice': cpu_choice}
    user = {'name':  'John', 'choice': user_choice}
    start_game([user, cpu], number_of_pencils())