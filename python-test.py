def prnt (parm):
    print(str(parm) + "  ==>  " + eingText)

while True:
    i = input ("Wie oft gruessen? ")
    eingText = "Hallo Welte, Erde,..."

    while i > 0:
        prnt(i)
        i = i - 1
        
    print("Geschafft!")

