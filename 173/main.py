from random import randint, choice

def generate():
    return f'{randint(2, 9)} {choice(["+", "-", "*"])} {randint(2, 9)}'


def parse(task):
    is_operator = lambda char: char in ["+", "-", "*", "/"]
    
    digits = []
    operators = []
    tokens = []
    level = 0
    block_level = 1
    for c in task:
        if c.isnumeric():
            digits.append(c)
            continue
        if is_operator(c):
            operators.append(c)
            continue
        if c == " ":
            if len(digits): 
                tokens.append("".join(digits))
                digits.clear()
                level += 1
            elif level > block_level:
                tokens.append(operators.pop())
                level -= 1
    if len(digits): 
        tokens.append("".join(digits))
        digits.clear()
    if len(operators):
        tokens.append(operators.pop())
    return tokens


def get_result(task):
    stack = []

    for token in parse(task):
        if token.isnumeric():
            stack.append(int(token))
        elif token == "+":
            stack.append(stack.pop(-2) + stack.pop())
        elif token == "-":
            stack.append(stack.pop(-2) - stack.pop())
        elif token == "*":
            stack.append(stack.pop(-2) * stack.pop())
        elif token == "-":
            stack.append(stack.pop(-2) / stack.pop())
    return stack.pop()


def check_int(s):
    if len(s) < 1:
        return False
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()


def get_option():
    print('Which level do you want? Enter a number:')
    print('1 - simple operations with numbers 2-9')
    print('2 - integral squares of 11-29')
    while (user_input := input()) not in ['1', '2']:
        print("Incorrect format.")
    return int(user_input)


def lv1_quiz():
    quiz = generate()
    print(quiz)
    while not check_int(user_input := input()):
        print("Incorrect format.")
    if int(user_input) != get_result(quiz):
        print("Wrong!")
        return 0
    
    print("Right!")
    return 1


def lv2_quiz():
    number = randint(11, 29)
    print(number)
    while not check_int(user_input := input()):
        print("Incorrect format.")
    if int(user_input) != number ** 2:
        print("Wrong!")
        return 0
    
    print("Right!")
    return 1


if __name__ == "__main__":
    mark = 0
    options = ['simple operations with numbers 2-9', 'integral squares of 11-29']
    option = get_option()
    for i in range(5):
        if option == 1:
            mark += lv1_quiz()
        elif option == 2:
            mark += lv2_quiz()
    print(f"Your mark is {mark}/5. Would you like to save the result? Enter yes or no.")
    if input() in ['yes', 'YES', 'y', 'Yes']:
        print('What is your name?')
        name = input()
        with open('results.txt', 'a') as f:
            f.write(f'{name}: {mark}/5 in level {option} ({options[option - 1]})')
            f.close()
            print('The results are saved in "results.txt".')