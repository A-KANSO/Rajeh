import random
import requests
from time import sleep
import argparse

def makeRequest(url):
    response = requests.get(url)
    print(f"Request made to {url}. Response status code: {response.status_code}")
    return

def getURL():
    return sites[random.randint(0, len(sites) - 1)].rstrip()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simulate browsing session.")
    parser.add_argument("sites_file", help="Path to the file containing URLs.")
    parser.add_argument("clickthrough", type=float, default=0.9, help="Clickthrough probability (default: 0.9)")
    parser.add_argument("sleeptime", type=int, default=0, help="Maximum sleep time in seconds (default: 0)")
    args = parser.parse_args()
    
    clickthrough = args.clickthrough
   
    sleeptime = args.sleeptime
    
    
    # Read sites from the specified file
    with open(args.sites_file, "r") as f:
        sites = f.readlines()
    
    # Start browsing session
    while random.random() < clickthrough:
        url = getURL()
        makeRequest(url)
        sleep(random.randint(0, sleeptime))
