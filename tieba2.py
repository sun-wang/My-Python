#!/usr/bin/env python
# -*- coding:utf-8 -*-
import urllib
import urllib2
import re

class TOOL:
	reimg=re.compile('<img.*?>')
	rebr=re.compile('<br>')
	rea=re.compile('<a href.*?>')
	rea1=re.compile('</a>')
	def replace(self,i):
		i=re.sub(self.reimg,'',i)
		i=re.sub(self.rea,'',i)
		i=re.sub(self.rea1,'',i)
		i=re.sub(self.rebr,'\n',i)
		return i.strip()
		
class BDTB:
	def __init__(self,baseurl,seelz):
		self.baseurl=baseurl
		self.seelz='?see_lz='+str(seelz)
		self.tool=TOOL()
	def getcontent(self,pagenum):
		a='<div id="post_content_.*?>(.*?)</div>'
                pattern=re.compile(a)
		with open('baidu.txt','w+') as f:

			for j in range(1,int(pagenum)+1):
				print 'doing'+str(j)
				content=self.getpage(j)
				match=re.findall(pattern,content)
				for i in match:
					line=self.tool.replace(i).encode('utf-8')+'-----------------------------------------------------'
					f.write(line)
						
	def getpagenum(self):
		contents=self.getpage(1)
		a='<li class="l_reply_num".*?</span>.*?<span.*?>(.*?)</span>'
		pattern=re.compile(a)
		result=re.search(pattern,contents)
		if result:
			return result.group(1).strip()
		else:
			return None
			
	def getpage(self,page):
		try:
			url=self.baseurl+self.seelz+'&pn='+str(page)
			req=urllib2.Request(url)
			res=urllib2.urlopen(req)
       	        	content=res.read().decode('utf-8')
			return content
		except urllib2.URLError,e:
			if hasattr(e,"reason"):
				print 'connect failed'
				return None
               
baseurl='http://tieba.baidu.com/p/3138733512'
bdtb=BDTB(baseurl,1)
a=bdtb.getpagenum()
content=bdtb.getcontent(a)


