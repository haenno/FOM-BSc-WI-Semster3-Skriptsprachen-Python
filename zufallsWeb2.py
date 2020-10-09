# demo from with changes 07.10.2020 haenno: https://stackoverflow.com/questions/19196105/how-to-check-if-a-network-port-is-open-on-linux/55663026#55663026

from time import sleep
import socket, ipaddress, threading, random
from pprint import pprint

max_threads = 50
port = 80
file_openports = "wwwips.txt"

def rndSubnet():
    min = 1
    max = 254
    seperator = '.'
    return str(str(int(random.uniform(min,max)))+seperator+str(int(random.uniform(min,max)))+seperator+str(int(random.uniform(min,max)))+seperator+str("0"))


def check_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP
        #sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
        socket.setdefaulttimeout(2.0) # seconds (float)
        result = sock.connect_ex((ip,port))
        if result == 0:
            print ("http://"+str(ip)+":"+str(port)+" is open")
            final[ip] = "http://"+str(ip)+":"+str(port)+" is open"
            newIps.write("http://"+str(ip)+":"+str(port)+" is open")
        else:
            # print (str(ip)+":"+str(port)+"  is closed/filtered")
            final[ip] = str(ip)+":"+str(port)+"  is closed/filtered"
        sock.close()
    except:
        pass

while (True):
	final = {}
	newIps = open(file_openports,'a')

	for ip in ipaddress.IPv4Network(rndSubnet()+'/24'): 
	    threading.Thread(target=check_port, args=[str(ip), port]).start()
	    #sleep(0.1)

	# limit the number of threads.
	while threading.active_count() > max_threads :
	    sleep(1)

	pprint(final)