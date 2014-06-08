#!/usr/bin/python
import markdown, sys, csv, getpass, smtplib
from email.mime.text import MIMEText
from jinja2 import Template

if (len(sys.argv) >= 3):
    username = raw_input("Username: ")
    password = getpass.getpass("Password: ")
    subject = raw_input("Subject: ")
    emails_sent = 0

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

	if (sys.argv[3] == "verbose"):
	    print msg

        print "Email sent to: %s\n" % row['email']
	emails_sent += 1

    print "\nTotal Emails Sent:", emails_sent
else:
    print """
Usage: ./markdown-email.py <markdown file> <csv file>
    <markdown file> - path to markdown file ( email.md )
    <csv file> - path to csv data file ( data.csv )
    <verbose> - type verbose to see emails in raw format

    You must enter your email address, password, and subject for email.
    """
