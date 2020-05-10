# Write a program to read contents from a txt file line by line and store
# each line into a list.

file_name = "list_line.txt"

with open(file_name, 'r') as f:
    print(".....storing lines in list.....")
    list_line = f.readlines()
    print("list of lines: ", list_line)
    print(".....closing file.....")
