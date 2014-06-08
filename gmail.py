import smtplib
import csv
from email.mime.text import MIMEText

username = ''
password = ''
fromaddr = ''

f = open('email.csv', 'r')
reader = csv.reader(f, delimiter=',')

def send_mail(email, name, company, optional, promo):
 body = """
Hello %s,

 %s \n""" % (name, company)

 if (promo != ""):
	body += """
Promo Code: %s
  """ % promo

 body += """
Thanks,

 """

 msg = MIMEText(body)
 msg['Subject'] = 'Test Email'
 msg['From'] = fromaddr
 msg['To'] = email

 print msg
 print ""

 #server = smtplib.SMTP("smtp.gmail.com:587")
 #server.starttls()
 #server.login(username, password)
 #server.sendmail(fromaddr, [email], msg.as_string())
 #server.close()

for i in reader:
	send_mail(i[0], i[1], i[2], i[3], i[4])
