#!/usr/bin/env python
# -*- coding:utf-8 -*-
import urllib
import urllib2
import re

class BDTB:
	def __init__(self,baseurl,seelz):
		self.baseurl=baseurl
		self.seelz='?see_lz='+str(seelz)
	def getpage(self,page):
		url=self.baseurl+self.seelz+'&pn='+str(page)
		req=urllib2.Request(url)
		res=urllib2.urlopen(req)
       	        content=res.read().decode('utf-8')
		
                a='<div id="post_content_.*?>(.*?)</div>'
		pattern=re.compile(a)
		
		match=re.findall(pattern,content)
		
		for i in match:
			b='<img.*?>'
			d='<a href.*?>'
			e='</a>'
			c='<br>'
			i=re.sub(b,'',i)
			i=re.sub(d,'',i)
			i=re.sub(e,'',i)
			i=re.sub(c,'\n',i)
			print i.strip()
			print '------------------------------------------------'
		
		

baseurl='http://tieba.baidu.com/p/3138733512'
bdtb=BDTB(baseurl,1)
bdtb.getpage(1)

