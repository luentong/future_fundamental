import keywords

with open('东兴.txt',encoding='utf-8') as f:
    lines = f.readlines()
idea = {}
items = ["期指","期债","动力煤","铜","PTA","PVC","天然橡胶","生猪","玉米"]
next = False
prev_item = ""
for l in lines:
    stripped = l.strip()
    if stripped == "":
        continue
    if stripped.split("：")[0] in items:
        next = True
        prev_item = stripped.split("：")[0]
        continue
    if next:
        if prev_item.strip("：") in idea:
            idea[prev_item.strip()] += l.strip().strip('\n')
        else:
            idea[prev_item.strip()] = l.strip().strip('\n')

topop = []
toadd = []
for key in idea:
    if key == "期指":
        topop.append("期指")
        toadd.append(["股指", idea[key]])
    if key == "期债":
        topop.append("期债")
        toadd.append(["国债", idea[key]])
    if key == "天然橡胶":
        topop.append("天然橡胶")
        toadd.append(["橡胶", idea[key]])


for i in topop:
    idea.pop(i)
for i in toadd:
    idea[i[0]] = i[1]

yongan_old = {}
for i in idea:
    yongan_old[i] = idea[i][:]

for key in idea:
    if not idea[key].isdecimal():
        idea[key] = keywords.simplify_sent(idea[key])


for i in yongan_old:
    if i in idea:
        yongan_old[i] = idea[i] + " 永安 " + yongan_old[i]
    else:
        yongan_old[i] = ""

yongan_idea = idea
for i in idea:
    print(i)
    print(idea[i])