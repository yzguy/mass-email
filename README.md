Markdown-Email
==============

#### Prerequisites
* jinja2
* markdown

To quickly create HTML emails, pass in data from external source (ex. csv file), and send out emails in bulk.

Usage: ./markdown-email.py <markdown file> <csv file>  
    <markdown file> - path to markdown file
    <csv file> - path to csv data file

The markdown file uses standard markdown syntax, but with Jinja2 templating. This allows you to input data from the csv file based on the column title.

The CSV file must have a first row, with the column names. Not all columns need to be filled out for each row, however, you will need to put an if statement in the template to handle that.

`{% if promocode %}  
    * Promo Code: {{ promocode }}  
{% endif}`
