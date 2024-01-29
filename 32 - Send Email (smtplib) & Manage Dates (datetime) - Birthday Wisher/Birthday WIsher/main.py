##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import random
import datetime as dt
import smtplib
import pandas
import os

#Read data
data = pandas.read_csv("info.csv")
data_array = []

# Iterate through rows
for index, row in data.iterrows():
    person = {
        "name": row['name'],
        "email": row['email'],
        "birthday": dt.datetime(month=row['month'], day=row['day'], year=row['year'])
    }
    data_array.append(person)

my_email = "oslovdobrov@gmail.com"
password = os.environ.get("OSLO_MAIL_KEY")


for person in data_array:
    if dt.datetime.now().month == person["birthday"].month and dt.datetime.now().day == person["birthday"].day:
        
        with open(f"letter_templates/letter_{random.randint(1, 3)}.txt") as file:
            letter = file.readlines()

        letter = [line.replace("[NAME]", person['name']) for line in letter]
        letter = ''.join(letter)
        
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=f"{person['email']}",
                msg=f"Subject:милый {person['name']}\n\n {letter}".encode('utf-8')
            )
            connection.close()



