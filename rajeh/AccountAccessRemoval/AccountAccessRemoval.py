import platform
import argparse
import getpass 
from win32com import adsi

def setWindowsPassword(username, password):
    
    ads_obj = adsi.ADsGetObject("WinNT://localhost/%s,user" % username)
    ads_obj.Getinfo()
    ads_obj.SetPassword(password)

def setLinuxPassword(username, password):
    import os
    os.system('echo -e "newpass\nnewpass" | passwd %s' % username)

def changeCriteria(username):
    if username in ["testuser", "user1", "FYP"]:
        return True
    else:
        return False

def main(computer, username, new_password):
    if platform.system() == "Windows":
        import wmi
        w = wmi.WMI()
        for user in w.Win32_UserAccount():
            if user.Name == username and changeCriteria(username):
                print("Changing password: %s" % username)
                setWindowsPassword(username, new_password)
                print("Password changed successfully.")
                break
    else:
        import pwd
        for p in pwd.getpwall():
            if p.pwd_name == username and (p.pwd_uid == 0 or p.pw_uid > 500) and changeCriteria(username):
                print("Changing password: %s" % username)
                setLinuxPassword(username, new_password)
                print("Password changed successfully.")
                break
        else:
            print("User not found or does not meet criteria.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Change user password on a computer.")
    parser.add_argument("computer", help="Name of the computer")
    parser.add_argument("username", help="Username")
    parser.add_argument("new_password", help="New password")
    args = parser.parse_args()

    main(args.computer, args.username, args.new_password)
