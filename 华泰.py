import keywords
with open('��̩.txt',encoding='utf-8') as f:
    lines = f.readlines()
idea = {}
items = ["��ָ�ڻ�","����","��ծ�ڻ�","ԭ��","ԭ��","ȼ����","Һ��ʯ����","ʯ������","PX��PTA��PF","�״�",
         "��ϩ��","EG","EB","����","��Ȼ����ϳ���","�ȼ�","PVC","�ռ�","�����",
         "ͭ","п","�������","��","Ǧ","��ҵ��","̼���","�ֲ�","����","˫��","��������","˫��",
         "��֬","�󶹹۵�","�����۵�","����۵�","���׹۵�","����۵�","�����۵�","ƻ���۵�","����۵�","�޻��۵�","ֽ���۵�","���ǹ۵�"]
next = False
prev_item = ""
for l in lines:
    stripped = l.strip().strip('\n')
    if stripped == "":
        continue
    if stripped in items:
        next = True
        prev_item = stripped
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
    if key == "��Ȼ��":
        topop.append("��Ȼ��")
        toadd.append(["��", idea[key]])
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