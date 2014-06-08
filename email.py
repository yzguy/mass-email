#!venv/bin/python
import markdown

f = open("email.md", "r")
md = f.read()
f.close()

html = markdown.markdown(md)
print html
