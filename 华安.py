#coding=gb2312

import keywords
with open('����.txt',encoding='gbk') as f:
    lines = f.readlines()
idea = {}
items = ["��ָ","����ָ����ŷ�ߣ�","�ƽ�","ͭ","��","̼���","˫��","����","����","�����","����","�ֲ�","����","PVC","ֽ��","��֬","����","����","����",
         "�޻�"]
next = False
prev_item = ""
for l in lines:
    stripped = l.strip().strip('\n')
    if stripped == "":
        continue
    if stripped in items:
        next = True
        prev_item = stripped.split("��")[0]
        continue
    if next:
        if prev_item in idea:
            idea[prev_item] += l.strip().strip('\n')
        else:
            idea[prev_item] = l.strip().strip('\n')
huaan_old = {}
for i in idea:
    huaan_old[i] = idea[i][:]

topop = []
toadd = []
for key in idea:
    if key == "����ָ����ŷ�ߣ�":
        topop.append("����ָ����ŷ�ߣ�")
        toadd.append(["����", idea[key]])
    if key == "˫��":
        topop.append("˫��")
        toadd.append(["��ú", idea[key]])
        toadd.append(["��̿", idea[key]])
    if key == "����":
        topop.append("����")
        toadd.append(["��", idea[key]])
    if key == "�ֲ�":
        topop.append("�ֲ�")
        toadd.append(["����", idea[key]])
        toadd.append(["�Ⱦ�", idea[key]])
    if key == "��֬":
        topop.append("��֬")
        toadd.append(["�����", idea[key]])
        toadd.append(["����", idea[key]])
        toadd.append(["����", idea[key]])

for i in topop:
    idea.pop(i)
for i in toadd:
    idea[i[0]] = i[1]

huaan_old = {}
for i in idea:
    huaan_old[i] = idea[i][:]

for key in idea:
    if not idea[key].isdecimal():
        idea[key] = keywords.simplify_sent(idea[key])


for i in huaan_old:
    if i in idea:
        huaan_old[i] = idea[i] + " ���� " + huaan_old[i]
    else:
        huaan_old[i] = ""

huaan_idea = idea
for i in idea:
    print(i)
    print(idea[i])
    print(huaan_old[i])
