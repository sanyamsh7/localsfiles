# You have a record of n students. Each record contains the student's name, and
# their percent marks in Maths, Physics and Chemistry. The marks can be floating
# values. You are required to save the record in a dictionary data type.
# Student's name is the key. Marks stored in a list is the value. The user enters
# a student's name. Output the average percentage marks obtained by that student.

print("...ENTER THE DATA OF STUDENTS...")
N = int(input("ENTER NUMBER OF STUDENTS: "))
data = dict()

for i in range(1, N+1):
    name = input("NAME: ")
    marks = list(map(int, input("MARKS: ").split()))
    data.update({name: marks})

student = input("ENTER A NAME: ")
marks =  data[student]
average = sum(marks)/3
print("AVERAGE PERCENTAGE MARKS:", average)
