import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey, literal
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
    if session.query(literal(True)).filter(q.exists()).scalar():
        tag_id = q.value(Tag.id)
    else:
        tg = Tag(name=tname)
        session.add(tg)
        tag_id = tg.id
    session.commit()
    return tag_id

def add_tagid_option(tagopt, session):
    """
    Add an option to the Tag identified by the tag_id
    """
    q = session.query(Option).filter_by(tag_id=tagopt[0], value=tagopt[1])
    if session.query(literal(True)).filter(q.exists()).scalar():
        return tagopt[0]
    else:
        opt = Option(tag_id=tagopt[0], value=tagopt[1])
        session.add(opt)
        session.commit()
        return tagopt[0]

def add_tag_option(tagopt, session):
    """
    Add a single (tag, option) pair
    """
    tag_id = add_tag(tagopt[0], session)
    add_tagid_option((tag_id, tagopt[1]), session)
    return tag_id

def add_tag_options(tagopts, session):
    """
    Add an array of options associated with a single tag
    """
    tag_id = add_tag(tname=tagopts[0], session=session)
    for tag_opt in tagopts[1]:
        add_tagid_option((tag_id, tag_opt), session)
    return tag_id
