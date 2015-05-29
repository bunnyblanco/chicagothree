from sqlalchemy import literal
from model import Base, Option, Tag

def create_schema(session):
    Base.metadata.bind=session.bind
    if len(Base.metadata.tables)>0:
        Base.metadata.drop_all()
    Base.metadata.create_all()
    session.commit()

def add_tag(tname, session):
    """
    Add a unique tag to the database.  Returns the associated tag_id
    """
    q = session.query(Tag.id).filter_by(name=tname)
    if session.query(literal(True)).filter(q.exists()).scalar():
        tag_id = q.value(Tag.id)
    else:
        tg = Tag(name=tname)
        session.add(tg)
        session.commit()
        tag_id = tg.id
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
