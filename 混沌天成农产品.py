#!/usr/bin/python
# -*- coding: utf-8 -*-
import keywords

with open('混沌天成农产品.txt',encoding='gbk') as f:
    lines = f.readlines()
idea = {}
items = ["油脂油料","棉花","玉  米","豆  粕","鸡  蛋","生  猪","苹  果","纸  浆"]
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
hundunneng_old = {}
for i in idea:
    hundunneng_old[i] = idea[i][:]

topop = []
toadd = []
for key in idea:
    if key == "油脂油料":
        topop.append("油脂油料")
        toadd.append(["豆油", idea[key]])
        toadd.append(["菜油", idea[key]])
        toadd.append(["棕榈油", idea[key]])
    if key == "玉  米":
        topop.append("玉  米")
        toadd.append(["玉米", idea[key]])
    if key == "豆  粕":
        topop.append("豆  粕")
        toadd.append(["豆粕", idea[key]])
    if key == "鸡  蛋":
        topop.append("鸡  蛋")
        toadd.append(["鸡蛋", idea[key]])
    if key == "生  猪":
        topop.append("生  猪")
        toadd.append(["生猪", idea[key]])
    if key == "苹  果":
        topop.append("苹  果")
        toadd.append(["苹果", idea[key]])
    if key == "纸  浆":
        topop.append("纸  浆")
        toadd.append(["纸浆", idea[key]])

for i in topop:
    idea.pop(i)
for i in toadd:
    idea[i[0]] = i[1]

hundunneng_old = {}
for i in idea:
    hundunneng_old[i] = idea[i][:]

for key in idea:
    if not idea[key].isdecimal():
        idea[key] = keywords.simplify_sent(idea[key])


for i in hundunneng_old:
    if i in idea:
        hundunneng_old[i] = idea[i] + " 混沌能化 " + hundunneng_old[i]
    else:
        hundunneng_old[i] = ""

hundunneng_idea = idea
for key in idea:
    print(key)
    print(idea[key])