import socket
import os
import rsa
from terminal_sim import execute
with open("./private.pem","rb") as f:
    data = f.read()
    server_private_key = rsa.PrivateKey.load_pkcs1(data)

HOST = '25.95.91.150'    
PORT = 5005  

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP SOCKET

s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()  
print('Client connected: ', addr)


while True:
    data = conn.recv(1024)
    if not data or data == "":
        break
    decoded_data = data
    orig_mess = rsa.decrypt(decoded_data, server_private_key).decode('utf8')
    out = execute(orig_mess)
    final_msg = ''
    for mess in out:
        final_msg += mess
    conn.sendall(final_msg.encode())
conn.close()
