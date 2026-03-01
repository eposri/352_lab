from Cryptodome.Signature import DSS
from Cryptodome.PublicKey import DSA
from Cryptodome.Hash import SHA256

def dsa_sign(message):
    # create a private key
    key = DSA.generate(2048)

    # save the private key to the file
    f = open("dsa_private_key.pem", "wb")
    f.write(key.export_key())
    f.close()

    # save the corresponding key to the file
    f = open("dsa_public_key.pem", "wb")

    # get the corresponding public key
    pub_key =  key.publickey().export_key()
    f.write(pub_key)
    f.close()

    # sign a message
    hash_obj = SHA256.new(message.encode())
    signer = DSS.new(key, 'fips-186-3')
    signature = signer.sign(hash_obj)

    return signature


def dsa_verify(message, signature):
    # load the public key
    f = open("dsa_public_key.pem", "rb")
    hash_obj = SHA256.new(message.encode())
    pub_key = DSA.import_key(f.read())
    verifier = DSS.new(pub_key, 'fips-186-3')

    # verify the authenticity of the message
    try:
            verifier.verify(hash_obj, signature)
            print("The DSA signature is authentic.")
    except ValueError:
            print("The DSA signature is not authentic.")
