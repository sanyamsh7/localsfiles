 # Write a program to accept the file name to be opened from the user,
 # if file exist print the contents of the file in title case or else handle
 # the exception and print an error message.

file_name = input("enter the file name: ")

try:
    with open(file_name, "r") as f:
        content = f.read()
    print(content.title()) # printing content in title case

except IOError:
    print("ERROR MESSAGE: The file does not exist.")
