import unittest as ut
import lxml.html as lh
import chicagothree
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
        chicagothree.create_schema(self.session)
        q = self.session.query(chicagothree.Tag.id)
        self.assertEqual(len(q.all()),0)
        chicagothree.add_tag('invTest', self.session)
        self.assertEqual(len(q.all()),1)
        chicagothree.add_tag('invTest', self.session)
        self.assertEqual(len(q.all()),1)
        q2 = self.session.query(chicagothree.Option.id)
        self.assertEqual(len(q2.all()),0)
        chicagothree.add_tag_option(('invTest2', 'TEST2'), self.session)
        self.assertEqual(len(q.all()),2)
        self.assertEqual(len(q2.all()),1)
        chicagothree.add_tag_option(('invTest', 'TEST'), self.session)
        self.assertEqual(len(q.all()),2)
        self.assertEqual(len(q2.all()),2)

if __name__=='__main__':
    ut.main()
