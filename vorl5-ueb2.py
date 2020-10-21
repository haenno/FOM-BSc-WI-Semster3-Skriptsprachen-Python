# 5. Vorlesung 17.10.2020, Skript Python 4 (07_Python_04.pdf)
# Übung 2: Datei auslesen, Summen aus Artikel Anz und Einzelpreisen bilden

import re 

muster = "(\d+),.*\s(\d+\.\d+)"
gesamtpreis = 0.0
qd = open("vorl5-ueb2-daten.txt","r")

for qdZeile in qd:
    ergebnis = re.search(muster,qdZeile)
    if ergebnis:
        print("Gefunden: Artikelanzahl '"+ ergebnis.group(1)+"' und Einzelpreis '"+ ergebnis.group(2)+"'")
        gesamtpreis = gesamtpreis + (float(ergebnis.group(1))*float(ergebnis.group(2)))
        print("Zwischensumme: " + str(gesamtpreis))
    else:
        print("In dieser Zeile nichts gefunden!")

print("\n ==> Gesamtsumme = %.2f Euro" % gesamtpreis)