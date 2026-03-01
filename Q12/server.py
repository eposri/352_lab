import socket
import sys

from aes import aes_decrypt
from dsa import dsa_verify
from rsa import rsa_verify

# Requirement 2: python3 server.py <port number> <key>
if len(sys.argv) != 3:
    print("Usage: python3 server.py <port number> <16-byte key>")
    sys.exit()

PORT_NUMBER = int(sys.argv[1])
key = sys.argv[2].encode()

if len(key) != 16:
    print("Error: key must be exactly 16 bytes.")
    sys.exit()

# create a socket and associate to the inputted port number
server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server_sock.bind(('', PORT_NUMBER)) 
server_sock.listen(1)
print("Server listening on port:", PORT_NUMBER)

# server continuously accepting clients
while True:
    print("Waiting for clients to connect...")
    # print("Enter 'quit' to exit server.") to implement later
    
    # TCP creates new socket for each client connection
    connection_sock, addr = server_sock.accept()
    print("Client connected from:", addr)

    # receive encrypted message
    cipher_text = b""
    while True:
        chunk = connection_sock.recv(1024) # get up to 4096 bytes of data
        if not chunk:
            break
        cipher_text += chunk
    connection_sock.close()

    if len(cipher_text) == 0:
        print("No data received.")
        continue
    
    try:
        # decrypt message using AES
        plain_text, signature, choice = aes_decrypt(key, cipher_text)
        if choice == "1":
            rsa_verify(plain_text.decode(), signature)
        else:
            dsa_verify(plain_text.decode(), signature)
    except TypeError:
        print("Secret key mismatch between server and client.")