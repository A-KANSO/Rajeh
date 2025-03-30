import pathlib
import argparse

def getTimestamps(filename):
    fname = pathlib.Path(filename)
    if not fname.exists():  # File does not exist
        return []
    stats = fname.stat()
    return (stats.st_ctime, stats.st_mtime, stats.st_atime)

def checkTimestamps(filename, create, modify, access):
    stats = getTimestamps(filename)
    if len(stats) == 0:
        return False  # File does not exist
    (ctime, mtime, atime) = stats
    if float(create) != float(ctime):
        return False  # File creation time is incorrect
    elif float(modify) != float(mtime):
        return False  # File modification time is incorrect
    elif float(access) != float(atime):
        return False  # File access time is incorrect
    return True

def checkDecoyFiles(decoy_file):
    with open(decoy_file, "r") as f:
        for line in f:
            vals = line.rstrip().split(",")
            if len(vals) != 4:
                print(f"Invalid format in line: {line}")
                continue
            filename, create, modify, access = vals
            if not checkTimestamps(filename, create, modify, access):
                print(f"{filename} has been tampered with.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Check the timestamps of decoy files.")
    parser.add_argument("decoy_file", help="Path to the decoys.txt file")
    args = parser.parse_args()
    
    checkDecoyFiles(args.decoy_file)
    
