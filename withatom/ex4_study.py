import argparse
#the program displays nothing when no positional or optional argument is specified.
#with only these two lines we get an extra argument --help or -h ,
# nothin else.

#parser = argparse.ArgumentParser()
#parser.parse_args()

###now introducing positional arguments

#parser = argparse.ArgumentParser()
#parser.add_argument('echo', help = 'echo the string you have specified')

#to specify the options which the program is willing to accept.
#parse_args returns some data from the options specified(in the case echo)

#print(args.echo) #now we have to specify the option while calling the program
#parser.add_argument('square', help = 'display a square of the number', type = int)

#argparse takes the arguments as strings

#args = parser.parse_args()
#print(args.square**2)
#print(args.echo)

###now introducing optional arguments
#there will be no error when running the program without optional arguments
parser = argparse.ArgumentParser()
parser.add_argument('--verbosity', help = 'increase output verbosity',
                    action = 'store_true')
args = parser.parse_args()
if args.verbosity: # this will be true only if we specify verbosity argument
                    #along with any integer
    print('verbosity turned on')
else:
    print('verobsity is off')
#alot more functionality is explained on below links
#https://docs.python.org/3/howto/argparse.html
#https://docs.python.org/3/library/argparse.html
