import keywords

with open('国泰君安.txt') as f:
    lines = f.readlines()
idea = {}
for l in lines:
    if ':' in l:
        idea[l.split(":")[0]] = l.split(":")[1].strip('\n')
    if '：' in l:
        idea[l.split("：")[0]] = l.split("：")[1].strip('\n')

guotai_old = {}
for i in idea:
    guotai_old[i] = idea[i][:]

topop = []
toadd = []
for key in idea:
    if not idea[key].isdecimal():
        idea[key] = keywords.simplify_sent(idea[key])
    if key == "铁矿石":
        topop.append("铁矿石")
        toadd.append(["铁矿", idea[key]])
    if key == "螺纹钢":
        topop.append("螺纹钢")
        toadd.append(["螺纹", idea[key]])
    if key == "热轧卷板":
        topop.append("热轧卷板")
        toadd.append(["热卷", idea[key]])
    if key == "玉米":
        toadd.append(["淀粉", idea[key]])
    if key == "LLDPE":
        topop.append("LLDPE")
        toadd.append(["塑料", idea[key]])
    if key == "燃料油":
        topop.append("燃料油")
        toadd.append(["燃油", idea[key]])
    if key == "豆粕":
        toadd.append(["菜粕", idea[key]])
    if key == "乙二醇":
        topop.append("乙二醇")
        toadd.append(["MEG", idea[key]])

for i in topop:
    idea.pop(i)
for i in toadd:
    idea[i[0]] = i[1]

print(idea)
guotai_idea = idea



for key in idea:
    print(key)
    print(idea[key])