import chicagothree.services as services

tags = services.get_service_dict()
if len(tags)>0:
    for k, v in tags.items():
        print k, v

if len(tags)>0:
    tag = tags.items()[0][0]
    url = services.get_loc_service_url('PCE')
    print url

print services.get_search_url('PCE')
