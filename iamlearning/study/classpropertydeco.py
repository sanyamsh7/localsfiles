#property decorator allows


class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last
##        self.email = first + "." + last + "@email.com"

    # one solution is to define the email as a method instead of the attribute
    #but for this sol. we will have to change each occurrence of email in the code
##    def email(self):
##        return "{}.{}@email.com".format(self.first, self.last)

    # better solution to this
    # to use the method defines above as an attribute and not affect the
    # entire code with the changes made we use property decorator
    # this will let us access the method like an attribute print(emp_1.email)
    @property
    def email(self):
        return "{}.{}@email.com".format(self.first, self.last)

    def fullname(self):
        print(self.email)
        return "{} {}".format(self.first, self.last)

emp_1 = Employee("sanyam", "sharma")

emp_1.first = "sam"

#after above line the email attribute does not change but first and fullname()
#gets updated (problem statement)
##print(emp_1.first) #sam
##print(emp_1.email) #sanyam.sharma@gmail.com
##print(emp_1.fullname()) # sam sharma

#print(emp_1.email()) #sam.sharma@email.com
#now by using the deco
print(emp_1.email) #the method can now be used as attribute
#we can even do this on fullname to access the method like an attribute
