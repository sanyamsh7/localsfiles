#implementing sort command of unix.
import argparse

def parse_arg():

    parser = argparse.ArgumentParser()
    parser.add_argument('-o', type = str, help = 'writing stdout to a new file')
    parser.add_argument('-r', action = 'store_true', help = 'reverse')
    parser.add_argument('-f', action = 'store_true', help = 'ignore case')
    parser.add_argument('-g', action = 'store_true', help = 'sort numerically')
    parser.add_argument('file', type = str, help = 'input_file')
    return parser.parse_args()

def sort(args):
    ouput = []
    with open(args.file) as file:
        output = sorted(file,  reverse = args.r,
                                key = lambda s: s.lower() if args.f else s)
    if args.o:
        with open(args.o, 'w+') as file:
            for i in output:
                file.write(i)
    else:
        for i in output:
            print(i, end = "")
