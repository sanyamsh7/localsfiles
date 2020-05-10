import sys
import re

def sed(*args):
    command = args[0].split('/')
    if command[0] == 's':
        subs(command, args[1])
    elif command[0] =='r':
        r_file(command, args[1])

def subs(*s_args):
    command = s_args[0]
    regex = re.compile(command[1])
    with open(s_args[1]) as f:
        string = f.read()
    string = regex.sub(command[2], string)
    with open(s_args[1], 'w') as f:
        f.write(string)

def r_file(*r_args):
    with open(r_args[1]) as file:
        print(file.read())

script, command, file = sys.argv
sed(command, file)
