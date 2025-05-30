import os

# run the user's program in our generated folders
os.chdir('module/root_folder')


# put your code here
text = 'Input the command'
while (user_input := input(text)) != "quit":
    cmd = user_input.split()
    if cmd[0] not in ['pwd', 'cd'] or user_input == 'cd':
        print('Invalid command')
    try:
        if cmd[0] == 'cd':
            os.chdir(cmd[1])
        print(os.getcwd())
    except FileNotFoundError:
        print('Invalid command')
    text = ""