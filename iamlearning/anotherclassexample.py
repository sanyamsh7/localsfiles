#!/usr/bin/env python3
#creating a class 
class Song(object):
##    def again_nothing(self, lyrics):
##        self.lyrics = lyrics
#from the above function it is clear __init__ is necessary
#so that the list that we are passing below in the class Song()
#is passed to the lyrics variable in __init__
    def __init__(self, lyrics):
    #me varaible becomes one of the attributes of Song() object
    #when we use self with it so that we can use this variable in other
    #methods of class Song() like below 
        self.me = lyrics
    #creating another function self
    #if we dont do this the python will raise TypeError saying
    #sing_me_a_song requires 0 argument 1 given
    #so here self works as a imaginary argument for the same function
    def sing_me_a_song(self):
        for line in self.me:
            print(line)
    #remove self to see the woring of it
    def nothing(self,name):
        self.words = name.split()
        print(self.words)
        print("Nothing here",name)
        print(self.me)
        
happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally aroung the family",
                        "With pockets full of shells"])
#here as the sing_me_a_song() has self in it above so the happy_bday object is
#passed in it(this is how the python works behind)
happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()
happy_bday.nothing("sanyam")
