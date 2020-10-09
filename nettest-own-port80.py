# Eigener Versuch, nur Port 80 in IP Bereich, Threaded
# Anregungen + Codeschnipsel von... https://www.tutorialspoint.com/python_penetration_testing/python_penetration_testing_network_scanner.htm 
# und https://www.geeksforgeeks.org/threaded-port-scanner-using-sockets-in-python/?ref=rp

import socket
import time
import threading

from queue import Queue
socket.setdefaulttimeout(0.75)
print_lock = threading.Lock()

net = input("Enter the IP address: ")
net1 = net.split('.')
a = '.'

net2 = net1[0] + a + net1[1] + a + net1[2] + a
st1 = int(input("Enter the Starting Number: "))
en1 = int(input("Enter the Last Number: "))
en1 = en1 + 1


def portscan(targetIp):
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   try:
      con = s.connect((targetIp, 80))
      with print_lock:
         print(targetIp, 'is online')
      con.close()
   except:
      pass

def threader():
   while True:
      workerTargetIp = q.get()
      portscan(workerTargetIp)
      q.task_done()
      
q = Queue()
startTime = time.time()
   
for x in range(20):
   t = threading.Thread(target = threader)
   t.daemon = True
   t.start()
   
for workerTargetIp in range(st1,en1):
   ipToScan = net2 + str(workerTargetIp) 
   q.put(ipToScan)
   
q.join()
print('Time taken:', time.time() - startTime)