import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('where.com', 80))
cmd = 'GET http://url/target.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)


# decode based on the character set
while True:
    data = mysock.recv(512)  #bytes
    if len(data) < 1:
        break
    mystring = data.decode()  #unicode
    print(mystring)
    # print(data.decode(),end='')

mysock.close()
