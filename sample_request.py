import chicagothree.services as services

tags = services.get_service_dict()
if len(tags)>0:
    for k, v in tags.items():
        print k, v


