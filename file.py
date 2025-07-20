" File Handling:- open(), read(), write(), with"

" open( Function)"

"""
'r'  read (default)
'w'  write (overwrites)
'a'  append (adds to end)
'x'  create new file (error if exists)
'b'  binary (for images, videos etc)
't'  text mode (default)
"""

" Creating a file"

file  = open("Warrior.txt",  "w")
file.write("I am henry\n" \
"Iam the best AI dev\n" \
"I am the best and foreveen will be") # Adds content to file
file.close()

" Reading file"
"""
.read()  reads full file
.readline()  reads one line
.readlines()  reads all lines into a list
"""

file = open("Warrior.txt", "r")
content = file.read()
print(content)
file.close()

file = open("Warrior.txt", "r")
content2 = file.readlines()
print(content2)

" Appending to file"

file = open("Warrior.txt", "a")
file.write("\nAnd imma have my dream life")
file.close()

# Result

file = open("Warrior.txt", "r")
content3 = file.read()
print(content3)
file.close()

" Using with Block"

with open("Warrior.txt" , "r") as file:
    content = file.read()
    print(content)
# Auto closes the file — cleaner and safer.

with open("Warrior.txt", "a") as file:
    file.write("\nAND?")

" Check if File Exists"

import os
if os.path.exists("Warrior.txt"):
    print("Exists")
else:
    print("Dosent")
