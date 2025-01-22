#coding=gb2312

import keywords
with open('��̩.txt',encoding='gbk') as f:
    lines = f.readlines()
idea = {}
items = ["��ָ�ڻ�","����","��ծ�ڻ�","ԭ��","ȼ����","Һ��ʯ����","ʯ������","PX��PTA��PF","�״�","����","����","����","����","����","ƻ��","����","�޻�","ֽ��","����",
         "��ϩ��","EG","EB","����","��Ȼ��","�ȼ�","PVC","�ռ�","�����","˳����","�����","�������","�ֲ�",
         "ͭ","п","�������","��","Ǧ","��ҵ��","̼���","�ֲ�","����","˫��","��������","˫��","����","��","����",
         "��֬","�󶹹۵�","�����۵�","����۵�","���׹۵�","����۵�","�����۵�","ƻ���۵�","����۵�","�޻��۵�","ֽ���۵�","���ǹ۵�"]
next = False
prev_item = ""
for l in lines:
    stripped = l.strip().strip('\n')
    if stripped == "":
        continue
    if "��" in stripped and stripped.split("��")[0] in items:
        next = True
        prev_item = stripped.split("��")[0]
        continue
    if "�۵�" in stripped and stripped.split("�۵�")[0] in items:
        next = True
        prev_item = stripped.split("�۵�")[0]
        continue
    if l.startswith('�����ڻ�') and stripped not in items:
        next = False
        continue
    if next:
        if prev_item in idea:
            idea[prev_item] += l.strip().strip('\n')
        else:
            idea[prev_item] = l.strip().strip('\n')
huatai_old = {}
for i in idea:
    huatai_old[i] = idea[i][:]

topop = []
toadd = []
for key in idea:
    if key == "����":
        topop.append("����")
        toadd.append(["����", idea[key]])
    if key == "��":
        topop.append("��")
        toadd.append(["��һ", idea[key]])
    if key == "��������":
        topop.append("��������")
        toadd.append(["����", idea[key]])
        toadd.append(["����", idea[key]])
    if key == "�ֲ�":
        topop.append("�ֲ�")
        toadd.append(["����", idea[key]])
        toadd.append(["�Ⱦ�", idea[key]])
    if key == "�������":
        topop.append("�������")
        toadd.append(["��", idea[key]])
        toadd.append(["�����", idea[key]])
    if key == "�����":
        topop.append("�����")
        toadd.append(["�ƽ�", idea[key]])
        toadd.append(["����", idea[key]])
    if key == "˳����":
        topop.append("˳����")
        toadd.append(["�ϳ���", idea[key]])
    if key == "��Ȼ��":
        topop.append("��Ȼ��")
        toadd.append(["��", idea[key]])
    if key == "EG":
        topop.append("EG")
        toadd.append(["MEG", idea[key]])
    if key == "EB":
        topop.append("EB")
        toadd.append(["����ϩ", idea[key]])
    if key == "��ϩ��":
        topop.append("��ϩ��")
        toadd.append(["PP", idea[key]])
        toadd.append(["����", idea[key]])
    if key == "����":
        topop.append("����")
        toadd.append(["����", idea[key]])
    if key == "PX��PTA��PF":
        topop.append("PX��PTA��PF")
        toadd.append(["PX", idea[key]])
        toadd.append(["PTA", idea[key]])
        toadd.append(["����", idea[key]])
    if key == "ʯ������":
        topop.append("ʯ������")
        toadd.append(["����", idea[key]])
    if key == "Һ��ʯ����":
        topop.append("Һ��ʯ����")
        toadd.append(["LPG", idea[key]])
    if key == "ȼ����":
        topop.append("ȼ����")
        toadd.append(["ȼ��", idea[key]])
    if key == "��ծ�ڻ�":
        topop.append("��ծ�ڻ�")
        toadd.append(["��ծ", idea[key]])
    if key == "��ָ�ڻ�":
        topop.append("��ָ�ڻ�")
        toadd.append(["��ָ", idea[key]])
    if key == "˫��":
        topop.append("˫��")
        toadd.append(["��ú", idea[key]])
        toadd.append(["��̿", idea[key]])
    if key == "˫��":
        topop.append("˫��")
        toadd.append(["����", idea[key]])
        toadd.append(["�̹�", idea[key]])
    if key == "��ͭ":
        topop.append("��ͭ")
        toadd.append(["ͭ", idea[key]])
    if key == "����":
        topop.append("����")
        toadd.append(["��", idea[key]])
    if key == "��п":
        topop.append("��п")
        toadd.append(["п", idea[key]])
    if key == "��Ǧ":
        topop.append("��Ǧ")
        toadd.append(["Ǧ", idea[key]])
    if key == "��֬":
        topop.append("��֬")
        toadd.append(["�����", idea[key]])
        toadd.append(["����", idea[key]])
        toadd.append(["����", idea[key]])
    if key == "����/����":
        topop.append("����/����")
        toadd.append(["����", idea[key]])
        toadd.append(["����", idea[key]])

for i in topop:
    idea.pop(i)
for i in toadd:
    idea[i[0]] = i[1]

huatai_old = {}
for i in idea:
    huatai_old[i] = idea[i][:]

for key in idea:
    if not idea[key].isdecimal():
        idea[key] = keywords.simplify_sent(idea[key])


for i in huatai_old:
    if i in idea:
        huatai_old[i] = idea[i] + " ��̩ " + huatai_old[i]
    else:
        huatai_old[i] = ""

huatai_idea = idea
for i in idea:
    print(i)
    print(idea[i])
    print(huatai_old[i])