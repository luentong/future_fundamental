import keywords

with open('国都期货.txt',encoding='utf-8') as f:
    lines = f.readlines()
idea = {}
items = ["图片豆粕","豆粕","PTA","涤纶短纤","橡胶","棉花","豆类","橡胶","油脂","白糖","玉米、淀粉","生猪"]
next = False
prev_item = ""
for l in lines:
    stripped = l.strip()
    print(stripped)
    if stripped == "":
        continue
    if stripped == "国都期货研究所":
        break
    if stripped in items:
        next = True
        prev_item = stripped
        continue
    if next:
        if prev_item.strip("：") in idea:
            idea[prev_item.strip()] += l.strip().strip('\n')
        else:
            idea[prev_item.strip()] = l.strip().strip('\n')

guodu_old = {}
for i in idea:
    guodu_old[i] = idea[i][:]

for i in guodu_old:
    print(i)
    print(guodu_old[i])

topop = []
toadd = []
for key in idea:
    if not idea[key].isdecimal():
        idea[key] = keywords.simplify_sent(idea[key])
    if key == "图片豆粕":
        topop.append("图片豆粕")
        toadd.append(["豆粕", idea[key]])
    if key == "涤纶短纤":
        topop.append("涤纶短纤")
        toadd.append(["短纤", idea[key]])
    if key == "油脂":
        topop.append("油脂")
        toadd.append(["豆油", idea[key]])
        toadd.append(["菜油", idea[key]])
        toadd.append(["棕榈油", idea[key]])
    if key == "豆类":
        topop.append("豆类")
        toadd.append(["豆粕", idea[key]])
        toadd.append(["菜粕", idea[key]])
    if key == "玉米、淀粉":
        topop.append("玉米、淀粉")
        toadd.append(["玉米", idea[key]])
        toadd.append(["淀粉", idea[key]])

for i in topop:
    idea.pop(i)
for i in toadd:
    idea[i[0]] = i[1]

guodu_idea = idea