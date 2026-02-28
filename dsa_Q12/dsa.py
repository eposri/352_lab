from Cryptodome.Signature import DSS
from Cryptodome.PublicKey import DSA
from Cryptodome.Hash import SHA256

def dsa_sign(message):
    # Create a private key
    key = DSA.generate(2048)

    # Save the private key to the file
    f = open("dsa_private_key.pem", "wb")
    f.write(key.export_key())
    f.close()

    # Save the corresponding key to the file
    f = open("dsa_public_key.pem", "wb")
    # Get the corresponding public key
    pubKey =  key.publickey().export_key()
    f.write(pubKey)
    f.close()

    # Sign a message
    hash_obj = SHA256.new(message.encode())
    signer = DSS.new(key, 'fips-186-3')
    signature = signer.sign(hash_obj)

    return signature


def dsa_verify(message, signature):
    # Load the public key
    f = open("dsa_public_key.pem", "rb")
    hash_obj = SHA256.new(message.encode())
    pub_key = DSA.import_key(f.read())
    verifier = DSS.new(pub_key, 'fips-186-3')

    # Verify the authenticity of the message
    try:
            verifier.verify(hash_obj, signature)
            print("The message is authentic.")
    except ValueError:
            print("The message is not authentic.")
