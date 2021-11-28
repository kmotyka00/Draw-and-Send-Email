import os
import smtplib

# to test messages with this code you need to open smtp server in terminal
# writing python -m smtpd -c DebuggingServer -n localhost:1025

# my email address
EMAIL_ADDRESS = os.environ.get('GMAIL_PYTHON_USER')

with smtplib.SMTP('localhost', 1025) as smtp:

    # simple message title and body
    subject = 'Last weekend'
    body = 'Last weekend I was doing...'

    # simple message construction Subject: {subject}\n\n{body}
    msg = f'Subject: {subject}\n\n{body}'

    smtp.sendmail(EMAIL_ADDRESS, 'kacpermotyka4@gmail.com', msg)
