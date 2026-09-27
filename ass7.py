# Experiment No. 7
# Regular Expressions (Regex) - Pattern Matching

import re


def find_emails(text):
    # Pattern for finding email addresses
    pattern = r"[a-zA-Z0-9._-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}"

    # Find all email addresses
    emails = re.findall(pattern, text)

    return emails


# Main program
text = input("Enter a text containing email addresses: ")

emails = find_emails(text)

if emails:
    print("\nEmail addresses found:")
    for email in emails:
        print(email)
else:
    print("\nNo email addresses found.")
