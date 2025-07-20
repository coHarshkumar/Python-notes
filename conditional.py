" Conditionals:- if, elif, else"

"They are of three types: If, Else(If not) and Elif(Else if)."

" Basic example"

"""Input = input("Weapon : ")"""

"""if Input == "Katana":
    print("Sword fight is true battle")
elif Input == "Kunai":
    print("Hiding in shadows, True shinobi")
else :
    print("The war is over")
"""


" Multiple conditions"

War = True
AttackNow = False

if War and AttackNow:
    print("Saaaha hiireee")
elif War or AttackNow:
    print("Shinobi time")
else:
    print("Rest in honour")


" Nested conditionals"

Enemy = "Ronin"
Asasination = 10

if Enemy == "Ronin":
    if Asasination > 9:
        print("Assasinate!!!")
elif Enemy == "Ronin":
    Asasination < 9
    print("Level up")


