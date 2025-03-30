import socket
import sys
from Crypto.Cipher import AES

def decrypt(data, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return cipher.decrypt(data)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python EncryptedChannelServer.py <host> <port> <key>")
        sys.exit(1)

    host = sys.argv[1]
    port = int(sys.argv[2])
    key = bytes(sys.argv[3], 'utf-8')

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print(f"Server listening on {host}:{port}")
        conn, addr = s.accept()
        with conn:
            while True:
                iv = conn.recv(16)
                length = conn.recv(1)   # Assumes short messages
                data = conn.recv(1024)
                if not data:
                    break
                print("Received: %s" % decrypt(data, key, iv).decode("utf-8")[:ord(length)])
