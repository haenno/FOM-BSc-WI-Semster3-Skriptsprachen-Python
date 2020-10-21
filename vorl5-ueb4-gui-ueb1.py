# 5. Vorlesung 17.10.2020, Skript Python 4 (07_Python_04.pdf)
# Übung 4: GUI Übung 1: Stren zeichnen

from tkinter import *

main = Tk()
main.title("Ein Stern")

cnv = Canvas (main, width=200, height=200)
cnv.pack()

points = [
    100,20,
    110,50,
    140,60,
    110,70,
    100,100,
    90,70,
    60,60,
    90,50
    ]

# Unfertiges folgt...
'''
x=100 # Startpunkt x
y=20 # Startpunkt y
l = 40 # Sternarmlänge
b = 10 # Sternarmbreite

points = [
    x,y,
    x+b,y+l,
    x+b+l,y+l+b, 
    x+b,y+l+b,        

    x,y+l+l,    
    x-b,y+l+b,
    x-b-l,y-l-b-b,
    x-b,y-l
    ]
'''

cnv.create_polygon(points,outline="black",fill="yellow",width=2)
cnv.create_text(100,10, text="Stern...")

mainloop()
