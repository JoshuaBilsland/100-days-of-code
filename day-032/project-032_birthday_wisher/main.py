##################### Normal Starting Project ######################
import datetime as dt
import pandas
import random
import smtplib

MY_EMAIL = "an@email.com"
MY_PASSWORD = "apassword"

# 2. Check if today matches a birthday in the birthdays.csv
today = (dt.datetime.now().month(), dt.datetime.now().day)
data = pandas.read_csv("day-032\project-032_birthday_wisher\birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today in birthdays_dict:
    path = f"day-032\project-032_birthday_wisher\letter_templates\letter_{random.randint(1,3)}.txt"

# 3. If there is a match, pick a random letter (letter_1.txt/letter_2.txt/letter_3.txt) from letter_templates and replace the [NAME] with the person's actual name from birthdays.csv
    with open(path) as letter:
        contents = letter.read()
        contents = contents.replace("[NAME]", birthdays_dict[today]["name"])

# 4. Send the letter generated in step 3 to that person's email address.    
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL
            to_addrs=birthdays_dict[today]["email"]
            msg=f"Subject: Happy Birthday!\n\n{contents}"
        )
