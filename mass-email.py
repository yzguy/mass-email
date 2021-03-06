#!/usr/bin/python

# Imports
import markdown, sys, csv, getpass, smtplib, argparse
from email.mime.text import MIMEText
from jinja2 import Template

# Argument Parsing
parser = argparse.ArgumentParser()
parser.add_argument('-m', '--markdown', help='Path to Markdown Template', required=True)
parser.add_argument('-c', '--csv', help='Path to CSV file', required=True)
parser.add_argument('-v', '--verbose', help='Write out emails')
args = parser.parse_args() 

# Variables
markdownf = args.markdown
csvf = args.csv
verbose = False

# User input
username = raw_input("Username: ")
password = getpass.getpass("Password: ")
name = raw_input("Name: ")
subject = raw_input("Subject: ")
emails_sent = 0

# Login to SMTP Server
def login(username, password):
    try:
        server = smtplib.SMTP("smtp.gmail.com:587")
        server.starttls()
        server.login(username, password)
        return server
    except smtplib.SMTPAuthenticationError:
        print "Incorrect Username or Password"
        server.close()
        sys.exit(1)

server = login(username, password)

# Read Markdown file into template
with open(markdownf, 'r') as md_file:
    md_template = Template(md_file.read())

# Read CSV file, render template
with open(csvf, 'r') as csv_file:
    csv_data = csv.DictReader(csv_file)
    for row in csv_data:
        rendered_template = md_template.render(row)
        html = markdown.markdown(rendered_template)

        # Format Email
        msg = MIMEText(html, 'html')
        msg['Subject'] = subject
        msg['From'] = name
        msg['To'] = row['email']

        # Print out emails to screen
        if verbose == True:
            print msg.as_string()

        # Send email
        server.sendmail(username, [row['email']], msg.as_string())
        print "Email sent to: %s" % row['email']
        emails_sent += 1
server.close()
print "\nTotal Emails Sent:", emails_sent

