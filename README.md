# Ransomware Defense Tool

Overview

The Ransomware Defense Tool is a Python-based defense system designed to monitor file changes in a specified directory, detect suspicious file activities (such as file modifications, deletions, or renaming), and create secure backups. In case of any unusual behavior—such as files being encrypted by ransomware—the tool can notify the user via email alerts. The tool also allows for regular backups of important files to a separate directory for disaster recovery purposes.

This project can be run on mobile devices using Termux and can integrate with Gmail for email notifications. It is a useful defense mechanism for users who want to monitor their files and protect against potential ransomware attacks.


---

Features

Directory Monitoring: Monitors the specified directory for any file changes, including modifications, deletions, or renaming.

Email Alerts: Sends real-time email alerts to notify the user when files are modified or tampered with.

Automatic Backups: Periodically creates backups of the monitored directory in a separate location.

Cloud Integration (Future): Plan to add cloud storage integration (Google Drive, Dropbox) for backup redundancy.

File Encryption & Quarantine (Future): In development to encrypt backup files for added security and isolate suspicious files.

Machine Learning-Based Ransomware Detection (Future): Planned to incorporate machine learning to detect ransomware behavior based on file modifications.



---

How It Works

1. Directory Monitoring: The tool watches a specific folder (e.g., the Downloads folder on mobile) and logs file changes.


2. File Backup: At regular intervals (e.g., every 10 minutes), the tool backs up all files in the directory to a designated backup folder.


3. Email Alerts: If any file is modified, deleted, or added, the tool sends an email alert to the user to notify them of the change.


4. Automation: All processes run automatically in the background and require minimal user intervention after setup.




---

Installation

This tool is designed to run on mobile devices through Termux, a terminal emulator for Android. Follow these steps to set it up:

Requirements

Android Device

Termux App

Git Installed

Python Installed

Gmail account for email alerts (with app password)


Step 1: Install Termux and Git

1. Download and install Termux from the Play Store.


2. Install Git by running the following command in Termux:

pkg install git



Step 2: Clone the Repository

After installing Termux and Git, clone the repository from GitHub:

git clone https://github.com/yourusername/your-repo.git

Step 3: Install Required Python Libraries

Navigate to your project directory and install the necessary libraries:

cd your-repo
pip install -r requirements.txt

Step 4: Set Up Email Alerts

For email alerts, ensure that 2-Step Verification (2SV) is enabled for your Gmail account and create an App Password. Use this password for sending emails from the tool.


---

Usage

1. Modify the Configuration: Update the source_directory and backup_directory variables in the code to reflect the paths you want to monitor and back up.

source_directory = "/storage/emulated/0/Download"
backup_directory = "/storage/emulated/0/Backup"


2. Run the Tool: Start the Ransomware Defense Tool by running the following command:

python3 ransomware_defense_tool.py


3. The tool will continuously monitor the specified directory, create backups, and send alerts via email.




---

Email Alerts Configuration

To receive email alerts, the tool uses the smtplib library in Python. You will need to update the email configuration section with your Gmail credentials and app password:

EMAIL_ADDRESS = "your-email@gmail.com"
EMAIL_PASSWORD = "your-app-password"

Make sure you have created an app password via Google to bypass 2-step verification.


---

Advanced Features (Planned)

Cloud Backup: The next version will support integration with Google Drive and Dropbox for remote backups.

File Quarantine: Implementing an automated quarantine system that moves suspicious files to a safe location for analysis.

Machine Learning Detection: Adding machine learning algorithms to detect ransomware behaviors like mass file renaming and encryption.



---

Contribution

Contributions are welcome! If you'd like to add new features, fix bugs, or improve the code, feel free to fork the repository and submit a pull request.
