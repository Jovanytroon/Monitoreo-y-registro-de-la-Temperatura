from matplotlib import pyplot as plt
from matplotlib import animation as ani
import threading
import socket
import sys

server="192.168.1.197"
port=55000

gData1=[]
gData1.append([0])
gData1.append([1])

gData2=[]
gData2.append([0])
gData2.append([1])

gData3=[]
gData3.append([0])
gData3.append([1])

gData4=[]
gData4.append([0])
gData4.append([1])

def GetLimite():
    plt.xlim(0,50)
    plt.ylim(0,50)

fig=plt.figure(num='MONITOREO DE TEMPERATURA',figsize=(9.0,10.0),tight_layout=True)
ax=fig.add_subplot(2,2,1)
plt.title('Sensor 1')
plt.ylabel('°C')
hl1, =plt.plot(gData1[0],gData1[1],'g-')
GetLimite()

bx=fig.add_subplot(2,2,2)
plt.title('Sensor 2')
plt.ylabel('°C')
hl2, =plt.plot(gData2[0],gData2[1],'b-')
GetLimite()

cx=fig.add_subplot(2,2,3)
plt.title('Sensor 3')
plt.ylabel('°C')
hl3, =plt.plot(gData3[0],gData3[1],'r-')
GetLimite()

dx=fig.add_subplot(2,2,4)
plt.title('Sensor 4')
plt.ylabel('°C')
hl4, =plt.plot(gData4[0],gData4[1],'m-')
GetLimite()

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((server,port))
s.listen()

 
def GetData(out_data,out_data2,out_data3,out_data4):
    while True:
        client, addr = s.accept()
        content=client.recv(1024)
        bite=content.decode('utf-8')
        if (bite.split('/'))==3:
            temp1=bite.split('/')[1][0:-23]
            temp2=bite.split('/')[1][-22:-17]
            temp3=bite.split('/')[1][-16:-11]
            temp4=bite.split('/')[1][-10:-5]
            print(str(temp1)+", "+str(temp2)+", "+str(temp3)+", "+str(temp4)) 
            out_data[1].append(float(temp1))
            out_data2[1].append(float(temp2))
            out_data3[1].append(float(temp3))
            out_data4[1].append(float(temp4))
            client.sendall(content)
        client.close()

def update1(i,hl1,dato):
    gData1.append(dato)
    hl1.set_data(range(len(gData1[1])),gData1[1])
    return hl1, 
def update2(i,hl2,dato2):
    gData2.append(dato2)
    hl2.set_data(range(len(gData2[1])),gData2[1])
    return hl2, 
def update3(i,hl3,dato3):
    gData3.append(dato3)
    hl3.set_data(range(len(gData3[1])),gData3[1])
    return hl3, 
def update4(i,hl4,dato4):
    gData4.append(dato4)
    hl4.set_data(range(len(gData4[1])),gData4[1])
    return hl4, 


lin1=ani.FuncAnimation(fig, update1,fargs=(hl1, gData1[1]), interval=50, blit=True)
lin2=ani.FuncAnimation(fig, update2,fargs=(hl2, gData2[1]), interval=50, blit=True)
lin3=ani.FuncAnimation(fig, update3, fargs=(hl3, gData3[1]),interval=50, blit=True)
lin4=ani.FuncAnimation(fig, update4, fargs=(hl4, gData4[1]), interval=50, blit=True)

hilo=threading.Thread(target=GetData, args=(gData1,gData2,gData3,gData4,))
hilo.start()
plt.show()
hilo.join()
