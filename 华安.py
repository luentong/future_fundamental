#coding=gb2312

import keywords
with open('华安.txt',encoding='gbk') as f:
    lines = f.readlines()
idea = {}
items = ["股指","集运指数（欧线）","黄金","铜","铝","碳酸锂","双焦","纯碱","玻璃","不锈钢","沪镍","钢材","塑料","PVC","纸浆","油脂","豆粕","鸡蛋","生猪",
         "棉花"]
next = False
prev_item = ""
for l in lines:
    stripped = l.strip().strip('\n')
    if stripped == "":
        continue
    if stripped in items:
        next = True
        prev_item = stripped.split("：")[0]
        continue
    if next:
        if prev_item in idea:
            idea[prev_item] += l.strip().strip('\n')
        else:
            idea[prev_item] = l.strip().strip('\n')
huaan_old = {}
for i in idea:
    huaan_old[i] = idea[i][:]

topop = []
toadd = []
for key in idea:
    if key == "集运指数（欧线）":
        topop.append("集运指数（欧线）")
        toadd.append(["集运", idea[key]])
    if key == "双焦":
        topop.append("双焦")
        toadd.append(["焦煤", idea[key]])
        toadd.append(["焦炭", idea[key]])
    if key == "沪镍":
        topop.append("沪镍")
        toadd.append(["镍", idea[key]])
    if key == "钢材":
        topop.append("钢材")
        toadd.append(["螺纹", idea[key]])
        toadd.append(["热卷", idea[key]])
    if key == "油脂":
        topop.append("油脂")
        toadd.append(["棕榈油", idea[key]])
        toadd.append(["豆油", idea[key]])
        toadd.append(["菜油", idea[key]])

for i in topop:
    idea.pop(i)
for i in toadd:
    idea[i[0]] = i[1]

huaan_old = {}
for i in idea:
    huaan_old[i] = idea[i][:]

for key in idea:
    if not idea[key].isdecimal():
        idea[key] = keywords.simplify_sent(idea[key])


for i in huaan_old:
    if i in idea:
        huaan_old[i] = idea[i] + " 华安 " + huaan_old[i]
    else:
        huaan_old[i] = ""

huaan_idea = idea
for i in idea:
    print(i)
    print(idea[i])
    print(huaan_old[i])
