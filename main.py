'''import math
import random

print(math.sqrt(9))
for _ in range(50):
   print(random.randint(1,6))
'''
try:
    eredmeny = 10 / 0
except ZeroDivisionError:
    print("hiba: nullával való osztás")
except NameError:
    print("Hiba: névhiba")
else:
   print(eredmeny)
