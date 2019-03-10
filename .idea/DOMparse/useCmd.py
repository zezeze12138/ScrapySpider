#cmd="curl http://localhost:6800/schedule.json -d project="+project+" -d spider="+spider+" -d category="+str(NewsTopicId)

import os
# p=os.chdir("F:\\")
# print(p)
# s = os.chdir("F:\\autoScrapy\\demo1\\demo1")
# print(os.system("dir"))
newContext = '''
# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Demo1Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
'''

i1 = 'test1 = scrapy.Field()'
i2 = 'test2 = scrapy.Field()'
i3 = 'test3 = scrapy.Field()'
i4 = 'test4 = scrapy.Field()'
i5 = 'test5 = scrapy.Field()'

newContext = newContext+'\t'+i1
newContext = newContext+'\n'+'\t'+i2
newContext = newContext+'\n'+'\t'+i3
newContext = newContext+'\n'+'\t'+i4
newContext = newContext+'\n'+'\t'+i5

#print(newContext)

w = open('F:\\autoScrapy\\demo1\\demo1\\items.py','w')
w.write(newContext)
w.close()


f = open('F:\\autoScrapy\\demo1\\demo1\\items.py','r')
itemsFile = f.read()
f.close()
print("****************")
print(itemsFile)
print("****************")
# p=os.system("scrapy shell www.baidu.com")
# p1 = os.system("scrapy shel response")
# print(p1)