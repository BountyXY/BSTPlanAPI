# -*- coding: utf-8 -*-
from urllib import request
import codecs
import re
url_requested = request.urlopen('https://bs-technik-schwerin.de/lankow/klassen/frames/navbar.htm')
#print(url_requested.code)
if 200 == url_requested.code:
    html_content = str(url_requested.read(), 'latin1')
    re_search_chunk = str(re.findall('var classes = (.*?);', html_content))
    classesRaw = re_search_chunk[3:-3].replace('"','').split(',')
