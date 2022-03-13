import keywords

with open('南华.txt',encoding='utf-8') as f:
    lines = f.readlines()
idea = {}
items = ["螺纹","热卷","铁矿","焦煤","动力煤","纯碱","玻璃","白糖","棉花","红枣","油料","油脂","原油","甲醇","燃料油","PVC","聚酯","沥青",
         "PTA","MEG","PF","LPG","纸浆","橡胶","铜","铝","锌","镍不锈钢","锡","贵金属"]
next = False
prev_item = ""
for l in lines:
    stripped = l.strip()
    print(stripped)
    if stripped == "":
        continue
    if "：" in stripped and stripped.split("：")[0] in items:
        next = True
        prev_item = stripped.split("：")[0]
        idea[prev_item] = stripped.split("：")[1]
        continue
    if ":" in stripped and stripped.split(":")[0] in items:
        next = True
        prev_item = stripped.split(":")[0]
        idea[prev_item] = stripped.split(":")[1]
        continue
    if next:
        if prev_item in idea:
            idea[prev_item] += l.strip().strip('\n')
        else:
            idea[prev_item] = l.strip().strip('\n')

haitong_old = {}
for i in idea:
    haitong_old[i] = idea[i][:]

topop = []
toadd = []
for key in idea:
    if not idea[key].isdecimal():
        idea[key] = keywords.simplify_sent(idea[key])
    if key == "油脂":
        topop.append("油脂")
        toadd.append(["豆油", idea[key]])
        toadd.append(["菜油", idea[key]])
        toadd.append(["棕榈油", idea[key]])
    if key == "油料":
        topop.append("油料")
        toadd.append(["豆粕", idea[key]])
        toadd.append(["菜粕", idea[key]])
    if key == "燃料油":
        topop.append("燃料油")
        toadd.append(["燃油", idea[key]])
    if key == "聚烯烃":
        topop.append("聚烯烃")
        toadd.append(["PP", idea[key]])
        toadd.append(["塑料", idea[key]])
    if key == "PF":
        topop.append("PF")
        toadd.append(["短纤", idea[key]])
    if key == "贵金属":
        topop.append("贵金属")
        toadd.append(["白银", idea[key]])
        toadd.append(["黄金", idea[key]])
    if key == "镍不锈钢":
        topop.append("镍不锈钢")
        toadd.append(["镍", idea[key]])
        toadd.append(["不锈钢", idea[key]])


for i in topop:
    idea.pop(i)
for i in toadd:
    idea[i[0]] = i[1]

haitong_idea = idea

for i in idea:
    print(i)
    print(idea[i])
