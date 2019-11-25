# -*- coding: utf-8 -*-
from urllib import request



def getPage(url):
    url_requested = request.urlopen(url)
    #print(url_requested.code)
    if 200 == url_requested.code:
        html_content = str(url_requested.read(), 'latin1')
        return html_content
    pass


#print(getPage('https://bs-technik-schwerin.de/lankow/lehrer/45/t/t00001.htm'))
