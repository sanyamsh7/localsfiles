# Write a program to find the longest word from the txt file contents,
# assuming that the file will have only one longest word in it.

def index_len(word, index = -1):

    return (index, len(word))

FILE = "longest_word.txt"
print("TEXT_FILE:", FILE)
with open(FILE, 'r') as f:
    content = f.read()

longest = ''
for i in content.split():
    if len(longest) < len(i):
        longest = i
    else:
        continue

print("longest word in file:", FILE, "is:", longest,"--length", len(longest))
