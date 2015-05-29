import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey
import sqlalchemy.orm
from sqlalchemy.orm import relationship, backref
import sqlalchemy.ext.declarative as declarative

Base = declarative.declarative_base()

class Tag(Base):
    __tablename__='tbl_tag'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)
    options = relationship('Option', backref='Tag')

    def __str__(self):
        return '<Tag: %s %s>' % (self.name, self.default)

class Option(Base):
    __tablename__='tbl_option'
    id = Column(Integer, primary_key=True)
    tag_id = Column(Integer, ForeignKey('tbl_tag.id'))
    value = Column(String(20), nullable=False)

    def __str__(self):
        return '<Option:  %s>' % (self.value)

