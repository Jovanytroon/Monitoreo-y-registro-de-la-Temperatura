import matplotlib.pyplot as plt
import matplotlib.animation as animation
import threading
import socket
import sys

gData=[]
gData.append([0])
gData.append([0])

#Configuramos la gráfica
fig=plt.figure()
ax=fig.add_subplot(111)
hl, =plt.plot(gData[0], gData[1])
plt.ylim(0, 90)
plt.xlim(0, 200)

def GetData(out_data):
    #connexion
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("192.168.1.197",55000))
    s.listen()
    while True:
        
        client, addr =s.accept()
        content=client.recv(1024)
        bite=content.decode('utf-8')
        if len(bite.split('/'))==3:
            temp1=bite.split('/')[1][0:-5]
            out_data[1].append(float(temp1))
            print(temp1)
            client.sendall(content)
                    
        client.close()
        

def update_line(num,hl,data):
    hl.set_data(range(len(data[1])), data[1])
    return hl,

line_ani=animation.FuncAnimation(fig,update_line,fargs=(hl,gData),interval=50,blit=False)

dataCollector=threading.Thread(target=GetData,args=(gData,))
dataCollector.start()

plt.show()
dataCollector.join()