from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


# PKCS7 padding function
def pad(text):
    block_size = AES.block_size
    padding = block_size - len(text) % block_size
    return text + bytes([padding] * padding)

#padding the key to AES 128 bit key
def pad_string_to_128_bytes(input_string):
    desired_length = 16

    input_bytes = input_string.encode("utf-8")
    if len(input_bytes) >= desired_length:
        result_bytes = input_bytes[:desired_length]
    else:
        padding_length = desired_length - len(input_bytes)
        padding = b"\x00" * padding_length
        result_bytes = input_bytes + padding

    return result_bytes
