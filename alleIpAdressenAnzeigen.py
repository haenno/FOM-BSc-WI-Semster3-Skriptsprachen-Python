from datetime import datetime 

min = 0
max = 255
seperator = '.'
datei = open('ips.txt','a')
   
for b1 in range((min),(max+1)):
    for b2 in range(min,(max+1)):
        for b3 in range(min,(max+1)):
            for b4 in range(min,(max+1)):
                ipAddr = str(b1) + seperator + str(b2) + seperator + str(b3) + seperator + str(b4)
                print ('"' + ipAddr + '";"' + str(datetime.now()) + '"')
                datei.write('"' + ipAddr + '";"' + str(datetime.now()) + '"' + '\n')

datei.close()
print ("done")

# Todo: viel zu langsam, threading half im ersten versuch auch nicht. 
#      später quasi unmöglich gut mit zu arbeiten...
#    besser: random ip erzeugen, mit arbeiten, ergebnis  in liste/datei/db schreiben
#             + bei jede rnd erzeugten ip, prüfen ob schon benutzt, falls ja verwerfen, nächste