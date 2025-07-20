" OOP:- class, object, __init__, inheritance"

#OOP = a way of organizing code using classes and objects
#Helps you build scalable, reusable, and clean AI syste"


" class and object"

class Ninjas():
    pass
#class is a blueprint

ninja = Ninjas()
#object is the actual thing created from it

print(type(ninja))
#<class '__main__.Ninjas'>


" __init__() Method"
#Called automatically when object is created — used to initialize data.

class Ninjas:
    def __init__(self, name):
        self.name = name
#Self refers to the object, as of establing connection
n = Ninjas("Yaasuke")
print(n.name)

" Methods (Functions inside classes)"

class Ninjas:
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def intro(self):
        print(f"I am {self.name}, and my power is {self.power}")

intro = Ninjas("Yasuke", "1000")
intro.intro()


" Class vs Instance Variables"

class Ninjas:
    type = "Samurai"
# Class variable shared by all
    def __init__(self, name):
        self.name = name
# init variable shared among uniqe object 
n1 =Ninjas("Yasuke")
n2 = Ninjas("Jin Sakai")

print(n1.type)
print(n1.name)

" Inheritance"

class Warrior:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"I am {self.name}")

# Now inherating other class
class Shinobi(Warrior):
    def special(self):
        print("Shadow clone activated")

i = Shinobi("Naoe")
i.greet()
i.special()

"  super() — Call Parent's Method"

class Warrior:
    def __init__(self, name):
        self.name = name

class Shinobi(Warrior):
    def __init__(self,name,rank):
        super().__init__(name)
        self.rank = rank

    def final(self):
        print(f"{self.name}, rank {self.rank}")

i = Shinobi("Harsh", "Samurai")
i.final()


" Method overriding"

class Warrior:
    def attack(self):
        print("Normal Attack")

class Shinobi(Warrior):
    def attack(self):  # Overriding the parent method
        print("Silent Shadow Slash")

n = Shinobi()
n.attack()  # Output: Silent Shadow Slash
