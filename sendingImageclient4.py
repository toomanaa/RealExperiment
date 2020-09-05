# Importing libraries
import socket
import sys

# Lets catch the 1st argument as server ip
host = '0.0.0.0'


# Now we can create socket object
s = socket.socket()


# Lets choose one port and connect to that port
port = 40000


# Lets connect to that port where server may be running
s.connect((host, port))

# We can send file sample.txt
file = open("sheep.jpeg", "rb")
SendData = file.read(60000)


while SendData:
    # Now we can receive data from server
    print("\n\n################## Below message is received from server ################## \n\n ", s.recv(1024).decode("utf-8"))
    #Now send the content of sample.txt to server
    s.send(SendData)
    SendData = file.read(60000)  
    s.shutdown(socket.SHUT_WR)
    print("The prediction results are: ")
    print("\n")
    print (s.recv(1024).decode())

 

# Close the connection from client side
s.close()