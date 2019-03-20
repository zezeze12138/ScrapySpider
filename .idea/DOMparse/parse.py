#coding=utf-8
from xml.dom.minidom import parse
from editScrapy import EditClass
#xmlStr = open('E:\scrapy.xml','r')
doc=parse('E:\scrapy.xml')
root=doc.documentElement

editClass = EditClass.EditClass()

#spider获取
spider = root.getElementsByTagName("spider")[0]
name = spider.getElementsByTagName('name')[0]
start_urls = spider.getElementsByTagName('start_urls')[0]
allowed_domains = spider.getElementsByTagName('allowed_domains')[0]
start_url = []
allowed_domain = []
#for url in start_urls:
start_url.append(start_urls.childNodes[0].data)
#for allowed in allowed_domains:
allowed_domain.append(allowed_domains.childNodes[0].data)
print (editClass.addSpiderClass("spiderTest", name.childNodes[0].data, allowed_domain, start_url))
print(name.childNodes[0].data)
print(allowed_domains.childNodes[0].data)
print(start_urls.childNodes[0].data)
parse = spider.getElementsByTagName('parse')[0]
xpaths = parse.getElementsByTagName('xpath')
for xpath in xpaths:
    print (xpath.getAttribute("item"))
    print (xpath.childNodes[0].data)

#item获取
items=root.getElementsByTagName("items")[0]
for item in items.getElementsByTagName("item"):
    print (item.childNodes[0].data)

