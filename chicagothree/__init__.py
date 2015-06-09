"""
Set of code for simplifying the process of working with forms and URL used
by the City of Chicago's online 311 service.  This file should define all code
specific to the City of Chicago's system.
"""
import lxml.html as lh

base_url = 'https://servicerequest.cityofchicago.org/web_intake_chic/'

def reset_request():
    """
    Reset the request by generating the appropriate URL.  A way to note
    the correct syntax...
    """
    action = "Controller?op=reset"
    url = base_url+action
    return url

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

def get_form_url(form): #A work in progress...
    sep = "&"
    url_tags = []
    url_tags = [form.action,form.attrib['name']]
    url = sep.join(url_tags)
    url = base_url+url
    return url

