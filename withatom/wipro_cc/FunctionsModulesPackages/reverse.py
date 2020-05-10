# Write a function to return the reverse of a string.
# Sample String : "1234abcd"
# Expected Output : "dcba4321

def reverse(string):
    return string[::-1]

string = input("enter your string: ")
print("reverse string: ", reverse(string))
