import keywords
with open('东吴.txt',encoding='utf-8') as f:
    lines = f.readlines()
idea = {}
items = ["螺卷","铁矿","双焦","双硅","原油","沥青","LPG","甲醇","PVC","天然橡胶",
         "沪铜","沪铝","沪锌","沪铅","油脂","豆粕/菜粕","玉米","白糖","鸡蛋",
         "生猪","苹果","红枣","花生"]
next = False
prev_item = ""
for l in lines:
    stripped = l.strip().strip('\n').strip('【').strip('】').strip("：")
    if stripped == "":
        continue
    if stripped in items:
        next = True
        prev_item = stripped
        continue
    if l.startswith('银河期货') and stripped not in items:
        next = False
        continue
    if next:
        if prev_item in idea:
            idea[prev_item] += l.strip().strip('\n')
        else:
            idea[prev_item] = l.strip().strip('\n')
dongwu_old = {}
for i in idea:
    dongwu_old[i] = idea[i][:]

topop = []
toadd = []
for key in idea:
    if key == "螺卷":
        topop.append("螺卷")
        toadd.append(["螺纹", idea[key]])
        toadd.append(["热卷", idea[key]])
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

dongwu_old = {}
for i in idea:
    dongwu_old[i] = idea[i][:]

for key in idea:
    if not idea[key].isdecimal():
        idea[key] = keywords.simplify_sent(idea[key])


for i in dongwu_old:
    if i in idea:
        dongwu_old[i] = idea[i] + " 东吴 " + dongwu_old[i]
    else:
        dongwu_old[i] = ""

dongwu_idea = idea
for i in idea:
    print(i)
    print(idea[i])