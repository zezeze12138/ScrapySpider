
import EditClass
import LogicClass

code = EditClass.EditClass.addClass('testClass');
code = code + EditClass.EditClass.addDef('addTestDef')
code = code + EditClass.EditClass.addVar(3,'str') + " = " + "'werewrw'" + "\n"
code = code + EditClass.EditClass.addDefAndparam("addParamDef",["var1","var2","var3"])
print(code)

fun = EditClass.EditClass()
spiderHead = fun.addSpiderClass('doemSpider','sinaNew1',[],[])
print(spiderHead)

parseClass = EditClass.EditClass.addDefAndparam('start_requests',['self','response']);
spiderMain = parseClass;
print (spiderMain)

judgeFun = LogicClass.LoginClass()
judgeCondition = 'test == 1'
#print(judgeFun.ifelse('if', 2, judgeCondition))
responseXpath = '''response.xpath("//div[@class='wrap-inner']")'''
print(judgeFun.forLogin(2, "entity", responseXpath))

Item = EditClass.EditClass()
print(Item.addVar(3,"item = ExampleItem()"))

Items = LogicClass.LoginClass()
itemArr = ['title','content_html','content_text','date']
xpathArr = ['//h1[@id="artibodyTitle"]/text()',
            '//div[@class="article article_16"]/p',
            '//div[@class="article article_16"]/p/text()',
            '//span[@class="time-source"]/text()']
Items.itemsAndXpaths(3,itemArr,xpathArr)

print(Item.addVar(3,"yield item"))