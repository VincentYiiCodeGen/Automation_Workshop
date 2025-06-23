# 1 pyton library
import smtplib
import ssl
from email.message import EmailMessage

#2function
def send_email(sender_email,receiver_email,subject,message,password):
  #create email
  msg = EmailMessage()
  msg['From'] = sender_email
  msg['To'] = receiver_email
  msg['Subject'] = subject
  msg.set_content(message)

# Secure connection with Gmail's SMTP server
  secure_context = ssl.create_default_context()
  with smtplib.SMTP_SSL('smtp.gmail.com',465,contect=secure_context) as server:
    server.login(sender_email,password)
    server.send_message(msg)
    print('send successfully')

#3 main pprogram
sender_email = 'example.codegen@gmail.com'
app_password = "ejod ywch yvkk zfud"
receiver_email = input ('please enter the receiver email:')
subject = input ('please enter your subject:')
message = input ('entermessage:')

send_email(sender_email, app_password, receiver_email, subject, message)