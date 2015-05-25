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

def add_tags(tags):
    """
    Add a dictionary of tags along with default values
    """
    for k, v in tags.items():
        tag = Tag(name=k, value=v)
        session.add(tag)

    session.commit()

def add_values(tag, vals):
    for v in vals:
        val = Value(name=tag, value=v)
        session.add(val)
    session.commit()
