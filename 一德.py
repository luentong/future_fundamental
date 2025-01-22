#!/usr/bin/python
# -*- coding: utf-8 -*-
import keywords

with open('一德.txt') as f:
    lines = f.readlines()
idea = {}
items = ["期指","期债","黄金/白银","螺纹/热卷","煤焦","硅锰","硅铁","动力煤","铁矿石","沪铝","沪镍","沪铜","沪锌",
         "沪铅","苹果","红枣","鸡蛋","生猪","白糖","甲醇","PVC","纯碱","玻璃","塑料/PP","苯乙烯","聚酯"]

next = False
prev_item = ""
for l in lines:
    stripped = l.strip().strip('\n').strip('【').strip('】')
    if stripped == "":
        continue
    if '：' in stripped:
        stripped_first = l.strip().strip('\n').split('：')[0].strip(" ")
        if "（" in stripped_first:
            stripped_first = stripped_first.split("（")[0]
        print(stripped_first)
        if stripped_first in items:
            next = True
            prev_item = stripped_first
    if next:
        if prev_item in idea:
            idea[prev_item] += l.strip().strip('\n')
        else:
            idea[prev_item] = l.strip().strip('\n')
yide_old = {}
for i in idea:
    yide_old[i] = idea[i][:]

topop = []
toadd = []
for key in idea:
    if not idea[key].isdecimal():
        idea[key] = keywords.simplify_sent(idea[key])
    if key == "期指":
        topop.append("期指")
        toadd.append(["股指", idea[key]])
    if key == "期债":
        topop.append("期债")
        toadd.append(["国债", idea[key]])
    if key == "黄金/白银":
        topop.append("黄金/白银")
        toadd.append(["黄金", idea[key]])
        toadd.append(["白银", idea[key]])
    if key == "螺纹/热卷":
        topop.append("螺纹/热卷")
        toadd.append(["螺纹", idea[key]])
        toadd.append(["热卷", idea[key]])
    if key == "煤焦":
        toadd.append(["焦炭", idea[key]])
    if key == "硅锰":
        topop.append("硅锰")
        toadd.append(["锰硅", idea[key]])
    if key == "塑料/PP":
        topop.append("塑料/PP")
        toadd.append(["塑料", idea[key]])
        toadd.append(["PP", idea[key]])
    if key == "聚酯":
        topop.append("聚酯")
        toadd.append(["PTA", idea[key]])
        toadd.append(["MEG", idea[key]])
        toadd.append(["短纤", idea[key]])
    if key == "铁矿石":
        topop.append("铁矿石")
        toadd.append(["铁矿", idea[key]])
    if key == "沪铝":
        topop.append("沪铝")
        toadd.append(["铝", idea[key]])
    if key == "沪镍":
        topop.append("沪镍")
        toadd.append(["镍", idea[key]])
    if key == "沪铜":
        topop.append("沪铜")
        toadd.append(["铜", idea[key]])
    if key == "沪锌":
        topop.append("沪锌")
        toadd.append(["锌", idea[key]])
    if key == "沪铅":
        topop.append("沪铅")
        toadd.append(["铅", idea[key]])


for i in topop:
    idea.pop(i)
for i in toadd:
    idea[i[0]] = i[1]

yide_idea = idea
