import requests
from base64 import b64encode, b64decode
import argparse

def C2(url, data):
    encoded_data = b64encode(data.encode("utf-8")).decode("utf-8")  # Convert bytes to string
    response = requests.get(url, headers={'Cookie': encoded_data})
    if response.status_code == 200:
        content = response.content.decode("utf-8")
        # Properly pad the base64 string
        padding = 4 - (len(content) % 4)
        if padding != 4:
            content += "=" * padding
        print(b64decode(content).decode("utf-8"))  # Decode response content
    else:
        print(f"Error: {response.status_code} - {response.reason}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Send data to a specified URL.')
    parser.add_argument('url', type=str, help='The URL to send data to')
    parser.add_argument('data', type=str, help='The data to send')

    args = parser.parse_args()

    url = args.url
    data = args.data

    C2(url, data)
