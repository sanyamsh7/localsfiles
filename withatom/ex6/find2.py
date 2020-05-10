#implementing find command
import argparse
import pathlib
from sys import exit
from os.path import exists
from glob import glob
from os import remove

def parse_arg():

    parser = argparse.ArgumentParser()
    parser.add_argument("-.", dest = 'dot', action = 'store_true',
                            help = "search files in current location")
    parser.add_argument("-name", type = str,
                            help = " requires the name of file")
    parser.add_argument("-type", type = str,
                            help = "searche files of given type(wildcards allowed)")
    parser.add_argument("-print", action = "store_true",
                            help = "prints the content of the file")
    parser.add_argument("-exec", type = str, choices = ['delete', 'count'],
                            help = "executes the given command on the file")
    return parser.parse_args()

def find(arg):
    if arg.dot:
        if arg.name and not arg.type:
            path = (pathlib.Path.cwd() / arg.name)
            return find_name(path, arg)
        elif arg.type and not arg.name:
            return find_type(arg.type, arg)
        else:
            print('Error: either use -name or -type')
    else:
        print('Error: dot parameter not given')
        exit(1)


def find_name(path, arg):
    if exists(path):
        if arg.print:
            with open(path, 'r') as file:
                print("---------------------\n")
                print(file.read())
        print("FILE EXISTS AT:",path)
    else:
        print("Error: file does not exist in current location")
        exit(1)

def find_type(type, arg):
    count = 0
    for f in glob(type):
        count+=1
        if arg.print and not arg.exec:
            with open(f, 'r') as file:
                print("FILE_NAME",f, end = "-------\n")
                print(file.read())
        elif arg.exec == 'delete':
            remove(f)

        else:
            print("FILE",f)
    if arg.exec == 'count':
        print('total number of files of type -',type, 'are:', count)

find(parse_arg())
