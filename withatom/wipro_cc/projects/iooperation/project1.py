# HINTS TO FIND SECRET MESSAGE:
# 1. THE NUMBER OF LINES TELLS ABOUT THE TIME OF MEETING
#         NOTE: 1 <= NUMBER OF LINES <= 24
#         IF THE NUMBER OF LINES IS EXCEEDING 12, YOU NEED TO CONVERT IT TO 12 HRS.
#         FORMAT.
# 2. THE WORD APPEARING FOR THE MAXIMUM NUMBER OF TIMES TELLS YOU THE MEETING PLACE.
#     NOTE: MEETING PLACE WILL BE A STREET NAME
#
def time_and_place(FILE_NAME):
    freq = dict()
    with open(FILE_NAME, "r") as file:
        content = file.readlines()

    total_lines = len(content)

    for line in content:
        string = line.strip("\n")
        words = string.split()

        for word in words:
            word = word.strip(".")
            if word not in freq:
                freq.update({word: 1})
            else:
                freq[word] += 1

    freq_values = freq.values()
    max_occurrence = max(freq_values)
    for key in freq.keys():
        if freq[key] == max_occurrence:
            place = key
    return (total_lines, place)

FILE_NAME =  input("enter file name: ")
lines, place = time_and_place(FILE_NAME)
if lines > 12:
    time = lines - 12
    print("Meeting time: {}P.M".format(time))
else:
    time = lines
    print("Meeting time: {}A.M".format(time))
print("Meeting place:", place, "street")
