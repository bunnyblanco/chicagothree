import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey
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
    tagId = Column(Integer, ForeignKey(Tag.id))
    value = Column(String(20), nullable=False)

    def __repr__(self):
        return '<Tag Values: %s %s>' % (self.tagId, self.value)

