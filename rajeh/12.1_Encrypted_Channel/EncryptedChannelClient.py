import socket
import os
import sys
from Crypto.Cipher import AES

def encrypt(data, key, iv):
    # Pad data as needed
    data += " " * (16 - len(data) % 16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return cipher.encrypt(bytes(data, "utf-8"))

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python EncryptedChannelClient.py <host> <port> <key> <message>")
        sys.exit(1)

    host = sys.argv[1]
    port = int(sys.argv[2])
    key = sys.argv[3].encode('utf-8')
    message = sys.argv[4]

    if len(key) not in [16, 24, 32]:
        print("Error: Key must be 16, 24, or 32 bytes long.")
        sys.exit(1)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        iv = os.urandom(16)
        s.send(iv)
        s.send(bytes([len(message)]))
        encrypted = encrypt(message, key, iv)
        print("Sending %s" % encrypted.hex())
        s.sendall(encrypted)
