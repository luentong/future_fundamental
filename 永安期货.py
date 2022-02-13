import keywords

with open('永安期货.txt',encoding='utf-8') as f:
    lines = f.readlines()
idea = {}
items = ["钢 材","铁 矿 石","动 力 煤","焦煤焦炭","纸 浆","【原油】","【沥青】","橡胶","【LPG】","尿 素","豆类油脂","棉花","白 糖","生 猪","生猪","豆粕","液化气","RU","聚烯烃","聚酯"]
next = False
prev_item = ""
for l in lines:
    stripped = l.strip()
    print(stripped)
    if stripped == "":
        continue
    if stripped in items:
        next = True
        prev_item = stripped
        continue
    if next:
        if prev_item.strip("：") in idea:
            idea[prev_item.strip()] += l.strip().strip('\n')
        else:
            idea[prev_item.strip()] = l.strip().strip('\n')

yongan_old = {}
for i in idea:
    yongan_old[i] = idea[i][:]

for i in yongan_old:
    print(i)
    print(yongan_old[i])

topop = []
toadd = []
for key in idea:
    if not idea[key].isdecimal():
        idea[key] = keywords.simplify_sent(idea[key])
    if key == "焦煤焦炭":
        topop.append("焦煤焦炭")
        toadd.append(["焦煤", idea[key]])
        toadd.append(["焦炭", idea[key]])
    if key == "钢 材":
        topop.append("钢 材")
        toadd.append(["螺纹", idea[key]])
        toadd.append(["热卷", idea[key]])
    if key == "动 力 煤":
        topop.append("动 力 煤")
        toadd.append(["动力煤", idea[key]])
    if key == "纸 浆":
        topop.append("纸 浆")
        toadd.append(["纸浆", idea[key]])
    if key == "铁 矿 石":
        topop.append("铁 矿 石")
        toadd.append(["铁矿", idea[key]])
    if key == "【原油】":
        topop.append("【原油】")
        toadd.append(["原油", idea[key]])
    if key == "【沥青】":
        topop.append("【沥青】")
        toadd.append(["沥青", idea[key]])
    if key == "【LPG】":
        topop.append("【LPG】")
        toadd.append(["LPG", idea[key]])
    if key == "尿 素":
        topop.append("尿 素")
        toadd.append(["尿素", idea[key]])
    if key == "豆类油脂":
        topop.append("豆类油脂")
        toadd.append(["豆一", idea[key]])
        toadd.append(["豆油", idea[key]])
        toadd.append(["菜油", idea[key]])
        toadd.append(["棕榈油", idea[key]])
    if key == "白 糖":
        topop.append("白 糖")
        toadd.append(["白糖", idea[key]])
    if key == "生 猪":
        topop.append("生 猪")
        toadd.append(["生猪", idea[key]])





for i in topop:
    idea.pop(i)
for i in toadd:
    idea[i[0]] = i[1]

yongan_idea = idea

for i in idea:
    print(i)
    print(idea[i])
