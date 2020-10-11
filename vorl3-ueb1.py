# 3. Vorlesung 09.10.2020
# Aufgabe 1 aus Skript Python 2 (05_Python_02.pdf)

while True:
    while True:
        quellDateiname = input("Ganze Zahlen aus Datei einlesen. Dateiname? ")
        try:
            quellDatei = open (quellDateiname, 'r')
        except:
            print("  Fehler: Datei konnte nicht geöffnet werden!\n\n")
            break 

        zielDatei = open("output_"+quellDateiname,'a')  # mit 'w' wird inhalt der zieldatei komplett überschrieben

        for quellZeile in quellDatei:
            zielDatei.write(str(float(quellZeile)) + "\n")
            print ("Quelle: " + quellZeile + " --> Ziel: " + str(float(quellZeile)))
        
        quellDatei.close()
        zielDatei.close()
        



