import unittest
import lxml.html as lh
import chicagothree
import chicagothree.util as util

f = open('downloads/result.html','r')
page = lh.document_fromstring(f.read())
form = page.forms[0]
tags1 = util.get_tags(form)
tgs1, val1 = util.get_tag_value(form)

g = open('downloads/result.html','r')
page2 = lh.document_fromstring(g.read())
form = page2.forms[0]
tags2 = util.get_tags(form)
tgs2, val2 = util.get_tag_value(form)

import sqlalchemy

db = sqlalchemy.create_engine('sqlite:///tags.db')

chicagothree.Base.metadata.bind=db
chicagothree.session.connection(bind=db)

chicagothree.create_schema()
#chicagothree.add_tags(tags2)
chicagothree.add_tag('invTest')
chicagothree.add_tag_option('invTest', 'TEST') #Stills generates an exception

