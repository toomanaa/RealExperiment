import socket
import psutil
import platform
import time
from datetime import datetime
s=socket.socket()
host=socket.gethostname()
port=8080
s.bind((host,port))
s.listen(5)
while 1:
    c,address=s.accept()
    averageServerUtilization = psutil.cpu_percent()
    c.send(str.encode(str(averageServerUtilization)))
    start_time = time.time()
    a, b = [int(i) for i in c.recv(2048).decode('utf-8').split('\n')]
    print("Recieved two  from client is n=%d,e=%d\n"%(a,b))
    su=a*b
    print("sum is %d\n"%su)
    c.send(str.encode(str(su)))
    print("--- %s seconds ---" % (time.time() - start_time))
s.close