import os
import shutil

def calculate_file_size(size):
    d = ['B', 'KB', 'MB', 'GB']
    c = 0
    while size >= 1024:
        size //= 1024
        c += 1
    return f'{size}{d[c]}'


def cmd_remove(cmd):
    if len(cmd) < 2:
        print('Specify the file or directory')
        exit()
    try:
        if os.path.isdir(cmd[1]):
            shutil.rmtree(cmd[1])
        else:
            os.remove(cmd[1])
    except FileNotFoundError:
        print('No such file or directory')
        exit()


def cmd_makedir(cmd):
    if len(cmd) < 2:
        print('Specify the name of the directory to be made')
        exit()
    if os.path.exists(cmd[1]):
        print('The directory already exists')
        exit()
    try:
        os.mkdir(cmd[1])
    except Exception as e:
        print(e)
        exit()


def cmd_move(cmd):
    if len(cmd) < 3:
        print('Specify the current name of the file or directory and the new location and/or name')
        exit()
    if os.path.isfile(cmd[2]):
        print('The file or directory already exists')
        exit()
    try:
        shutil.move(cmd[1], cmd[2])
    except FileNotFoundError:
        print('No such file or directory')
        exit()


def cmd_copy(cmd):
    if len(cmd) < 3:
        print('Specify the file')
        exit()
    if len(cmd) > 3:
        print('Specify the current name of the file or directory and the new location and/or name')
        exit()
    if not os.path.isfile(cmd[1]):
        print('No such file or directory')
        exit()
    if os.path.isfile(cmd[2]):
        print(f'{os.path.basename(cmd[2])} already exists in this directory')
        exit()
    if os.path.exists(cmd[2]):
        des = cmd[2]
        if os.path.isdir(des):
            des += f'/{os.path.basename(cmd[1])}'
        if os.path.isfile(des):
            print(f'{os.path.basename(des)} already exists in this directory')
            exit()
        try:
            shutil.copy(cmd[1], des)
        except PermissionError:
            print('No such file or directory')
            exit()
    else:
        print('No such file or directory')
        exit()


# run the user's program in our generated folders
os.chdir('module/root_folder')


# put your code here
text = 'Input the command'
while (user_input := input(text)) != "quit":
    cmd = user_input.split()
    supported_cmds = ['pwd', 'cd', 'ls', 'rm', 'mv', 'cp']
    if cmd[0] not in supported_cmds or user_input == 'cd':
        print('Invalid command')
    try:
        if cmd[0] == 'cp':
            cmd_copy(cmd)
        if cmd[0] == 'rm':
            cmd_remove(cmd)
        if cmd[0] == 'mkdir':
            cmd_makedir(cmd)
        if cmd[0] == 'mv':
            cmd_move(cmd)
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
        print('No such file or directory')
    text = ""