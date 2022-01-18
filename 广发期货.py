import keywords

with open('广发期货.txt',encoding='utf-8') as f:
    lines = f.readlines()
idea = {}
items = ["贵金属：","铜 ：","锌：","铝：","镍：","不锈钢：","锡：","钢材：","铁矿石：","焦炭：","焦煤：","动力煤：","豆粕：","油脂：","生猪：","玉米：","白糖：","棉花：","鸡蛋：","花生：","红枣：",
         "原油：","沥青：","PTA：","乙二醇：","短纤：","苯乙烯：","LLDPE：","PP：","尿素:","PVC：","甲醇：","纯碱：","玻璃：","橡胶："]
next = False
prev_item = ""
for l in lines:
    stripped = l.strip().strip('\n').strip('【').strip('】')
    if stripped == "":
        continue
    if "纯碱：" in stripped:
        if "纯碱" in idea:
            idea["纯碱"] += stripped
        else:
            idea["纯碱"] = stripped
        prev_item = "纯碱："
        continue
    if "玻璃：" in stripped:
        if "玻璃" in idea:
            idea["玻璃"] += stripped
        else:
            idea["玻璃"] = stripped
        prev_item = "玻璃："
        continue
    if stripped in items:
        next = True
        prev_item = stripped
        continue
    if next:
        if prev_item.strip("：") in idea:
            idea[prev_item.strip("：") ] += l.strip().strip('\n')
        else:
            idea[prev_item.strip("：") ] = l.strip().strip('\n')
guangfa_old = {}
for i in idea:
    guangfa_old[i] = idea[i][:]


topop = []
toadd = []
for key in idea:
    if not idea[key].isdecimal():
        idea[key] = keywords.simplify_sent(idea[key])
    if key == "贵金属":
        topop.append("贵金属")
        toadd.append(["黄金", idea[key]])
        toadd.append(["白银", idea[key]])
    if key == "油脂":
        topop.append("油脂")
        toadd.append(["豆油", idea[key]])
        toadd.append(["菜油", idea[key]])
        toadd.append(["棕榈油", idea[key]])
    if key == "乙二醇":
        topop.append("乙二醇")
        toadd.append(["MEG", idea[key]])
    if key == "LLDPE":
        topop.append("LLDPE")
        toadd.append(["塑料", idea[key]])
    if key == "尿素:":
        topop.append("尿素:")
        toadd.append(["尿素", idea[key]])
    if key == "钢材":
        topop.append("钢材")
        toadd.append(["螺纹", idea[key]])
        toadd.append(["热卷", idea[key]])
    if key == "猪":
        topop.append("猪")
        toadd.append(["生猪", idea[key]])
        toadd.append(["", idea[key]])
    if key == "铁矿石":
        topop.append("铁矿石")
        toadd.append(["铁矿", idea[key]])



for i in topop:
    idea.pop(i)
for i in toadd:
    idea[i[0]] = i[1]