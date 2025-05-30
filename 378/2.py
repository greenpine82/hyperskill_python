import os

def calculate_file_size(size):
    d = ['B', 'KB', 'MB', 'GB']
    c = 0
    while size >= 1024:
        size //= 1024
        c += 1
    return f'{size}{d[c]}'

# run the user's program in our generated folders
os.chdir('module/root_folder')


# put your code here
text = 'Input the command'
while (user_input := input(text)) != "quit":
    cmd = user_input.split()
    if cmd[0] not in ['pwd', 'cd', 'ls'] or user_input == 'cd':
        print('Invalid command')
    try:
        if cmd[0] == 'ls':
            if user_input.find('-') == -1:
                dir = cmd[1] if len(cmd) == 2 else '.'
                print('\n'.join([name for name in os.listdir(dir) if os.path.isdir(name)]))
                print('\n'.join([name for name in os.listdir(dir) if os.path.isfile(name)]))
            else:
                dir = cmd[2] if len(cmd) == 3 else '.'
                print('\n'.join([name for name in os.listdir(dir) if os.path.isdir(name)]))
                if cmd[1].find('l') != -1:
                    if cmd[1].find('h') != -1:
                        print('\n'.join([name + ' ' + calculate_file_size(os.stat(name).st_size) for name in os.listdir(dir) if os.path.isfile(name)]))
                    else:
                        print('\n'.join([name + ' ' + str(os.stat(name).st_size) for name in os.listdir(dir) if os.path.isfile(name)]))       
        else:
            if cmd[0] == 'cd':
                os.chdir(cmd[1])
            print(os.getcwd())
    except FileNotFoundError:
        print('Exception')
        print('Invalid command')
    text = ""