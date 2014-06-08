#!venv/bin/python
import markdown, sys

if (len(sys.argv) > 0):
    mdfile = sys.argv[1]
    #csvfile = sys.argv[2]

    f = open(mdfile, "r")
    md = f.read()
    f.close()

    html = markdown.markdown(md)
    print html
else:
    print """
Usage: ./email.py <markdown file> <csv file>
    <markdown file> - path to markdown file ( ~/email.md )
    <csv file> - path to csv data file ( ~/data.csv )
    """
