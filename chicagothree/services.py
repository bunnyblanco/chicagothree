import lxml.html as lh
import requests
from ConfigParser import ConfigParser

config = ConfigParser()
config.read('./instance/chicago.cfg')
base_url = config.get('URL','base_url')

def get_service_dict():
    """
    Get a dictionary of services offered through Chicago's online 311 form
    """
    services = {}
    options = []
    r = requests.get(base_url)
    if r.status_code==200:
        page = lh.document_fromstring(r.text)
        options = page.xpath('//option')
    else:
        print r.url

    if len(options)>0:
        services = {}
        for opt in options:
            items = opt.items()
            tag = items[0]
            services[tag[1]] = opt.text
    return services

def get_service_url(tag):
    """
     Get an appropriately formed URL to request the initial form needed
    to submit a service request for the service identified by the tag.
    """
    url = 'https://'
    params = {}
    params['op'] = 'locform'
    params['invserv'] = tag
#...
    r = requests.get(base_url, params=params)
    if r.status_code==200:
        url = r.url
    return url
