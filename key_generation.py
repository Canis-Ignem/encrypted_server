from rsa import PublicKey, PrivateKey, newkeys,  encrypt,  decrypt

(public, private) = newkeys(512)

with open("./public.pem","wb") as f:
    pk = PublicKey.save_pkcs1(public)
    f.write(pk)
    
    
    
with open("./private.pem","wb") as f:
    pk = PrivateKey.save_pkcs1(private)
    f.write(pk)
    

#loading the keys
'''
with open("./public.pem","rb") as f:
    data = f.read()
    public = PublicKey.load_pkcs1(data)
    
    
with open("./private.pem","rb") as f:
    data = f.read()
    private = PrivateKey.load_pkcs1(data)
    
'''

message = 'Bob says hi to Alice!'.encode('utf8')
crypto = encrypt(message, public)
print(crypto)
message = decrypt(crypto, private)
print(message.decode('utf8'))



