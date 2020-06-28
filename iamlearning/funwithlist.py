#defining a space seperated string with items in it
ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")
#making a list of the above string with space seperated items in it
#thus using split() method
stuff = ten_things.split(' ')
#creating another list of things 
more_stuff = ["Day", "Night", "Song", "Frisbee",
              "Corn", "Banana", "Girl", "Boy"]
#this loop goes on till the length of the list is not equal to 10
while len(stuff) != 10:
    #poping out the elements at each iteration and assigning it to a variable 
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    #appending it at the end of the stuff list created earlier
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")
#printing the modified list 
print("There we go: ",stuff)

print("Let's do some things with stuff.")
#accessing element at 1
print(stuff[1])
#accessing element at last of stuff
print(stuff[-1])
#popping the last element
print(stuff.pop())
#joining the list again to create a string 
print(' '.join(stuff))
#joining particular elements
print('#'.join(stuff[3:5]))

