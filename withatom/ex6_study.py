#studying a bit of pathlib and glob modules
#import glob
#difference between absolute and relative paths:
#relative path points to a location in th current directory whereas, absolute
#path points to the location of the file irrespective of the current directory.

#this method can be used to find all the files in the current directory.
#for p in glob.glob('*.txt'):
#    print(p)

#import glob
#mport os
#import shutil

#while os.path considers paths as regular strings whereas, pathlib uses
#path object. this object has all the necessary methods and properties.

#for file_name in glob.glob('*.txt'):   #iterates through all the text files
#    newpath = os.path.join('archive_for_ex_6', file_name)  #joins the path strings
#    shutil.move(file_name, newpath)    #moves each file to newpath

from pathlib import Path
print(Path.cwd()) #this works same as os.getcwd()

#remaining is implemented in the find.py file.
