" List Comprehension:- [x for x in iterable if condition]"

#list = [expression for item in iterable if conf=dition]

" Square of all numbers"

num = [1,2,3,4,5]
squares = [x*x for x in num]
print(squares)

" Only even numbers"

num = [1,2,3,4,5]
even = [x for x in num if x % 2 == 0]
print(even)

" Convert to uppercase"

names = ["harsh", "yasuke", "jin"]
upper = [name.upper() for name in names]
print(upper)       # ['HARSH', 'YASUKE', 'JIN']

" Nested loop in one line"

pairs = [(x, y) for x in [1, 2] for y in [3, 4]]
print(pairs)    


" If-else in list comprehension"

nums = [1, 2, 3, 4, 5]
labels = ["Even" if x % 2 == 0 else "Odd" for x in nums]
print(labels)   