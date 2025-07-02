#!/usr/bin/env python3

import email.message
import mimetypes
import os
import smtplib

def generate_email(sender, receiver, subject, body, att$
    message = email.message.EmailMessage()
    message["From"] = sender
    message["To"] = receiver
    message["Subject"] = subject
    message.set_content(body)

    if attachment:
        filename = os.path.basename(attachment)
        mime_type, _ = mimetypes.guess_type(attachment)
        mime_main, mime_sub = mime_type.split("/", 1)

        with open(attachment, "rb") as attachment_file:
            message.add_attachment(
                attachment_file.read(),
                maintype=mime_main,
                subtype=mime_sub,
                filename=filename,
    return message

def send_email(message):
    with smtplib.SMTP("localhost") as mail_server:
        mail_server.send_message(message)

