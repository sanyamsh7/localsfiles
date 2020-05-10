# Given the participant's score sheet for your University Sports Day, you are
# required to find the runner-up score. You have scores. Store them in a list and
# find the score of the runner-up.

input_list = list(map(int, input().split())) #input space seperated numbers
print('list of scores is:', input_list)
try:
    largest = max(input_list)
    while largest in input_list:
        input_list.remove(largest)
    print("The runner-up score is:", max(input_list))

except :  #handling the case: [5,5,5,5]
    print("No runner-ups, everyone is a winner.")
