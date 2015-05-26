import lxml.html as lh
import sqlalchemy
from chicagothree import session
from chicagothree.model import *

db = sqlalchemy.engine.create_engine('sqlite:///tags.db')
Base.metadata.bind=db
session.connection(bind=db)

def create_schema():
    Base.metadata.drop_all()
    Base.metadata.create_all()

def add_tag(name, val=''):
    tag = Tag(name=name, value=val)
    session.add(tag)
    session.commit()

def add_tag_value(tname, tval):
    """
    Add a single required value tval for tag tname
    """
    if session.query(Tag.name).filter_by(name=tname).count()==0:
        add_tag(tname)
    val = Value(tname, tval)
    session.add(val)
    session.commit()

def add_tags(tags):
    """
    Add a dictionary of tags along with default values
    """
    for k, v in tags.items():
        tag = Tag(name=k, value=v)
        session.add(tag)

    session.commit()

