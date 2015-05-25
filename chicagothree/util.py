import requests
import lxml.html as lh
"""
Some utility functions
"""

def get_tag_value(form):
    """
    Get all the tags and indicated values for the POST request
    """
    tgs = {}
    vals = {}
    inputs = form.inputs
    selects = form.xpath('//select')
#Now we parse the tags for the URL
#We can use the tree to figure out what goes with what
    for input in inputs:
        tgs[input.name] = input.type
    for select in selects:
        vals[select.name] = []
        options = select.getchildren()
        if len(options)>0:
            for opt in options:
                opt_vals = opt.values()
                if len(opt_vals)>0:
                    vals[select.name].append(opt_vals[0])

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
    url = url+form.action
    tgs0, val = util.get_tag_value(form)

    return url
