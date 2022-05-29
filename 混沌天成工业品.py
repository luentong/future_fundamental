#!/usr/bin/python
# -*- coding: utf-8 -*-
import keywords

with open('混沌天成工业品.txt',encoding='gbk') as f:
    lines = f.readlines()
idea = {}
items = ["钢材","铁矿石","焦煤","焦炭","铜","铝","锌","镍","不锈钢"]
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
yinhe_old = {}
for i in idea:
    yinhe_old[i] = idea[i][:]
for i in yinhe_old:
    print(i)
    print(yinhe_old[i])

topop = []
toadd = []
for key in idea:
    if not idea[key].isdecimal():
        idea[key] = keywords.simplify_sent(idea[key])
    if key == "钢材":
        topop.append("钢材")
        toadd.append(["螺纹", idea[key]])
        toadd.append(["热卷", idea[key]])
    if key == "铁矿石":
        topop.append("铁矿石")
        toadd.append(["铁矿", idea[key]])

for i in topop:
    idea.pop(i)
for i in toadd:
    idea[i[0]] = i[1]

yinhe_idea = idea
for key in idea:
    print(key)
    print(idea[key])