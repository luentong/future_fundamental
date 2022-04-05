import keywords

with open('鲁证期货.txt',encoding='utf-8') as f:
    lines = f.readlines()
idea = {}
items = ["棉花","白糖","油脂油料","鸡蛋","苹果","玉米系","红枣","花生","生猪","原油","塑料","橡胶","甲醇","纯碱","PVC","聚酯产业链","纸浆","尿素","铜","铝","镍","不锈钢","贵金属","螺矿","煤焦","铁合金"]
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
    if key == "油脂油料":
        topop.append("油脂油料")
        toadd.append(["豆油", idea[key]])
        toadd.append(["菜油", idea[key]])
        toadd.append(["棕榈油", idea[key]])
    if key == "玉米系":
        topop.append("玉米系")
        toadd.append(["玉米", idea[key]])
        toadd.append(["淀粉", idea[key]])
    if key == "聚酯产业链":
        topop.append("聚酯产业链")
        toadd.append(["PTA", idea[key]])
        toadd.append(["短纤", idea[key]])
    if key == "贵金属":
        topop.append("贵金属")
        toadd.append(["黄金", idea[key]])
        toadd.append(["白银", idea[key]])
    if key == "螺矿":
        topop.append("螺矿")
        toadd.append(["螺纹", idea[key]])
        toadd.append(["热卷", idea[key]])
        toadd.append(["铁矿", idea[key]])
    if key == "铁合金":
        topop.append("铁合金")
        toadd.append(["锰硅", idea[key]])
        toadd.append(["硅铁", idea[key]])
    if key == "煤焦":
        topop.append("煤焦")
        toadd.append(["焦煤", idea[key]])
        toadd.append(["焦炭", idea[key]])
for i in topop:
    idea.pop(i)
for i in toadd:
    idea[i[0]] = i[1]

guodu_idea = idea

for i in idea:
    print(i)
    print(idea[i])
