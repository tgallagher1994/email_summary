import imaplib
import email
from dotenv import load_dotenv

import os

# check if virtual environment is running
def is_virtualenv():
    return 'VIRTUAL_ENV' in os.environ

if is_virtualenv():
    print("Running inside a virtual environment.")
else:
    print("Not running inside a virtual environment.")

class EmailClient:
    def __init__(self):
        # Load environment variables
        load_dotenv()
        self.email_user = os.getenv("EMAIL_USER")
        self.email_pass = os.getenv("EMAIL_PASS")
        self.mail_server = imaplib.IMAP4_SSL("imap.outlook.com")
           

    def login_email(self, email_user, email_pass):
        #Fetches unread emails and prints subject, sender, and date.
        self.mail.login("EMAIL_USER", "EMAIL_PASS")
        self.mail.select("inbox")

    def fetch_unread_emails(self):
        """Fetches unread emails and prints subject, sender, and date."""
        if not self.mail:
            print("❌ Not connected to any mail server. Call connect() first.")
            return

        try:
            status, messages = self.mail.search(None, 'UNSEEN')  # Fetch unread emails
            email_ids = messages[0].split()

            if not email_ids:
                print("📭 No unread emails.")
                return

            print(f"📩 Found {len(email_ids)} unread emails.\n")

            for e_id in email_ids:
                status, msg_data = self.mail.fetch(e_id, "(RFC822)")
                
                for response_part in msg_data:
                    if isinstance(response_part, tuple):
                        msg = email.message_from_bytes(response_part[1])

                        # Decode email subject
                        subject, encoding = decode_header(msg["Subject"])[0]
                        if isinstance(subject, bytes):
                            subject = subject.decode(encoding or "utf-8")

                        # Extract sender
                        sender = msg.get("From")

                        # Extract date
                        date = msg.get("Date")

                        print(f"Subject: {subject}")
                        print(f"From: {sender}")
                        print(f"Date: {date}\n")

        except imaplib.IMAP4.error as e:
            print(f"❌ IMAP Error: {e}")
box1 = EmailClient()
box1.fetch_unread_emails()


