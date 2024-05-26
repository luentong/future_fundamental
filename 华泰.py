#coding=gb2312

import keywords
with open('华泰.txt',encoding='gbk') as f:
    lines = f.readlines()
idea = {}
items = ["股指期货","航运","国债期货","原油","燃料油","液化石油气","石油沥青","PX、PTA、PF","甲醇",
         "聚烯烃","EG","EB","尿素","天然橡胶与合成橡胶","氯碱","PVC","烧碱","贵金属",
         "铜","锌","镍不锈钢","铝","铅","工业硅","碳酸锂","钢材","铁矿","双焦","玻璃纯碱","双硅",
         "油脂","大豆观点","花生观点","粕类观点","玉米观点","生猪观点","鸡蛋观点","苹果观点","红枣观点","棉花观点","纸浆观点","白糖观点"]
next = False
prev_item = ""
for l in lines:
    stripped = l.strip().strip('\n')
    if stripped == "":
        continue
    if "：" in stripped and stripped.split("：")[0] in items:
        next = True
        prev_item = stripped.split("：")[0]
        continue
    if l.startswith('银河期货') and stripped not in items:
        next = False
        continue
    if next:
        if prev_item in idea:
            idea[prev_item] += l.strip().strip('\n')
        else:
            idea[prev_item] = l.strip().strip('\n')
huatai_old = {}
for i in idea:
    huatai_old[i] = idea[i][:]

topop = []
toadd = []
for key in idea:
    if key == "PX、PTA、PF":
        topop.append("PX、PTA、PF")
        toadd.append(["PX", idea[key]])
        toadd.append(["PTA", idea[key]])
        toadd.append(["短纤", idea[key]])
    if key == "石油沥青":
        topop.append("石油沥青")
        toadd.append(["沥青", idea[key]])
    if key == "液化石油气":
        topop.append("液化石油气")
        toadd.append(["LPG", idea[key]])
    if key == "燃料油":
        topop.append("燃料油")
        toadd.append(["燃油", idea[key]])
    if key == "国债期货":
        topop.append("国债期货")
        toadd.append(["国债", idea[key]])
    if key == "股指期货":
        topop.append("股指期货")
        toadd.append(["股指", idea[key]])
    if key == "双焦":
        topop.append("双焦")
        toadd.append(["焦煤", idea[key]])
        toadd.append(["焦炭", idea[key]])
    if key == "双硅":
        topop.append("双硅")
        toadd.append(["硅铁", idea[key]])
        toadd.append(["锰硅", idea[key]])
    if key == "天然橡胶":
        topop.append("天然橡胶")
        toadd.append(["橡胶", idea[key]])
    if key == "沪铜":
        topop.append("沪铜")
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
    if key == "油脂":
        topop.append("油脂")
        toadd.append(["棕榈油", idea[key]])
        toadd.append(["豆油", idea[key]])
        toadd.append(["菜油", idea[key]])
    if key == "豆粕/菜粕":
        topop.append("豆粕/菜粕")
        toadd.append(["豆粕", idea[key]])
        toadd.append(["菜粕", idea[key]])

for i in topop:
    idea.pop(i)
for i in toadd:
    idea[i[0]] = i[1]

huatai_old = {}
for i in idea:
    huatai_old[i] = idea[i][:]

for key in idea:
    if not idea[key].isdecimal():
        idea[key] = keywords.simplify_sent(idea[key])


for i in huatai_old:
    if i in idea:
        huatai_old[i] = idea[i] + " 华泰 " + huatai_old[i]
    else:
        huatai_old[i] = ""

huatai_idea = idea
for i in idea:
    print(i)
    print(idea[i])