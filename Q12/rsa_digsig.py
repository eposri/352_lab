# sudo apt install python3-pip
# python3 -m venv env
# sudo pip3 install pycryptodomex
# cd env
# source ./env/bin/activate
# python3 rsasig.py 

from Cryptodome.PublicKey import RSA
from Cryptodome.Signature.pkcs1_15 import PKCS115_SigScheme
from Cryptodome.Hash import SHA256
import binascii
import Cryptodome.Signature.pkcs1_15 

###############################################################
# If you want to randomly generate keys instead of loading 
# pre-generated keys from files, uncomment this.
# Generate 1024-bit RSA key pair (private + public key)
keyPair = RSA.generate(bits=1024)
# Get just the public key
pubKey = keyPair.publickey()
privKey = keyPair.privatekey()
###############################################################


def rsa_client(user_msg): 
    # The name of the public key file
    #PUBLIC_KEY_FILE_NAME = "public-key.pem"
    # Private key file name
    #PRIVATE_KEY_FILE_NAME = "private-key.pem"
    # Load the public key
    #pubKey = RSA.import_key(open(PUBLIC_KEY_FILE_NAME).read())
    # Load the private key
    #privKey = RSA.import_key(open(PRIVATE_KEY_FILE_NAME).read())

    # Save the private key to the file
    f = open("rsa_private_key.pem", "wb")
    f.write(privKey.export_key())
    f.close()

    # Save the private key to the file
    f = open("rsa_public_key.pem", "wb")
    # Get the corresponding public key
    f.write(pubKey.export_key())
    f.close()

    # User's message to be digitally signed by RSA
    msg = user_msg.encode()

    # Compute the hashes of both messages
    hash = SHA256.new(msg)

    # Sign the hash
    sig1 = Cryptodome.Signature.pkcs1_15.new(privKey)
    signature = sig1.sign(hash)
    return signature


##################### On the arrival side #########################
# Note, we will have to take the decrypted message, hash it and then provide the hash and the signature to the 
# verify function

def rsa_server(decrypted_msg, signature):

    hash = SHA256.new(decrypted_msg.encode())
        
    verifier = Cryptodome.Signature.pkcs1_15.new(pubKey)


    # If the verification succeeds, nothing is returned.  Otherwise a ValueError exception is raised
    # Let's try this with the valid message
    try:
        verifier.verify(hash, signature)
        print("The signature is valid!")
    except ValueError:    
        print("The signature is not valid!")
