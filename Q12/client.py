import socket
import sys

from aes import aes_encrypt
from dsa import dsa_sign
from rsa import rsa_sign

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

print("\n======= Digital Signature Menu =======")
print("1. RSA")
print("2. DSA")

while True:
    choice = input("Choose signature option (1, or 2): ").strip()

    message = input("Enter message to send: ")

    if choice == "1":
        signature = rsa_sign(message)
        break
    elif choice == "2":
        signature = dsa_sign(message)
        break
    else:
        print("Invalid input, please enter 1 or 2.")

# append signature to message for AES with delimiter for separation later
message = message.encode() + b"+++" + choice.encode() + b"+++" + signature

# encrypt message using AES
cipher_text = aes_encrypt(message, key)

# create a connection to server to be able to transfer 
# ciphertext to be able decrypt soon
cli_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cli_sock.connect((SERVER_IP, SERVER_PORT))
cli_sock.sendall(cipher_text)
cli_sock.close()