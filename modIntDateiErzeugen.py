# MIT License, Copyright (c) 2020 haenno 

import random
from pathlib import Path

def createRndIntFile(fileName, anz):
    try: 
        if Path.is_file(Path(fileName)):
            raise ValueError('Datei ist schon vorhanden!')
        try:
            anz = int(anz)
            if anz <= 0:
                raise ValueError
        except:
            raise ValueError('Keine Ganzzahl größer 0 eingegeben!')

        dstFile = open(fileName,'w')
        dstFile.write(str(int(random.uniform(1,999))))
        for i in range(1,anz): 
            dstFile.write("\n"+str(int(random.uniform(1,999))))
        dstFile.close()
        print("Datei erfolgreich erstellt.")
    except ValueError as error:
        print(" ==> Fehler: Datei mit Zufallsinhalt erzeugen fehlgeschlagen! \n   -> ", error)
        
createRndIntFile(input("Dateiname? "), input("Anzahl Zufallszahlen? ")) 
