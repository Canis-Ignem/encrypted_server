import socket
import rsa
from colorama import Fore

with open("./public.pem","rb") as f:
    data = f.read()
    server_public_key = rsa.PublicKey.load_pkcs1(data)

HOST = '25.95.91.150'    
PORT = 5005
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
print('Client connected.')
while True:
    user_input = str(input())  
    if user_input == "exit":  
        break
    mess = user_input.encode()
    cypher = rsa.encrypt(mess, server_public_key)
    s.sendall(cypher)  
    #out = s.recv(1024)
    #print(Fore.RED+ "System: ", Fore.GREEN+ out.decode())
    