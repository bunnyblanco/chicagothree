import unittest
import lxml.html as lh
import chicagothree.data as data

f = open('downloads/result.html','r')
page = lh.document_fromstring(f.read())
form = page.forms[0]
tags1 = data.get_tags(form)

g = open('downloads/result.html','r')
page2 = lh.document_fromstring(g.read())
form = page2.forms[0]
tags2 = data.get_tags(form)

data.add_dict(tags2)

