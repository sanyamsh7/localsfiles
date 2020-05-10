#impementing sed command of UNIX.

import sys

_ , option, file = sys.argv

option = option.split('/')

with open(file) as f:
    f.mode = 'r'
    string = f.readlines()

if option[0] == 's'
    with open(file, 'w+') as f:
        if option[3] == "g":
            for s in range(len(string)):
                line = string[s].split()
                for i in range(len(line)):
                    if line[i] == option[1]:
                        line[i] = option[2]
                line = ' '.join(line)
                f.write(line + "\n")
