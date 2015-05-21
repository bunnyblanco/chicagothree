import requests
import lxml.html as lh
"""
Some utility functions
"""

def get_url_tags(page):
    """
    Get all the tags for the POST request
    """
    tags = {}
    forms = page.forms
    for form in forms:
        inputs = form.xpath('//input')
        selects = form.xpath('//select')
        #Now we parse the tags for the URL
        for input in inputs:
            print input
        for select in selects:
            print select

