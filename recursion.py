
" Recursion:- Function calling itself"

"Its when a function calls itself,\n"
"to solve a smaller version of the orignal problem"

"# STRUCTURE"
"""
def function_name(params):
    if base_condition:
        return some_value
    else:
        return function_name(smaller_input)
"""

" Example"

def factorial(number):
    if number == 0:
        return 1
    else:
        return number * factorial(number - 1)
    
print(factorial(27))

def sum(number):
    if number == 1:
        return 1
    else:
        return number + sum(number - 1)

print(sum(10))
