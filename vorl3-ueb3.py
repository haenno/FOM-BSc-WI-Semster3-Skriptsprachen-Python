# 3. Vorlesung 09.10.2020
# Aufgabe 3 aus Skript Python 2 (05_Python_02.pdf):
# Rechnen mit 'math'

import math

# Teil 1 
for i in range(1,11):
    print("Potenz von '" + str(i) + "' ist '" + str(pow(i,2)) + "'")

# Teil 2
for i in range(10,101,10):
    print("Quadratwurzen von '" + str(i) + "' ist '" + str(math.sqrt(i)) + "'")

# Teil 3
from math import pow as potenz, sqrt as quadwurz 
for i in range(1,11):
    print("Potenz von '" + str(i) + "' ist '" + str(potenz(i,2)) + "'")
for i in range(10,101,10):
    print("Quadratwurzen von '" + str(i) + "' ist '" + str(quadwurz(i)) + "'")
