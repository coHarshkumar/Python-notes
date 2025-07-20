" Sets:- Unordered, no duplicate"

Sets = {"Katana", "Kunai", "Shuriken"}

" Set methods"

Sets.add("Bow")
print(Sets)

Sets.remove("Kunai")
print(Sets)

print(len(Sets))


" Set Opreation"

A = {1,2,3,4}
B = {4,1,5,6}

print(A.union(B))
"Unites both sets"

print(A.intersection(B))
"Removes what common in both"

print(A.difference(B))
"Gives the uncommon in both"