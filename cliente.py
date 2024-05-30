import socket
cliente = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
cliente.connect(('localholst',7777))
print('conectado!\n')
namefile = str (input ('arquivo>'))
cliente.send(namefile.encode())
with open(namefile,'wb') as file:
    while 1: 
        data = cliente.recv(1000000)
        if not  data:  
            break
        file.write(data)
        print(f'{namefile} recebido\n')