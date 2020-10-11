# 3. Vorlesung 09.10.2020
# Aufgabe 4 aus Skript Python 2 (05_Python_02.pdf):
# Eigene Moduldatei erzeugen, laden und nutzen

from vorl3ueb4modul import kreisFlaeche as krFl, kreisUmfang as krUm 

while True:
    try:
        kreisRadius = input("\n\nBerechnung Kreisumfang und -fläche:\n --> Bitte Radius eines Kreises eingeben: \n                                                                    (Ende mit x)     \n")
        if kreisRadius == "x":
            break
        print("Der Kreisumfang beträgt '" + str(krUm(kreisRadius)) + "'.")
        print("Der Kreisfläche beträgt '" + str(krFl(kreisRadius)) + "'.")
    except:
        print("Fehler. Neustart...\n\n")
