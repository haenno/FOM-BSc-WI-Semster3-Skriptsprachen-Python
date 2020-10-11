# 3. Vorlesung 09.10.2020
# Aufgabe 4 aus Skript Python 2 (05_Python_02.pdf):
# Hier die zu ladende Moduldatei...

import math

def kreisFlaeche(radius):
    flaeche = math.pi * (math.pow(float(radius),2))
    return flaeche

def kreisUmfang(radius):
    umfang = 2 *math.pi * float(radius)
    return umfang
