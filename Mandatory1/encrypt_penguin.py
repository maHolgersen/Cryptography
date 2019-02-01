from PIL import Image
from Crypto.Cipher import AES

from os import urandom

image = Image.open("tux.png").convert("RGBA").convert("RGB")
image_bytes_array = image.tobytes()


# Pads the data to satisfy AES's multiple-of-16-bytes requirements (to be completed)
def pad(data):
    return data + b"\x00"*(16-len(data)%16)


# create AES encryptor(to be completed)
def aes_encryption(data, key):
    IV = "A"*16
    aes = AES.new(key, AES.MODE_CBC, IV.encode("utf8"))
    ciphertext = aes.encrypt(data)
    return ciphertext


# Encrypt data with AES encryptor (to be completed)
# Removes paddding from the resulting ciphertext (to be completed)
def encrypt_data(data):
    key = urandom(16)
    encryption = aes_encryption(pad(data), key)

    return encryption


# Create a new PIL Image object and saves the siphertext image into the new image
ciphertext = encrypt_data(image_bytes_array)

# (uncomment the next two lines when the skeleton is complete)
ciphertext_image = Image.frombytes(image.mode, image.size, ciphertext, "raw", "RGB")
ciphertext_image.save("tux_encrypted.png")
