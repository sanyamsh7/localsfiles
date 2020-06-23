class MyStuff(object):
    def __init__(self):
        self.tangerine = "And now a thousand years between"

    def apple(self):
        print("I AM CLASSY APPLES!")

#instantiating an object alot like calling a function
#giving all the functions in class to thing object(new empty object)
#self is the empty object that python made for us
#MyStuff() instantiates the object 
thing = MyStuff()#this line assigns this newly created object to thing variable
thing.apple()
print(thing.tangerine)
