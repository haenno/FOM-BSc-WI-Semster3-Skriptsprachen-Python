# demo from with changes 07.10.2020 haenno: https://stackoverflow.com/questions/19196105/how-to-check-if-a-network-port-is-open-on-linux/55663026#55663026

from time import sleep
import socket, ipaddress, threading, random

max_threads = 50
port = 80
file_openports = "wwwips.txt"
file_subnetsChecked = "wwwsubn.txt"

def checkSubnetNew(subnetStr):
    checked = False
    return checked

def writeResult(logEvent):
    newIps = open(file_openports,'a')
    newIps.write(logEvent+"\n")
    newIps.close()

def rndSubnet():
    min = 1
    max = 254
    seperator = '.'
    needNewSubnet = True
    rtnStr = ""
    while needNewSubnet:
        tmpSubNet = str(str(int(random.uniform(min,max)))+seperator+str(int(random.uniform(min,max)))+seperator+str(int(random.uniform(min,max)))+seperator+str("0/24"))
        known=0
        doneSubNets = open(file_subnetsChecked,'r')
        for subnet in doneSubNets:
            if subnet == tmpSubNet:
                known = known + 1
        if known == 0:
            needNewSubnet = False
            rtnStr = tmpSubNet
        doneSubNets.close()
    doneSubNets = open(file_subnetsChecked,'a')
    doneSubNets.write(rtnStr+"\n")
    doneSubNets.close()
    return rtnStr


def check_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP
        #sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
        socket.setdefaulttimeout(2.0) # seconds (float)
        result = sock.connect_ex((ip,port))
        if result == 0:
            writeResult("http://"+str(ip)+":"+str(port)+" is open")
        sock.close()
    except:
        pass

while (True):
    scnip = ipaddress.IPv4Network(rndSubnet())
    print ("Starte scan von " + str(scnip) + "...")
    writeResult("Starte scan von " + str(scnip) + "...")
    for ip in scnip: 
        threading.Thread(target=check_port, args=[str(ip), port]).start()
        sleep(0.01)
    # limit the number of threads.
    while threading.active_count() > max_threads :
        sleep(1)
    print ("...done. Next!")
    writeResult("...done. Next!")
