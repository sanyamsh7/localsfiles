#implementing the linux cut tool.
import argparse

def parse_arg():
    parser = argparse.ArgumentParser()
    parser.add_argument('file_name', type = str,
                    help = 'Takes the name of file to carve.')
    parser.add_argument('-c', dest = 'char', type = str, help = 'Characters to carve.')
    parser.add_argument('-d', dest = 'delimit', type = str,  help = 'Delimiter')
    parser.add_argument('-f', dest = 'field', type = int, nargs = 2, help = 'Fields to display.')
    return parser.parse_args()

def cut(arg):
    with open(arg.file_name, 'r') as f:
        data = f.readlines()
    for c in data:
        if arg.char:
            arg.char = list(map(int, arg.char.split('-', 1)))
            if len(arg.char) == 1:
                print(c[arg.char[0]]) #index bug
            else:
                print(c[arg.char[0]: arg.char[1] + 1]) #spaces bug
        elif arg.delimit and arg.field:
            line = c.split(arg.delimit)
            if len(line)> arg.field[0]:
                print(line[arg.field[0] - 1], line[arg.field[1] - 1])
cut(parse_arg())
