# Write a program to accept a welcome message through command line arguments and
#  display the file name along with the welcome message.
import sys
script, greetings = sys.argv

print("FILENAME:", script, "WELCOME MESSAGE:", greetings)
