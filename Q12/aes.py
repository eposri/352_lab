from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import unpad, pad


def aes_encrypt(message, key):
    # pad message into 16 bytes
    padded_msg = pad(message, 16)

    # declare encrypting tool with key
    # then use encCipher to encrypt client message with .encrypt()
    enc_cipher = AES.new(key, AES.MODE_ECB)
    cipher_text = enc_cipher.encrypt(padded_msg)
    return cipher_text

def aes_decrypt(key, cipher_text):
    # Decrypt and print
    try:
        dec_cipher = AES.new(key, AES.MODE_ECB)
        padded_plain = dec_cipher.decrypt(cipher_text)
        plain_text = unpad(padded_plain, 16)

        # for submitting purposes fix this
        #if b"+++" in plain_text:
        cipher_text, choice, signature = plain_text.split(b"+++")
        print("Decrypted message:", cipher_text.decode())
        choice = choice.decode()
        return cipher_text, signature, choice
        #else:
            #print("Decrypted message:", plain_text.decode())
            #return plain_text, None
    except:
        print("Decryption failed (wrong key or corrupted data).")