import keywords

with open('广州期货.txt',encoding='utf-8') as f:
    lines = f.readlines()
idea = {}
items = ["原油","沥青","铜","郑棉","螺纹钢","焦炭","铝","锌","焦煤","镍","不锈钢","动力煤","纯碱","玻璃","生猪","豆粕"]
next = False
prev_item = ""
for l in lines:
    if "：" in l and len(l) <= 30:
        idea[l.split('：')[0]] = l.split('：')[1]

guangzhou_old = {}
for i in idea:
    guangzhou_old[i] = idea[i][:]

topop = []
toadd = []
for key in idea:
    if not idea[key].isdecimal():
        idea[key] = keywords.simplify_sent(idea[key])
    if key == "郑棉":
        topop.append("郑棉")
        toadd.append(["棉花", idea[key]])
    if key == "螺纹钢":
        topop.append("螺纹钢")
        toadd.append(["螺纹", idea[key]])
        toadd.append(["热卷", idea[key]])
    if key == "钢材":
        topop.append("钢材")
        toadd.append(["螺纹", idea[key]])
        toadd.append(["热卷", idea[key]])
    if key == "猪":
        topop.append("猪")
        toadd.append(["生猪", idea[key]])
    if key == "铁矿石":
        topop.append("铁矿石")
        toadd.append(["铁矿", idea[key]])
    if key == "液化气":
        topop.append("液化气")
        toadd.append(["LPG", idea[key]])



for i in topop:
    idea.pop(i)
for i in toadd:
    idea[i[0]] = i[1]

guangzhou_idea = idea


for key in idea:
    print(key)
    print(idea[key])