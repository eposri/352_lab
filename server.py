import socket
import sys
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import unpad

# Requirement 2: python3 server.py <port number> <key>
#Check the argument length of what the user inputs for server
#3 arguments in terminal: server.py(0), portnumber(1) 16 - byte key(2)
if len(sys.argv) != 3:
    print("Usage: python3 server.py <port number> <16-byte key>")
    sys.exit()

#PORT_NUMBER will be set equal to argument 1 in terminal
#in this case <port number>
#Then program will initialize variable key to argument 2 in terminal
#in this case <16-byte key>
PORT_NUMBER = int(sys.argv[1])
key = sys.argv[2].encode()

#key case here just in case key is not exactly 16 bytes
#will inform user to enter exactly 16 byte key
if len(key) != 16:
    print("Error: key must be exactly 16 bytes.")
    sys.exit()

# Create socket from which client and server can communicate in
serverSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSock.bind(("", PORT_NUMBER))
serverSock.listen(100)

#will show to user where server listening on what port
print("Server listening on port:", PORT_NUMBER)

# Here is server keep accepting clients forever using while statement
while True:
    #accepts communication from client by client info
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

#cipherText case just in case client enters message that is 0 length
    if len(cipherText) == 0:
        print("No data received.")
        continue

    # Decrypt and print
    try:
        #announcing decCIpher whic will be used to decrypt message
        #Then will decrypt ciphertext from client side 
        #Once decrypted will use unpad function to remove extra bytes added to give original text
        #finally will turn message from bits to str format for user to understand with .decode()
        decCipher = AES.new(key, AES.MODE_ECB)
        paddedPlain = decCipher.decrypt(cipherText)
        plainText = unpad(paddedPlain, 16)
        print("Decrypted message:", plainText.decode(errors="replace"))
    except:
        print("Decryption failed (wrong key or corrupted data).")

