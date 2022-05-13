import keywords

with open('海通.txt',encoding='utf-8') as f:
    lines = f.readlines()
idea = {}
items = ["铝","钢材铁矿","油脂","焦煤焦炭","纸 浆","【原油】","【沥青】","橡胶","【LPG】","尿 素","豆类油脂","棉花","白 糖","生 猪","生猪","豆粕","液化气","RU","聚烯烃","聚酯"]
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

haitong_old = {}
for i in idea:
    haitong_old[i] = idea[i][:]

for i in haitong_old:
    print(i)
    print(haitong_old[i])

topop = []
toadd = []
for key in idea:
    if not idea[key].isdecimal():
        idea[key] = keywords.simplify_sent(idea[key])
    if key == "焦煤焦炭":
        topop.append("焦煤焦炭")
        toadd.append(["焦煤", idea[key]])
        toadd.append(["焦炭", idea[key]])
    if key == "钢材铁矿":
        topop.append("钢材铁矿")
        toadd.append(["铁矿", idea[key]])
        toadd.append(["螺纹", idea[key]])
        toadd.append(["热卷", idea[key]])
    if key == "油脂":
        topop.append("油脂")
        toadd.append(["豆油", idea[key]])
        toadd.append(["菜油", idea[key]])
        toadd.append(["棕榈油", idea[key]])

for i in topop:
    idea.pop(i)
for i in toadd:
    idea[i[0]] = i[1]

haitong_idea = idea

for i in idea:
    print(i)
    print(idea[i])
