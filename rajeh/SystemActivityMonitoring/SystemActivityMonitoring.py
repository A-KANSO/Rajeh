import win32evtlog
import argparse

def checkEvents(server, logtype, event_id):
    flags = win32evtlog.EVENTLOG_FORWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ
    failures = {}
    
    h = win32evtlog.OpenEventLog(server, logtype)
    while True:
        events = win32evtlog.ReadEventLog(h, flags, 0)
        
        if events:
            for event in events:
                if event.EventID == event_id:
                    if event.StringInserts[0].startswith("S-1-5-21"):
                        account = event.StringInserts[1]
                        if account in failures:
                            failures[account] += 1
                        else:
                            failures[account] = 1
        else:
            break
    
    return failures

def main(server, logtype, event_id):
    failures = checkEvents(server, logtype, event_id)
    
    for account in failures:
        print("%s: %s logins with administrative rights or privileges granted through group membership or user rights assignments." % (account, failures[account]))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Check event log for specific events.")
    parser.add_argument("--server", default="localhost", help="Name of the server to check.")
    parser.add_argument("--logtype", default="Security", help="Type of log to check (e.g., Security, System, Application).")
    parser.add_argument("--event_id", type=int, default=4672, help="Event ID to check for.")
    args = parser.parse_args()
    
    main(args.server, args.logtype, args.event_id)
