#!/usr/bin/env python
# -*- coding:utf-8 -*-
import urllib2
import re
from bs4 import BeautifulSoup

headers={'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:31.0) Gecko/20100101 Firefox/31.0'}

url='http://tieba.baidu.com/p/3138733512?see_lz=1&pn=1'
req=urllib2.Request(url,headers=headers)
res=urllib2.urlopen(req)
content=res.read().decode('utf-8')

a='<span.*?class="lzl_content_main">(.*?)</span>'

pattern=re.compile(a,re.S)
match=re.findall(pattern,content)
for i in match:
	print i



