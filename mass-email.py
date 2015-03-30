#!/usr/bin/python

# Imports
import markdown, sys, csv, getpass, smtplib
from email.mime.text import MIMEText
from jinja2 import Template

def login():
    try:
        server = smtplib.SMTP("smtp.gmail.com:587")
        server.starttls()
        server.login(username, password)
        return server
    except smtplib.SMTPAuthenticationError:
        print "Incorrect Username or Password"
        server.close()
        sys.exit(1)

if (len(sys.argv) == 3):
    username = raw_input("Username: ") + "@gmail.com"
    password = getpass.getpass("Password: ")
    name = raw_input("Name: ")
    subject = raw_input("Subject: ")

    server = login()
    emails_sent = 0

    with open(sys.argv[1], 'r') as md_file:
        md_template = Template(md_file.read())

    with open(sys.argv[2], 'r') as csv_file:
        csv_data = csv.DictReader(csv_file)
        for row in csv_data:
            rendered_template = md_template.render(row)
            html = markdown.markdown(rendered_template)

            msg = MIMEText(html, 'html')
            msg['Subject'] = subject
            msg['From'] = name
            msg['To'] = row['email']

            server.sendmail(username, [row['email']], msg.as_string())
            print "Email sent to: %s" % row['email']
            emails_sent += 1
    server.close()
    print "\nTotal Emails Sent:", emails_sent
else:
    print """
Usage: ./markdown-email.py <markdown file> <csv file>
    <markdown file> - path to markdown file ( email.md )
    <csv file> - path to csv data file ( data.csv )
    <verbose> - type verbose to see emails in raw format

    You must enter your email address, password, and subject for email.
    """
