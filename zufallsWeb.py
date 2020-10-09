def rndIP():
    min = 1
    max = 254
    seperator = '.'
    return str(str(int(random.uniform(min,max)))+seperator+str(int(random.uniform(min,max)))+seperator+str(int(random.uniform(min,max)))+seperator+str(int(random.uniform(min,max))))

def portscan(targetIp):
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #tcp
   try:
      con = s.connect((targetIp, 80))
      with print_lock:
         print("   http://"+ targetIp, ' ist online...')
      con.close()
   except:
      pass

def threader():
   while True:
      workerTargetIp = q.get()
      portscan(workerTargetIp)
      q.task_done()



print ("\n\n\n...ooooOO> Zufallswebseiten-Tours <OOoooo...\nSuchen und öffnen zufälliger Webseiten/-server...\n\n")
while True:
    input ("\nScan starten?     -->      Ja: Anykey     -->      Nein: CTRL+C")
    
    from queue import Queue
    import random 
    import socket
    import time
    import threading

    socket.setdefaulttimeout(0.75)
    print_lock = threading.Lock()

    net =  rndIP()
    net1 = net.split('.')
    a = '.'
    net2 = net1[0] + a + net1[1] + a + net1[2] + a
    st1 = 1
    en1 = 254
    print ("\nScanbereich nun von " + str(net2) + str(st1) + " bis " + str(net2) + str(en1) +"...")
    q = Queue()
    startTime = time.time()

    for x in range(80):
        t = threading.Thread(target = threader)
        t.daemon = True
        t.start()

    for workerTargetIp in range(st1,en1):
        ipToScan = net2 + str(workerTargetIp) 
        q.put(ipToScan)

    q.join()
    print('       ==> Scandauer in Sekunden:', time.time() - startTime)
    input("Beliebige Taste für Abschluss...") 


# ToDo:
#  - Private Ips ausfiltern
#  - bereits besuchte/gescannte Bereiche abspeichern (irgendwo) und nicht doppelt besuchen
#  - HTTP Header auslesen, abspeichern