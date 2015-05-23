import requests
import lxml.html as lh
"""
Some utility functions
"""

def get_url_tags(form):
    """
    Get all the tags for the POST request
    """
    tags = {}
    values = {}
    inputs = form.xpath('//input')
    selects = form.xpath('//select')
#Now we parse the tags for the URL
#We can use the tree to figure out what goes with what
    for input in inputs:
        tags[input.name] = input.type
    for select in selects:
        values[select.name] = []
        options = select.getchildren()
        for opt in options:
            values[select.name].append(opt.values()[0])

    return tags, values

def get_url_from_tags(tags, values, url):
    """
    Using the data structures defined above, assemble URL for submission
    """
    url = url + "?op=locform"
    params = {}
#For this level of automation, we'd need more time
    for k, v in tags.items():
        if v == 'text':
            print "Please enter "+k
