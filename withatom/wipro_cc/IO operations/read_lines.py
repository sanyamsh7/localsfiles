#Write a program to read first n lines from a txt file. Get n as user input.
file_name = "read_lines.txt"
lines = int(input("enter number of lines to read: "))

print("reading contents of file: ", file_name)

with open(file_name, 'r') as f:
    r_lines = f.readlines()
    if lines <= len(r_lines):

        for i in range(lines):
            print(r_lines[i])
        print("closing file>.....")
    else:
        print("ERROR: NUMBER IS GREATER THAN THE LINES IN FILE.")
