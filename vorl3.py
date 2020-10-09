# 3. Vorlesung 09.10.2020
# Aufgabe 1 aus Skript Python 2 (05_Python_02.pdf)

while True:
    quellDateiname = input("Ganze Zahlen aus Datei einlesen. Dateiname? ")
    quellDatei = open (quellDateiname, 'r')
    zielDatei = open("output_"+quellDateiname,'w')

    for quellZeile in quellDatei:
        zielDatei.write(str(float(quellZeile)) + "\n")
        print ("Quelle: " + quellZeile + " // Ziel: " + str(float(quellZeile)))
    



