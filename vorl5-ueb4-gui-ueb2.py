# 5. Vorlesung 17.10.2020, Skript Python 4 (07_Python_04.pdf)
# Übung 4: GUI Übung 2: Länderflaggen aus Textfeld zeichnen...

from tkinter import *

def updateGui(event):
    if textFeld.get() == "Deutschland":
        fahneOben.configure(bg="black")
        fahneMitte.configure(bg="red")
        fahneUnten.configure(bg="gold")
    elif textFeld.get() == "Frankreich":
        fahneOben.configure(bg="blue")
        fahneMitte.configure(bg="white")
        fahneUnten.configure(bg="red")
    elif textFeld.get() == "Piraten":
        fahneOben.configure(bg="black")
        fahneMitte.configure(bg="black")
        fahneUnten.configure(bg="black")
    else:
        labelAnweisung.configure(text="...Land nicht verfügbar!")
        textFeld.delete(0,END)

main = Tk()
main.title("Länderflaggen")

labelAnweisung = Label(main, text="Bitte Ländername eingeben...")
textFeld = Entry(main)
textFeld.bind("<Return>", updateGui)
schalterLaden = Button(main, text="Lade Flagge...", width=25, command=updateGui)

fahneOben = Label(main,bg="green")
fahneMitte = Label(main,bg="blue")
fahneUnten = Label(main,bg="red")

labelAnweisung.pack()
textFeld.pack()
schalterLaden.pack()
fahneOben.pack(fill=X)
fahneMitte.pack(fill=X)
fahneUnten.pack(fill=X)


mainloop()
