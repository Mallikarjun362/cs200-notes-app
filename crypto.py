from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


# PKCS7 padding function
def pad(text):
    block_size = AES.block_size
    padding = block_size - len(text) % block_size
    return text + bytes([padding] * padding)

