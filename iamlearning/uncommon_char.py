
first_word = input()
second_word = input()
constant = list(set(first_word + second_word))
uncommon = ""
for letter in constant:
    if letter in first_word and letter in second_word:
        continue
    else:
        uncommon += letter
print(uncommon)
