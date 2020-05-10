# You had saved the items and their price details in a text file, which you
# purchased yesterday from a nearby super market.
# You need to know:
# 1. How many items did you purchase?
# 2. How many items are free?
# 3. What is the total amount you had to pay?
# 4. What is the discount amount?
# 5. What is the final amount did you pay after the discount?
from sys import exit

file_name = input("Enter the file name: ")
try:
    with open(file_name, "r") as f:
        content = f.readlines()
except IOError:
    print("FILE DOES NOT EXIST")
    exit(1)

free_items = 0
amount = 0
discount = 0
items_purchased = 0

for line in content:
    if line != "\n":
        line = line.strip("\n")
        l = line.split()

        if l[1] in ["Free", "free"]:
            free_items += 1

        elif l[0] in ["Discount", "discount"]:
            try :
                discount += int(l[1])

            except ValueError:
                print("discount is not a number at line:", line)
                print("edit the item list")
                exit(1)
        else:
            try:
                amount += int(l[1])
                items_purchased += 1

            except ValueError:
                print("price is not a number at line: ", line)
                print("edit the item list")
                exit(1)
    else:
        continue

print("NO. of items purchased:", items_purchased)
print("NO. of free items", free_items)
print("Amount to pay:", amount)
print("Discount given:", discount)
print("Final amount paid:", amount-discount)
