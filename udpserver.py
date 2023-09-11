from socket import *
serverName=
'127.0.0.1'
serverPort= 12000
serverSocket=
socket(AF_INET,SOCK_STREAM)
serverSocket.bind((serverName,serverPort))
serverSocket.listen(1)
while 1:
print("Ther Server is ready to receive")
conectionSocket,addr=serverSocket.accept()
sentence=conectionSocket.recv(1024).decode()
file=open(sentence,"r")
l=file.read(1024)
conectionSocket.send(l.encode()
) print("\nSent contets of
"+sentence)file=close()
connectionSocket.close()
