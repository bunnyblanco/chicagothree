import lxml.html as lh
from chicagothree import scrape

f = open('downloads/311_loc_search.html','r')
page = lh.document_fromstring(f.read())
form = page.forms[0]
opts = scrape.get_select_options(form)

if __name__=='__main__':
    for opt in opts:
        print opt
        for op in opt:
            print op
