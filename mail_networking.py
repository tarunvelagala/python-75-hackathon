#Sending mail using Networking
import smtplib
from email.mime.text import MIMEText
body = 'This is my text mail'
msg = MIMEText(body)
fromaddr = 'tarunvelagala80@gmail.com'
toaddr = 'tsectioncse@gmail.com'
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Hello"
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "mypassword")
server.send_message(msg)
print('Mail sent......')
server.quit()
