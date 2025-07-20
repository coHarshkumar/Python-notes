
" Loops:- for, while, break, continue"
" For loop - for known repetitions"
"Loops through each element in a sequence (list, string, tuple, etc.)"

Cars = ["Amg", "BMW", "Audi"]
for car in Cars:
    print(car)

" Range function"

for i in range(3):
    print(i)

for i in range(100,1000):
    print(i)

for i in range(1,10,3):
    print(i)
"The last value determines diffrence between the ordered range"

" While Loop - for unkown length"

Damage = 0

while Damage < 101:
    print("Attack", "Damage given : ",Damage)
    Damage += 10
    if Damage == 100:
        print("end")
        
"""
" Break - exits the loop immediately, even if the loop condition is still True."

for damage in range(100, 1000, 100):
    print("Damage : ", damage)
    if damage == 1000:
        print("And thats your Enddddd!!!")
        break
        
   

while Damage < 101:
    print("Attack")
    Damage += 10
    if Damage == 100:
     print("Defeated")
     break
 
"""
" Continue - Skips the current iterations, And goes straigh to loop afterwards"

for i in range(10,100):
    if i == 91:
        continue
    print(i)