import socket
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad


# Server's IP address
SERVER_IP = '127.0.0.1'


# The server's port number
SERVER_PORT = 1235
'''
well-known ports: 0-1023
registered ports: 1024-49151
    => 1234 / 1235 is a registered port for custom
dynamic/private ports: 49152-65535
'''

######### BASIC ENCRYPTION ###########

while True:
# The key (must be 16 bytes)
    sixteen_byt_key = input("Please enter a 16 byte key: ").strip()
    # given key: abcdefghnbfghasd (Requirement 4)
    key = sixteen_byt_key.encode()
    # makes sure that the users input is exactly 16 bytes
    if len(key) != 16:
        print("Invalid key size, try again")
    else:
        break
    
message = input("Enter message to send: ").strip()
message_byt = message.encode()

# Padding the message below to be as multiple of 16
padded_msg = pad(message_byt, 16)

# Set up the AES encryption class
encCipher = AES.new(key, AES.MODE_ECB)

# AES requires plain/cipher text blocks to be 16 bytes
cipherText = encCipher.encrypt(padded_msg)

print(type(key))

print("Cipher text: ", cipherText)

# Send the message to the server
# NOTE: the user input is of type string
# Sending data over the socket requires.
# First converting the string into bytes.
# encode() function achieves this.

# The client's socket
cliSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Attempt to connect to the server
cliSock.connect((SERVER_IP, SERVER_PORT))

cliSock.send(cipherText)
cliSock.close()
print("The Encrypted message was sent over to server.")
