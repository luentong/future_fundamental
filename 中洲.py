#!/usr/bin/python
# -*- coding: utf-8 -*-
import keywords

with open('中洲.txt') as f:
    lines = f.readlines()
idea = {}
items = ["原油","钢材","铁矿","焦煤焦炭","沪铜","沪铝","苯乙烯","美豆、豆粕","玉米","白糖","鸡蛋","生猪"]

next = False
prev_item = ""
for l in lines:
    stripped = l.strip().strip('\n').strip('【').strip('】')
    if stripped == "":
        continue
    if '|' in stripped:
        stripped_first = l.strip().strip('\n').split('|')[0].strip(" ")
        if stripped_first in items:
            next = True
            prev_item = stripped_first
    if next:
        if prev_item in idea:
            idea[prev_item] += l.strip().strip('\n')
        else:
            idea[prev_item] = l.strip().strip('\n')
zhongzhou_old = {}
for i in idea:
    zhongzhou_old[i] = idea[i][:]

topop = []
toadd = []
for key in idea:
    if not idea[key].isdecimal():
        idea[key] = keywords.simplify_sent(idea[key])
    if key == "钢材":
        topop.append("钢材")
        toadd.append(["螺纹", idea[key]])
        toadd.append(["热卷", idea[key]])
    if key == "焦煤焦炭":
        topop.append("焦煤焦炭")
        toadd.append(["焦煤", idea[key]])
        toadd.append(["焦炭", idea[key]])
    if key == "沪铜":
        topop.append("沪铜")
        toadd.append(["铜", idea[key]])
    if key == "沪铝":
        topop.append("沪铝")
        toadd.append(["铝", idea[key]])
    if key == "美豆、豆粕":
        topop.append("美豆、豆粕")
        toadd.append(["豆粕", idea[key]])
        toadd.append(["菜粕", idea[key]])



for i in topop:
    idea.pop(i)
for i in toadd:
    idea[i[0]] = i[1]

zhongzhou_idea = idea