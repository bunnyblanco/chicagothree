import lxml.html as lh
import sqlalchemy
from sqlalchemy.orm import Session
import model

db = sqlalchemy.engine.create_engine('sqlite:///tags.db')
from model import *
Base.metadata.bind=db
session = Session(db)

Base.metadata.drop_all(db)
Base.metadata.create_all(db)

def get_tags(form):
    tags = {}
    for input in form.inputs:
        if input.attrib.has_key('type') and input.attrib['type'] != 'button':
            tags[input.attrib['name']] = input.attrib['value']
    return tags

def add_dict(tags):
    """
    Add a dictionary of tags along with default values
    """
    for k, v in tags.items():
        tag = Tag(name=k, value=v)
        session.add(tag)

    session.flush()
    session.commit()
