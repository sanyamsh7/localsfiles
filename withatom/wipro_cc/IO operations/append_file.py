 #Write a program to accept input from user and append it to a txt file.
content = input("enter content to append: ")
file_name = "append_file.txt"
print("FILENAME:", file_name)
print(".................")
with open(file_name, "a") as f:
    print("appending content to file:", file_name)
    f.write(content)
    print("...content written...")
    print("...closing file...")
