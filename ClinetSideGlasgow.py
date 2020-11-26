# Importing libraries
import random 
import socket
import sys
import time
from time import ctime
import struct
from statistics import mean
import statistics
import numpy as np
import matplotlib.pyplot as plt
import csv 
import pandas as pd
import seaborn as sns

i = 0
allResult1 = []
t = []
allResult2 = []
while i<1000:
    exe_time = 1
    
    seq = [1,2,3,4]
    selection = random.randint(1,4)
    print("we are at stage:")
    print(i)
    print(selection)
    #if(selection==1):
        #host='0.0.0.0'
    #elif(selection==2):
       # host = '192.168.1.103'
    #elif(selection==3):
       # host = '192.168.1.108'
    ##elif(selection==4):
        #host = '192.168.1.104'
    #host="172.20.10.13"
    #host = '192.168.1.104'
    #host = '0.0.0.0'
    host = '192.168.1.104'
    port=40000    
    s = socket.socket()
    s.connect((host, port))    
    start_time = time.time()
    # We can send file sample.txt
    images = ["sheep.jpeg","plane.jpeg","tree.jpeg","stone.jpeg"]
    imageSeq = random.randint(0,3)
    file = open(images[imageSeq], "rb")
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
    t.append(ctime())
    allResult2 = {'Time':t, 'Execution Time':allResult1}
    i=i+1
    time.sleep(1)



m = mean(allResult1)
sd = statistics.pstdev(allResult1)

ax = plt.subplot()
plt.hist(allResult1, 50,range=[0.5, 1.2] ,density= True,edgecolor="black", alpha=0.75)
#n, bins, patches = plt.hist(allResult1, 50, density=True, alpha=0.75)

#ax.set_title("MacBook Pro 1 Execution Time: "'\u03BC = %.2f, \u03C3 = %.2f ' %(m,sd), fontsize = 18)
#ax.set_title("MacBook Pro 2 Execution Time: "'\u03BC = %.2f, \u03C3 = %.2f ' %(m,sd), fontsize = 18)
#ax.set_title("VM Execution Time: "'\u03BC = %.2f, \u03C3 = %.2f ' %(m,sd), fontsize = 18)
ax.set_title("Raspberry Pi Execution Time: "'\u03BC = %.2f, \u03C3 = %.2f ' %(m,sd), fontsize = 18)
#ax.set_title("Random Selection: "'\u03BC = %.2f, \u03C3 = %.2f ' %(m,sd), fontsize = 18)
#plt.tight_layout()
plt.xlabel('Execution time (s)', size = 18)
plt.ylabel('Density', size = 18)
plt.xticks(fontsize=15)
plt.yticks(fontsize = 15)
plt.grid(True)
plt.tight_layout()
#plt.savefig('MacBookPro2ProbabilityDist.eps')
plt.savefig('RasberryPiProbabilityDist.eps')
#plt.savefig('virtualizedDeviceProbabilityDist.eps')
plt.show()
#plt.savefig('MacBookPro1ProbabilityDist.eps')
print(mean(allResult1))
#df =  pd.DataFrame(allResult1)
df =  pd.DataFrame(allResult2)
cul = ['Time', 'Execution Time']
df.columns = cul
#df.to_csv('VM', sep=',', header=True, index=None)
#df.to_csv('VirtualizedDeviceExecutionTime', sep=',', header=None, index=None)
#df.to_csv('MacBookPro2', sep=',', header=True, index=None)
df.to_csv('RasberryPi', sep=',', header=True, index=None)
#df.to_csv('RandExecutionTime', sep=',', header=None, index=None)
     

