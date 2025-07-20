" Data Types:- int, float, str, list, tuple, dict, set, bool."

String = "Harsh"
Int = 17
Float = 17.3
List = [1, 2, 3, "2"]
Tuple = (1, 2, 3, 4, 5)
Dict = {
"Name": "Harsh",
"Age": "17",
"Student" : True
}

"Functions in Dictionaries"

" Prints the Key value stored in dict"
print(Dict["Name"])         

" Updats the value of key"
Dict["Age"] = "18" 
print(Dict["Age"])

" To get keys (safer way)"
print(Dict.get("Name"))

" Get all keys/values"
print(Dict.values())
print(Dict.keys())

" Get all keys along values"
for key, value in Dict.items():
    print(key, ":", value)

" Remove a specific key"
Dict.pop("Name")
print(Dict)

