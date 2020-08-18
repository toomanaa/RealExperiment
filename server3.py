import socket
import psutil
import platform
from datetime import datetime
s=socket.socket()
host=socket.gethostname()
port=8080
s.bind((host,port))
s.listen(5)
while 1:
    c,address=s.accept()
    a, b = [int(i) for i in c.recv(2048).decode('utf-8').split('\n')]
    print("Recieved two  from client is n=%d,e=%d\n"%(a,b))
    su=a*b
    print("sum is %d\n"%su)
    c.send(str.encode(str(su)))
s.close