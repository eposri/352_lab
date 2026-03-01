import socket
import sys
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import unpad

# Requirement 2: python3 server.py <port number> <key>
if len(sys.argv) != 3:
    print("Usage: python3 server.py <port number> <16-byte key>")
    sys.exit()

PORT_NUMBER = int(sys.argv[1])
key = sys.argv[2].encode()

if len(key) != 16:
    print("Error: key must be exactly 16 bytes.")
    sys.exit()

# Create a socket
serverSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# Associate the socket with the port
serverSock.bind(('', PORT_NUMBER)) 

# Start listening for incoming connections (max 100)
serverSock.listen(100)

# will show to user where server listening on what port
print("Server listening on port:", PORT_NUMBER)

# Here is server keep accepting clients forever using while statement
while True:
    # accepts communication from client by client info
    print("Waiting for clients to connect...")
    cliSock, cliInfo = serverSock.accept()
    print("Client connected from:", cliInfo)

    # Receive encrypted message
    cipherText = b""
    while True:
        chunk = cliSock.recv(1024)#get up to 4096 bytes of data
        if not chunk:
            break
        cipherText += chunk

    cliSock.close()

# cipherText case just in case client enters message that is 0 length
    if len(cipherText) == 0:
        print("No data received.")
        continue

    # Decrypt and print
    try:
        decCipher = AES.new(key, AES.MODE_ECB)
        paddedPlain = decCipher.decrypt(cipherText)
        plainText = unpad(paddedPlain, 16)
        print("Decrypted message:", plainText.decode(errors="replace"))
    except:
        print("Decryption failed (wrong key or corrupted data).")