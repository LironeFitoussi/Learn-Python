##################### Extra Hard Starting Project ######################
import datetime as dt
import random
import pandas as pd
from mailer import sendmail

# 2. Check if today matches a birthday in the birthdays.csv
today = dt.datetime.now()

# Check todays month and day
today_month = today.month
today_day = today.day

# load the birthdays.csv
bd_file = pd.read_csv("birthdays.csv")
bd_dict = bd_file.to_dict(orient="records")

# Check if today matches a birthday in the birthdays.csv

for bd in bd_dict:
    if bd["month"] == today_month and bd["day"] == today_day:
        birthday_person = bd["name"]
        birthday_person_email = bd["email"]
        print(f"Today is {birthday_person}'s birthday!")
    
    # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
        with open(f"letter_templates/letter_{random.randint(1,3)}.txt") as file:
            letter = file.read()
            letter = letter.replace("[NAME]", birthday_person)
            print(letter)
    # 4. Send the letter generated in step 3 to that person's email address.
        sendmail(birthday_person_email, letter)



