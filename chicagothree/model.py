import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref
import sqlalchemy.ext.declarative as declarative

Base = declarative.declarative_base()

class Tag(Base):
    __tablename__='tbl_tag'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    value = Column(String(50))
    
    def __repr__(self):
        return '<Tag: %s %s>' % (self.name, self.value)

class Value(Base):
    __tablename__='tbl_value'
    id = Column(Integer, primary_key=True)
    tag_id = Column(Integer, ForeignKey(Tag.id))
    value = Column(String(20), nullable=False)
    tag = relationship("Tag", backref=backref('Value', order_by=id))

    def __init__(self, name, value):
        self.tag.name = name
        self.value = value

    def __repr__(self):
        return '<Tag Values: %s %s>' % (self.tagId, self.value)

