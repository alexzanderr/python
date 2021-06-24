
import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from core.json__ import *

automation_account_path = r"emails\AutomationAccount.json"

def SendEmail(sender_address, sender_password, reciever_address, subject, content, files_paths=[]):
  __path MIME short for multipurpose internet mail extensions
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = reciever_address
    message['Subject'] = subject
    message.attach(MIMEText(content, 'plain'))

    # setup the attachment
    if files_paths != []:
        for file_path in files_paths:
            file_read = open(file_path, 'rb')
            pay_load = MIMEBase('application', 'octet-stream')
            pay_load.set_payload(file_read.read())
            encoders.encode_base64(pay_load)

            items = file_path.split("\\")
            filename = items[len(items) - 1]

            pay_load.add_header('Content-Disposition', 'attachment', filename=filename)
            message.attach(pay_load)

    # connecting to server using 3rd party app (this);
    # to do this you need to have less secure apps
    # connections enabled  in google account
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_address, sender_password)
        content = message.as_string()
        server.sendmail(sender_address, reciever_address, content)
        server.quit()
        print(f"Email sent to '{reciever_address}' successfully.")
    except Exception as error:
        print(type(error))
        print(error)
        print("Email failed to send.")
        print("Activate less secure app in google account settings.")


def SendEmailTo(reciever_address, subject, content, files_paths=[]):
    automation_account = read_json_from_file(automation_account_path)

    sender_address = automation_account["email"]
    sender_password = automation_account["password"]

    if reciever_address == "me":
        reciever_address = sender_address

    # setup MIME short for multipurpose internet mail extensions
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = reciever_address
    message['Subject'] = subject
    message.attach(MIMEText(content, 'plain'))
    # setup the attachment

    if files_paths != []:
        for file_path in files_paths:
            file_read = open(file_path, 'rb')
            pay_load = MIMEBase('application', 'octet-stream')
            pay_load.set_payload(file_read.read())
            encoders.encode_base64(pay_load)

            items = file_path.split("\\")
            filename = items[len(items) - 1]

            pay_load.add_header('Content-Disposition', 'attachment', filename=filename)
            message.attach(pay_load)

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_address, sender_password)
        content = message.as_string()
        server.sendmail(sender_address, reciever_address, content)
        server.quit()
        print(f"Email sent to '{reciever_address}' successfully.")
    except Exception as error:
        print(type(error))
        print(error)
        print("Mail failed to send.")
        print("Activate less secure app in google account settings.")

# testing
if __name__ == '__main__':
    # SendEmailTo()
    pass
