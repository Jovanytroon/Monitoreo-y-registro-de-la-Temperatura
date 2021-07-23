#Librerías
import socket 
import sys

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)#objeto del socket
s.bind(("192.168.1.197",55000))#Se asigna la dirección y el puerto por el que se comunicaran
s.listen()#El socket escucha
while True: 
    client, addr =s.accept()#se acepta la conexión con el cliente
    content=client.recv(1024)#se reciben los datos que envio el modulo con una resolución de 1024 bits
    bite=content.decode('utf-8')#se deccodifica la informacion
    if len(bite.split('/'))==3:#si a dividir la petición en cada diagonal que encuentra existen 3 divisiones 
        temp1=bite.split('/')[1][0:-5]#busca la segunda división por diagonal y solamente se asigna en temp1 el valor númerico
        print(temp1)#se imprime el valor de temp1
        client.sendall(content)#se manda el dato de recibido
    
    client.close()#se cierra la conexión del cliente
    