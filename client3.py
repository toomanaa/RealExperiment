import socket
s=socket.socket()
host=socket.gethostname()
port=8080

a=int(input("Enter a number) "))

b=int(input("Enter a number) "))



s.connect((host, port))
s.sendall(str.encode("\n".join([str(a), str(b)])))

m=int((s.recv(2048)).decode('utf-8'))
print("Recieved sum is %d"%m)
s.close
