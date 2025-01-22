import keywords

with open('东证.txt',encoding='utf-8') as f:
    lines = f.readlines()
total = ""
for l in lines:
    total += l
idea = {}
items = ["贵金属（黄金）","黑色金属（焦煤/焦炭）","黑色金属（螺纹钢/热轧卷板）","有色金属（镍）","有色金属（铝）","农产品（棉花）","农产品（豆粕）","航运指数（集装箱运价）"]
index = 0
for i in items[:-1]:
    after = total.split(i)[1]
    comment = after.split("投资建议：")[1]
    final = comment.split(items[index + 1])[0]
    idea[i.split("（")[1].split("）")[0]] = final
    index += 1
    total = after



for i in idea:
    print(i)
    print(idea[i])

haitong_old = {}
for i in idea:
    haitong_old[i] = idea[i][:]

topop = []
toadd = []
for key in idea:
    if not idea[key].isdecimal():
        idea[key] = keywords.simplify_sent(idea[key])
    if key == "黄金":
        toadd.append(["白银", idea[key]])
    if key == "焦煤/焦炭":
        topop.append("焦煤/焦炭")
        toadd.append(["焦煤", idea[key]])
        toadd.append(["焦炭", idea[key]])
    if key == "螺纹钢/热轧卷板":
        topop.append("螺纹钢/热轧卷板")
        toadd.append(["螺纹", idea[key]])
        toadd.append(["热卷", idea[key]])


for i in topop:
    idea.pop(i)
for i in toadd:
    idea[i[0]] = i[1]

haitong_idea = idea

for i in idea:
    print(i)
    print(idea[i])
