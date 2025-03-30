# Decryption script (decrypt_files.py)

from pathlib import Path
from Crypto.Cipher import AES
import os
import sys

# Define function to decrypt data using AES decryption
def decrypt(data, key, iv): 
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return cipher.decrypt(data)

# Define function to decrypt a file
def decryptFile(path, key, iv):
    with open(str(path), "rb") as f:
        data = f.read()

    try:
        decrypted_data = decrypt(data, key, iv)
        
        # Determine original file name (remove .encrypted extension)
        original_path = str(path).replace(".encrypted", "")
        
        with open(original_path, "wb") as f:
            f.write(decrypted_data)
        
        os.remove(str(path))  # Remove the encrypted file after decryption
        print(f"Decrypted {path} successfully.")
    except Exception as e:
        print(f"Failed to decrypt {path}: {e}")

# Define function to get files with a specific extension in a directory
def getFiles(directory, ext):
    paths = list(Path(directory).rglob("*" + ext))
    return paths

# Check if command-line arguments are provided
if len(sys.argv) != 3:
    print("Usage: python decrypt_files.py <key> <directory>")
    sys.exit(1)

# Extract encryption key and directory from command-line arguments
key = sys.argv[1].encode()  # Ensure key is encoded in the same format
directory = sys.argv[2]

# Generate a random initialization vector (IV)
iv = os.urandom(16)

# Specify file extension of encrypted files
ext = ".encrypted"

# Get list of file paths with the specified extension in the directory
paths = getFiles(directory, ext)

# Debugging: Print key, directory, and file paths for troubleshooting
print("Encryption key:", key)
print("Directory:", directory)
print("File paths:")
for path in paths:
    print(path)

# Decrypt each file in the list of file paths
for path in paths:
    decryptFile(path, key, iv)

print("Files decrypted successfully.")
