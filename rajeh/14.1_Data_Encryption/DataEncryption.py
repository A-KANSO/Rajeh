from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from pathlib import Path
import os
import sys

# Retrieve command-line arguments
key = sys.argv[1].encode()  # Convert key to bytes
directory = sys.argv[2]
ext = sys.argv[3]

# Define encryption key and initialization vector
iv = os.urandom(16)

# Define function to encrypt data using AES encryption with PKCS#7 padding
def encrypt(data):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_data = pad(data, AES.block_size)
    return cipher.encrypt(padded_data)

# Define function to encrypt a file
def encryptFile(path):
    with open(path, "rb") as f:
        data = f.read()
    encrypted_data = encrypt(data)
    encrypted_file_path = path + ".encrypted"
    with open(encrypted_file_path, "wb") as f:
        f.write(encrypted_data)
    os.remove(path)

# Define function to get files with a specific extension in a directory
def getFiles(directory, ext):
    paths = list(Path(directory).rglob("*" + ext))
    return paths

# Get list of file paths with the specified extension in the directory
paths = getFiles(directory, ext)

# Encrypt each file in the list of file paths
for path in paths:
    encryptFile(str(path))

print("Files encrypted successfully.")
