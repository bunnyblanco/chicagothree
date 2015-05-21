import requests
import lxml.html as lh
import chicagothree.util as util
from ConfigParser import ConfigParser

config = ConfigParser()
config.read('./instance/chicago.cfg')
r = requests.get(config.get('URL','base_url'), params={'op': 'locform', 'InvSRType': 'PCE'})
page = lh.document_fromstring(r.text)
#So we can use the tree to figure out what goes with what
forms = page.forms
for form in forms:
    inputs = form.xpath('//input')
    selects = form.xpath('//select')
    tags = {}
    values = {}
    for input in inputs:
        tags[input.name] = input.type
    for select in selects:
        values[select.name] = []
        options = select.getchildren()
        for opt in options:
            values[select.name].append(opt.values()[0])
