# Übung/Aufgabe 3: Fibonacci Folge bis zu Zahl

def fib(fibMax):
    fibZuvor = 0
    fibAktuell = 1
    while fibAktuell < fibMax:
        fibTmp = fibZuvor + fibAktuell
        fibZuvor = fibAktuell
        fibAktuell = fibTmp
        print (str(fibAktuell))

while True:
    fibMax = input ("Bitte die gewünschte höchst Zahl (fib) eingaben: ")
    fib(int(fibMax))


# ToDo: 1) Variante mit angabe der Position/Folge der Fib-Folge 2) Fib Rekursiv darstellen