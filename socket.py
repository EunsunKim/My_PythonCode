import socket


url = input('Enter: ')
words = url.split('/')
host = words[2]

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((host, 80))
cmd = 'GET'+url+ 'HTTP/1.0\r\n\r\n'.encode()
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
