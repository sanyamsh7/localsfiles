#implementing sort command of unix.
import argparse

def parse_arg():

    parser = argparse.ArgumentParser()
    parser.add_argument('-r', action = 'store_true', help = 'reverse')
    parser.add_argument('file', type = str, help = 'input_file')
    return parser.parse_args()

def sort(args):
    ouput = []
    with open(args.file) as file:
        output = sorted(file,  reverse = args.r,
                                key = lambda s: s.lower())
    return output
