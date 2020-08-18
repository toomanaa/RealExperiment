import socket
import time 
s=socket.socket()
host=socket.gethostname()
port=8080




s.connect((host, port))
averageServerUtilization = float(s.recv(2048).decode('utf-8'))
print("CPU utilization is %d"%averageServerUtilization)
if(averageServerUtilization) <=10:
    start_time = time.time()
    a=int(input("Enter a number) "))

    b=int(input("Enter a number) "))
    s.sendall(str.encode("\n".join([str(a), str(b)])))

    m=int((s.recv(2048)).decode('utf-8'))
    print("Recieved sum is %d"%m)
    print("--- %s seconds ---" % (time.time() - start_time))
else:
    print("CPU is  high with %d"%averageServerUtilization)
s.close
