#input format(first we have to take all the inputs in new lines-->reason for using the first loop)
#2          number of test cases
#3          numbers in first sequence(sequence 1)
#4          numbers in second sequence(sequence 2)
#output format:
#1 1 2      for sequence 1
#1 1 2 2    for sequence 2
#console should look like
#2
#3
#4
#1 1 2
#1 1 2 2 

#code
#number of test cases input by user
N = int(input())
#empty list of integers
integer_list = []                           

for a in range(N):
    #taking input from the user in new lines putting in integer list
    integer_list.append(int(input()))
    
#for every test_case
for b in integer_list:
    #creating an empty list
    z = []
    #intializing this list from 1 
    sum_sequence = [1]
    #final result sequence empty list
    final_sequence = []
    
    #main code logic
    for i in range(1, b+1):
        for j in range(i):
            #creating a list [1,2,2,3,3,3,4,4,4,4,........]
            z.append(i)
        #appending sum in sum_sequence list
        sum_sequence.append(sum_sequence[i-1]+z[i-1])
        #below two lines create the entire sequence
        final_sequence.append(sum_sequence[i-1])    
        final_sequence.append(z[i-1])
    #printing the required values upto N terms
    for l in range(b):
        print(final_sequence[l], end = " ")
    #putting an empty string as required in the test cases of the problem
    print("")
    
