#!/usr/bin/env python
# -*- coding:utf-8 -*-
import urllib2
import re
from bs4 import BeautifulSoup

headers={'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:31.0) Gecko/20100101 Firefox/31.0'}

url='http://www.qiushibaike.com/'
req=urllib2.Request(url,headers=headers)
res=urllib2.urlopen(req)
content=res.read().decode('utf-8')
print content

pattern=re.compile('<div class="author.*?<h2>(.*?)</h2>.*?<div.*?content">(.*?)</div>.*?<i class="number">(.*?)</i>.*?<i class="number">(.*?)</i>',re.S)
items=re.findall(pattern,content)
for i in items:
	print i[0],i[1],i[2],i[3]





	
