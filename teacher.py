# -*- coding: utf-8 -*-
from urllib import request
import codecs
import re
url_requested = request.urlopen('https://bs-technik-schwerin.de/lankow/lehrer/frames/navbar.htm')
#print(url_requested.code)
if 200 == url_requested.code:
    html_content = str(url_requested.read(), 'latin1')
    re_search_chunk = str(re.findall('var teachers = (.*?);', html_content))
    teacherRaw = re_search_chunk[3:-3].replace('"','').split(',')
    #for teacher in range(len(teacherRaw)):
    #    print(str(teacher+1) + ' - ' + teacherRaw[teacher])
    #    pass
