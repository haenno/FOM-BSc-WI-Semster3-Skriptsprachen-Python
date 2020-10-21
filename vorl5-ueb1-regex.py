# 5. Vorlesung 17.10.2020, Skript Python 4 (07_Python_04.pdf)

import re 

# Übung 1:
'''
1. Finden des Worts "Python" oder "python"
2. Inhalt einer gesamte Kommentarzeile
3. Ein Zeichen das eine Ziffer oder ein Vorzeichen ist (+/-)
'''

# Aufgabe 1
#daten = "ython python -*0201/637434* -467.1345"
#muster = "^[Pp]ython" 

# Aufgabe 2
#daten = " # Kommentarzeile mit vielen Wörtern und so...besser wäre einlesen einer Datei, zeilenweise"
#muster = "^([#]|[ #]).*" 

# Aufgabe 3
#daten = "Python python -*0201/637434* -467.1345"
#muster = "[0-9]|[-]|[+]" 


'''
4. Ein Zeichen das kein Buchstabe ist
5. eine IP Adresse
6. Eine Textzeile mit genau drei Zeichen
'''

# Aufgabe 4
#daten = "ython python -*0201/637434* -467.1345"
#muster = "[^A-Za-z]" 

# Aufgabe 5
#daten = "ython python 127.0.0.1  0.0.0.0  192.168.0.1   10.10.10.1  -*0201/637434* -467.1345"
#muster = "\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}" 

# Aufgabe 6  '" + gefunden +"'"
#daten = "yth"
#muster = "^.{3}$"


'''
7. Ein Datum (12.12.12, 1.1.20 oder 12.12.2012)
8. Eine gültige E-Mail Adresse
9. Eine negative Zahl mit 4 Nachkommastellen
10. Eine Festnetznummer mit je einem Stern davor und danch *1231/121231*

'''

# Aufgabe 7
#daten = "ython 01.01.2020  python -*0201   20.2.123  /637434*  14.10.1999 -467.1345asdh ahsdl 1.2.09"
#muster = "\d{1,2}\.\d{1,2}\.\d{2,4}"  # doof: auch Jahrezahlen mit 3 Stellen werden gefunden

# Aufgabe 8
#daten = "ython 01.01.2020 haenno.haenno@haenno.de a_b@c.d 1-2@3.4 pytho max@muster.de -*0201   karl@backenzahn.de 20.2.123  /637434*  14.10.1999 -467.1345asdh ahsdl 1.2.09"
#muster = "[\.\_\-\w]+\@[\w]+\.[\w]+"

# Aufgabe 9
#daten = "ython 01.01.2020 -123,1234  123.1234 321,4321 -431,5431123 -1.1234567 python -*0201   20.2.123  /637434*  14.10.1999 -467.1345asdh ahsdl 1.2.09"
#muster = "\s(-\d+[,\.]\d{4})"

# Aufgabe 10
#daten = "ython python -*0201/637434* -467.1345"
#muster = "\*\d+/\d+\*" 


ergebnis = re.findall(muster,daten)
if ergebnis:
    print("Gefunden: ")
    for fundstelle in ergebnis:
        print("  ->  '" + fundstelle +"'")

else:
    print("Nicht gefunden!")
