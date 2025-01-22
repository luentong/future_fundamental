#coding=gb2312

import keywords
with open('��ͨ.txt',encoding='gbk') as f:
    lines = f.readlines()
idea = {}
items = ["��ָ","����ָ����ŷ�ߣ�","�ƽ�","ͭ","��","̼���","˫��","����","����","����","�ֲ�","����","PVC","ֽ��","����",
         "����","����","�޻�","��ծ","��̿","�״�","�����","��֬","��װ���˼�"]
next = False
prev_item = ""
for l in lines:
    stripped = l.strip().strip('\n')
    if stripped == "":
        continue
    if "��" in stripped and stripped.split("��")[0] in items:
        next = True
        prev_item = stripped.split("��")[0]
        idea[prev_item] = stripped.split("��")[1]
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
    if key == "��װ���˼�":
        topop.append("��װ���˼�")
        toadd.append(["����", idea[key]])
    if key == "��̿":
        toadd.append(["��ú", idea[key]])
    if key == "��֬":
        topop.append("��֬")
        toadd.append(["�����", idea[key]])
        toadd.append(["����", idea[key]])
        toadd.append(["����", idea[key]])
    if key == "�ֲ�":
        topop.append("�ֲ�")
        toadd.append(["����", idea[key]])
        toadd.append(["�Ⱦ�", idea[key]])

for i in topop:
    idea.pop(i)
for i in toadd:
    idea[i[0]] = i[1]

haitong_old = {}
for i in idea:
    haitong_old[i] = idea[i][:]

for key in idea:
    if not idea[key].isdecimal():
        idea[key] = keywords.simplify_sent(idea[key])


for i in haitong_old:
    if i in idea:
        haitong_old[i] = idea[i] + " ���� " + haitong_old[i]
    else:
        haitong_old[i] = ""

haitong_idea = idea
for i in idea:
    print(i)
    print(idea[i])
    print(haitong_old[i])
