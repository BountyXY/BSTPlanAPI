# -*- coding: utf-8 -*-
from urllib import request
import codecs
import re
url_requested = request.urlopen('https://bs-technik-schwerin.de/lankow/lehrer/frames/navbar.htm')
#print(url_requested.code)
if 200 == url_requested.code:
    html_content = str(url_requested.read(), 'latin1')
    re_search_chunk = str(re.findall('var rooms = (.*?);', html_content))
    roomsRaw = re_search_chunk[3:-3].replace('"','').split(',')
