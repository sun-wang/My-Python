#!/usr/bin/env python
# -*- coding:utf-8 -*-
import re

url='<a href="http://www.qiushibaike.com/users/25700600" target="_blank" title="一页双刀三禾土"><h2>一页双刀三禾土</h2></a></div><div class="content">lz有一同事长得魁梧，脾气特犟，我们给他起个外号“驴”    就这样喊了好多年，都忘记他名字了。<br>昨天在超市买东西，远远就看见他了，追上一看不是他。这人发现我在看他，就说:“看什么看”。我赶紧赔礼道:“不好意思，我还以为你是驴呢”。<br>这小子从四楼一直追道我一楼！！<!--1452085823--></div><div class="stats"><span class="stats-vote"><i class="number">1329</i> 好笑</span><span class="stats-comments">'
pattern=re.compile('<div.*?content">(.*?)</div')
for i in re.findall(pattern,url):
	print i
