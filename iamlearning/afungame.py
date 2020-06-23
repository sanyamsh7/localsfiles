#A FUN GAME 
#importing exit from sys 
from sys import exit
#exit is used to exit from the terminal
#creating a gold room fucntion 
def gold_room():
    #user interactino string
    print("This room is full of gold. How much do you take?")
    #user input as choice of user 
    choice = input("> ")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Man, learn to type a number.")
    if how_much < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("You greedy bastard!")
#creating a bear room 
def bear_room():
    #user interaction strings
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to moce the bear?")
    #bear is initially not moved
    bear_moved = False
    #
    while True:
        choice = input("> ")

        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door.")
            print("You can go through it now.")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means.")
#if the user choose to enter right then this method is called
def cthulhu_room():
    #user interaction strings
    print("Here you see the great evil Cthulhu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")
    #letting user take decisions here
    choice = input("> ")
    #if flee is the user's input then do this
    if "flee" in choice:
        #the game is started again here calling the start method 
        start()
    elif "head" in choice:
        #if head is user's input
        #then dead method is called putting the below string in why paramter
        #and printing it 
        dead("Well that was tasty!")
    else:
        #if the user's input is different
        #then the entire method is called again
        cthulhu_room()
#creating a function for death methods
#why parameter is this function takes the strings given by the caller in the functions above 
def dead(why):
    print(why, "Good job!")
    #exit(0) is for successful termination of the terminal
    exit(0)
#this function starts the entire game 
def start():
    #user interaction strings 
    print("You are in a dark room.")
    print("There is a door to yout right and left.")
    print("Which one do you take?")
    #taking user's input as choice of the user 
    choice = input("> ")
    if choice == "left":
        #calling bear_room method when the user choice is left
        bear_room()
    elif choice == "right":
        #calling cthulhu method when the user choice is right 
        cthulhu_room()
    else:
        #if the user choice is different then the expected answer
        #this string is printed
        dead("You stumble around the room until you starve.")
#calling start method to start the game
start()
        
