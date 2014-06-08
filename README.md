Markdown-Email
==============

Have you ever wanted to send out essentially the same email out to a bunch of people, but changing a little information? Well, with Markdown-Email you can do that.  

All you need to do is provide a CSV file with the different information, and a Markdown template referencing the columns in the CSV file.

When you are done, you can just run the python script and enter your google email account information, and the subject of the email.

Prerequisites
-------------
* jinja2 (`pip install jinja2`)
* markdown (`pip install markdown`)

### CSV File Syntax
The first row of the CSV file will be the variable name for the different information between emails.

`name,email,company,promocode`

After this, each row will be the information per contact.

| name | email | company | promocode |
| ---- | ----- | ------- | --------- |
|Adam Smith | asmith@smith.com | Yzguy | 12345 | 
|Marky Mark|mmark@mark.com|Mark Co| |


You do not need to have every column for each contact, but if you don't you must handle that in your Markdown template with an `if statement`. This will be shown later (Notice Marky Mark does not have a promo code).

### Markdown File Syntax
The Markdown file uses existing Markdown Syntax (https://help.github.com/articles/markdown-basics), but now you will be able to use Jinja2 templating syntax to add in your per-contact information.

```
Yzguy Product Promo
===================

Hello {{ name }},

We would like to thank you and {{ company }} for continued loyalty.

{% if promocode %}
For being a long time customer, here is a promo code for a free product:  
    * Promo Code: {{ promocode }}  
{% endif}

Thank you,
   Adam
```  

Notice the `if statement` to handle there being a promo code or not, this is how you should handle fields that are not present for all contacts.

## Script Execution
Executing the script is pretty straight forward, you only need to pass in two arguments, these being a path to Markdown file, and the CSV file.

ex. `./markdown-email.py ~/loyaltytemplate.md ~/loyaltydata.csv`

After that, you will need to enter your Google Email credentials (they are not stored), and a Subject for the emails.

```
root@host: ~$ ./markdown-email.py example-template.md example-data.csv 
Username: admin@admin.com
Password: 
Subject: Yzguy Product Promo    
Email sent to: asmith@smith.com
Email sent to: mmark@mark.com

Total Emails Sent: 2
```
