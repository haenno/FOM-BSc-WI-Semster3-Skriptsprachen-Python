# 3. Vorlesung 09.10.2020
# Aufgabe 2 aus Skript Python 2 (05_Python_02.pdf):
# Fehlerbehandlung (Div durch 0)

while True:
    try:
        print("Fehler wird erzeugt: Division durch die Zahl 0...\n")
        (a,b) = (1.0,0.0)
        c = a/b
    except:
        print(" --> Fehler: Bei der Ausfühung ist ein undefinierter Fehler aufgetreten.\n")
    input("\n Beliebige Taste drücken um fortzufahren...")

