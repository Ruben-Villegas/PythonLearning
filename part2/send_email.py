import smtplib

def send_email(sender, password, recipient, subject, message):
    with smtplib.SMTP("smtp.example.com", 587) as server:
        server.starttls()
        server.login(sender, password)
        msg = f"Subject: {subject}\n\n{message}"
        server.sendmail(sender, recipient, msg)

# 示例调用
# send_email("your_email@example.com", "password", "recipient@example.com", "Test", "Hello!")
