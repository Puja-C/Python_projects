from email.message import EmailMessage

from email_app import password    # the password for the sender's email is stored in another python file called
# email_app for privacy
import ssl
import smtplib

sender = 'youremail@gmail.com'
password = password

receiver = 'betoye7764@oniecan.com'         # temporary email id generated through google

subject = "My first email through Python"

body = """
Hello, 
This is my first email sent through Python. Cool isn't it? 
Exciting times!
Regards.
"""

em = EmailMessage()
em['From'] = sender
em['To'] = receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context= context) as smtp:
    smtp.login(sender, password)
    smtp.sendmail(sender, receiver, em.as_string())
