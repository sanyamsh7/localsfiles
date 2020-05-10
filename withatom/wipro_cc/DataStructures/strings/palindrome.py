#Write a program that will check whether a given String is Palindrome or not.
string = input("enter your string: ")

if string[:] == string[::-1]:
    print("the string is palindrome.")
else:
    print("the string is not palindrome.")
