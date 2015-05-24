import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey
import sqlalchemy.ext.declarative as declarative

Base = declarative.declarative_base()

class Tags(Base):
    __tablename__='tbl_tag'
    id = Column('id', Integer, primary_key=True)
    tag = Column('str_tag', String(50), nullable=False)
    default = Column('str_default', String(50))
    
    def __init__(self, tag, default_value=''):
        self.tag = tag
        self.default = default_value

    def __str__(self):
        return '<Tag: %s %s>' % (self.tag, self.default)

class Values(Base):
    __tablename__='tbl_value'
    id = Column('id', Integer, primary_key=True)
    tag_id = Column('id_tag', Integer, ForeignKey('tbl_tag.id'))
    value = Column('str_val', String(20), nullable=False)

    def __init__(self, tag_id, value):
        self.tag_id = tag_id
        self.value = value

    def __str__(self):
        return '<Tag Values: %r %r>' % (self.tag_id, self.value)

