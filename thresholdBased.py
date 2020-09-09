#import socket library
import socket
import pickle 
import image 
import os
import psutil
import platform
import time
from datetime import datetime
import threading
from imageai.Prediction import ImagePrediction

prediction = ImagePrediction()
prediction.setModelTypeAsResNet()
prediction.setModelPath("resnet50_weights_tf_dim_ordering_tf_kernels.h5")
prediction.loadModel()

# Now we can create socket object
s = socket.socket()


# Lets choose one port and start listening on that port
port = 40000

print("\n Server is listing on port :", port, "\n")
host = '0.0.0.0'
# Now we need to bind to the above port at server side
s.bind(('', port))

# Now we will put server into listenig  mode 
s.listen(10)

#Open one recv.txt file in write mode
file = open("recv.jpeg", "wb") 
print("\n Copied file name will be recv.txt at server side\n")
#CPU utilization list 
cpuUtilization = []
cpu_load = [x/os.cpu_count()*100 for x in os.getloadavg()][-1]
print(cpu_load)

# Now we do not know when client will concatct server so server should be listening contineously  
while True:
    conn, addr = s.accept()
    averageServerUtilization1 = psutil.cpu_percent(0.1)
    conn.send(str.encode(str(averageServerUtilization1)))
    averageServerUtilization2 = psutil.cpu_percent(0.1)
    conn.send(str.encode(str(averageServerUtilization2)))
    averageServerUtilization3 = psutil.cpu_percent(0.1)
    conn.send(str.encode(str(averageServerUtilization3)))
    print("we will go the fifth server utilization")
        
       

    cpuUtilization = str(cpuUtilization)
    print(cpuUtilization)
    #conn.send(str.encode(str(averageServerUtilization)))

    # Send a hello message to client
    msg = "\n\n|---------------------------------|\n Hi Client[IP address: "+ addr[0] + "], \n ֲֳ**Welcome to Server** \n -Server\n|---------------------------------|\n \n\n"    
    conn.send(msg.encode())
    # Receive any data from client side
    RecvData = conn.recv(1024)
    while RecvData:
        file.write(RecvData)
        RecvData = conn.recv(1024)

    # Close the file opened at server side once copy is completed
    file.close()
    print("\n File has been copied successfully \n")
    predictions, percentage_probabilities = prediction.predictImage("recv.jpeg", result_count=5)
    results = []
    for index in range(len(predictions)):
        #print(predictions[index] , " : " , percentage_probabilities[index])
        results.append(predictions[index])
        results.append(percentage_probabilities[index])
    results = str(results)
    # Close connection with client
    conn.send(results.encode())
    conn.close()
    
    print("\n Server closed the connection \n")

    # Come out from the infinite while loop as the file has been copied from client.
    break

print(results)