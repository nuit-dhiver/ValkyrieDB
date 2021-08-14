
import pandas as pd


def command_interpreter(command):
    if command[0].lower() == 'create':
        create_func(command[1:])
    elif command[0].lower() == 'delete':
        delete_func(command[1:])
    elif command[0].lower() == 'alter':
        alter_func(command[1:])
    else:
        print(f'Error at {command[0].upper()}! Command is not valid.')

def create_func(command):
    if command[0].lower() == 'user':
        create_user(command[1:])
    elif command[0].lower() == 'table':
        create_table(command[1:])
    else:
        print(f'Error at {command[0].upper()}! Command is not valid.')

def delete_func(command):
    if command[0].lower() == 'table':
        delete_table(command[1:])
    else:
        print(f'Error at {command[0]}. Command not found!')

def alter_func(command):
    if command[0].lower() == 'table':
        alter_table(command[1:])
    else:
        print('Command not found!')

def create_user(command):
    print('Feature "CREATE USER" is not saupported yet!')

def create_table(command):
        globals()[command[0].lower()] = pd.DataFrame(columns=command[1:])

def delete_table(command):
    if command[0].lower() in globals():
        del globals()[command[0].lower()]
        print('Table deleted succesfuly.')
    else:
        print(f'Table name {command[0]} not fount.')
        
def alter_table(command):
    if command[1].lower() == 'add':
        if command[2].lower() == 'column':
            globals()[command[0].lower()].insert(len(globals()[command[0].lower()].columns), command[3:], '')
    if command[1].lower() == 'drop':
        if command[2].lower() == 'column':
            globals()[command[0].lower()].drop(columns = command[3:])
    if command[1].lower() == 'make':
        if command[2].lower() == 'persistant':
            globals()[command[0]].to_csv()            



while True:
    command = input().split()
    if command[0] == 'end':
        break
    command_interpreter(command)