class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first =  first
        self.last =  last
        self.pay = pay
        self.email = first + '.' + last + '@email.com'

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

class Developer(Employee): #python follows the chain until it finds what it
                                        #is looking for , this chain is also called METHOD RESOLUTION ORDER
    raise_amt = 1.10    #this will not update the variable of parent this will only work for the instance of child

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)  #similar to Employee.__init__(self, first, last, pay)
       #above line inherits the init of parent
        self.prog_lang = prog_lang

class Manager(Employee):

    def __init__(self, first, last, pay, employees = None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employee = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print("-->", emp.fullname())


dev_1 = Developer("Sanyam", "Sharma", 50000, "python")
dev_2 = Developer("Test", "Employee", 60000, "java")

print(help(Developer)) #gives mrd
print(dev_1.email)
print(dev_2.email)

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)

print(dev_1.email)
print(dev_1.prog_lang)

mgr_1 = Manager("Sue", "Smith", 90000, [dev_1])

print(mgr_1.email)
mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_1)
mgr_1.print_emps()
