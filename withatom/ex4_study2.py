#Here we compare other cmd-line parsing libraries.
#the alternative to argparse lib are docopt and click
##for argparse --->
#import argparse
#parser = argparse.ArgumentParser()
#subparser = parser.add_subparsers()

#hello_parser = subparser.add_parser('hello')
#goodbye_parser = subparser.add_parser('goodbye')
#--> now we have to commands as arguments (hello) and (goodbye)
#args = parser.parse_args()
##for docopt --->
#if we run this the help message which is a docstring
#is echo on the terminal and it remains same when we
#specify hello or goodbye arguments in the terminal.
#"""Greater.

#Usage:
#    ex4_study2.py hello
#    ex4_study2.py goodbye
#    ex4_study2.py -h | --help
#Options:
#    -h --help    Show this screen
#"""
#from docopt import docopt

#arguments = docopt(__doc__)
##for click --->
import click

@click.group()
def greet():
    pass

@greet.command()
def hello(**kwargs):
    pass

@greet.command()
def goodbye(**kwargs):
    pass

greet()
