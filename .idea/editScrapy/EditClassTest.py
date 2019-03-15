
import EditClass

code = EditClass.EditClass.addClass('testClass');
code = code + EditClass.EditClass.addDef('addTestDef')
code = code + EditClass.EditClass.addVar(3,'str') + " = " + "'werewrw'" + "\n"
code = code + EditClass.EditClass.addDefAndparam("addParamDef",["var1","var2","var3"])
print(code)

fun = EditClass.EditClass()
spiderHead = fun.addSpiderClass('doemSpider','sinaNew1',[],[])
print(spiderHead)

parseClass = EditClass.EditClass.addDefSelf('start_requests');
spiderMain = parseClass;
print (spiderMain)