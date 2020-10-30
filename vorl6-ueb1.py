# 6. Vorlesung 30.10.2020, Skript Python 4 (07_Python_04.pdf)
# Übung 1: GUI, Skala mit Benzinverbräuchen

from tkinter import *

def calc_result():
    km = float(entry_km.get())
    l = float(entry_l.get())

    result = (l / km) * 100
    label_result.configure(text="Der Druchschnittliche Verbrauch beträgt %.2f Liter auf 100 km!" % result)

    cnv.delete("all")
    create_fresh_canvas()
    
    result_gui = (290 - int(round(result,0))*10)
    cnv.create_rectangle(140,result_gui,160,290, fill="blue")
    result_gui_text = ("%.2f Liter" % result)
    cnv.create_text(165,result_gui, text=result_gui_text, anchor="nw")    


def create_fresh_canvas():
    cnv.create_text(10,275, text="0 Liter", anchor="nw")
    cnv.create_rectangle(80,220,100,290, fill="green")
    cnv.create_text(10,220, text="7 Liter", anchor="nw")
    cnv.create_rectangle(80,190,100,220, fill="yellow")
    cnv.create_text(10,190, text="10 Liter", anchor="nw")
    cnv.create_rectangle(80,90,100,190, fill="red")
    cnv.create_text(10,90, text="20 Liter", anchor="nw")

gui = Tk()
gui.title("Verbrauchsrechner")
gui.geometry("400x500")

label_km = Label(gui, text="Geben Sie bitte die gefahrenen Kilomenter ein: ")
label_km.pack()
entry_km = Entry(gui)
entry_km.bind("<Return>",calc_result)
entry_km.pack()

label_l = Label(gui, text="Geben Sie bitte die getankten Liter ein: ")
label_l.pack()
entry_l = Entry(gui)
entry_l.bind("<Return>",calc_result)
entry_l.pack()



button = Button(gui, text="Berechnen", width=25, command=calc_result)
button.pack()

label_result = Label(gui, text="")
label_result.pack()


cnv = Canvas (gui, width=300, height=300, background="grey")
cnv.pack()
create_fresh_canvas()

mainloop()
