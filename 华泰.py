import keywords
with open('华泰期货.txt',encoding='utf-8') as f:
    lines = f.readlines()
idea = {}
items = ["原油","燃料油","沥青","PTA","甲醇","橡胶","贵金属","铜","镍不锈钢","锌铝","钢材","铁矿石","双焦","动力煤","玻璃纯碱","油脂油料","玉米与淀粉","鸡蛋","生猪","郑棉"]
next = False
prev_item = ""
for l in lines:
    print("华泰" + l)
    stripped = l.strip().strip('\n')
    if stripped == "":
        continue
    if stripped.split("：")[0] in items:
        next = True
        prev_item = stripped.split("：")[0]
        continue
    if "策略：" in l and len(l) < 5:
        next = False
    if next:
        if prev_item in idea:
            if "策略：" in l:
                if "套利：" in l:
                    idea[prev_item] = l.strip().strip('\n').split("套利：")[0]
                    next = False
                else:
                    idea[prev_item] = l.strip().strip('\n')
                    next = False
            else:
                idea[prev_item] += l.strip().strip('\n')
        else:
            if "策略：" in l:
                if "套利：" in l:
                    idea[prev_item] = l.strip().strip('\n').split("套利：")[0]
                    next = False
                else:
                    idea[prev_item] = l.strip().strip('\n')
                    next = False
            else:
                idea[prev_item] = l.strip().strip('\n')
huatai_old = {}
for i in idea:
    huatai_old[i] = idea[i][:]


for i in huatai_old:
    print(i)
    print(huatai_old[i])

topop = []
toadd = []
for key in idea:
    if key == "双焦":
        topop.append("双焦")
        toadd.append(["焦煤", idea[key]])
        toadd.append(["焦炭", idea[key]])
    if key == "燃料油":
        topop.append("燃料油")
        toadd.append(["燃油", idea[key]])
    if key == "贵金属":
        topop.append("贵金属")
        toadd.append(["黄金", idea[key]])
        toadd.append(["白银", idea[key]])
    if key == "锌铝":
        topop.append("锌铝")
        toadd.append(["锌", idea[key]])
        toadd.append(["铝", idea[key]])
    if key == "钢材":
        topop.append("钢材")
        toadd.append(["螺纹", idea[key]])
        toadd.append(["热卷", idea[key]])
    if key == "玻璃纯碱":
        topop.append("玻璃纯碱")
        toadd.append(["锰硅", idea[key]])
        toadd.append(["硅铁", idea[key]])
    if key == "镍不锈钢":
        topop.append("镍不锈钢")
        toadd.append(["镍", idea[key]])
        toadd.append(["不锈钢", idea[key]])
    if key == "铁矿石":
        topop.append("铁矿石")
        toadd.append(["铁矿", idea[key]])
    if key == "玉米与淀粉":
        topop.append("玉米与淀粉")
        toadd.append(["玉米", idea[key]])
        toadd.append(["淀粉", idea[key]])

for i in topop:
    idea.pop(i)
for i in toadd:
    idea[i[0]] = i[1]

for key in idea:
    if not idea[key].isdecimal():
        idea[key] = keywords.simplify_sent(idea[key])

for i in idea:
    print(i)
    print(idea[i])

for i in huatai_old:
    if i in idea:
        huatai_old[i] = idea[i] + " 华泰 " + huatai_old[i]
    else:
        huatai_old[i] = ""


huatai_idea = idea
for key in idea:
    print(key)
    print(idea[key])