class Parent(object):

    def altered(self):
        print('i am sam')
class Child(Parent):
    def altered(self):
        print('i am sanyam')
        super(Child, self).altered()
        print("i am sharma")

dad = Parent()
son = Child()

dad.altered()
son.altered()
