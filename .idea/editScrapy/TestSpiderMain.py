# -*- coding: utf-8 -*-
import EditClass
import LogicClass

SpiderStr = ""

editClass = EditClass.EditClass()
logic = LogicClass.LoginClass()
#SpiderStr = SpiderStr +
###########爬虫核心文件编写################
#爬虫依赖编写
spiderImportStr = editClass.addVar(0,"import scrapy")
spiderImportStr = spiderImportStr + editClass.addVar(0,"from demo1.items import Demo1Item")
SpiderStr = SpiderStr + spiderImportStr

#爬虫类（头部）编写
spiderHead = editClass.addSpiderClass('Demo1Spider','demoSpider',['travel.sina.com.cn'],['http://travel.sina.com.cn/domestic/news/2018-06-26/detail-ihencxtu2975652.shtml'])
#print(spiderHead)
SpiderStr = SpiderStr + spiderHead

#爬虫（解析方法）编写
parseDef = EditClass.EditClass.addDefAndparam('parse',['self','response']);
spiderMain = parseDef;
#print (spiderMain)
SpiderStr = SpiderStr + spiderMain

#爬虫（解析方法内逻辑）编写
responseXpath = '''response.xpath("//div[@class='wrap-inner']")'''
judgeFor = logic.forLogin(2, "entity", responseXpath)
SpiderStr = SpiderStr + judgeFor

Item = EditClass.EditClass()
itemStr = Item.addVar(4,"item = Demo1Item()")
SpiderStr = SpiderStr + itemStr

Items = LogicClass.LoginClass()
itemArr = ['title','content_html','content_text','date']
xpathArr = ["//h1[@id='artibodyTitle']/text()",
            "//div[@class='article article_16']/p",
            "//div[@class='article article_16']/p/text()",
            "//span[@class='time-source']/text()"]
ItemsStr = Items.itemsAndXpaths(3,itemArr,xpathArr)
SpiderStr = SpiderStr + ItemsStr

yieldStr = Item.addVar(3,"yield item")
SpiderStr = SpiderStr + yieldStr

print(SpiderStr)
#写入文件
spiderFile = open('F:\\autoScrapy\\demo1\\demo1\\spiders\\spider.py','w')
spiderFile.write(SpiderStr)
spiderFile.close()

##############爬虫item文件编写##################
itemsPyStr = ""
#item类编写
itemImportStr = editClass.addVar(0,"import scrapy")
itemClassStr = editClass.addClassAndParams("Demo1Item", "scrapy.Item")
itemStr = logic.itemsScrapyField(itemArr)
itemsPyStr = itemImportStr + itemClassStr + itemStr
print(itemsPyStr)

#写入文件
itemPyFile = open('F:\\autoScrapy\\demo1\\demo1\\items.py','w')
itemPyFile.write(itemsPyStr)
itemPyFile.close()