class Employee:
    raise_amount = 0
    first = "sam"
    def __init__(self, first, last, pay):

        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' +  last + "@company.com"
        Employee.raise_amount  += 1

    @classmethod
    #in these we receive the class as the first argument
    #instead of instance (self) in it
    #these are accessed only via class(cls)
    def set_raise(cls, amount):
        cls.raise_amount = amount

    #classmethod can also be used as alternative constructors
    @classmethod
    def from_string(cls, emp_str):
        print(cls.first)
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)

    #staticmethod do not pass either the instance or the class as the first
    #argument
    #these can also be accessed by both class instance or the class itself
    #class or class instance shouldn't be accessed within the static method
    #no self or cls
    @staticmethod
    def is_work_day(day):
        print(day)
##        if day.weekday() == 5 or day.weekday() == 6:
##            return False
##        return True

emp1 = Employee("sanyam", "sharma", 50000)
emp2 = Employee("test", "user", 60000)
string = "sanyam-sharma-50000"

print(emp1.from_string(string))
