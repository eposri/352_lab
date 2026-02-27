
'''
well-known ports: 0-1023
registered ports: 1024-49151
    => 1234 / 1235 is a registered port for custom
dynamic/private ports: 49152-65535
'''
import socket
import sys
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad

#CLient has to exactly type in terminal argument of 4
#which are: python3, client.py, serverIP, server port, 16 byte key 
if len(sys.argv) != 4:
    print("Usage: python3 client.py <server IP> <server port> <16-byte key>")
    sys.exit()

#here declaring SERVER_IP to be argument 1 in terminal in this case server IP
#setting SERVER_PORT to be argument 2 in terminal in this case <server port>
#Setting key which used to encrypt to argument 3 in this case <16-byte key> 
# in terminal & turn into bits
SERVER_IP = sys.argv[1]
SERVER_PORT = int(sys.argv[2])
key = sys.argv[3].encode()

#key case just in case key not exactly 16 bytes then will tell client need 
# be exactly exactly 16 bytes
if len(key) != 16:
    print("Error: key must be exactly 16 bytes.")
    sys.exit()

#ask client enter message then turn message into bits with .encode()
message = input("Enter message to send: ")
message_bytes = message.encode()

#padd message into 16 bytes just incase user not d0 16 bytes because
#AES works in 16 bytes
padded_msg = pad(message_bytes, 16)

#declare encrypting tool with key
#then use encCipher to encrypt client message with .encrypt()
encCipher = AES.new(key, AES.MODE_ECB)
cipherText = encCipher.encrypt(padded_msg)

print("Cipher text:", cipherText)

#create a connection to server to be able to transfer 
# ciphertext to be able decrypt soon
cliSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliSock.connect((SERVER_IP, SERVER_PORT))
cliSock.sendall(cipherText)
cliSock.close()
