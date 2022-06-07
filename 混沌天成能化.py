#!/usr/bin/python
# -*- coding: utf-8 -*-
import keywords

with open('混沌天成能化.txt',encoding='gbk') as f:
    lines = f.readlines()
idea = {}
items = ["纯碱玻璃","橡胶","PVC","LLDPE日评","尿素","甲醇","MEG日评：","PTA日评","原油","PP日评："]
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
    if key == "纯碱玻璃":
        topop.append("纯碱玻璃")
        toadd.append(["纯碱", idea[key]])
        toadd.append(["玻璃", idea[key]])
    if key == "LLDPE日评":
        topop.append("LLDPE日评")
        toadd.append(["塑料", idea[key]])
    if key == "MEG日评：":
        topop.append("MEG日评：")
        toadd.append(["MEG", idea[key]])
    if key == "PTA日评":
        topop.append("PTA日评")
        toadd.append(["PTA", idea[key]])
    if key == "PP日评：":
        topop.append("PP日评：")
        toadd.append(["PP", idea[key]])

for i in topop:
    idea.pop(i)
for i in toadd:
    idea[i[0]] = i[1]

yinhe_idea = idea
for key in idea:
    print(key)
    print(idea[key])