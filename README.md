# encrypted_server
This project contains the means to generating a pair of rsa512 keys in order to encrypt comunications
between a python client and server.

The deafult set up os the server is as an SSH alternative offering a more secure conection.

The data that can be sent via this method is only limited by the fact that it needs to be encoded
via UTF-8. So it can be used as a secure FTP.
