#implementing grep command of linux
#grep --> 'global regular expression print'
import argparse
import re
from glob import glob

def parse_arg():
    parser = argparse.ArgumentParser()
    parser.add_argument('regex', type = str, help = "pattern to find")
    parser.add_argument('file', type = str, help = "file_name or type")
    parser.add_argument('-w', help = 'avoids matching substrings')
    return parser.parse_args()

def grep(arg):
    regex = re.compile(arg.regex)
    for f in glob(arg.file):
        print("FILE: ", f)
        file(regex, f)

def file(r, file):
    with open(file, 'r') as f:
        s_list = f.readlines()  #line by line access(not efficient -->some loop
                                #iterations are wasted)
        for i in range(len(s_list)):
            word = r.findall(s_list[i])
            if word:
                #cant break the loop when there is no word because
                #for an exception the first list can also be empty.
                print("line:{}".format(i+1), s_list[i])
