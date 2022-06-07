#!/usr/bin/python
# -*- coding: utf-8 -*-
import keywords

with open('弘业.txt',encoding='gbk') as f:
    lines = f.readlines()
idea = {}
items = ["原油","PTA","乙二醇","短纤","聚烯烃","液化石油气","沥青","甲醇","苯乙烯","橡胶","玻璃","纯碱","尿素","纸浆","黄金&白银","沪镍","沪铜&国际铜","沪铝","沪锌","沪铅",
         "螺纹&热卷","铁矿石","焦煤&焦炭","动力煤","铁合金","油脂","油料","花生","玉米&淀粉","棉花&棉纱","生猪","鸡蛋","白糖","苹果","红枣"]
next = False
prev_item = ""
for l in lines:
    stripped = l.strip().strip('\n').strip('【').strip('】')
    if stripped == "":
        continue
    if stripped in items:
        next = True
        prev_item = stripped
        continue
    if l.startswith('银河期货') and stripped not in items:
        next = False
        continue
    if next:
        if prev_item in idea:
            idea[prev_item] += l.strip().strip('\n')
        else:
            idea[prev_item] = l.strip().strip('\n')
hongye_old = {}
for i in idea:
    hongye_old[i] = idea[i][:]

topop = []
toadd = []
for key in idea:
    if key == "棉花&棉纱":
        topop.append("棉花&棉纱")
        toadd.append(["棉花", idea[key]])
        toadd.append(["棉纱", idea[key]])
    if key == "玉米&淀粉":
        topop.append("玉米&淀粉")
        toadd.append(["玉米", idea[key]])
        toadd.append(["淀粉", idea[key]])
    if key == "油料":
        topop.append("油料")
        toadd.append(["豆粕", idea[key]])
        toadd.append(["菜粕", idea[key]])
    if key == "油脂":
        topop.append("油脂")
        toadd.append(["豆油", idea[key]])
        toadd.append(["菜油", idea[key]])
        toadd.append(["棕榈油", idea[key]])

    if key == "铁合金":
        topop.append("铁合金")
        toadd.append(["硅铁", idea[key]])
        toadd.append(["锰硅", idea[key]])
    if key == "焦煤&焦炭":
        topop.append("焦煤&焦炭")
        toadd.append(["焦煤", idea[key]])
        toadd.append(["焦炭", idea[key]])
    if key == "铁矿石":
        topop.append("铁矿石")
        toadd.append(["铁矿", idea[key]])
    if key == "螺纹&热卷":
        topop.append("螺纹&热卷")
        toadd.append(["螺纹", idea[key]])
        toadd.append(["热卷", idea[key]])
    if key == "沪镍":
        topop.append("沪镍")
        toadd.append(["镍", idea[key]])
    if key == "沪铜&国际铜":
        topop.append("沪铜&国际铜")
        toadd.append(["铜", idea[key]])
    if key == "沪铝":
        topop.append("沪铝")
        toadd.append(["铝", idea[key]])
    if key == "沪锌":
        topop.append("沪锌")
        toadd.append(["锌", idea[key]])
    if key == "沪铅":
        topop.append("沪铅")
        toadd.append(["铅", idea[key]])
    if key == "黄金&白银":
        topop.append("黄金&白银")
        toadd.append(["黄金", idea[key]])
        toadd.append(["白银", idea[key]])
    if key == "液化石油气":
        topop.append("液化石油气")
        toadd.append(["LPG", idea[key]])
    if key == "聚烯烃":
        topop.append("聚烯烃")
        toadd.append(["PP", idea[key]])
        toadd.append(["塑料", idea[key]])
        toadd.append(["PVC", idea[key]])

for i in topop:
    idea.pop(i)
for i in toadd:
    idea[i[0]] = i[1]

hongye_old = {}
for i in idea:
    hongye_old[i] = idea[i][:]

for key in idea:
    if not idea[key].isdecimal():
        idea[key] = keywords.simplify_sent(idea[key])


for i in hongye_old:
    if i in idea:
        hongye_old[i] = idea[i] + " 弘业 " + hongye_old[i]
    else:
        hongye_old[i] = ""

hongye_idea = idea
for key in idea:
    print(key)
    print(idea[key])