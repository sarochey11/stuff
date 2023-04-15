import os
import smtplib
from datetime import datetime, timedelta
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# EmailSender class is used to send emails with attachments
class EmailSender:
    # Initialize the object with the recipient's email address, the subject and body of the email, and the file path of the attachment
    def __init__(self, to, subject, body, filePath):
        self.to = to
        self.subject = subject
        self.body = body
        self.filePath = filePath
    
    # send email method
    def send_email(self):
        msg = MIMEMultipart()
        msg['From'] = 'from@bandicoot.co.uk'
        msg['To'] = self.to
        msg['Subject'] = self.subject
        msg.attach(MIMEText(self.body, 'plain'))

        # create server
        s = smtplib.SMTP('localhost')
        # start TLS for security
        s.starttls()
        # send message via server.
        s.sendmail(msg['From'], msg['To'], msg.as_string())
        # Terminating the session
        s.quit()

# main function
def main():
    # Function to check if a file was modified within the past 24 hours
    def modifiedWithin24Hr(filePath):

        # Check if the file exists
        if not os.path.exists(filePath):
            # if the file does not exist, return False
            return False

        # Get the current time
        now = datetime.now()
        # Get the last modified time of the file
        lastModifiedTime = datetime.fromtimestamp(os.stat(filePath).st_mtime)
        # Check if the difference between the current time and the last modified time is less than 24 hours

        return now - lastModifiedTime < timedelta(hours=24)

    # List of folder paths
    folders = ["N:\\i1", "N:\\v2", "N:\\v3"]

    # Iterate through the folders
    for folder in folders:
        # Get a list of all the files in the folder
        files = os.listdir(folder)
        # Filter the list of files to only include files that were modified within the past 24 hours
        recentFiles = [os.path.join(folder, f) for f in files if modifiedWithin24Hr(os.path.join(folder, f))]

        # If there are no recent files, output a message
        if not recentFiles:
            emailSender = EmailSender('sender@bandicoot.co.uk', 'Backup Failure', 'Backup Failure - No recent files in ' + folder, '') # Create an EmailSender object with the recipient's email address, the subject and body of the email, and the file path of the attachment
            emailSender.send_email() # Send the email
            continue

main()