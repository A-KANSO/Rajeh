import os
import re
import sys
from zipfile import ZipFile

email_regex = '[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}'
phone_regex = '[(]*[0-9]{3}[)]*-[0-9]{3}-[0-9]{4}'
ssn_regex = '[0-9]{3}-[0-9]{2}-[0-9]{4}'
regexes = [email_regex, phone_regex, ssn_regex]

def findPII(data):
    matches = []
    for regex in regexes:
        m = re.findall(regex, data)
        matches += m
    return matches

def printMatches(filedir, matches):
    if len(matches) > 0:
        print(filedir)
        for match in matches:
            print(match)

def parseDocx(root, docs):
    for doc in docs:
        matches = None
        filedir = os.path.join(root, doc)
        try:
            with ZipFile(filedir, "r") as zip:
                data = zip.read("word/document.xml")
                matches = findPII(data.decode("utf-8"))
            printMatches(filedir, matches)
        except Exception as e:
            print(f"An error occurred while processing {filedir}: {e}")

def parseText(root, txts):
    for txt in txts:
        filedir = os.path.join(root, txt)
        try:
            with open(filedir, "r", encoding="utf-8") as f:
                data = f.read()
            matches = findPII(data)
            printMatches(filedir, matches)
        except UnicodeDecodeError:
            print(f"UnicodeDecodeError: Could not decode {filedir} using utf-8 encoding.")
        except Exception as e:
            print(f"An error occurred while reading {filedir}: {e}")

def findFiles(directory, file_types):
    txt_ext = [ext.strip() for ext in file_types.split(",") if ext.strip() != ".docx"]
    print(f"Searching in directory: {directory}")
    print(f"File types: {txt_ext}")
    for root, dirs, files in os.walk(directory):
        parseDocx(root, [f for f in files if f.endswith(".docx")])
        for ext in txt_ext:
            parseText(root, [f for f in files if f.endswith(ext)])

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python FileDiscovery.py <directory> <file_types>")
        sys.exit(1)

    directory = sys.argv[1]
    file_types = sys.argv[2]
    print(f"Received directory: {directory}")
    print(f"Received file types: {file_types}")
    findFiles(directory, file_types)
