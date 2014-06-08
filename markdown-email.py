#!/usr/bin/python
import markdown, sys, csv, getpass, smtplib
from email.mime.text import MIMEText
from jinja2 import Template

if (len(sys.argv) > 0):
    username = raw_input("Username: ")
    password = getpass.getpass("Password: ")
    subject = raw_input("Subject: ")

    markd_file = open(sys.argv[1], "r")
    md = markd_file.read()
    markd_file.close()

    csv_file = csv.DictReader(open(sys.argv[2], 'r'))

    for row in csv_file:
        template = Template(md)
        rendered_template = template.render(row)
        html = markdown.markdown(rendered_template)

        msg = MIMEText(html, 'html')
        msg['Subject'] = subject
        msg['From'] = username
        msg['To'] = row['email']

        server = smtplib.SMTP("smtp.gmail.com:587")
        server.starttls()
        server.login(username, password)
        server.sendmail(username, [row['email']], msg.as_string())
        server.close()

        print "Email sent to: %s" % row['email']
else:
    print """
Usage: ./markdown-email.py <markdown file> <csv file>
    <markdown file> - path to markdown file ( email.md )
    <csv file> - path to csv data file ( data.csv )

    You must enter your email address and password.
    """
