import os
import time
import shutil
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Function to create a backup of the monitored directory
def backup_files(source_dir, backup_dir):
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)

    timestamp = time.strftime("%Y%m%d-%H%M%S")
    backup_subdir = os.path.join(backup_dir, f"backup-{timestamp}")
    
    shutil.copytree(source_dir, backup_subdir)
    print(f"[INFO] Backup created at: {backup_subdir}")

# Function to send email notifications
def send_email_alert(subject, body, recipient_email):
    sender_email = "your_email@gmail.com"
    sender_password = "your_password"
    
    try:
        # Email setup
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # Connect to Gmail's SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        text = msg.as_string()
        server.sendmail(sender_email, recipient_email, text)
        server.quit()
        print("[INFO] Alert sent successfully via email!")
    except Exception as e:
        print(f"[ERROR] Failed to send email alert: {str(e)}")

# Function to monitor a directory for file changes with filters
def monitor_directory(directory):
    print(f"[INFO] Monitoring directory: {directory}")
    
    file_snapshot = {f: os.path.getmtime(os.path.join(directory, f)) for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))}

    allowed_extensions = ['.pdf', '.docx', '.zip']  # File types to monitor
    size_threshold = 1024 * 100  # Minimum size difference of 100KB to trigger an alert

    while True:
        time.sleep(5)  # Check every 5 seconds

        for f in os.listdir(directory):
            full_path = os.path.join(directory, f)

            if os.path.isfile(full_path):
                file_extension = os.path.splitext(f)[1]

                # Filter files by extension
                if file_extension not in allowed_extensions:
                    continue

                current_mtime = os.path.getmtime(full_path)
                current_size = os.path.getsize(full_path)

                if f not in file_snapshot:
                    print(f"[ALERT] New file detected: {f}")
                    send_email_alert("New File Detected", f"A new file '{f}' has been created.", "your_email@gmail.com")
                    file_snapshot[f] = current_mtime
                elif file_snapshot[f] != current_mtime and abs(current_size - file_snapshot[f]) > size_threshold:
                    print(f"[ALERT] File modified or renamed: {f}")
                    send_email_alert("File Modified", f"The file '{f}' has been modified or renamed.", "your_email@gmail.com")
                    file_snapshot[f] = current_mtime

        # Check for deleted files
        deleted_files = [f for f in file_snapshot if not os.path.exists(os.path.join(directory, f))]
        for f in deleted_files:
            print(f"[ALERT] File deleted: {f}")
            send_email_alert("File Deleted", f"The file '{f}' has been deleted.", "your_email@gmail.com")
            del file_snapshot[f]

# Main function
def ransomware_defense_tool(source_dir, backup_dir):
    backup_interval = 10 * 60  # 10 minutes in seconds
    last_backup_time = time.time()

    while True:
        monitor_directory(source_dir)
        if time.time() - last_backup_time >= backup_interval:
            backup_files(source_dir, backup_dir)
            last_backup_time = time.time()

if __name__ == "__main__":
    source_directory = "/storage/emulated/0/Download"  # Directory to monitor
    backup_directory = "/storage/emulated/0/Backup"  # Backup directory

    print("[INFO] Starting Ransomware Defense Tool...")
    ransomware_defense_tool(source_directory, backup_directory)
