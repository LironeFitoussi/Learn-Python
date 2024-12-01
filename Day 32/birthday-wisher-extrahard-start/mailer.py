import smtplib
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Retrieve variables from environment
my_email = os.getenv("MY_EMAIL")
password = os.getenv("MY_PASSWORD")

def sendmail(target, msg):
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=target,
                msg=msg
                # f"Subject:Happy Birth Day\n\n{letter}"
            )
        print("Email sent successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")