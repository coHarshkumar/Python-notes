
" Exception Handling:- try, except, finally"

" Basic structure"

try:
    x = 10000000 / 0
except:
    print("You cant divide it by zero")

" Catching specific errors"

try:
    int("a")
except ValueError:
    print("Invalid input")
# Valueerror is a function for classifying if value is false

try:
    open("Naxius.txt")
except FileNotFoundError:
    print("File not found")

" finally Block (Always runs)"

try:
    x = 10000000 / 0
except:
    print("You cant divide it by zero")
finally:
    print("Pogram complete")


" else Block (only rune=s if no error)"

try:
    x = 10000000 / 2
except:
    print("You cant divide it by zero")
else:
    print("No error, We got = ",x)

"""
" Raising custom errors"

Hieght = -172
if Hieght < 0:
    raise ValueError("Hieght cant be negative")

"""
# raise: Forces a specific error