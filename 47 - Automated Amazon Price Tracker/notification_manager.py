import requests
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header



class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.

    email = os.environ.get("email")
    password = os.environ.get("password")

    def send_email(self, receiver, subject, message):
        try:
            # Create a MIME multipart message
            msg = MIMEMultipart()
            msg['From'] = NotificationManager.email
            msg['To'] = receiver
            msg['Subject'] = Header(subject, 'utf-8')

            # Attach the message body (plain text)
            msg.attach(MIMEText(message, 'plain', 'utf-8'))

            # Connect to the SMTP server and send the email
            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(user=NotificationManager.email, password=NotificationManager.password)
                connection.send_message(msg)  # Use send_message for MIMEText objects
                connection.close()
        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")
        else:
            print(f"Message to {receiver} sent successfully")

    pass