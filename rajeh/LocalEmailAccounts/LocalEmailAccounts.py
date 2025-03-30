import argparse
from libratom.lib.pff import PffArchive

def process_archive(filename):
    archive = PffArchive(filename)
    for folder in archive.folders():
        if folder.get_number_of_sub_messages() != 0:
            for message in folder.sub_messages:
                print("Sender: %s" % message.get_sender_name())
                print("Subject: %s" % message.get_subject())
                print("Message: %s" % message.get_plain_text_body())

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process an Outlook PST file.")
    parser.add_argument("filename", help="Path to the .pst file")
    args = parser.parse_args()
    filename = args.filename.replace("/", "\\")  # Replace forward slashes with backslashes
    
    process_archive(filename)
