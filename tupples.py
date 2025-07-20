" Tuples:- Immutable, ordered"

"Cant be changed. Cant be messed with. Just used wisely"

Tupple = ("Henry" ,"Arthur" ,"Walter" ,"Corrupt", 1000, True)

" Accessing elements"

print(Tupple[0])

print(Tupple[-1])

print(Tupple[1:2])
"Above prints in between elements"

" Menthods of tupple"

print(Tupple.count("Henry"))
"Counts the number of time the value has came"

print(Tupple.index("Walter"))
"Gives index of value"

print(len(Tupple))

"""
When to Use Tuples?
Data that should never change
Fixed configuration
Better performance (theyre slightly faster than lists)
"""