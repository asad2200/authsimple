import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from simpleAuth import *


def send_mail(receiver, subject, message):
    me = SENDER_EMAIL_ID
    my_password = SENDER_PASSWORD
    you = receiver

    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = me
    msg['To'] = you

    html = message
    part2 = MIMEText(html, 'html')

    msg.attach(part2)

    # Send the message via gmail's regular server, over SSL - passwords are being sent, afterall
    s = smtplib.SMTP_SSL(SERVER_NAME)
    # uncomment if interested in the actual smtp conversation
    # s.set_debuglevel(1)
    # do the smtp auth; sends ehlo if it hasn't been sent already
    s.login(me, my_password)

    s.sendmail(me, you, msg.as_string())
    s.quit()
