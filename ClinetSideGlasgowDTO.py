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
    print("we are at:")
    print(i)
    exe_time = 1
    seq = [1,2,3,4]
    random.shuffle(seq)
    print(seq)
    selection = seq[3]
    #a = [0.1,0.2,0.3,0.4]
    #a = [0.4,0.4,0.4,0.4]
    aveExe = [0.10,0.38,0.39,0.9]
    for option in range(0,3):
        if(aveExe[seq[option]-1]<=0.27):
            selection = seq[option]
            break

    if(selection==1):
       host='0.0.0.0'
    elif(selection==2):
        host = '192.168.1.103'
    elif(selection==3):
        host = '192.168.1.108'
    else:
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
plt.hist(allResult1, 50,range=[0, 0.5] ,density= True,edgecolor="black", alpha=0.75)
#n, bins, patches = plt.hist(allResult1, 50, density=True, alpha=0.75)

#ax.set_title("MacBook 1 Execution time: "'\u03BC = %.2f, \u03C3 = %.2f ' %(m,sd))
#ax.set_title("Virtualized device xecution time: "'\u03BC = %.2f, \u03C3 = %.2f ' %(m,sd))
#ax.set_title("Raspberry pi 4 device Execution time: "'\u03BC = %.2f, \u03C3 = %.2f ' %(m,sd))
#ax.set_title("MacBook 2 Execution time: "'\u03BC = %.2f, \u03C3 = %.2f ' %(m,sd))
#ax.set_title("DTO: "'\u03BC = %.2f, \u03C3 = %.2f ' %(m,sd), fontsize = 18)
ax.set_title(" COT: "'\u03BC = %.2f, \u03C3 = %.2f, C= 0.1, V = 0.27' %(m,sd), fontsize = 18)
plt.xlabel('Execution time (s)', size = 15)
plt.ylabel('Density', size = 15)
plt.xticks(fontsize=15)
plt.yticks(fontsize = 15)
plt.grid(True)
#plt.tight_layout()
#plt.savefig('MyMac2ProbabilityDist.eps')
#plt.savefig('DTOProbabilityDis.eps')
plt.savefig('COTProbabilityDis.eps')
#plt.savefig('virtualizedDeviceProbabilityDist.eps')
plt.show()
#plt.savefig('MyMacProbabilityDist.eps')
print(mean(allResult1))
#df =  pd.DataFrame(allResult1)
#df.to_csv('VirtualizedDeviceExecutionTime', sep=',', header=None, index=None)
#df.to_csv('OldmacExecutionTime', sep=',', header=None, index=None)
#df.to_csv('RasberryPiExecutionTime', sep=',', header=None, index=None)


     

