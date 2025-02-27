import imaplib
import email
import pandas as pd
from email.header import decode_header

IMAP_SERVER = "imap.gmail.com"
EMAIL = "robustemmanuel@gmail.com"
PASSWORD = "titvmceuhymbcucn"

mail = imaplib.IMAP4_SSL(IMAP_SERVER)
mail.login(EMAIL, PASSWORD)
mail.select("inbox")


status, messages = mail.search(None, "UNSEEN")
email_ids = messages[0].split()

emails = []
for email_id in email_ids[:20]:
    status, msg_data = mail.fetch(email_id, "(RFC822)")
    for response_part in msg_data:
        if isinstance(response_part, tuple):
            msg = email.message_from_bytes(response_part[1])
            subject, encoding = decode_header(msg["Subject"])[0]
            subject = subject.decode(encoding) if encoding else subject
            emails.append({"subject": subject, "from": msg["From"]})

mail.logout()

# Convertir en DataFrame
df_emails = pd.DataFrame(emails)
df_emails.to_csv("emails_recus.csv", index=False)
