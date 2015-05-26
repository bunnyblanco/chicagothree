import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey
import sqlalchemy.orm 
from sqlalchemy.orm import relationship, backref
import sqlalchemy.ext.declarative as declarative
from sqlalchemy.orm import Session

session = Session()
Base = declarative.declarative_base()

class Tag(Base):
    __tablename__='tbl_tag'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)
    default = Column(String(50))
    
    def __repr__(self):
        return '<Tag: %s %s>' % (self.name, self.default)

class Option(Base):
    __tablename__='tbl_option'
    id = Column(Integer, primary_key=True)
    tag_id = Column(Integer, ForeignKey(Tag.id))
    value = Column(String(20), nullable=False)
    tag = relationship(Tag, backref=backref('tbl_option', order_by=id))

    def __repr__(self):
        return '<Tag Options:  %s %s>' % (self.tag, self.value)

def create_schema():
    Base.metadata.drop_all()
    Base.metadata.create_all()

def add_tag(tname, opt=''):
    tg = Tag(name=tname, default=opt)
    if session.query(Tag.name).filter_by(name=tname).count()==0:
        tg = Tag(name=tname, default=opt)
        session.add(tg)
        session.commit()
    return tg

def add_tag_option(tname, opt):
    """
    Add a single option value opt for tag tname
    """
    if session.query(Tag.name).filter_by(name=tname).count()==0:
        tg = add_tag(tname)
    else:
        tg = Tag(name=tname, default='')
    val = Option(tag=tg, value=opt)
    session.add(val)
    session.commit()

