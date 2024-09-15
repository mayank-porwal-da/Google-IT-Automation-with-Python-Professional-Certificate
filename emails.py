#!/usr/bin/env python3

import email
import smtplib
"""
Use the following details to pass the parameters to emails.generate_email():

From: automation@example.com
To: student@example.com
Subject line: Upload Completed - Online Fruit Store
E-mail Body: All fruits are uploaded to our website successfully. A detailed list is attached to this email.
Attachment: Attach the path to the file processed.pdf
"""

def generate_email(from_email="automation@example.com", to_email = "student@example.com", 
                   subject = '', body = '', attachment_path=''):
    email_info = email.message.EmailMessage()
    email_info['From'] = from_email
    email_info['To'] = to_email
    email_info['Subject'] = subject
    email_info.set_content(body)
    try:
        with open(attachment_path, 'rb') as attachment:
            email_info.add_attachment(attachment.read(), 
                                    maintype='application', 
                                    subtype='octet-stream', 
                                    filename=attachment_path.split('/')[-1])
    except:
        print("Attachment not found")
    return email_info

def send_email(message):
    # Code to send the email
    # mail_server = smtplib.SMTP('localhost')
    mail_server = smtplib.SMTP('smtp.gmail.com', 587)
    mail_server.starttls()
    with open("google_pass_key.txt", "r") as file:
        google_pass_key = file.read().strip()
    mail_server.login('mayankporwal14@gmail.com', google_pass_key)
    mail_server.send_message(message)
    mail_server.quit()
    print("Email sent successfully!")

    