import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey
import sqlalchemy.orm 
from sqlalchemy.orm import relationship, backref, Session
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

def create_schema(session):
    Base.metadata.bind=session.bind
    Base.metadata.drop_all()
    Base.metadata.create_all()

def add_tag(tname, session):
    q = session.query(Tag.id).filter_by(name=tname)
    if len(q.all())==1:
        tag_id = q.value(Tag.id)
    else:
        tg = Tag(name=tname)
        session.add(tg)
        tag_id = tg.id
    session.commit()
    return tag_id

def add_tag_option(tag, option, session):
    q = session.query(Tag.id).filter_by(name=tag)
    if len(q.all())==1:
        tag_id = q.value(Tag.id)
    else:
        tg = Tag(name=tag)
        session.add(tg)
        session.commit()
        tag_id = tg.id
    q2 = session.query(Option.id, Option.tag_id).filter_by(tag_id=tag_id, value=option)
    if len(q2.all())==0:
        opt = Option(tag_id=tag_id, value=option)
        session.add(opt)
    session.commit()
    return tag_id

