import keywords

with open('五矿.txt',encoding='utf-8') as f:
    lines = f.readlines()
idea = {}
items = ["油脂","蛋白粕","鸡蛋","生猪","白糖","苹果","棉花","贵金属","铜","锌","铅",
         "铝","镍","锡","锰硅","硅铁","铁矿石","钢材","双焦","橡胶","甲醇","尿素","苯乙烯","PVC","PTA","玻璃","纯碱","LPG","沥青"]
next = False
prev_item = ""
for l in lines:
    if l.strip().strip('\n') == "":
        continue
    stripped = l.strip().strip('\n')
    if stripped in items:
        next = True
        prev_item = stripped
        continue
    if next:
        if prev_item in idea:
            idea[prev_item] += l.strip().strip('\n')
        else:
            idea[prev_item] = l.strip().strip('\n')
        next = False
print(idea)
wukuang_old = {}
for i in idea:
    wukuang_old[i] = idea[i][:]

topop = []
toadd = []
for key in idea:
    if not idea[key].isdecimal():
        idea[key] = keywords.simplify_sent(idea[key])
    if key == "贵金属":
        topop.append("贵金属")
        toadd.append(["黄金", idea[key]])
        toadd.append(["白银", idea[key]])
    if key == "双焦":
        topop.append("双焦")
        toadd.append(["焦煤", idea[key]])
        toadd.append(["焦炭", idea[key]])
    if key == "铁矿石":
        topop.append("铁矿石")
        toadd.append(["铁矿", idea[key]])
    if key == "钢材":
        topop.append("钢材")
        toadd.append(["螺纹", idea[key]])
        toadd.append(["热卷", idea[key]])
    if key == "油脂":
        topop.append("油脂")
        toadd.append(["菜油", idea[key]])
        toadd.append(["棕榈油", idea[key]])
    if key == "蛋白粕":
        topop.append("蛋白粕")
        toadd.append(["豆粕", idea[key]])
        toadd.append(["菜粕", idea[key]])



for i in topop:
    idea.pop(i)
for i in toadd:
    idea[i[0]] = i[1]

wukuang_idea = idea

for key in idea:
    print(key)
    print(idea[key])