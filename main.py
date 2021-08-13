import pandas as pd

users = {}

def command_interpreter(command):
    if command[0] == 'create':
        create_func(command[1:])
    elif command[0] == 'delete':
        delete_func(command[1:])
    elif command[0] == 'add':
        delete_func(command[1:])
    elif command[0] =='remove':
        remove_func(command[1:])
    elif command[0] == 'change':
        change_func(command[1:])
    elif command[0] == 'search':
        search_func(command[1:])
    elif command[0] == 'print':
        print_func(command[1:])
    else:
        print('error at ' + command[0] + ' ! Command is not valid.')

def create_func(command):
    if command[0] == 'user':
        create_user(command[1:])
    elif command[0] == 'table':
        create_table(command[1:])
    else:
        print('error at ' + command[0] + ' ! Command is not valid.')

def create_user(command):
    if command[1] == 'editor' or command[1] == 'viewer':
        if command[0] in users:
            print('User ' + command[0] + ' already exists!')
        else:
            users[command[0]] = command[1]
    else:
        print(command[1] + ' is not a valid role!')

def create_table(command):
    if users[command[1]] == 'editor':
        globals()[command[0]] = pd.DataFrame()
    else:
        print('Access Denied!')

def delete_func(command):
    if command[0] == 'table':
        delete_table(command[1:])
    else:
        print(f'Error at {command[0]}. Command not found!')

def delete_table(command):
    if command[0] in globals():
        del globals()[command[0]]
    else:
        print(f'Table name {command[0]} not fount.')

while True:
    command = input().split()
    if command[0] == 'done':
        break
    command_interpreter(command)