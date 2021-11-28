import os 
import smtplib
import imghdr

from email.message import EmailMessage

# getting email address and password from system variables
EMAIL_ADDRESS = os.environ.get('GMAIL_PYTHON_USER')
EMAIL_PASSWORD = os.environ.get('GMAIL_PYTHON_PASSWORD')

# contacts list
contacts = ['kacpermotyka4@gmail.com', 'kmotyka2000@gmail.com']

# creating message
msg = EmailMessage()
msg['Subject'] = 'Last weekend'
msg['From'] = EMAIL_ADDRESS

# creating coma separated string which is needed instead of list
msg['To'] = ', '.join(contacts)
msg.set_content('Last weekend I was making an awesome robot!\nImage attached below')

files = ['case.png', 'plate.png']

# open a file you want to attach
for file in files:
    with open(file, 'rb') as f:

        # reading from file
        file_data = f.read()
        # determining what type of photo we have (png, jpeg...)
        file_type = imghdr.what(f.name)
        # reading file name
        file_name = f.name

    msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)

# connecting to a gmail server on port 465
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:

    # login to gmail account using system variables
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    # sending message
    smtp.send_message(msg)


