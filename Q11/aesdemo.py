### To install the pycryptodome library ####
# sudo apt install python3-pip
# python3 -m venv env
# sudo pip3 install pycryptodomex
# source ./env/bin/activate
# python3 aesdemo.py
 
from Cryptodome.Cipher import AES

######### BASIC ENCRYPTION ###########

# The key (must be 16 bytes)
key = b'Sixteen byte key'

# Set up the AES encryption class
encCipher = AES.new(key, AES.MODE_ECB)

# AES requires plain/cipher text blocks to be 16 bytes
cipherText = encCipher.encrypt(b'hello12345678s0d1111111111111111')

print("Cipher text: ", cipherText)


########### BASIC DECRYPTION ##############

# Set up the AES encryption class
decCipher = AES.new(key, AES.MODE_ECB)

# AES requires plain/cipher text blocks to be 16 bytes
plainText = decCipher.decrypt(cipherText)

print("Decrypted text: ", plainText)