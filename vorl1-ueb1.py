# Übung/Aufgabe 1: Funktion Celsius zu Fahrenheit umrechnen (C = (F-32)/1.8 )

def tempCtoF(tempC):
    return tempC * 1.8 + 32

while True:
    tempC = float(input ("Bitte geben Sie die Temperatur in °C ein: "))
    print ("Die Temperatur in Fahrenheit ist: %.2f" % (tempCtoF(tempC)))