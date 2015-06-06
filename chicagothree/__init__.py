import requests
import lxml.html as lh

def get_attrib_url(attrib):
    """
    Create a string suitable for a URL from the dict attrib
    """
    tag_string = '='.join([attrib['name'], attrib['value']])
    return tag_string

def get_form_action(form):
    """
    Try to extract information about the URL form will return by getting
    the action of the form.
    """
    url_action = form.action
    if '?' in url_action: #Looks good so far
        return url_action
    else:
        return ''

def get_form_url(form):
    sep = "&"
    tags = []
    for k, v in form.items():
        if k=='action':
            tags.append(v)
        elif k=='name' and len(tags)!=0:
            tags.append(v)
        elif k=='method':
            method = v
        else:
            continue
    for child in form.getchildren():
        if child.attrib.has_key('type') and child.attrib['type']=='hidden':
            tags.append(get_attrib_url(child.attrib))
    url = sep.join(tags)
    return url

