import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(("date.pr4e", 80))
cmd ="GER http://date.pr4e.org/romeo.text HTTP/1.0\r\n\r\n".encode()
mysock.send(cmd)

while True:
    date = mysock.recv(512)
    if(len(date)<1):
        break
        print(date.decode(),end="")
mysock.close()