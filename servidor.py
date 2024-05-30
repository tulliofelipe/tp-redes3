import socket 
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localholst', 7777))
server.listen(1)
connnection, address =  server.accept()
namefile = connnection.recv(1024).decode()
with open(namefile,'rb')as file:
    for data in file.readlines()
        connnection.send(data)
    print("arquivo enviado!")
    
