import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import schedule
import time
from datetime import datetime


reminders = [
    {"email": "xyz@gmail.com", "subject": "Meeting Reminder", "message": "Don't forget the meeting at 4 PM.", "time": "16:20"},
    {"email": "recipient2@example.com", "subject": "Project Due", "message": "The project is due tomorrow.", "time": "12:00"}
]


def send_email(subject, body, to_email):
    # Your email credentials
    from_email = 'sabiyatabasum04@gmail.com'
    password = '*********'  

    # Create email message
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # Connect to email server and send email
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, password)
        text = msg.as_string()
        server.sendmail(from_email, to_email, text)
        server.quit()
        print(f"Email sent to {to_email}")
    except Exception as e:
        print(f"Failed to send email: {e}")

def send_reminders():
    current_time = datetime.now().strftime('%H:%M')  # Get current time in HH:MM format
    for reminder in reminders:
        if reminder['time'] == current_time:
            send_email(reminder['subject'], reminder['message'], reminder['email'])

# Schedule the task to run every minute to check for reminders
schedule.every(1).minutes.do(send_reminders)

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)


