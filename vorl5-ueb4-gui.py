# 5. Vorlesung 17.10.2020, Skript Python 4 (07_Python_04.pdf)
# Übung 4: GUI

from tkinter import *

def text_out(event):
    label.configure(text=entry.get())

main = Tk()
main.title("MeineApp")

label = Label(main, text="Howdy TKinter!", fg="red")
entry = Entry(main)
entry.bind("<Return>",text_out)
button = Button(main, text="Drück mich", width=25, command=text_out)

label.pack()
entry.pack()
button.pack()

cnv = Canvas (main, width=200, height=200)
cnv.pack()
points = [100,60,120,100,80,100]

cnv.create_polygon(points,outline="black",fill="white",width=3)

mainloop()
