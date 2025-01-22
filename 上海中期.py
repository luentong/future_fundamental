import keywords

with open('上海中期.txt',encoding='utf-8') as f:
    lines = f.readlines()
idea = {}
items = ["贵金属","铜(CU)","螺纹(RB)","热卷(HC)","铝(AL)","锌(ZN)","铅(PB)","镍(NI)","不锈钢(SS)","铁矿石(I)",
         "天胶及20号胶","原油(SC)","燃油(FU)","乙二醇(EG)","PVC(V)","沥青(BU)","塑料(L)","聚丙烯(PP)","PTA(TA)","苯乙烯(EB)","焦炭(J)","焦煤(JM)","动力煤(TC)","甲醇(ME)","尿素(UR)",
         "玻璃(FG)","白糖(SR)","大豆(A)","豆粕(M)","豆油(Y)","棕榈油(P)","菜籽类","鸡蛋(JD)","苹果(AP)","生猪(LH)","花生(PK)","棉花及棉纱"]
next = False
prev_item = ""
for l in lines:
    if "：" in l and len(l) <= 50:
        idea[l.split('：')[0]] = l.split('：')[1]

zhongqi_old = {}
for i in idea:
    zhongqi_old[i] = idea[i][:]

topop = []
toadd = []
for key in idea:
    if not idea[key].isdecimal():
        idea[key] = keywords.simplify_sent(idea[key])
    if key == "铜及国际铜":
        topop.append("铜及国际铜")
        toadd.append(["铜", idea[key]])
        toadd.append(["国际铜", idea[key]])
    if key == "铁矿石":
        topop.append("铁矿石")
        toadd.append(["铁矿", idea[key]])
    if key == "燃油及低硫燃油":
        topop.append("燃油及低硫燃油")
        toadd.append(["燃油", idea[key]])
        toadd.append(["低硫燃油", idea[key]])
    if key == "天然橡胶":
        topop.append("天然橡胶")
        toadd.append(["橡胶", idea[key]])
    if key == "乙二醇":
        topop.append("乙二醇")
        toadd.append(["MEG", idea[key]])
    if key == "聚丙烯":
        topop.append("聚丙烯")
        toadd.append(["PP", idea[key]])
    if key == "棉花及棉纱":
        topop.append("棉花及棉纱")
        toadd.append(["棉花", idea[key]])
        toadd.append(["棉纱", idea[key]])
    if key == "玉米及玉米淀粉":
        topop.append("玉米及玉米淀粉")
        toadd.append(["玉米", idea[key]])
        toadd.append(["淀粉", idea[key]])
    if key == "大豆":
        topop.append("大豆")
        toadd.append(["豆一", idea[key]])
    if key == "菜籽类":
        topop.append("菜籽类")
        toadd.append(["菜粕", idea[key]])
    if key == "贵金属":
        topop.append("贵金属")
        toadd.append(["黄金", idea[key]])
        toadd.append(["白银", idea[key]])



for i in topop:
    idea.pop(i)
for i in toadd:
    idea[i[0]] = i[1]

zhongqi_idea = idea


for key in idea:
    print(key)
    print(idea[key])