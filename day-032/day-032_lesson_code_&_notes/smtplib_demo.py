import smtplib

MY_EMAIL = "name@gmail.com"
MY_PASSWORD = "mypassword"

connection = smtplib.SMTP("smtp.gmail.com")  # Connect to SMTP server
connection.starttls()  # Encrypt the connection
connection.login(user=MY_EMAIL, password=MY_PASSWORD)
connection.sendmail(from_addr=MY_EMAIL,
                    to_addrs="receiver@gmail.com",
                    msg="Subject:Hello\n\nThis is the body of the email.")
connection.close()
