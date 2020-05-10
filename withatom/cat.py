#imlementing cat command of UNIX.
import argparse

#function for all arguments
def parse_arg():
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', metavar = 'F', type = str, nargs = "+",
                                            help = 'input files')
    parser.add_argument('->', "--caret", type = str,
                                            help = "copy inputfile > outputfile")
    parser.add_argument('-n', help = 'lines with the line numbers',
                                            action = 'store_true')
    parser.add_argument('-e', help = "$ at the end of lines(wiht -v)",
                                            action = 'store_true')
    parser.add_argument('-b', help = "omits line numbers from blank lines(with -n)",
                                            action = 'store_true')
    return parser.parse_args()

def caret(arg, f):
    with open(arg.caret, 'a+') as new_f:
        new_f.write(f.read())

def line_n(arg, file):
    n = 0
    for line in file:
        n+=1
        if arg.b:
            if len(line) == 1:
                print(line, end ="")
                continue
        print("line:"+str(n), line, end = "")
    print("--------------",'\n', end ="")

def dollar(arg, file):
    for line in file:
        for ch in line:
            if ch=="\n":
                ch = "$"
            print(ch,end = "")
        print(end = "\n")

def cat(arg):
    for file in arg.filenames:

        with open(file, 'r') as file:
            if arg.n:
                line_n(arg, file)
            elif arg.e:
                dollar(arg, file)
            elif arg.caret:
                caret(arg, file)
            else:
                print(file.read())
cat(parse_arg())
