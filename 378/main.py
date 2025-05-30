import os
import shutil
import glob


def calculate_file_size(size):
    units = ['B', 'KB', 'MB', 'GB']
    level = 0
    while size >= 1024:
        size //= 1024
        level += 1
    return f'{size}{units[level]}'


def cmd_remove(cmd):
    if len(cmd) < 2:
        print('Specify the file or directory')
        exit()
    try:
        if os.path.isdir(cmd[1]):
            shutil.rmtree(cmd[1])
        elif cmd[1].startswith('.'):
            files = glob.glob(f'*{cmd[1]}')
            if len(files) == 0:
                print(f'File extension {cmd[1]} not found in this directory')
                exit()
            else:
                for file in files:
                    os.remove(file)
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
    
    if cmd[1].startswith('.'):
        files = glob.glob(f'*{cmd[1]}')
        if len(files) == 0:
            print(f'File extension {cmd[1]} not found in this directory')
            exit()
        else:
            for file in files:
                move_file(file, f'{cmd[2]}/{file}', replace_mode=True)
    else:
        move_file(cmd[1], cmd[2])
                

def move_file(src, des, replace_mode=False):
    if os.path.isfile(des):
        if replace_mode:
            if input(f'{des} already exists in this directory. Replace? (y/n)') != 'y':
                exit()
        else:
            print('The file or directory already exists')
            exit()
    try:
        shutil.move(src, des)
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
    if not cmd[1].startswith('.') and not os.path.isfile(cmd[1]):
        print('No such file or directory')
        exit()
    if os.path.exists(cmd[2]):
        des = cmd[2]
        if os.path.isdir(des):
            des += f'/{os.path.basename(cmd[1])}'
        if os.path.isfile(des):
            print(f'{os.path.basename(des)} already exists in this directory')
            exit()
        if cmd[1].startswith('.'):
            files = glob.glob(f'*{cmd[1]}')
            if len(files) == 0:
                print(f'File extension {cmd[1]} not found in this directory')
                exit()
            for file in files:
                copy_file(file, f'{cmd[2]}/{file}', replace_mode=True)
        else:
             copy_file(cmd[1], des)
    else:
        print('No such file or directory')
        exit()


def copy_file(src, des, replace_mode=False):
    if os.path.isfile(des):
        if replace_mode:
            if input(f'{des} already exists in this directory. Replace? (y/n)') != 'y':
                exit()
        else:
            print(f'{os.path.basename(des)} already exists in this directory')
            exit()
    try:
        shutil.copy(src, des)
    except Exception as e:
        print('No such file or directory')
        exit()


def cmd_ls(cmd):
    if len(cmd) > 1 and cmd[1].find('-') != -1:
        dir = cmd[2] if len(cmd) == 3 else '.'
        names = os.listdir(dir)
        print('\n'.join([name for name in names if os.path.isdir(name)]))
        if cmd[1].find('l') != -1:
            if cmd[1].find('h') != -1:
                print('\n'.join([name + ' ' + calculate_file_size(os.stat(name).st_size) for name in names if os.path.isfile(name)]))
            else:
                print('\n'.join([name + ' ' + str(os.stat(name).st_size) for name in names if os.path.isfile(name)]))
    else:
        dir = cmd[1] if len(cmd) == 2 else '.'
        names = os.listdir(dir)
        print('\n'.join([name for name in names if os.path.isdir(name)]))
        print('\n'.join([name for name in names if os.path.isfile(name)]))


def cmd_cd(cmd):
    if len(cmd) == 1:
        print('Invalid command')
    try:
        os.chdir(cmd[1])
    except FileNotFoundError:
        print('No such file or directory')


# run the user's program in our generated folders
os.chdir('module/root_folder')


# put your code here
text = 'Input the command'
while (user_input := input(text)) != "quit":
    cmd = user_input.split()

    if cmd[0] == 'cp':
        cmd_copy(cmd)
    elif cmd[0] == 'rm':
        cmd_remove(cmd)
    elif cmd[0] == 'mkdir':
        cmd_makedir(cmd)
    elif cmd[0] == 'mv':
        cmd_move(cmd)
    elif cmd[0] == 'ls':
        cmd_ls(cmd)    
    elif cmd[0] == 'cd':
        cmd_cd(cmd)
    else:
        print('Invalid command')
    text = ""