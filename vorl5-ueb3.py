# 5. Vorlesung 17.10.2020, Skript Python 4 (07_Python_04.pdf)
# Übung 3: Log Datei bearbeiten (Daten raus löschen)

import re 

muster = "\d+\/\d+"

qd = open("vorl5-ueb3-daten.txt","r")
zd = open ("vorl5-ueb3-daten-ziel.txt","w")

for qdZeile in qd:
    ergebnis = re.sub(muster,"xxx/xxx",qdZeile)
    if ergebnis:
        print("Gefunden: "+ ergebnis )
    else:
        ergebnis = qdZeile
    zd.write(ergebnis)

print("\n ==> Done!")

zd.close()
qd.close()