# Importing libraries
import random 
import socket
import sys
import time
import struct
import numpy as np
from statistics import mean
import matplotlib.pyplot as plt
from statistics import mean
import statistics
i = 0
allResult1 = []
allResult2 = []
while i<1000:
    exe_time = 1
    seq = [1,2,3,4]
    random.shuffle(seq)
    print(seq)
    print("we are at stage:")
    print(i)
    selection = seq[0]

    if(selection==1):
        host='0.0.0.0'
    elif(selection==2):
        host = '192.168.1.103'
    elif(selection==3):
        host = '192.168.1.108'
    elif(selection==4):
        host = '192.168.1.104'
    #host="172.20.10.13"

    #host = '0.0.0.0'
    port=40000    
    s = socket.socket()
    s.connect((host, port))    
    start_time = time.time()
    # We can send file sample.txt
    file = open("sheep.jpeg", "rb")
    SendData = file.read(60000)

    while SendData:
        print("\n\n################## Below message is received from server ################## \n\n ", s.recv(1024).decode("utf-8"))
        s.send(SendData)
        SendData = file.read(60000)
        s.shutdown(socket.SHUT_WR)
        print("The prediction results")
        print(s.recv(1024).decode())
        
    exe_time = (time.time() - start_time)
    print("--- %s seconds ---" % exe_time)
    # Close the connection from client side
    s.close()
    allResult1.append(exe_time)
    allResult2.append(selection)
    i=i+1
    time.sleep(1)

m = mean(allResult1)
sd = statistics.pstdev(allResult1)

ax = plt.subplot()
plt.hist(allResult1, 50,range=[0.5, 2] ,density= True,edgecolor="black", alpha=0.75)
#n, bins, patches = plt.hist(allResult1, 50, density=True, alpha=0.75)

#ax.set_title("MacBook 1 Execution time: "'\u03BC = %.2f, \u03C3 = %.2f ' %(m,sd))
#ax.set_title("Virtualized device xecution time: "'\u03BC = %.2f, \u03C3 = %.2f ' %(m,sd))
#ax.set_title("Raspberry pi 4 device Execution time: "'\u03BC = %.2f, \u03C3 = %.2f ' %(m,sd))
#ax.set_title("MacBook 2 Execution time: "'\u03BC = %.2f, \u03C3 = %.2f ' %(m,sd))
ax.set_title("First Option: "'\u03BC = %.2f, \u03C3 = %.2f ' %(m,sd), fontsize = 18)
plt.xlabel('Execution time (s)', size = 13)
plt.ylabel('Density', size = 15)
plt.xticks(fontsize=15)
plt.yticks(fontsize = 15)
plt.grid(True)
plt.tight_layout()
plt.savefig('FirstOptionProbabilityDist.eps')
plt.savefig('RasberryPiProbabilityDist.eps')
#plt.savefig('virtualizedDeviceProbabilityDist.eps')
plt.show()
#plt.savefig('MyMacProbabilityDist.eps')
print(mean(allResult1))
#df =  pd.DataFrame(allResult1)
#df.to_csv('VirtualizedDeviceExecutionTime', sep=',', header=None, index=None)
#df.to_csv('OldmacExecutionTime', sep=',', header=None, index=None)
#df.to_csv('RasberryPiExecutionTime', sep=',', header=None, index=None)


     

