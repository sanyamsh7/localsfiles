def ispalindrome(name):
    if name[:] == name[::-1]:
        print("Yes it is a palindrome.")
    else:
        print("Not a palindrome.")

def count_the_vowels(name):
    vowels = ["a", "e", "i", "o", "u"]
    count = 0
    for letter in name:
        if letter in vowels:
            count += 1
        else:
            continue
    print("Number of vowels:", count)

def frequency_of_letter(name):
    freq = dict()
    freq_list = []
    for letter in name:
        if letter == " ":
            continue
        elif letter not in freq:
            freq.update({letter: 1})
        else:
            freq[letter] += 1
    for key in freq:
        freq_list.append("{}-{}".format(key, freq[key]))
    print("Frequency of letters:", ",".join(freq_list))
