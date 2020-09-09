# Importing libraries
import socket
import sys
import time


# host="192.168.1.3"
host="0.0.0.0"
port=40000

# Now we can create socket object
s = socket.socket()

# Lets connect to that port where server may be running
s.connect((host, port))

# averageServerUtilization = float(s.recv(2048).decode('utf-8'))

# print("CPU utilization is %d"%averageServerUtilization)

averageServerUtilization1 = float(s.recv(2048).decode('utf-8'))

print("CPU utilization is %d"%averageServerUtilization1)  
   
#s.shutdown(socket.SHUT_WR)

averageServerUtilization2 = float(s.recv(2048).decode('utf-8'))

print("CPU utilization is %d"%averageServerUtilization2)

#s.shutdown(socket.SHUT_WR)

baseLine = min(averageServerUtilization1,averageServerUtilization2)

averageServerUtilization3 = float(s.recv(2048).decode('utf-8'))

print("CPU utilization is %d"%averageServerUtilization3)


#s.shutdown(socket.SHUT_WR)

if(averageServerUtilization3 < baseLine):
   
    # We can send file sample.txt
    file = open("sheep.jpeg", "rb")
    SendData = file.read(60000)

    start_time = time.time()

    while SendData:
        # Now we can receive data from server
        #Now send the content of sample.txt to server
         # Now we can receive data from server
        print("\n\n################## Below message is received from server ################## \n\n ", s.recv(1024).decode("utf-8"))
        s.send(SendData)
        SendData = file.read(60000)
        s.shutdown(socket.SHUT_WR)
        print("The prediction results")
        print(s.recv(1024).decode())
   

    print("--- %s seconds ---" % (time.time() - start_time))
    # Close the connection from client side
    s.close()

else:
    print("The cpu is too high")
    s.close()