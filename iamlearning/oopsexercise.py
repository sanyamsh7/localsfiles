## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass
## ??
class Dog(Animal):
    def __init__(self, name):
        ## ??
        self.name = name
## ??
class Cat(Animal):
    def __init__(self, name):
        ## ??
        self.name = name

## person is a object
class Person(object):
    def __init__(self, name):
        ## person has a name of name 
        self.name = name
        ## Person has-a pet of some kind
        self.pet = None
## employee is a person
class Employee(Person):
    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic?
        super(Employee, self).__init__(name)
        ## employee has a salary of salary 
        self.salary = salary
## fish is a object 
class Fish(object):
    pass
## salmon is a fish 
class Salmon(Fish):
    pass
## halibut is a fish 
class Halibut(Fish):
    pass
## rover is-a Dog
rover = Dog("Rover")
## saran is a cat
satan = Cat("Satan")
## mary is a person
mary = Person("Mary")

## mary has a pet which is a satan
mary.pet = satan
## frank is a employee which has a name frank and salary 120000
frank = Employee("Frank", 120000)

## frank has a pet which is a rover
frank.pet = rover
## flipper is a fish 
flipper = Fish()
## crouse is a salmon
crouse = Salmon()
## harry is a halibut 
harry = Halibut()
