" Modules:import, from, user-defined modules"

" Built-in Module Examples"

import math
print(math.sqrt(16))    
print(math.pi)           
print(math.factorial(5)) 


import random
print(random.randint(1, 10))           # Random int between 1 and 10
print(random.choice(['Harsh', 'Yasuke', 'Jin']))  # Random name


import datetime
now = datetime.datetime.now()
print(now)               # e.g., 2025-07-07 13:45:30.123456
print(now.year)          # 2025
print(now.strftime("%A"))  # Day name like 'Monday'


import os
print(os.getcwd())                       # Current working directory
print(os.path.exists("Warrior.txt"))     # True or False

" Aliasing Modules (as)"

import math as m

import numpy as np

"17.3 Creating Your Own Module (User-Defined)"

# Error idk,although easy
