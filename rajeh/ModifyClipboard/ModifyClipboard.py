import win32clipboard  # Library for accessing the clipboard on Windows
import re              # Library for regular expressions
import argparse        # Library for command-line argument parsing
from time import sleep # Library for adding delays

# Regular expressions for identifying sensitive information
email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
phone_regex = r'\b(?:\d{3}[-.]?|\(\d{3}\) )?\d{3}[-.]?\d{4}\b'
url_regex = r'\bhttps?://\S+\b'
date_regex = r'\b\d{1,2}/\d{1,2}/\d{4}\b'
ip_regex = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
credit_card_regex = r'\b\d{4}[- ]?\d{4}[- ]?\d{4}[- ]?\d{4}\b'
ssn_regex = r'\b\d{3}-\d{2}-\d{4}\b'

# Descriptions for each type of sensitive information
email_regex_description = "Email addresses"
phone_regex_description = "Phone numbers"
url_regex_description = "URLs"
date_regex_description = "Dates"
ip_regex_description = "IP addresses"
credit_card_regex_description = "Credit card numbers"
ssn_regex_description = "Social security numbers"

def replace_sensitive_info(data, pattern, replacement):
    """
    Replace sensitive information in clipboard data based on a regular expression pattern.
    Args:
        data (str): The clipboard data as a string.
        pattern (str): The regex pattern to identify sensitive information.
        replacement (str): The value to replace matched information with.
    Returns:
        str: Modified clipboard data with sensitive information replaced.
    """
    modified_data = re.sub(pattern, replacement, data)
    return modified_data

def parse_arguments():
    """
    Parse command-line arguments for the type of sensitive information to replace and the replacement value.
    Returns:
        Namespace: Parsed command-line arguments.
    """
    parser = argparse.ArgumentParser(description="Replace sensitive information in clipboard data.")
    parser.add_argument("--type", choices=['email', 'phone', 'url', 'date', 'ip', 'credit_card', 'ssn'], required=True, help="Type of sensitive information to replace")
    parser.add_argument("--replacement", required=True, help="Replacement value for sensitive information")
    return parser.parse_args()

def main():
    """
    Main function to monitor clipboard data and replace specified sensitive information with a custom replacement.
    """
    args = parse_arguments()
    # Map each type choice to its regex pattern and description
    choices = {
        'email': (email_regex, email_regex_description),
        'phone': (phone_regex, phone_regex_description),
        'url': (url_regex, url_regex_description),
        'date': (date_regex, date_regex_description),
        'ip': (ip_regex, ip_regex_description),
        'credit_card': (credit_card_regex, credit_card_regex_description),
        'ssn': (ssn_regex, ssn_regex_description)
    }

    pattern, pattern_description = choices[args.type]
    replacement = args.replacement

    try:
        while True:
            # Access the clipboard data
            win32clipboard.OpenClipboard()
            data = win32clipboard.GetClipboardData()
            win32clipboard.CloseClipboard()

            # Replace sensitive information if it exists in the clipboard data
            modified_data = replace_sensitive_info(data, pattern, replacement)

            if modified_data != data:
                # If modifications were made, update the clipboard with the modified data
                win32clipboard.OpenClipboard()
                win32clipboard.EmptyClipboard()
                win32clipboard.SetClipboardText(modified_data)
                win32clipboard.CloseClipboard()
                print(f"Replaced {pattern_description} in clipboard with custom value")
                break  # Exit the loop after a successful replacement

            sleep(1)  # Delay to reduce CPU usage while waiting for clipboard changes

    except KeyboardInterrupt:
        print("Script terminated by user")  # Graceful exit on keyboard interrupt
    except Exception as e:
        print(f"An error occurred: {e}")  # Print any other exceptions

# Entry point for the script
if __name__ == "__main__":
    main()
