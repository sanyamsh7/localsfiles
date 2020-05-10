import argparse

parser = argparse.ArgumentParser()
#parser.add_argument('integers', metavar = 'N', type = int, nargs= '+',
#                    help = 'an integer for the accumulator')
parser.add_argument('square', type = int, help= 'display a square of the number')
parser.add_argument('-f1','--flag1', help = 'flag number 1',
                            action = 'store_true')
parser.add_argument('-f2','--flag2', help = 'flag number 2',
                            action = 'store_true')
parser.add_argument('-f3','--flag3', help = 'flag number 3',
                            action = 'store_true')
parser.add_argument('-op1','--optional1', help = 'first optional arg.',
                            type = int)
parser.add_argument('-op2','--optional2', help = 'second optional arg.',
                            type = int)
parser.add_argument('-op3','--optional3', help = 'third optional arg.',
                            type = int)
args = parser.parse_args()
print(args.square**2)
n1 = args.optional1
n2 = args.optional2
n3 = args.optional3
if args.flag1 and args.flag2 and args.flag3:
    print("all flags are working.")
else:
    print('nothing')#sum([n1,n2,n3]))
