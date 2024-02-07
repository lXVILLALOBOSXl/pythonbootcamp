import requests
import os
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException



class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.

    TWILIO_KEY = os.environ.get("TWILIO_KEY")
    TWILIO_SID = os.environ.get("TWILIO_SID")
    TWILIO_NUMBER = '+17604604539'

    def __init__(self):
        self.client = Client(NotificationManager.TWILIO_SID, NotificationManager.TWILIO_KEY)

    def send_message(self, receiver, subject, message):
        try:
            # This will try to send a text message from Twilio
            message = self.client.messages.create(
                from_= NotificationManager.TWILIO_NUMBER,
                body=f"{subject}\n{message}",
                to=receiver
            )
        except TwilioRestException as e:
            # This will print the error message from Twilio
            print(f"Twilio Error: {e.msg}")
        except Exception as e:
            # This will catch other exceptions and print the error message
            print(f"An unexpected error occurred: {str(e)}")
        else:
            print(f"Message to {receiver} sent it succesfully")

    pass