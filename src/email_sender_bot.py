# Email Sender Bot
#-------------------------------------------------------------------------------------------------------
import smtplib
import csv
import logging
import time
import os
from email.message import EmailMessage
from dotenv import load_dotenv
# ------------------------------------------------------------------------------------------------------
# Load environment variables (.env)
# ------------------------------------------------------------------------------------------------------
load_dotenv()
sender_email_id = os.getenv("EMAIL_ID")
app_password = os.getenv("EMAIL_APP_PASSWORD")
#--------------------------------------------------------------------------------------------------------
# Email Configuration
#--------------------------------------------------------------------------------------------------------
csv_file="Recipients.csv"
attachment="Report.pdf"
max_retries=3
#---------------------------------------------------------------------------------------------------------
# Logging Setup
#---------------------------------------------------------------------------------------------------------
logging.basicConfig(
    filename="email+log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
    force=True
)
#----------------------------------------------------------------------------------------------------------
# Function -> Sends Email
#----------------------------------------------------------------------------------------------------------
def send_email(name,receiver_email_id,smtp):
    msg=EmailMessage()
    msg["From"]=sender_email_id
    msg["To"]=receiver_email_id
    msg["Subject"]="Email for Testing"

    msg.set_content(
        f"Hi {name},\n\nThis Email was sent automatically through Python Language.\n\nWarm Regards,\nSafa"
        )
    #Attach File
    if os.path.exists(attachment):
        with open(attachment, "rb") as f:
            msg.add_attachment(
                f.read(),
                maintype="application",
                subtype="octet-stream",
                filename=os.path.basename(attachment)
                )
    else:
        logging.warning(f"Attachment '{attachment}' not found. Sending email without attachment.")
#--------------------------------------------------------------------------------------------------------------
# Main Program
#--------------------------------------------------------------------------------------------------------------
def main():
    print("Starting Email Sender BOT.............")
    with smtplib.SMTP_SSL("smtp.gmail.com",465)as smtp:
        smtp.login(sender_email_id,app_password)
        with open(csv_file,newline="") as file:
            reader=csv.DictReader(file)
            for row in reader:
                name=row["name"]
                email=row["email"]
                attempts=0
                sent=False
                while attempts<max_retries and not sent:
                    try:
                        send_email(name,email,smtp)
                        logging.info(f"Sent to {name} ({email})- SUCCESS")
                        print(f"Sent to {name}")
                        sent=True
                    except Exception as e:
                        attempts += 1
                        logging.warning(f"Attempt {attempts} failed for {name} ({email}): {e}")
                        time.sleep(2)
                if not sent:
                    logging.error(f"Failed to sent to {name} ({email})")
print("\nAll emails processed. Check email+log.txt for details.")
#--------------------------------------------------------------------------------------------------------------
if __name__=="__main__":
    main()
        
