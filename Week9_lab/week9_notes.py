#file modes
#When you open a file, you give python 2 things
#1.) the file name
#2.) the mode

#common modes:
#"w" = write
#creates a file if it doesnt exist, and overwrites it if it does

# "r" = read only
#files can be read, but not changed
#error if the file is nonexistent

#"a" = append (adding to)
#create a file if it dosnt exist
#adds new text to the end wihtout deleting content

# with open("Week9_lab/stuff.txt", "r") as file:
#     contents = file.read()
#     print(contents)

# with open("Week9_lab/stuff.txt", "w") as file:
#     file.write("this is gonna be line 1\n")
#     file.write("this is gonna be line 2\n")
#     file.write("this is gonna be line 3\n")
#     #\n makes a new line
#     # if you forget the \n, it will just keep writing on the same line

# with open("Week9_lab/new_file.txt", "a") as file:
#     file.write("This is a new file\n")

#reading from a file
#method 1: read the whole file at once
# with open("Week9_lab/stuff.txt", "r") as file:
#     contents = file.read()
#     print(contents)

# #method 2: read the file line by line using a for loop
# with open("Week9_lab/stuff.txt", "r") as file:
#     for line in file:
#         print(line)

with open("Week9_lab/stuff.txt", "a") as file:
    file.write("this is a new line added with append\n")
    file.write("this is another new line added with append\n")