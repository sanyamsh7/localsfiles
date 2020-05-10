#Write a program to count the frequency of a user entered word in a txt file

file = "frequency_text.txt"
with open(file, 'r') as f:
    print("READING CONTENTS OF FILE:", file)
    content = f.read()

word = input('enter word: ')
print('frequency of word in file:', content.count(word))
