#!/usr/bin/python
# -*- coding: utf-8 -*-
import keywords

with open('银河农产品.txt',encoding='gbk') as f:
    lines = f.readlines()
idea = {}
items = ["花生","棉花-棉纱","白糖","鸡蛋","生猪","玉米/玉米淀粉","油脂板块","大豆/粕类"]
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
    if key == "棉花-棉纱":
        topop.append("棉花-棉纱")
        toadd.append(["棉花", idea[key]])
        toadd.append(["棉纱", idea[key]])
    if key == "玉米/玉米淀粉":
        topop.append("玉米/玉米淀粉")
        toadd.append(["玉米", idea[key]])
        toadd.append(["淀粉", idea[key]])
    if key == "油脂板块":
        topop.append("油脂板块")
        toadd.append(["豆油", idea[key]])
        toadd.append(["菜油", idea[key]])
        toadd.append(["棕榈油", idea[key]])
    if key == "大豆/粕类":
        topop.append("大豆/粕类")
        toadd.append(["豆粕", idea[key]])
        toadd.append(["菜粕", idea[key]])


for i in topop:
    idea.pop(i)
for i in toadd:
    idea[i[0]] = i[1]

yinhe_idea = idea
for key in idea:
    print(key)
    print(idea[key])