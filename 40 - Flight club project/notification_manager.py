import requests
import os
import smtplib



class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.

    email = os.environ.get("email")
    password = os.environ.get("password")

    def send_email(self, receiver, subject, message):
        try:
            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(user=NotificationManager.email, password=NotificationManager.password)
                connection.sendmail(
                    from_addr=NotificationManager.email,
                    to_addrs=f"{receiver}",
                    msg=f"Subject:{subject}\n\n {message}"
                )
                connection.close()
        except Exception as e:
            # This will catch other exceptions and print the error message
            print(f"An unexpected error occurred: {str(e)}")
        else:
            print(f"Message to {receiver} sent it succesfully")

    pass