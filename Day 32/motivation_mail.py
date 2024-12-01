import smtplib
import datetime as dt
import os
from dotenv import load_dotenv
import random

now = dt.datetime.now()
weekday = now.weekday()

# Load environment variables from the .env file
load_dotenv()

# # Retrieve variables from environment
my_email = os.getenv("MY_EMAIL")
password = os.getenv("MY_PASSWORD")
to_email = os.getenv("TO_EMAIL")
   
print(my_email)
if weekday == 5:
    with open("quotes.txt") as file:
        all_quotes = file.readlines()
        random_quote = random.choice(all_quotes)
    print(random_quote)
    try: 
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=to_email,
                msg=f"Subject:Motivation\n\n{random_quote}"
            )
        print("Email sent successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")