# Importing libraries
import socket
import sys
import time


host="172.20.10.13"
port=40000

# Now we can create socket object
s = socket.socket()

# Lets connect to that port where server may be running
s.connect((host, port))

averageServerUtilization = float(s.recv(2048).decode('utf-8'))

print("CPU utilization is %d"%averageServerUtilization)

# We can send file sample.txt
file = open("plane.jpeg", "rb")
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

