# für vorl. 3 aufgabe 1

import random

def createRndIntFile(fileName, anz):
    # try: 
        #testFileExists = open(fileName,'r')
        #testFileExists.close()
        dstFile = open(fileName,'w')
        for i in range(0,anz): 
            dstFile.write(str(int(random.uniform(1,999)))+"\n")
        dstFile.close()
    # except:
        print("Fehler: Datei mit Zufallsinhalt erzeugen fehlgeschlagen!")
        
createRndIntFile("test.txt",100)
