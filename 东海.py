#coding=gb2312

import keywords
with open('����.txt',encoding='gbk') as f:
    lines = f.readlines()
idea = {}
items = ["��ָ","�ֲ�","����ʯ","��̿/��ú","����/����","ͭ","��","̼���","��","п","��/��","ԭ��","����","PTA",
         "�Ҷ���","�״�","�۱�ϩ","����","����","������","������","�����","����","����","�޻�"]
next = False
prev_item = ""
for l in lines:
    stripped = l.strip().strip('\n')
    if stripped == "":
        continue
    if "��" in stripped and "��" in stripped and stripped.split("��")[0].split("��")[1] in items:
        next = True
        prev_item = stripped.split("��")[0]
        idea[prev_item] = stripped.split("��")[1]
        continue
    if next:
        if prev_item in idea:
            idea[prev_item] += l.strip().strip('\n')
        else:
            idea[prev_item] = l.strip().strip('\n')
donghai_old = {}
for i in idea:
    donghai_old[i] = idea[i][:]

topop = []
toadd = []
for key in idea:
    if key == "������":
        toadd.append(["����", idea[key]])
        toadd.append(["����", idea[key]])
    if key == "������":
        toadd.append(["����", idea[key]])
    if key == "����":
        toadd.append(["��һ", idea[key]])
    if key == "�۱�ϩ":
        toadd.append(["PP", idea[key]])
    if key == "��̿/��ú":
        topop.append("��̿/��ú")
        toadd.append(["��ú", idea[key]])
        toadd.append(["��̿", idea[key]])
    if key == "����/����":
        topop.append("����/����")
        toadd.append(["����", idea[key]])
        toadd.append(["�̹�", idea[key]])
    if key == "��/��":
        topop.append("��/��")
        toadd.append(["�ƽ�", idea[key]])
        toadd.append(["����", idea[key]])
    if key == "����ʯ":
        toadd.append(["����", idea[key]])
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

donghai_old = {}
for i in idea:
    donghai_old[i] = idea[i][:]

for key in idea:
    if not idea[key].isdecimal():
        idea[key] = keywords.simplify_sent(idea[key])


for i in donghai_old:
    if i in idea:
        donghai_old[i] = idea[i] + " ���� " + donghai_old[i]
    else:
        donghai_old[i] = ""

donghai_idea = idea
for i in idea:
    print(i)
    print(idea[i])
    print(donghai_old[i])
