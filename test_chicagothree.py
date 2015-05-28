import unittest as ut
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
import sqlalchemy.orm

class TestDatabaseAPI(ut.TestCase):
    db = sqlalchemy.create_engine('sqlite:///tags.db')
    session = sqlalchemy.orm.Session(bind=db)

    def test_schema(self):
        chicagothree.Base.metadata.bind=self.session.bind
        chicagothree.Base.metadata.drop_all()
        self.session.commit()
        self.assertEqual(len(self.db.table_names()),0)
        chicagothree.create_schema(self.session)
        self.assertEqual(len(self.db.table_names()),2)
        self.assertTrue(self.db.has_table('tbl_tag'))
        self.assertTrue(self.db.has_table('tbl_option'))

    def test_insert(self):
        q = self.session.query(chicagothree.Tag.id)
        self.assertEqual(len(q.all()),0)
        chicagothree.add_tag('invTest', self.session)
        self.assertEqual(len(q.all()),1)
        chicagothree.add_tag('invTest', self.session)
        self.assertEqual(len(q.all()),1)
        q2 = self.session.query(chicagothree.Option.id)
        self.assertEqual(len(q2.all()),0)
        chicagothree.add_tag_option('invTest2', 'TEST2', self.session)
        self.assertEqual(len(q.all()),2)
        self.assertEqual(len(q2.all()),1)
        chicagothree.add_tag_option('invTest', 'TEST', self.session)
        self.assertEqual(len(q.all()),2)
        self.assertEqual(len(q2.all()),2)

if __name__=='__main__':
    ut.main()
