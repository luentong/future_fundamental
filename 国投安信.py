import keywords
with open('国投安信.txt', encoding='utf-8') as f:
    lines = f.readlines()
idea = {}
prev = ""
for l in lines:
    if "【" in l and len(l) < 20:
        a1 = l.replace("【", "")
        a2 = a1.replace("】", "")
        a3 = a2.replace("\n", "")
        prev = a3
    elif l.strip("\n") != "":
        a4 = l.replace("\n", "")
        idea[prev] = a4

guotou_old = {}
for i in idea:
    guotou_old[i] = idea[i][:]

topop = []
toadd = []
for key in idea:
    if not idea[key].isdecimal():
        idea[key] = keywords.simplify_sent(idea[key])
    if key == "贵金属":
        topop.append("贵金属")
        toadd.append(["黄金", idea[key]])
        toadd.append(["白银", idea[key]])
    if key == "螺纹&热卷":
        topop.append("螺纹&热卷")
        toadd.append(["螺纹", idea[key]])
        toadd.append(["热卷", idea[key]])
    if key == "燃料油":
        topop.append("燃料油")
        toadd.append(["燃油", idea[key]])
    if key == "液化石油气":
        topop.append("液化石油气")
        toadd.append(["LPG", idea[key]])
    if key == "聚丙烯&塑料":
        topop.append("聚丙烯&塑料")
        toadd.append(["塑料", idea[key]])
        toadd.append(["PP", idea[key]])
    if key == "天然橡胶":
        topop.append("天然橡胶")
        toadd.append(["橡胶", idea[key]])
    if key == "棕榈油&豆油":
        topop.append("棕榈油&豆油")
        toadd.append(["棕榈油", idea[key]])
        toadd.append(["豆油", idea[key]])
    if key == "乙二醇":
        topop.append("乙二醇")
        toadd.append(["MEG", idea[key]])
    # # 菜粕菜油自己改
    if key == "菜粕&菜油":
        topop.append("菜粕&菜油")
        toadd.append(["菜粕", "0"])
        toadd.append(["菜油", "0.3"])
    # # 玻璃纯碱自己改
    # if key == "纯碱":
    #     topop.append("纯碱")
    #     toadd.append(["纯碱", "1"])
    # if key == "玻璃":
    #     topop.append("玻璃")
    #     toadd.append(["玻璃", "0"])
    # if key == "塑料":
    #     topop.append("塑料")
    #     toadd.append(["塑料", "0"])
    # if key == "PP":
    #     topop.append("PP")
    #     toadd.append(["PP", "-0.7"])

for i in topop:
    idea.pop(i)
for i in toadd:
    idea[i[0]] = i[1]

idea.pop("股指")
print(idea)
anxin_idea = idea

for key in idea:
    print(key)
    print(idea[key])