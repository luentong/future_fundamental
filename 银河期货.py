import keywords

with open('银河期货.txt',encoding='utf-8') as f:
    lines = f.readlines()
idea = {}
items = ["铁矿","钢材","焦煤焦炭","镍及不锈钢","铜","锌","铝","沥青","原油","燃料油","纸浆","天然橡胶及20号胶","甲醇","尿素","动力煤","PTA","PF","MEG","EB","PP","塑料","PVC"]
next = False
prev_item = ""
for l in lines:
    stripped = l.strip().strip('\n').strip('【').strip('】')
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
yinhe_old = {}
for i in idea:
    yinhe_old[i] = idea[i][:]
for i in yinhe_old:
    print(i)
    print(yinhe_old[i])

topop = []
toadd = []
for key in idea:
    if not idea[key].isdecimal():
        idea[key] = keywords.simplify_sent(idea[key])
    if key == "焦煤焦炭":
        topop.append("焦煤焦炭")
        toadd.append(["焦煤", idea[key]])
        toadd.append(["焦炭", idea[key]])
    if key == "镍及不锈钢":
        topop.append("镍及不锈钢")
        toadd.append(["镍", idea[key]])
        toadd.append(["不锈钢", idea[key]])
    if key == "燃料油":
        topop.append("燃料油")
        toadd.append(["燃油", idea[key]])
    if key == "天然橡胶及20号胶":
        topop.append("天然橡胶及20号胶")
        toadd.append(["橡胶", idea[key]])
    if key == "PF":
        topop.append("PF")
        toadd.append(["短纤", idea[key]])
    if key == "EB":
        topop.append("EB")
        toadd.append(["苯乙烯", idea[key]])



for i in topop:
    idea.pop(i)
for i in toadd:
    idea[i[0]] = i[1]

yinhe_idea = idea
for key in idea:
    print(key)
    print(idea[key])