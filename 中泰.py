#!/usr/bin/python
# -*- coding: utf-8 -*-
import keywords

with open('中泰.txt') as f:
    lines = f.readlines()
idea = {}
items = ["股指期货","国债期货","棉花","白糖","油脂油料","鸡蛋","苹果","红枣","花生","生猪","原油","塑料","橡胶","甲醇","纯碱","沥青","PVC","苯乙烯","聚酯产业链","液化石油气","铝和氧化铝","镍",
         "碳酸锂","工业硅","螺矿","煤焦","铁合金"]


next = False
prev_item = ""
for l in lines:
    stripped = l.strip().strip('\n').strip('【').strip('】')
    if stripped == "":
        continue
    else:
        stripped_first = l.strip().strip('\n').split('|')[0].strip(" ")
        if stripped_first in items:
            next = True
            prev_item = stripped_first
    if next:
        if prev_item in idea:
            idea[prev_item] += l.strip().strip('\n')
        else:
            idea[prev_item] = l.strip().strip('\n')
zhongtai_old = {}
for i in idea:
    zhongtai_old[i] = idea[i][:]

topop = []
toadd = []
for key in idea:
    if not idea[key].isdecimal():
        idea[key] = keywords.simplify_sent(idea[key])
    if key == "股指期货":
        topop.append("股指期货")
        toadd.append(["股指", idea[key]])
    if key == "国债期货":
        topop.append("国债期货")
        toadd.append(["国债", idea[key]])
    if key == "油脂油料":
        topop.append("油脂油料")
        toadd.append(["豆粕", idea[key]])
        toadd.append(["豆油", idea[key]])
        toadd.append(["菜油", idea[key]])
        toadd.append(["棕榈油", idea[key]])
    if key == "聚酯产业链":
        topop.append("聚酯产业链")
        toadd.append(["PTA", idea[key]])
        toadd.append(["MEG", idea[key]])
        toadd.append(["短纤", idea[key]])
    if key == "液化石油气":
        topop.append("液化石油气")
        toadd.append(["LPG", idea[key]])
    if key == "铝和氧化铝":
        topop.append("铝和氧化铝")
        toadd.append(["铝", idea[key]])
        toadd.append(["氧化铝", idea[key]])
    if key == "螺矿":
        topop.append("螺矿")
        toadd.append(["螺纹", idea[key]])
        toadd.append(["热卷", idea[key]])
        toadd.append(["铁矿", idea[key]])
    if key == "煤焦":
        topop.append("煤焦")
        toadd.append(["焦煤", idea[key]])
        toadd.append(["焦炭", idea[key]])
    if key == "铁合金":
        topop.append("铁合金")
        toadd.append(["硅铁", idea[key]])
        toadd.append(["锰硅", idea[key]])


for i in topop:
    idea.pop(i)
for i in toadd:
    idea[i[0]] = i[1]

zhongtai_idea = idea

print(idea)