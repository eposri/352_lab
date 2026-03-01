from Cryptodome.PublicKey import RSA
from Cryptodome.Signature.pkcs1_15 import PKCS115_SigScheme
from Cryptodome.Hash import SHA256
import binascii
import Cryptodome.Signature.pkcs1_15 


def rsa_sign(message):
    # randomly generate keys instead of loading pre-generated keys
    key_pair = RSA.generate(bits=1024)
    pub_key = key_pair.publickey()
    
    # save private key to file
    f = open("rsa_private_key.pem", "wb")
    f.write(key_pair.export_key())
    f.close()

    # save corresponding public key to file
    f = open("rsa_public_key.pem", "wb")
    f.write(pub_key.export_key())
    f.close()

    hash_msg = SHA256.new(message.encode())
    signature = Cryptodome.Signature.pkcs1_15.new(key_pair)
    signature = signature.sign(hash_msg)
    return signature

def rsa_verify(message, signature):
    hash_msg = SHA256.new(message.encode())

    # load public key from file
    client_pub_key = RSA.import_key(open("rsa_public_key.pem", "rb").read())
    verifier = Cryptodome.Signature.pkcs1_15.new(client_pub_key)

    try:
        verifier.verify(hash_msg, signature)
        print("The RSA signature is authentic.")
    except ValueError:
        print("The RSA signature is not authentic.")