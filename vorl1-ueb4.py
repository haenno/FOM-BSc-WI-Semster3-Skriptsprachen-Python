# Übung/Aufgabe 4: Taschenrechner mit 4 Grundfunktionen (+ - / * )

def addi(a,b):
    return a+b

def subt(a,b):
    return a-b

def mult(a,b):
    return a*b

def divi(a,b):
    return a/b

def getAB():
    a = input("Gib die erste Zahl ein: ")
    b = input("Gib die zweite Zahl ein: ")
    return (float(a),float(b))

def printResult(result):
    print ("Ergebnis ist = " + str(result))
    input ("\nBeliebige Taste für Neustart...\n");

while True: 
    print ("\n\nWelche Rechenart soll durchgeführt werden?\n ")
    print ("   1 = Addition")
    print ("   2 = Subtraktion")
    print ("   3 = Multiplikation")
    print ("   4 = Division\n")
    rechenart = int(input (" Gib ein: (1/2/3/4) "))

    if rechenart == 1:
        print ("   \n\n >>Addition")
        (a,b) = getAB()
        printResult(addi(a,b))

    elif rechenart == 2:
        print ("   \n\n >>Subtraktion")
        (a,b) = getAB()
        printResult(subt(a,b))
        
    elif rechenart == 3:
        print ("   \n\n >>Multiplikation")
        (a,b) = getAB()        
        printResult(mult(a,b))        

    elif rechenart == 4: 
        print ("   \n\n >>Division")        
        (a,b) = getAB()        
        printResult(divi(a,b))

    else:
        print ("  --> Bitte nur 1, 2, 3 oder 5 eingeben!")
        input("")