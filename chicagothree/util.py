import requests
import lxml.html as lh
"""
Some utility functions
"""

def get_tag_value(form):
    """
    Get all the tags and indicated options for the POST request
    """
    tgs = {}
    vals = {}
    inputs = form.inputs
    for input in inputs:
        if input.attrib.has_key('type') and input.attrib.has_key('name'):
            tgs[input.attrib['name']] = ''
        elif input.attrib.has_key('type') and input.attrib['type']=='button':
            print None
        elif not input.attrib.has_key('type'):
            options = input.getchildren()
            for opt in options:
                if input.attrib.has_key('name') and not vals.has_key(input.attrib['name']):
                    vals[input.attrib['name']] = []
                if opt.attrib.has_key('value'):
                    vals[input.attrib['name']].append(opt.attrib['value'])
                else:
                    print opt.attrib
        else:
            print "huh?"
    return tgs, vals

def get_tags(form):
    tgs = {}
    for input in form.inputs:
        if input.attrib.has_key('name') and input.attrib.has_key('type') and input.attrib['type'] != 'button':
            if input.attrib.has_key('value'):
                tgs[input.attrib['name']] = input.attrib['value']
            else:
                tgs[input.attrib['name']] = ''
    return tgs

def get_url_from_form(params, form, url):
    """
    Construct a URL from the params, tags, and indicated values given by
    the form.
    """
    url = ''.join(url,form.action)
    tgs0, val = util.get_tag_value(form)

    return url
