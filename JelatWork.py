# Importing libraries
import socket
import sys
import time
import struct


host="0.0.0.0"
#host="172.20.10.13"
port=40000

# Now we can create socket object
s = socket.socket()

# Lets connect to that port where server may be running
s.connect((host, port))

# averageServerUtilization = float(s.recv(2048).decode('utf-8'))

unpacker = struct.Struct('f')

data = s.recv(unpacker.size)

averageServerUtilization1 = struct.unpack('f', data )
# print('received {!r}'.format(binascii.hexlify(averageServerUtilization1)))
averageServerUtilization1 = float('.'.join(str(ele) for ele in averageServerUtilization1)) 
averageServerUtilization1  = "{:.3f}".format(averageServerUtilization1)
print(type(averageServerUtilization1))
averageServerUtilization1 = float(averageServerUtilization1)
print("CPU utilization is ", averageServerUtilization1)
print(type(averageServerUtilization1))


unpacker = struct.Struct('f')

data2 = s.recv(unpacker.size)

averageServerUtilization2 = struct.unpack('f', data2 )
# print('received {!r}'.format(binascii.hexlify(averageServerUtilization1)))
averageServerUtilization2 = float('.'.join(str(ele) for ele in averageServerUtilization2)) 
averageServerUtilization2  = "{:.3f}".format(averageServerUtilization2)
print(type(averageServerUtilization2))
averageServerUtilization2 = float(averageServerUtilization2)
print("CPU utilization is ", averageServerUtilization2)
print(type(averageServerUtilization2))


unpacker = struct.Struct('f')

data3 = s.recv(unpacker.size)

averageServerUtilization3 = struct.unpack('f', data3 )
# print('received {!r}'.format(binascii.hexlify(averageServerUtilization1)))
averageServerUtilization3 = float('.'.join(str(ele) for ele in averageServerUtilization3)) 
averageServerUtilization3  = "{:.3f}".format(averageServerUtilization3)
print(type(averageServerUtilization3))
averageServerUtilization3 = float(averageServerUtilization3)
print("CPU utilization is ", averageServerUtilization3)
print(type(averageServerUtilization3))

baseLine = min(averageServerUtilization1,averageServerUtilization2)



if(averageServerUtilization3 <= baseLine):
    start_time = time.time()
    # We can send file sample.txt
    file = open("sheep.jpeg", "rb")
    SendData = file.read(60000)

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