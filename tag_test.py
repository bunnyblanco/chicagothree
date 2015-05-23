from chicagothree import util

tags = {}
tags['a'] = 'text'
tags['b'] = 'bla'
tags['c'] = 'bla'
tags['d'] = 'bla'
tags['e'] = 'text'
tags['f'] = 'huh'
tags['g'] = 'huh'
tags['h'] = 'huh'
tags['i'] = 'text'
tags['j'] = 'huh'

values = {}

util.get_url_from_tags(tags, values, '')

