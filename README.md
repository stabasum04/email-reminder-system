# Automated Email Reminder System

A simple Python application that automates sending scheduled email reminders by reading data from a CSV file. This project uses Python's `smtplib`, `csv`, and `schedule` libraries to achieve this functionality, while email credentials are securely handled with `getpass`.

## Features

- Read reminders from a CSV file.
- Send emails via Gmail's SMTP server.
- Securely handle email credentials with `getpass`.
- Schedule email reminders to be sent at specific times.
  
## Requirements

- Python 3.6+
- `schedule` library

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/email-reminder-system.git
   cd email-reminder-system
