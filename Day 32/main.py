# # Import necessary modules
# import smtplib
# import os
# from dotenv import load_dotenv

# # Load environment variables from the .env file
# load_dotenv()

# # Retrieve variables from environment
# my_email = os.getenv("MY_EMAIL")
# password = os.getenv("MY_PASSWORD")
# to_email = os.getenv("TO_EMAIL")

# # Email details
# subject = "Hello"
# body = "This is the body of the email."

# # Combine subject and body into the message
# message = f"Subject: {subject}\n\n{body}"

# try:
#     # Connect to the Gmail SMTP server on port 587
#     with smtplib.SMTP("smtp.gmail.com", 587) as connection:
#         connection.starttls()  # Secure the connection using TLS
#         connection.login(user=my_email, password=password)  # Log in to your email account
#         connection.sendmail(
#             from_addr=my_email,
#             to_addrs=to_email,
#             msg=message
#         )
#     print("Email sent successfully!")
# except Exception as e:
#     print(f"An error occurred: {e}")



import datetime as dt

# Create a new DaytimeClient object
now = dt.datetime.now()
# print(now)
# print(type(now))

# Get the current year
year = now.year
# print(year)
# print(type(year))

# Get the current month
month = now.month
print(month)

# Get the current day
day_of_week = now.weekday()
print(day_of_week)

# for israel time, the first day of the week is sunday
# for python, the first day of the week is monday
# so we need to convert the python day
print(day_of_week + 2)

if year == 2020:
    print("Wear a mask")
    
if year == 2024:
    print("Its a war in israel")
    
    
# ------- Create Special BirthDay ----------
birthday = dt.datetime(year=1999, month=10, day=26)
print(birthday)