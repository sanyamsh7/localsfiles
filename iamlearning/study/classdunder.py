#these special or dunder methods allow us for operator overloading and also
#to emulate the built in behaviour of python
class Employee:
    raise_amt = 1.04
    #this is also a special method
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@email.com"

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    #mostly used by the developer for debugging
    # used by repr()
    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    #meant for the end user
    def __str__(self):
        return "{} - {}".format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())

emp_1 = Employee("sanyam", "sharma", 50000)
emp_2 = Employee("Test", "user", 60000)

#example1
##print(1 + 2) #built in integer addition
##print("a" + "b") #built in string cancatenation

print(emp_1) #prnts Employee('sanyam', 'sharma', 50000) #representation of the instance
print(repr(emp_1)) # prints the representation using the __repr__ method
#print(emp_1) # by default the __str__ method works

#print(emp_1 + emp_2) #this works only if there exists the __add__ method
#
# #print(len(emp_1)) #this works only when there exists __len__ method
# above line is similar to print(emp_1.__len__())
