# import smtplib
# import os

# my_email = "oslovdobrov@gmail.com"
# password = os.environ.get("OSLO_MAIL_KEY")


# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="oslotesting7@gmail.com",
#         msg="Subject:Hello\n\nThis is the body of my email"
#     )
#     connection.close()

# Working with date and time in Python
# import datetime as dt

# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(day_of_week)

# date_of_birth = dt.datetime(year=1995, month=12, day=15, hour=4)
# print(date_of_birth)

import random
import os
import datetime as dt
import smtplib

weekday = dt.datetime.now().weekday()
if weekday == 0:
    with open("quotes.txt") as file:
        quotes = file.readlines()
        if quotes:
            random_quote = random.choice(quotes)

    my_email = "oslovdobrov@gmail.com"
    password = os.environ.get("OSLO_MAIL_KEY")

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="oslotesting7@gmail.com",
            msg=f"Subject:Motivation quote\n\n{random_quote}"
        )
        connection.close()


    


        

