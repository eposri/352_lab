import socket
import sys

from aes import aes_encrypt

# Requirement 4: python3 client.py <server IP> <server port> <key> 
if len(sys.argv) != 4:
    print("Usage: python3 client.py <server IP> <server port> <16-byte key>")
    sys.exit()

SERVER_IP = sys.argv[1]
SERVER_PORT = int(sys.argv[2])
key = sys.argv[3].encode()      # str to bytes

if len(key) != 16:
    print("Error: key must be exactly 16 bytes.")
    sys.exit()

message = input("Enter message to send: ")

# encrypt message using AES
cipher_text = aes_encrypt(message.encode(), key)

# create a connection to server to be able to transfer 
# ciphertext to be able decrypt soon
cli_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cli_sock.connect((SERVER_IP, SERVER_PORT))
cli_sock.sendall(cipher_text)
cli_sock.close()