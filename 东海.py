#coding=gb2312

import keywords
with open('东海.txt',encoding='gbk') as f:
    lines = f.readlines()
idea = {}
items = ["股指","钢材","铁矿石","焦炭/焦煤","硅锰/硅铁","铜","锡","碳酸锂","铝","锌","金/银","原油","沥青","PTA",
         "乙二醇","甲醇","聚丙烯","塑料","美豆","蛋白粕","豆菜油","棕榈油","玉米","生猪","棉花"]
next = False
prev_item = ""
for l in lines:
    stripped = l.strip().strip('\n')
    if stripped == "":
        continue
    if "【" in stripped and "】" in stripped and stripped.split("】")[0].split("【")[1] in items:
        next = True
        prev_item = stripped.split("：")[0]
        idea[prev_item] = stripped.split("】")[1]
        continue
    if next:
        if prev_item in idea:
            idea[prev_item] += l.strip().strip('\n')
        else:
            idea[prev_item] = l.strip().strip('\n')
donghai_old = {}
for i in idea:
    donghai_old[i] = idea[i][:]

topop = []
toadd = []
for key in idea:
    if key == "豆菜油":
        toadd.append(["豆油", idea[key]])
        toadd.append(["菜油", idea[key]])
    if key == "蛋白粕":
        toadd.append(["豆粕", idea[key]])
    if key == "美豆":
        toadd.append(["豆一", idea[key]])
    if key == "聚丙烯":
        toadd.append(["PP", idea[key]])
    if key == "焦炭/焦煤":
        topop.append("焦炭/焦煤")
        toadd.append(["焦煤", idea[key]])
        toadd.append(["焦炭", idea[key]])
    if key == "硅锰/硅铁":
        topop.append("硅锰/硅铁")
        toadd.append(["硅铁", idea[key]])
        toadd.append(["锰硅", idea[key]])
    if key == "金/银":
        topop.append("金/银")
        toadd.append(["黄金", idea[key]])
        toadd.append(["白银", idea[key]])
    if key == "铁矿石":
        toadd.append(["铁矿", idea[key]])
    if key == "油脂":
        topop.append("油脂")
        toadd.append(["棕榈油", idea[key]])
        toadd.append(["豆油", idea[key]])
        toadd.append(["菜油", idea[key]])
    if key == "钢材":
        topop.append("钢材")
        toadd.append(["螺纹", idea[key]])
        toadd.append(["热卷", idea[key]])

for i in topop:
    idea.pop(i)
for i in toadd:
    idea[i[0]] = i[1]

donghai_old = {}
for i in idea:
    donghai_old[i] = idea[i][:]

for key in idea:
    if not idea[key].isdecimal():
        idea[key] = keywords.simplify_sent(idea[key])


for i in donghai_old:
    if i in idea:
        donghai_old[i] = idea[i] + " 东海 " + donghai_old[i]
    else:
        donghai_old[i] = ""

donghai_idea = idea
for i in idea:
    print(i)
    print(idea[i])
    print(donghai_old[i])
