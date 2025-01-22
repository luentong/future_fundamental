#!/usr/bin/python
# -*- coding: utf-8 -*-
import keywords

with open('华联.txt') as f:
    lines = f.readlines()
idea = {}
items = ["股指","国债","铜","铝","橡胶","液化气","原油","PVC","甲醇","聚烯烃","螺纹钢","玻璃","焦煤","铁矿石","白糖","鸡蛋","生猪","油脂","饲料"]
next = False
prev_item = ""
for l in lines:
    stripped = l.strip().strip('\n').strip('【').strip('】')
    if stripped == "":
        continue
    if '】' in stripped:
        stripped_first = l.strip().strip('\n').strip('【').split('】')[0]
        if stripped_first in items:
            next = True
            prev_item = stripped_first
    if next:
        if prev_item in idea:
            idea[prev_item] += l.strip().strip('\n')
        else:
            idea[prev_item] = l.strip().strip('\n')
beite_old = {}
for i in idea:
    beite_old[i] = idea[i][:]

topop = []
toadd = []
for key in idea:
    if not idea[key].isdecimal():
        idea[key] = keywords.simplify_sent(idea[key])
    if key == "液化气":
        topop.append("液化气")
        toadd.append(["LPG", idea[key]])
    if key == "聚烯烃":
        topop.append("聚烯烃")
        toadd.append(["塑料", idea[key]])
        toadd.append(["PP", idea[key]])
    if key == "螺纹钢":
        topop.append("螺纹钢")
        toadd.append(["螺纹", idea[key]])
        toadd.append(["热卷", idea[key]])
    if key == "油脂":
        topop.append("油脂")
        toadd.append(["菜油", idea[key]])
        toadd.append(["棕榈油", idea[key]])
        toadd.append(["豆油", idea[key]])
    if key == "铁矿石":
        topop.append("铁矿石")
        toadd.append(["铁矿", idea[key]])
    if key == "饲料":
        topop.append("饲料")
        toadd.append(["豆粕", idea[key]])
        toadd.append(["菜粕", idea[key]])




for i in topop:
    idea.pop(i)
for i in toadd:
    idea[i[0]] = i[1]

beite_idea = idea
for key in idea:
    print(key)
    print(idea[key])