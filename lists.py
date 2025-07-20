" Lists:- Mutable, append(), pop(), indexing"
"Lists are ordered, indexed, and mutable (you can change them)."

List = ["Deek", "Joe", "Alice", 100, True]

" Accessing elements"

print(List)
print(List[0])
print(List[-1])

" Slicing"

print(List[1:2])

" IMP - List methods"

List.append(1)
print(List)
"Adds whatever written with append function"

List.pop(1)
print(List)
"Pops out desired position value outta list"

List.insert(1, "Yasuke")
print(List)
"Adds desired value on given index. (Index/position , Value)"

List.remove("Deek")
print(List)
"Removes first occurance of given value"
"""
List.clear()
print(List)
Clears the list
"""
"""
List.sort()
print(List)
"Only works if the list contaisn single type values"
"""

print(len(List))

List.reverse()
print(List)

"""
When to Use Lists:
Data will change — adding, removing, updating.
Dynamic content — user input, real-time data, etc.
You need list methods — like .append(), .pop(), .remove().
"""