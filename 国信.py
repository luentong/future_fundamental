import keywords

with open('国信期货.txt',encoding='utf-8') as f:
    lines = f.readlines()
idea = {}
items = ["贵金属","铜铝","锌","螺纹钢","铁合金","焦煤焦炭","豆类","油脂","白糖","棉花","玉米","生猪","花生","苹果","PTA","聚烯烃","原油","橡胶","燃料油","沥青","甲醇"]
next = False
prev_item = ""
for l in lines:
    print(l)
    stripped = l.strip().strip('\n').strip('【').strip('】')
    if stripped == "":
        continue
    if stripped in items:
        next = True
        prev_item = stripped
        continue
    if l.isnumeric():
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

topop = []
toadd = []
for key in idea:
    if not idea[key].isdecimal():
        idea[key] = keywords.simplify_sent(idea[key])
    if key == "焦煤焦炭":
        topop.append("焦煤焦炭")
        toadd.append(["焦煤", idea[key]])
        toadd.append(["焦炭", idea[key]])
    if key == "燃料油":
        topop.append("燃料油")
        toadd.append(["燃油", idea[key]])
    if key == "贵金属":
        topop.append("贵金属")
        toadd.append(["黄金", idea[key]])
        toadd.append(["白银", idea[key]])
    if key == "铜铝":
        topop.append("铜铝")
        toadd.append(["铜", idea[key]])
        toadd.append(["铝", idea[key]])
    if key == "螺纹钢":
        topop.append("螺纹钢")
        toadd.append(["螺纹", idea[key]])
        toadd.append(["热卷", idea[key]])
    if key == "铁合金":
        topop.append("铁合金")
        toadd.append(["锰硅", idea[key]])
        toadd.append(["硅铁", idea[key]])
    if key == "豆类":
        topop.append("豆类")
        toadd.append(["豆一", idea[key]])
        toadd.append(["豆粕", idea[key]])
    if key == "油脂":
        topop.append("油脂")
        toadd.append(["豆油", idea[key]])
        toadd.append(["菜油", idea[key]])
        toadd.append(["棕榈油", idea[key]])
    if key == "聚烯烃":
        topop.append("聚烯烃")
        toadd.append(["PVC", idea[key]])
        toadd.append(["PP", idea[key]])
        toadd.append(["塑料", idea[key]])




for i in topop:
    idea.pop(i)
for i in toadd:
    idea[i[0]] = i[1]

yinhe_idea = idea
for key in idea:
    print(key)
    print(idea[key])