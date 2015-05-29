from chicagothree import data
import sqlalchemy
import lxml.html as lh

def get_form_tags(form):
    """
    Extract the tags in form based on the idea that the input fields'
    names represent the tags in a request URL.
    """
    attribs = []
    for input in form.inputs:
        if input.attrib.has_key('name'):
            attribs.append(input.attrib['name'])
    return attribs

def extract_tags(page):
    """
    Extract a set of tags from a form.  Return a dictionary of tags and
    associated options.
    """
    attribs = []
    if len(page.forms)>1:
        for form in page.forms:
            attribs.append(get_form_tags(form))
    else:
        attribs = get_form_tags(page.forms[0])
    return attribs

if __name__=='__main__':
    db = sqlalchemy.create_engine("sqlite:///tags.db")
    session = sqlalchemy.orm.Session(bind=db)
  #data.create_schema(session)
    f = open('./downloads/311_form2.html','r')
    page = lh.document_fromstring(f.read())
    attribs = extract_tags(page)
    for attrb in attribs:
        data.add_tag(attrb, session)
