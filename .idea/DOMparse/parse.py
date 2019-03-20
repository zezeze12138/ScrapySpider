#coding=utf-8
from xml.dom.minidom import parse
from editScrapy import EditClass
#xmlStr = open('E:\scrapy.xml','r')
doc=parse('F:\ideaSP\ScrapySpider\.idea\DOMparse\scrapy.xml')
root=doc.documentElement

editClass = EditClass.EditClass()

#xml中获取spider
spider = root.getElementsByTagName("spider")[0]
name = spider.getElementsByTagName('name')[0]
start_urls = spider.getElementsByTagName('start_urls')[0]
allowed_domains = spider.getElementsByTagName('allowed_domains')[0]
start_url = []
allowed_domain = []
start_url.append(start_urls.childNodes[0].data)
allowed_domain.append(allowed_domains.childNodes[0].data)

#编写spider类初始化头部
print (editClass.addSpiderClass("spiderTest", name.childNodes[0].data, allowed_domain, start_url))
#编写parse解析方法
print (editClass.addDefAndparam("parse",["self","response"]))
#编写解析方法头部
print (editClass.addVar(3,"item = Demo1Item()"))

parse = spider.getElementsByTagName('parse')[0]
xpaths = parse.getElementsByTagName('xpath')
for xpath in xpaths:
    print (xpath.getAttribute("item"))
    print (xpath.childNodes[0].data)

#xml中获取item
items=root.getElementsByTagName("items")[0]
for item in items.getElementsByTagName("item"):
    print (item.childNodes[0].data)

