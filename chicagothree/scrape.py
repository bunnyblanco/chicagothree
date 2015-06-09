"""
The code that handles the actual extraction of spies from behind Nazi occupied
France.  Sorry, code that handles the extraction of the "tags" that form
the City of Chicago's API.
"""
import lxml.html as lh

def get_page(file):
    """
    Generate a document object from the open file/object with a read()
    method that generates a string representation of an HTML file.
    """
    page = lh.document_fromstring(file.read())
    return page

def get_form(page, n):
    """
    Get form number n from the list of forms in the given page, where n >= 0.  
    Returns a dummy form, if no form exists or index n does not exist.
    Return the sole form on the page, if the index n == 0.
    """
    form = None
    page = get_page(file)
    if len(page.forms)>0:
        if len(page.forms)==1 and n==0:
            form = page.forms[0]
        else:
             form = page.forms[n]
    return form

def get_select_options(form):
    """
    Return a dict or tags and descriptions based on the SELECT field in the
    given form.
    """
    tags = {}
    selects = []
    for input in form.inputs:
        if not input.attrib.has_key('type'):
            selects.append(input)
    for select in selects:
        tags[select.attrib['name']] = []
        for child in select.getchildren():
            tags[select.attrib['name']].append(child.attrib['value'])

    return tags
