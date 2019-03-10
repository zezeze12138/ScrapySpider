#cmd="curl http://localhost:6800/schedule.json -d project="+project+" -d spider="+spider+" -d category="+str(NewsTopicId)

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

i1 = 'title = scrapy.Field()'
i2 = 'content_html = scrapy.Field()'
i3 = 'content_text = scrapy.Field()'
i4 = 'date = scrapy.Field()'

newContext = newContext+'\t'+i1
newContext = newContext+'\n'+'\t'+i2
newContext = newContext+'\n'+'\t'+i3
newContext = newContext+'\n'+'\t'+i4

w = open('F:\\autoScrapy\\demo1\\demo1\\items.py','w')
w.write(newContext)
w.close()

f = open('F:\\autoScrapy\\demo1\\demo1\\items.py','r')
itemsFile = f.read()
f.close()
print("****************")
print(itemsFile)
print("****************")