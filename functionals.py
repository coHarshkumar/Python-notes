" Functions:- def, return, *args, **kwargs"

"What is a function ? - A block of code that does a specific job,\n"
"which's defined once and then can be used anytime"

" Define a function"

def say():
    print("Hello warrior")
say()

" Function with input parameter"

def hello(name):
    print("Welcome, ",name)
hello("Harsh")
hello("Henry")

" Function that returns a value"

def multiplydivide(v):
    return v * v + 2 - 100
" we defined a function to perform and \n"
"left to add a value for user, and when we get that, function runs"
result = multiplydivide(2)
print(result)

" *args - Many values can be stores like lists"

def buy(*cars):
    for car in cars:
        print(car, "is my dream, Imma have it.")
buy("BMW amg","Audi r8","Rolls royas")

" **Kwargs - Many keys can be there like as of a dictionary"

def report(**results):
    for key, value in results.items():
        print(key, ":" ,value )
report(Maths = 90, English = 20, Physics = 68)
