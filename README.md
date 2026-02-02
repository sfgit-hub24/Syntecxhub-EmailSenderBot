# Syntecxhub-EmailSenderBot

## Internship Task - Week 3
An automated email sender built using Python.
This script sends personalized emails with attachments using Gmail SMTP.  
Built as part of my Python Internship Task.
---
## Features
- Send emails automatically
- Read recipients from CSV
- Personalized messages
- Attachments support
- Retry logic for failures
- Logging of send status
- Secure credentials using .env
---
## Tech Stack
Python, smtplib, email, logging, python-dotenv
---
## Technologies Used
- Python 3
- smtplib (SMTP Email Sending)
- csv (Recipient data handling)
- logging (Email activity logs)
- python-dotenv (.env for secure credentials)
- Gmail SMTP Server
- Git & GitHub
---
## Setup

### Install dependencies
pip install -r requirements.txt
### Create .env
EMAIL_ID=your_email@gmail.com

EMAIL_APP_PASSWORD=your_app_password
### Run
python email_sender_bot.py
---
## Sample Outputs
⚠️ Privacy Notice:
All personal email IDs and sensitive credentials have been intentionally blurred/hidden in the screenshots to maintain security and confidentiality.
### Recepients.csv (Data) 
![Recipients.csv Data](assets/RECIPIENTS.CSV-DATA.jpg)
### Source Code (Output) 
![Source Code Output](assets/PROGRAM-OUTPUT.jpg)
### Email+log.txt (Data) 
![Email+log.txt Data](assets/EMAIL+LOG-OUTPUT.jpg)
### Emails Sent (Output)
![Email Output 1](assets/EMAIL-OUTPUT-1.jpg)
![Email Output 2](assets/EMAIL-OUTPUT-2.jpg)

---
## Security Note
- .env not uploaded
- emails anonymized
- logs ignored via .gitignore
---
## Author
Safa Fatima 
2nd Year CSE STUDENT
