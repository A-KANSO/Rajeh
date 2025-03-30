import psutil
import argparse
import time

conn_counts = {}
totalConns = 0

def buildBaseline(baseline_time):
    end_time = time.time() + baseline_time
    while time.time() < end_time:
        for p in psutil.pids():
            try:
                proc = psutil.Process(p)
                name = proc.name()
                hasConns = int(len(proc.connections()) > 0)
                if name in conn_counts:
                    (connected, total) = conn_counts[name]
                    conn_counts[name] = (connected + hasConns, total + 1)
                else:
                    conn_counts[name] = (hasConns, 1)
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                continue
        time.sleep(1)

def checkConnections(threshold):
    for p in psutil.pids():
        try:
            proc = psutil.Process(p)
            name = proc.name()
            hasConns = len(proc.connections()) > 0
            if hasConns:
                if name in conn_counts:
                    (connected, total) = conn_counts[name]
                    prob = connected / total
                    if prob < threshold:
                        print("Process %s has network connection at %f probability" % (name, prob))
                else:
                    print("New process %s has network connection" % name)
            else:
                if name in conn_counts:
                    (connected, total) = conn_counts[name]
                    prob = 1 - (connected / total)
                    if prob < threshold:
                        print("Process %s doesn't have network connection at %f probability" % (name, prob))
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Network connection monitor')
    parser.add_argument('--threshold', type=float, default=0.5, help='Threshold for network connection probability')
    parser.add_argument('--baseline_time', type=int, default=60, help='Time in seconds to establish the baseline')

    args = parser.parse_args()

    buildBaseline(args.baseline_time)
    checkConnections(args.threshold)
