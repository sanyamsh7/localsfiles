#Write a program to read the entire content from a txt file and display it to the user.

file_name = "read_txt.txt"

with open(file_name, 'r') as f:
    print("Reading the contents of the file: ", file_name, "\n")
    print(f.read())
    print("closing the file....")
