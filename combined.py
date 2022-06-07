import keywords
###########################################中信开始

with open('中信.txt',encoding='utf8') as f:
    lines = f.readlines()
if not lines:
    zhongxin_old = {}
    citrix_idea = {}
else:
    line = lines[0]
    keyword = ["黄金/白银", "黑色", "钢材", "铁矿", "焦炭", "焦煤", "动力煤", "有色", "铜", "铝", "锌", "铅", "镍", "不锈钢", "锡", "能源", "原油", "沥青",
               "燃料油", "低硫燃料油",
               "LPG", "化工", "甲醇", "尿素", "乙二醇", "PTA", "短纤", "PP", "塑料", "苯乙烯",
               "PVC", "软商品", "橡胶", "纸浆", "棉花", "白糖", "农产品", "油脂", "蛋白粕", "玉米/淀粉", "生猪", "鸡蛋", "玻璃"]
    indexes = [0, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 22, 23, 24, 25, 26, 27, 28, 29, 30, 32, 33,
               34, 35, 37, 38, 39, 40, 41]
    idea = {}
    for l in lines:
        if " "  in l and len(l.split(" ")[0]) < 7:
            idea[l.split(" ")[0]] = l.split(" ")[1]

    topop = []
    toadd = []
    for key in idea:
        if key == "黄金/白银":
            topop.append("黄金/白银")
            toadd.append(["黄金", idea[key]])
            toadd.append(["白银", idea[key]])
        if key == "钢材":
            topop.append("钢材")
            toadd.append(["热卷", idea[key]])
            toadd.append(["螺纹", idea[key]])
        if key == "低硫燃料油":
            topop.append("低硫燃料油")
            toadd.append(["低硫燃油", idea[key]])
        if key == "玉米/淀粉":
            topop.append("玉米/淀粉")
            toadd.append(["玉米", idea[key]])
            toadd.append(["淀粉", idea[key]])
        if key == "燃料油":
            topop.append("燃料油")
            toadd.append(["燃油", idea[key]])
        if key == "油脂":
            topop.append("油脂")
            toadd.append(["豆油", idea[key]])
            toadd.append(["菜油", idea[key]])
            toadd.append(["棕榈油", idea[key]])
        if key == "蛋白粕":
            topop.append("蛋白粕")
            toadd.append(["豆粕", idea[key]])
            toadd.append(["菜粕", idea[key]])
        if key == "乙二醇":
            topop.append("乙二醇")
            toadd.append(["MEG", idea[key]])

    for i in topop:
        idea.pop(i)
    for i in toadd:
        idea[i[0]] = i[1]

    zhongxin_old = {}
    for i in idea:
        zhongxin_old[i] = idea[i][:]


    for key in idea:
        if not idea[key].isdecimal():
            idea[key] = keywords.simplify_sent(idea[key])

    for i in zhongxin_old:
        if i in idea:
            zhongxin_old[i] = idea[i] + " 中信 " + zhongxin_old[i]
        else:
            zhongxin_old[i] = ""
    citrix_idea = idea

###########################################国泰开始

with open('国泰君安.txt',encoding='utf8') as f:
    lines = f.readlines()
idea = {}
for l in lines:
    if ':' in l:
        idea[l.split(":")[0]] = l.split(":")[1].strip('\n')
    if '：' in l:
        idea[l.split("：")[0]] = l.split("：")[1].strip('\n')

topop = []
toadd = []
for key in idea:
    if key == "铁矿石":
        topop.append("铁矿石")
        toadd.append(["铁矿", idea[key]])
    if key == "螺纹钢":
        topop.append("螺纹钢")
        toadd.append(["螺纹", idea[key]])
    if key == "期指":
        topop.append("期指")
        toadd.append(["股指", idea[key]])
    if key == "期债":
        topop.append("期债")
        toadd.append(["国债", idea[key]])
    if key == "热轧卷板":
        topop.append("热轧卷板")
        toadd.append(["热卷", idea[key]])
    if key == "玉米":
        toadd.append(["淀粉", idea[key]])
    if key == "LLDPE":
        topop.append("LLDPE")
        toadd.append(["塑料", idea[key]])
    if key == "低硫燃料油":
        topop.append("低硫燃料油")
        toadd.append(["低硫燃油", idea[key]])
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

guotai_old = {}
for i in idea:
    guotai_old[i] = idea[i][:]

for key in idea:
    if not idea[key].isdecimal():
        idea[key] = keywords.simplify_sent(idea[key])

for i in guotai_old:
    if i in idea:
        guotai_old[i] = idea[i] + " 国泰  " + guotai_old[i]
    else:
        guotai_old[i] = ""
guotai_idea = idea

###########################################国投安信开始
with open('国投安信.txt',encoding='utf8' ) as f:
    lines = f.readlines()
idea = {}
prev = ""
for l in lines:
    if "【" in l and len(l) < 20:
        a1 = l.replace("【", "")
        a2 = a1.replace("】", "")
        a3 = a2.replace("\n", "")
        prev = a3
    elif l.strip("\n") != "":
        a4 = l.replace("\n", "")
        idea[prev] = a4


topop = []
toadd = []
for key in idea:
    if key == "贵金属":
        topop.append("贵金属")
        toadd.append(["黄金", idea[key]])
        toadd.append(["白银", idea[key]])
    if key == "螺纹&热卷":
        topop.append("螺纹&热卷")
        toadd.append(["螺纹", idea[key]])
        toadd.append(["热卷", idea[key]])
    if key == "燃料油":
        topop.append("燃料油")
        toadd.append(["燃油", idea[key]])
    if key == "液化石油气":
        topop.append("液化石油气")
        toadd.append(["LPG", idea[key]])
    if key == "聚丙烯&塑料":
        topop.append("聚丙烯&塑料")
        toadd.append(["塑料", idea[key]])
        toadd.append(["PP", idea[key]])
    if key == "聚丙烯":
        topop.append("聚丙烯")
        toadd.append(["PP", idea[key]])
    if key == "20号胶&天然橡胶":
        topop.append("20号胶&天然橡胶")
        toadd.append(["橡胶", idea[key]])
    if key == "天然橡胶":
        topop.append("天然橡胶")
        toadd.append(["橡胶", idea[key]])
    if key == "棕榈油&豆油":
        topop.append("棕榈油&豆油")
        toadd.append(["棕榈油", idea[key]])
        toadd.append(["豆油", idea[key]])
    if key == "棕榈油&菜油":
        topop.append("棕榈油&菜油")
        toadd.append(["棕榈油", idea[key]])
        toadd.append(["菜油", idea[key]])
    if key == "乙二醇":
        topop.append("乙二醇")
        toadd.append(["MEG", idea[key]])
    if key == "聚丙烯&纯碱":
        topop.append("聚丙烯&纯碱")
        toadd.append(["PP", idea[key]])
        toadd.append(["纯碱", idea[key]])
    if key == "聚丙烯&纸浆":
        topop.append("聚丙烯&纸浆")
        toadd.append(["PP", idea[key]])
        toadd.append(["纸浆", idea[key]])
    if key == "聚丙烯&尿素":
        topop.append("聚丙烯&尿素")
        toadd.append(["PP", idea[key]])
        toadd.append(["尿素", idea[key]])
    if key == "聚丙烯&玻璃":
        topop.append("聚丙烯&玻璃")
        toadd.append(["PP", idea[key]])
        toadd.append(["玻璃", idea[key]])
    if key == "棕榈油&豆油":
        topop.append("棕榈油&豆油")
        toadd.append(["棕榈油", idea[key]])
        toadd.append(["豆油", idea[key]])
    # 菜粕菜油自己改
    if key == "菜粕&菜油":
        topop.append("菜粕&菜油")
        toadd.append(["菜粕", idea[key]])
        toadd.append(["菜油", idea[key]])

if "分析师团队" in idea:
    idea.pop("分析师团队")

if " " in idea:
    idea.pop(" ")

for i in topop:
    if i in idea:
        idea.pop(i)
for i in toadd:
    idea[i[0]] = i[1]


guotou_old = {}
for i in idea:
    guotou_old[i] = idea[i][:]

for key in idea:
    if not idea[key].isdecimal():
        idea[key] = keywords.simplify_sent(idea[key])

for i in guotou_old:
    if i in idea:
        guotou_old[i] = idea[i] + " 国投 " + guotou_old[i]
    else:
        guotou_old[i] = ""
anxin_idea = idea

###########################################光大开始

with open('光大.txt',encoding='utf8') as f:
    lines = f.readlines()
idea = {}
prev = ""
topop = []
toadd = []
for l in lines:
    print(l)
    if "完整报告请联系" in l:
        break
    if "风险：" in l:
        prev = ""
        continue
    if "免责声明" in l:
        break
    if "PTA来看" in l.strip():
        toadd.append(["PTA", l.strip()])
        continue
    if len(l) < 15 and l.strip().strip("\n") != "" and "操作建议" not in l and "期货方面" not in l and "现货方面" not in l and "图片" not in l and l.strip("\n") != " " and "重要提示" not in l and "免责声明" not in l:
        a1 = l.replace("【", "")
        a2 = a1.replace("】", "")
        a3 = a2.replace("\n", "")
        prev = a3
    elif l.strip("\n") != "":
        a4 = l.replace("\n", "")
        idea[prev] = a4


for key in idea:
    if key == "贵金属":
        topop.append("贵金属")
        toadd.append(["黄金", idea[key]])
        toadd.append(["白银", idea[key]])
    if key == "燃料油":
        topop.append("燃料油")
        toadd.append(["燃油", idea[key]])
    if key == "聚烯烃":
        topop.append("聚烯烃")
        toadd.append(["塑料", idea[key]])
        toadd.append(["PP", idea[key]])
    if key == "豆类":
        topop.append("豆类")
        toadd.append(["菜粕", idea[key]])
        toadd.append(["豆粕", idea[key]])
    if key == "螺纹钢":
        topop.append("螺纹钢")
        toadd.append(["螺纹", idea[key]])
        toadd.append(["热卷", idea[key]])
    if key == "PTA&MEG":
        topop.append("PTA&MEG")
        #toadd.append(["PTA", idea[key]])
        toadd.append(["MEG", idea[key]])
    if key == "乙二醇":
        topop.append("乙二醇")
        toadd.append(["MEG", idea[key]])
    if key == "玉米、淀粉":
        topop.append("玉米、淀粉")
        toadd.append(["玉米", idea[key]])
        toadd.append(["淀粉", idea[key]])
    if key == "玉米淀粉":
        topop.append("玉米淀粉")
        toadd.append(["玉米", idea[key]])
        toadd.append(["淀粉", idea[key]])
    if key == "油脂油料":
        topop.append("油脂油料")
        toadd.append(["豆粕", idea[key]])
        toadd.append(["菜粕", idea[key]])
        toadd.append(["豆油", idea[key]])
        toadd.append(["菜油", idea[key]])
        toadd.append(["棕榈油", idea[key]])
    if key == "铁矿石":
        topop.append("铁矿石")
        toadd.append(["铁矿", idea[key]])
    if key == "钢材":
        topop.append("钢材")
        toadd.append(["螺纹", idea[key]])
        toadd.append(["热卷", idea[key]])

if "" in idea:
    idea.pop("")

for i in topop:
    idea.pop(i)
for i in toadd:
    idea[i[0]] = i[1]


guangda_old = {}
for i in idea:
    guangda_old[i] = idea[i][:]

for key in idea:
    if not idea[key].isdecimal():
        idea[key] = keywords.simplify_sent(idea[key])

for i in guangda_old:
    if i in idea:
        guangda_old[i] = idea[i] + " 光大 " + guangda_old[i]
    else:
        guangda_old[i] = ""
guangda_idea = idea

###########################################上海中期期货
with open('上海中期.txt',encoding='utf8') as f:
    lines = f.readlines()
idea = {}
items = ["贵金属","铜(CU)","螺纹(RB)","热卷(HC)","铝(AL)","锌(ZN)","铅(PB)","镍(NI)","不锈钢(SS)","铁矿石(I)",
         "天胶及20号胶","原油(SC)","燃油(FU)","乙二醇(EG)","PVC(V)","沥青(BU)","塑料(L)","聚丙烯(PP)","PTA(TA)","苯乙烯(EB)","焦炭(J)","焦煤(JM)","动力煤(TC)","甲醇(ME)","尿素(UR)",
         "玻璃(FG)","白糖(SR)","大豆(A)","豆粕(M)","豆油(Y)","棕榈油(P)","菜籽类","鸡蛋(JD)","苹果(AP)","生猪(LH)","花生(PK)","棉花及棉纱"]
next = False
prev_item = ""
for l in lines:
    if "：" in l and len(l) <= 50:
        idea[l.split('：')[0].strip()] = l.split('：')[1].strip()

topop = []
toadd = []
for key in idea:
    if key == "铜及国际铜":
        topop.append("铜及国际铜")
        toadd.append(["铜", idea[key]])
        #toadd.append(["国际铜", idea[key]])
    if key == "铁矿石":
        topop.append("铁矿石")
        toadd.append(["铁矿", idea[key]])
    if key == "燃油及低硫燃油":
        topop.append("燃油及低硫燃油")
        toadd.append(["燃油", idea[key]])
        #toadd.append(["低硫燃油", idea[key]])
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
        toadd.append(["菜油", idea[key]])
    if key == "贵金属":
        topop.append("贵金属")
        toadd.append(["黄金", idea[key]])
        toadd.append(["白银", idea[key]])



for i in topop:
    idea.pop(i)
for i in toadd:
    idea[i[0]] = i[1]

zhongqi_old = {}
for i in idea:
    zhongqi_old[i] = idea[i][:]

for key in idea:
    if not idea[key].isdecimal():
        idea[key] = keywords.simplify_sent(idea[key])

for i in zhongqi_old:
    if i in idea:
        zhongqi_old[i] = idea[i] + " 中期 " + zhongqi_old[i]
    else:
        zhongqi_old[i] = ""

zhongqi_idea = idea


###########################################五矿开始

with open('五矿.txt',encoding='utf8') as f:
    lines = f.readlines()
idea = {}
items = ["股指","国债","油脂","蛋白粕","鸡蛋","生猪","白糖","苹果","棉花","贵金属","铜","锌","铅","原油",
         "铝","镍","锡","锰硅","硅铁","铁矿石","钢材","双焦","橡胶","甲醇","尿素","苯乙烯","PVC","PTA","玻璃","纯碱","LPG","沥青","动力煤"]
next = False
prev_item = ""
for l in lines:
    if l.strip().strip('\n') == "":
        continue
    stripped = l.strip().strip('\n')
    if stripped in items:
        next = True
        prev_item = stripped
        continue
    if next:
        if "期权" in l:
            l = l.split("期权")[0]
            next = False
        if prev_item in idea:
            idea[prev_item] += l.strip().strip('\n')
        else:
            idea[prev_item] = l.strip().strip('\n')

topop = []
toadd = []
for key in idea:
    if key == "贵金属":
        topop.append("贵金属")
        toadd.append(["黄金", idea[key]])
        toadd.append(["白银", idea[key]])
    if key == "双焦":
        topop.append("双焦")
        toadd.append(["焦煤", idea[key]])
        toadd.append(["焦炭", idea[key]])
    if key == "铁矿石":
        topop.append("铁矿石")
        toadd.append(["铁矿", idea[key]])
    if key == "钢材":
        topop.append("钢材")
        toadd.append(["螺纹", idea[key]])
        toadd.append(["热卷", idea[key]])
    if key == "油脂":
        topop.append("油脂")
        toadd.append(["豆油", idea[key]])
        toadd.append(["菜油", idea[key]])
        toadd.append(["棕榈油", idea[key]])
    if key == "蛋白粕":
        topop.append("蛋白粕")
        toadd.append(["豆粕", idea[key]])
        toadd.append(["菜粕", idea[key]])

if "分析师团队" in idea:
    idea.pop("分析师团队")

if " " in idea:
    idea.pop(" ")

for i in topop:
    idea.pop(i)
for i in toadd:
    idea[i[0]] = i[1]

wukuang_old = {}
for i in idea:
    wukuang_old[i] = idea[i][:]

for key in idea:
    if not idea[key].isdecimal():
        idea[key] = keywords.simplify_sent(idea[key])

for i in wukuang_old:
    if i in idea:
        wukuang_old[i] = idea[i] + " 五矿 " + wukuang_old[i]
    else:
        wukuang_old[i] = ""

wukuang_idea = idea

###########################################倍特期货


with open('倍特.txt',encoding='utf8') as f:
    lines = f.readlines()
idea = {}
items = ["金银","铜","尿素","橡胶","苹果","豆粕","螺纹钢","鸡蛋","油脂","花生","原油"]
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
    if l.startswith('【') and stripped not in items:
        next = False
        continue
    if next:
        if prev_item in idea:
            idea[prev_item] += l.strip().strip('\n')
        else:
            idea[prev_item] = l.strip().strip('\n')

topop = []
toadd = []
for key in idea:
    if key == "贵金属":
        topop.append("贵金属")
        toadd.append(["黄金", idea[key]])
        toadd.append(["白银", idea[key]])
    if key == "金银":
        topop.append("金银")
        toadd.append(["黄金", idea[key]])
        toadd.append(["白银", idea[key]])
    if key == "铁矿石":
        topop.append("铁矿石")
        toadd.append(["铁矿", idea[key]])
    if key == "钢材":
        topop.append("钢材")
        toadd.append(["螺纹", idea[key]])
        toadd.append(["热卷", idea[key]])
    if key == "油脂":
        topop.append("油脂")
        toadd.append(["豆油", idea[key]])
        toadd.append(["菜油", idea[key]])
        toadd.append(["棕榈油", idea[key]])
    if key == "螺纹钢":
        topop.append("螺纹钢")
        toadd.append(["螺纹", idea[key]])
        toadd.append(["热卷", idea[key]])
    if key == "蛋白粕":
        topop.append("蛋白粕")
        toadd.append(["豆粕", idea[key]])
        toadd.append(["菜粕", idea[key]])
    if key == "豆粕":
        topop.append("豆粕")
        toadd.append(["豆粕", idea[key]])
        toadd.append(["菜粕", idea[key]])

for i in topop:
    idea.pop(i)
for i in toadd:
    idea[i[0]] = i[1]

beite_old = {}
for i in idea:
    beite_old[i] = idea[i][:]


for key in idea:
    if not idea[key].isdecimal():
        idea[key] = keywords.simplify_sent(idea[key])

for i in beite_old:
    if i in idea:
        beite_old[i] = idea[i] + " 倍特 " + beite_old[i]
    else:
        beite_old[i] = ""

beite_idea = idea

###########################################银河开始

with open('银河.txt',encoding='utf8') as f:
    lines = f.readlines()
idea = {}
items = ["铁矿","钢材","焦煤焦炭","镍及不锈钢","铜","锌","铝","沥青","原油","燃料油","纸浆","天然橡胶及20号胶","甲醇","尿素","动力煤","PTA","PF","MEG","EB","PP","塑料","PVC","EB","贵金属"]
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
        if "套利：" in l:
            next = False
            idea[prev_item] += l.strip().strip('\n').split("套利：")[0]
            continue
        if prev_item == "焦煤焦炭":
            if "长期看" in l:
                idea[prev_item] = l.strip().strip('\n').split("长期看")[0]
                next = False
                continue
            if "驱动角度看" in l:
                next = False
                idea[prev_item] = l.strip().strip('\n').split("驱动角度看")[0]
                next = False
                continue
        if prev_item in idea:
            if "【交易策略】" in l:
                idea[prev_item] = l.strip().strip('\n').split("【交易策略】")[1]
            elif "【交易逻辑】" in l:
                idea[prev_item] = l.strip().strip('\n').split("【交易逻辑】")[1]
            else:
                idea[prev_item] += l.strip().strip('\n')
        else:
            if "【交易策略】" in l:
                idea[prev_item] = l.strip().strip('\n').split("【交易策略】")[1]
            elif "【交易逻辑】" in l:
                idea[prev_item] = l.strip().strip('\n').split("【交易逻辑】")[1]
            else:
                idea[prev_item] = l.strip().strip('\n')


topop = []
toadd = []
for key in idea:
    if key == "焦煤焦炭":
        topop.append("焦煤焦炭")
        toadd.append(["焦煤", idea[key]])
        toadd.append(["焦炭", idea[key]])
    if key == "贵金属":
        topop.append("贵金属")
        toadd.append(["黄金", idea[key]])
        toadd.append(["白银", idea[key]])
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
    if key == "钢材":
        topop.append("钢材")
        toadd.append(["螺纹", idea[key]])
        toadd.append(["热卷", idea[key]])



for i in topop:
    idea.pop(i)
for i in toadd:
    idea[i[0]] = i[1]

yinhe_old = {}
for i in idea:
    yinhe_old[i] = idea[i][:]

for key in idea:
    if not idea[key].isdecimal():
        idea[key] = keywords.simplify_sent(idea[key])

for i in yinhe_old:
    if i in idea:
        yinhe_old[i] = idea[i] + " 银河 " + yinhe_old[i]
    else:
        yinhe_old[i] = ""

yinhe_idea = idea

###########################################银河农产品开始

#!/usr/bin/python
# -*- coding: utf-8 -*-
import keywords

with open('银河农产品.txt',encoding='utf8') as f:
    lines = f.readlines()
idea = {}
items = ["花生","棉花-棉纱","白糖","鸡蛋","生猪","玉米/玉米淀粉","油脂板块","大豆/粕类","鸡肉"]
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
yinhenong_old = {}
for i in idea:
    yinhenong_old[i] = idea[i][:]

topop = []
toadd = []
for key in idea:
    if key == "棉花-棉纱":
        topop.append("棉花-棉纱")
        toadd.append(["棉花", idea[key]])
        toadd.append(["棉纱", idea[key]])
    if key == "玉米/玉米淀粉":
        topop.append("玉米/玉米淀粉")
        toadd.append(["玉米", idea[key]])
        toadd.append(["淀粉", idea[key]])
    if key == "油脂板块":
        topop.append("油脂板块")
        toadd.append(["豆油", idea[key]])
        toadd.append(["菜油", idea[key]])
        toadd.append(["棕榈油", idea[key]])
    if key == "大豆/粕类":
        topop.append("大豆/粕类")
        toadd.append(["豆粕", idea[key]])
        toadd.append(["菜粕", idea[key]])
if "鸡肉" in toadd:
    toadd.pop("鸡肉")
for i in topop:
    idea.pop(i)
for i in toadd:
    idea[i[0]] = i[1]

yinhenong_old = {}
for i in idea:
    yinhenong_old[i] = idea[i][:]

for key in idea:
    if not idea[key].isdecimal():
        idea[key] = keywords.simplify_sent(idea[key])

for i in yinhenong_old:
    if i in idea:
        yinhenong_old[i] = idea[i] + " 银河农产品 " + yinhenong_old[i]
    else:
        yinhenong_old[i] = ""

yinhenong_idea = idea

###########################################广发开始

import keywords

with open('广发.txt',) as f:
    lines = f.readlines()
idea = {}
items = ["国债期货：","贵金属：","铜：","锌：","铝：","镍：","不锈钢：","锡：","钢材：","铁矿石：","焦炭：","焦煤：","动力煤：","豆粕：","油脂：","生猪：","玉米：","白糖：","棉花：","鸡蛋：","花生：","红枣：",
         "原油：","沥青：","PTA：","乙二醇：","短纤：","苯乙烯：","LLDPE：","PP：","尿素:","PVC：","甲醇：","纯碱：","玻璃：","橡胶：","纸浆：","苹果："]
next = False
prev_item = ""
for l in lines:
    stripped = l.strip().strip('\n').strip('【').strip('】')
    if stripped == "":
        continue
    if "纯碱：" in stripped:
        if "纯碱" in idea:
            idea["纯碱"] += stripped
        else:
            idea["纯碱"] = stripped
        prev_item = "纯碱："
        continue
    if "玻璃：" in stripped:
        if "玻璃" in idea:
            idea["玻璃"] += stripped
        else:
            idea["玻璃"] = stripped
        prev_item = "玻璃："
        continue
    if "橡胶：" in stripped:
        idea["橡胶"] = stripped
        prev_item = "橡胶："
        next = True
        continue
    if stripped in items:
        next = True
        prev_item = stripped
        continue
    else:
        for i in items:
            if i in stripped:
                next = True
                prev_item = i.strip("：")
                break
    if next:
        if prev_item.strip("：") in idea:
            idea[prev_item.strip("：") ] += l.strip().strip('\n').split("【")[0].split("[")[0]
        else:
            idea[prev_item.strip("：") ] = l.strip().strip('\n').split("【")[0].split("[")[0]


topop = []
toadd = []
for key in idea:
    if key == "贵金属":
        topop.append("贵金属")
        toadd.append(["黄金", idea[key]])
        toadd.append(["白银", idea[key]])
    if key == "油脂":
        topop.append("油脂")
        toadd.append(["豆油", idea[key]])
        toadd.append(["菜油", idea[key]])
        toadd.append(["棕榈油", idea[key]])
    if key == "国债期货":
        topop.append("国债期货")
        toadd.append(["国债", idea[key]])
    if key == "乙二醇":
        topop.append("乙二醇")
        toadd.append(["MEG", idea[key]])
    if key == "LLDPE":
        topop.append("LLDPE")
        toadd.append(["塑料", idea[key]])
    if key == "尿素:":
        topop.append("尿素:")
        toadd.append(["尿素", idea[key]])
    if key == "钢材":
        topop.append("钢材")
        toadd.append(["螺纹", idea[key]])
        toadd.append(["热卷", idea[key]])
    if key == "猪":
        topop.append("猪")
        toadd.append(["生猪", idea[key]])
    if key == "铁矿石":
        topop.append("铁矿石")
        toadd.append(["铁矿", idea[key]])
    if key == "液化气":
        topop.append("液化气")
        toadd.append(["LPG", idea[key]])
    if key == "铜 ":
        topop.append("铜 ")
        toadd.append(["铜", idea[key]])

for i in topop:
    idea.pop(i)
for i in toadd:
    idea[i[0]] = i[1]

guangfa_old = {}
for i in idea:
    guangfa_old[i] = idea[i][:]

for key in idea:
    if not idea[key].isdecimal():
        idea[key] = keywords.simplify_sent(idea[key])

for i in guangfa_old:
    if i in idea:
        guangfa_old[i] = idea[i] + " 广发 " + guangfa_old[i]
    else:
        guangfa_old[i] = ""

guangfa_idea = idea

############################################广州开始

with open('广州.txt',encoding='utf8') as f:
    lines = f.readlines()
idea = {}
items = ["原油","沥青","铜","郑棉","螺纹钢","焦炭","铝","锌","焦煤","镍","不锈钢","动力煤","纯碱","玻璃","生猪","豆粕","液化气","RU","聚烯烃","聚酯"]
next = False
prev_item = ""
for l in lines:
    if "：" in l and len(l) <= 30 and l.split('：')[0] in items:
        idea[l.split('：')[0]] = l.split('：')[1]
    else:
        if ":" in l and len(l) <= 30 and l.split(':')[0] in items:
            idea[l.split(':')[0]] = l.split(':')[1]


topop = []
toadd = []
for key in idea:
    if key == "郑棉":
        topop.append("郑棉")
        toadd.append(["棉花", idea[key]])
    if key == "螺纹钢":
        topop.append("螺纹钢")
        toadd.append(["螺纹", idea[key]])
        toadd.append(["热卷", idea[key]])
    if key == "钢材":
        topop.append("钢材")
        toadd.append(["螺纹", idea[key]])
        toadd.append(["热卷", idea[key]])
    if key == "猪":
        topop.append("猪")
        toadd.append(["生猪", idea[key]])
    if key == "铁矿石":
        topop.append("铁矿石")
        toadd.append(["铁矿", idea[key]])
    if key == "液化气":
        topop.append("液化气")
        toadd.append(["LPG", idea[key]])
    if key == "RU":
        topop.append("RU")
        toadd.append(["橡胶", idea[key]])
    if key == "聚烯烃":
        topop.append("聚烯烃")
        toadd.append(["PP", idea[key]])
        toadd.append(["塑料", idea[key]])
    if key == "聚酯":
        topop.append("聚酯")
        toadd.append(["PTA", idea[key]])
        toadd.append(["MEG", idea[key]])


for i in topop:
    idea.pop(i)
for i in toadd:
    idea[i[0]] = i[1]

guangzhou_old = {}
for i in idea:
    guangzhou_old[i] = idea[i][:]

for key in idea:
    if not idea[key].isdecimal():
        idea[key] = keywords.simplify_sent(idea[key])

for i in guangzhou_old:
    if i in idea:
        guangzhou_old[i] = idea[i] + " 广州 " + guangzhou_old[i]
    else:
        guangzhou_old[i] = ""

guangzhou_idea = idea

###########################################国信开始

with open('国信.txt',encoding='utf8') as f:
    lines = f.readlines()
idea = {}
items = ["股指","国债","贵金属","铜铝","锌镍","锌","螺纹钢","铁合金","焦炭焦煤","镍","豆类","油脂","白糖","棉花","玉米","生猪","花生","苹果","PTA","聚烯烃","原油","橡胶","燃料油","沥青","甲醇","铁矿石","动力煤"]
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
    if l.isnumeric():
        next = False
        continue
    if next:
        if prev_item in idea:
            idea[prev_item] += l.strip().strip('\n')
        else:
            idea[prev_item] = l.strip().strip('\n')

topop = []
toadd = []
for key in idea:
    if key == "焦炭焦煤":
        topop.append("焦炭焦煤")
        toadd.append(["焦煤", idea[key]])
        toadd.append(["焦炭", idea[key]])
    if key == "燃料油":
        topop.append("燃料油")
        toadd.append(["燃油", idea[key]])
    if key == "贵金属":
        topop.append("贵金属")
        toadd.append(["黄金", idea[key]])
        toadd.append(["白银", idea[key]])
    if key == "铁矿石":
        topop.append("铁矿石")
        toadd.append(["铁矿", idea[key]])
    if key == "铜铝":
        topop.append("铜铝")
        toadd.append(["铜", idea[key]])
        toadd.append(["铝", idea[key]])
    if key == "锌镍":
        topop.append("锌镍")
        toadd.append(["锌", idea[key]])
        toadd.append(["镍", idea[key]])
    if key == "螺纹钢":
        topop.append("螺纹钢")
        toadd.append(["螺纹", idea[key]])
        toadd.append(["热卷", idea[key]])
    if key == "铁合金":
        topop.append("铁合金")
        toadd.append(["锰硅", idea[key]])
        toadd.append(["硅铁", idea[key]])
    if key == "豆类":
        topop.append("豆类")
        toadd.append(["豆粕", idea[key]])
    if key == "油脂":
        topop.append("油脂")
        toadd.append(["豆油", idea[key]])
        toadd.append(["菜油", idea[key]])
        toadd.append(["棕榈油", idea[key]])
    if key == "聚烯烃":
        topop.append("聚烯烃")
        toadd.append(["PP", idea[key]])
        toadd.append(["塑料", idea[key]])

for i in topop:
    idea.pop(i)
for i in toadd:
    idea[i[0]] = i[1]

guoxin_old = {}
for i in idea:
    guoxin_old[i] = idea[i][:]

for key in idea:
    if not idea[key].isdecimal():
        idea[key] = keywords.simplify_sent(idea[key])

for i in guoxin_old:
    if i in idea:
        guoxin_old[i] = idea[i] + " 国信 " + guoxin_old[i]
    else:
        guoxin_old[i] = ""

guoxin_idea = idea

##########################################永安开始

with open('永安.txt',encoding='utf8') as f:
    lines = f.readlines()
idea = {}
items = ["股指期货","钢 材","铁 矿 石","动 力 煤","ENERGY","焦煤焦炭","白糖","纸 浆","PULP","【原油】","【沥青】","橡胶","【ＬＰＧ】","【LPG】","尿 素",
         "豆类油脂","棉花","白 糖","生 猪","生猪","豆粕","液化气","RU","聚烯烃","聚酯","S T E E L"]
next = False
prev_item = ""
for l in lines:
    stripped = l.strip()
    if stripped == "":
        continue
    if stripped in items:
        next = True
        prev_item = stripped
        continue
    if next:
        if prev_item.strip("：") in idea:
            idea[prev_item.strip()] += l.strip().strip('\n')
        else:
            idea[prev_item.strip()] = l.strip().strip('\n')

topop = []
toadd = []
for key in idea:
    if key == "焦煤焦炭":
        topop.append("焦煤焦炭")
        toadd.append(["焦煤", idea[key]])
        toadd.append(["焦炭", idea[key]])
    if key == "钢 材":
        topop.append("钢 材")
        toadd.append(["螺纹", idea[key]])
        toadd.append(["热卷", idea[key]])
    if key == "ENERGY":
        topop.append("ENERGY")
        toadd.append(["原油", idea[key]])
    if key == "S T E E L":
        topop.append("S T E E L")
        toadd.append(["螺纹", idea[key]])
        toadd.append(["热卷", idea[key]])
    if key == "PULP":
        topop.append("PULP")
        toadd.append(["纸浆", idea[key]])
    if key == "动 力 煤":
        topop.append("动 力 煤")
        toadd.append(["动力煤", idea[key]])
    if key == "纸 浆":
        topop.append("纸 浆")
        toadd.append(["纸浆", idea[key]])
    if key == "股指期货":
        topop.append("股指期货")
        toadd.append(["股指", idea[key]])
    if key == "铁 矿 石":
        topop.append("铁 矿 石")
        toadd.append(["铁矿", idea[key]])
    if key == "【原油】":
        topop.append("【原油】")
        toadd.append(["原油", idea[key]])
    if key == "【沥青】":
        topop.append("【沥青】")
        toadd.append(["沥青", idea[key]])
    if key == "【LPG】":
        topop.append("【LPG】")
        toadd.append(["LPG", idea[key]])
    if key == "【ＬＰＧ】":
        topop.append("【ＬＰＧ】")
        toadd.append(["LPG", idea[key]])
    if key == "尿 素":
        topop.append("尿 素")
        toadd.append(["尿素", idea[key]])
    if key == "豆类油脂":
        topop.append("豆类油脂")
        toadd.append(["豆油", idea[key]])
        toadd.append(["菜油", idea[key]])
        toadd.append(["棕榈油", idea[key]])
        toadd.append(["豆油", idea[key]])
        toadd.append(["菜油", idea[key]])
    if key == "白 糖":
        topop.append("白 糖")
        toadd.append(["白糖", idea[key]])
    if key == "生 猪":
        topop.append("生 猪")
        toadd.append(["生猪", idea[key]])



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

##########################################海通开始


with open('海通.txt',encoding='utf8') as f:
    lines = f.readlines()
idea = {}
items = ["铝","钢材","油脂","焦煤焦炭","粕类","铁矿","油脂油料","豆粕","股指","国债","贵金属","铜","镍","锡","铁矿石","锰硅","硅铁","橡胶","玻璃","纯碱","原油","白糖","蛋白粕","油脂","苹果","生猪","苹果","生猪","鸡蛋"]
next = False
prev_item = ""
for l in lines:
    stripped = l.strip()
    if stripped == "":
        continue
    if stripped in items:
        next = True
        prev_item = stripped
        continue
    elif "铁矿" in stripped:
        next = True
        prev_item = "铁矿"
        idea[prev_item.strip()] = l.strip().strip('\n')
        continue
    elif "钢材" in stripped:
        next = True
        prev_item = "钢材"
        idea[prev_item.strip()] = l.strip().strip('\n')
        continue
    if next:
        if prev_item.strip("：") in idea:
            idea[prev_item.strip()] += l.strip().strip('\n')
        else:
            idea[prev_item.strip()] = l.strip().strip('\n')

topop = []
toadd = []
for key in idea:
    if key == "焦煤焦炭":
        topop.append("焦煤焦炭")
        toadd.append(["焦煤", idea[key]])
        toadd.append(["焦炭", idea[key]])
    if key == "贵金属":
        topop.append("贵金属")
        toadd.append(["白银", idea[key]])
        toadd.append(["黄金", idea[key]])
    if key == "钢材":
        topop.append("钢材")
        toadd.append(["螺纹", idea[key]])
        toadd.append(["热卷", idea[key]])
    if key == "油脂":
        topop.append("油脂")
        toadd.append(["豆油", idea[key]])
        toadd.append(["菜油", idea[key]])
        toadd.append(["棕榈油", idea[key]])
    if key == "油脂油料":
        topop.append("油脂油料")
        toadd.append(["豆油", idea[key]])
        toadd.append(["菜油", idea[key]])
        toadd.append(["棕榈油", idea[key]])
        toadd.append(["豆粕", idea[key]])
        toadd.append(["菜粕", idea[key]])
    if key == "粕类":
        topop.append("粕类")
        toadd.append(["豆粕", idea[key]])
        toadd.append(["菜粕", idea[key]])
    if key == "蛋白粕":
        topop.append("蛋白粕")
        toadd.append(["豆粕", idea[key]])
        toadd.append(["菜粕", idea[key]])
    if key == "铁矿石":
        topop.append("铁矿石")
        toadd.append(["铁矿", idea[key]])

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
        haitong_old[i] = idea[i] + " 海通 " + haitong_old[i]
    else:
        haitong_old[i] = ""


haitong_idea = idea

###########################################国都开始


with open('国都.txt',encoding='utf8') as f:
    lines = f.readlines()
idea = {}
items = ["图片豆粕","豆粕","PTA","涤纶短纤","橡胶","棉花","豆类","橡胶","油脂","白糖","玉米、淀粉","生猪"]
next = False
prev_item = ""
for l in lines:
    stripped = l.strip()
    if stripped == "":
        continue
    if stripped == "国都期货研究所":
        break
    if stripped in items:
        next = True
        prev_item = stripped
        continue
    if next:
        if prev_item.strip("：") in idea:
            idea[prev_item.strip()] += l.strip().strip('\n')
        else:
            idea[prev_item.strip()] = l.strip().strip('\n')

topop = []
toadd = []
for key in idea:
    if key == "图片豆粕":
        topop.append("图片豆粕")
        toadd.append(["豆粕", idea[key]])
    if key == "涤纶短纤":
        topop.append("涤纶短纤")
        toadd.append(["短纤", idea[key]])
    if key == "油脂":
        topop.append("油脂")
        toadd.append(["豆油", idea[key]])
        toadd.append(["菜油", idea[key]])
        toadd.append(["棕榈油", idea[key]])
    if key == "豆类":
        topop.append("豆类")
        toadd.append(["豆粕", idea[key]])
        toadd.append(["菜粕", idea[key]])
    if key == "玉米、淀粉":
        topop.append("玉米、淀粉")
        toadd.append(["玉米", idea[key]])
        toadd.append(["淀粉", idea[key]])

for i in topop:
    idea.pop(i)
for i in toadd:
    idea[i[0]] = i[1]

guodu_old = {}
for i in idea:
    guodu_old[i] = idea[i][:]

for key in idea:
    if not idea[key].isdecimal():
        idea[key] = keywords.simplify_sent(idea[key])


for i in guodu_old:
    if i in idea:
        guodu_old[i] = idea[i] + " 国都 " + guodu_old[i]
    else:
        guodu_old[i] = ""

guodu_idea = idea

###########################################鲁证期货


with open('鲁证.txt',encoding='utf8') as f:
    lines = f.readlines()
idea = {}
items = ["股指期货","国债期货","棉花","白糖","油脂油料","鸡蛋","苹果","玉米系","红枣","花生","生猪","原油","塑料","沥青","橡胶","甲醇",
         "纯碱","PVC","聚酯产业链","纸浆","尿素","铜","铝","镍","不锈钢","贵金属","螺矿","煤焦","铁合金","苯乙烯","液化石油气"]
next = False
prev_item = ""
for l in lines:
    stripped = l.strip()
    if "中泰期货股份有限公司" in l:
        break
    if stripped == "":
        continue
    if stripped in items:
        next = True
        prev_item = stripped
        continue
    if next:
        if prev_item.strip("：") in idea:
            idea[prev_item.strip()] += l.strip().strip('\n')
        else:
            idea[prev_item.strip()] = l.strip().strip('\n')

topop = []
toadd = []
for key in idea:
    if key == "油脂油料":
        topop.append("油脂油料")
        toadd.append(["豆油", idea[key]])
        toadd.append(["菜油", idea[key]])
        toadd.append(["棕榈油", idea[key]])
    if key == "玉米系":
        topop.append("玉米系")
        toadd.append(["玉米", idea[key]])
        toadd.append(["淀粉", idea[key]])
    if key == "聚酯产业链":
        topop.append("聚酯产业链")
        toadd.append(["PTA", idea[key]])
        toadd.append(["短纤", idea[key]])
        toadd.append(["MEG", idea[key]])
    if key == "贵金属":
        topop.append("贵金属")
        toadd.append(["黄金", idea[key]])
        toadd.append(["白银", idea[key]])
    if key == "液化石油气":
        topop.append("液化石油气")
        toadd.append(["LPG", idea[key]])
    if key == "螺矿":
        topop.append("螺矿")
        toadd.append(["螺纹", idea[key]])
        toadd.append(["热卷", idea[key]])
        toadd.append(["铁矿", idea[key]])
    if key == "铁合金":
        topop.append("铁合金")
        toadd.append(["锰硅", idea[key]])
        toadd.append(["硅铁", idea[key]])
    if key == "煤焦":
        topop.append("煤焦")
        toadd.append(["焦煤", idea[key]])
        toadd.append(["焦炭", idea[key]])
    if key == "股指期货":
        topop.append("股指期货")
        toadd.append(["股指", idea[key]])
    if key == "国债期货":
        topop.append("国债期货")
        toadd.append(["股指", idea[key]])
for i in topop:
    idea.pop(i)
for i in toadd:
    idea[i[0]] = i[1]

luzheng_old = {}
for i in idea:
    luzheng_old[i] = idea[i][:]

for key in idea:
    if not idea[key].isdecimal():
        idea[key] = keywords.simplify_sent(idea[key])


for i in luzheng_old:
    if i in idea:
        luzheng_old[i] = idea[i] + " 鲁证 " +luzheng_old[i]
    else:
        luzheng_old[i] = ""

luzheng_idea = idea

############################################南华期市早餐开始

with open('南华.txt',encoding='utf8') as f:
    lines = f.readlines()
idea = {}
items = ["国债日报","股指","螺纹","热卷","铁矿","焦煤","焦炭","锰硅","硅锰","硅铁","动力煤","纯碱","玻璃","白糖","棉花","苹果","红枣","油料","油脂","原油","油脂油料","甲醇","燃料油","PVC","聚酯","沥青",
         "PTA","MEG","PF","LPG","纸浆","橡胶","铜","铝","锌","镍不锈钢","锡","贵金属","聚烯烃","螺纹钢","铁矿石","郑棉","豆粕","生猪","MA","SC","RU","EB","乙二醇","苯乙烯","PTA&PF"]
next = False
prev_item = ""
for l in lines:
    stripped = l.strip()
    if stripped == "":
        continue
    if "以上评论由分析师" in stripped:
        stripped = stripped.split("以上评论由分析师")[0]
        next = False
    if "重要申明：本报告" in stripped:
        stripped = stripped.split("重要申明：本报告")[0]
        next = False
    if "：" in stripped and stripped.split("：")[0] in items:
        next = True
        prev_item = stripped.split("：")[0]
        idea[prev_item] = stripped.split("：")[1]
        continue
    if "：" in stripped and stripped.split("早评")[0] in items:
        next = True
        prev_item = stripped.split("早评")[0]
        idea[prev_item] = stripped.split("：")[1]
        continue
    if ":" in stripped and stripped.split(":")[0] in items:
        next = True
        prev_item = stripped.split(":")[0]
        idea[prev_item] = stripped.split(":")[1]
        continue
    if next:
        if prev_item in idea:
            idea[prev_item] += stripped.strip('\n')
        else:
            idea[prev_item] = stripped.strip('\n')

topop = []
toadd = []
for key in idea:
    if key == "油脂":
        topop.append("油脂")
        toadd.append(["豆油", idea[key]])
        toadd.append(["菜油", idea[key]])
        toadd.append(["棕榈油", idea[key]])
    if key == "油料":
        topop.append("油料")
        toadd.append(["豆粕", idea[key]])
        toadd.append(["菜粕", idea[key]])
    if key == "燃料油":
        topop.append("燃料油")
        toadd.append(["燃油", idea[key]])
    if key == "MA":
        topop.append("MA")
        toadd.append(["甲醇", idea[key]])
    if key == "SC":
        topop.append("SC")
        toadd.append(["原油", idea[key]])
    if key == "RU":
        topop.append("RU")
        toadd.append(["橡胶", idea[key]])
    if key == "EB":
        topop.append("EB")
        toadd.append(["苯乙烯", idea[key]])
    if key == "郑棉":
        topop.append("郑棉")
        toadd.append(["棉花", idea[key]])
    if key == "螺纹钢":
        topop.append("螺纹钢")
        toadd.append(["螺纹", idea[key]])
    if key == "铁矿石":
        topop.append("铁矿石")
        toadd.append(["铁矿", idea[key]])
    if key == "硅锰":
        topop.append("硅锰")
        toadd.append(["锰硅", idea[key]])
    if key == "国债日报":
        topop.append("国债日报")
        toadd.append(["国债", idea[key]])
    if key == "聚烯烃":
        topop.append("聚烯烃")
        toadd.append(["PP", idea[key]])
        toadd.append(["塑料", idea[key]])
    if key == "PTA&PF":
        topop.append("PTA&PF")
        toadd.append(["短纤", idea[key]])
        toadd.append(["PTA", idea[key]])
    if key == "PF":
        topop.append("PF")
        toadd.append(["短纤", idea[key]])
    if key == "贵金属":
        topop.append("贵金属")
        toadd.append(["白银", idea[key]])
        toadd.append(["黄金", idea[key]])
    if key == "镍不锈钢":
        topop.append("镍不锈钢")
        toadd.append(["镍", idea[key]])
        toadd.append(["不锈钢", idea[key]])
    if key == "乙二醇":
        topop.append("乙二醇")
        toadd.append(["MEG", idea[key]])

if "聚酯" in idea:
    idea.pop("聚酯")
if "油脂油料" in idea:
    idea.pop("油脂油料")
for i in topop:
    idea.pop(i)
for i in toadd:
    idea[i[0]] = i[1]



nanhua_old = {}
for i in idea:
    nanhua_old[i] = idea[i][:]

for key in idea:
    if not idea[key].isdecimal():
        idea[key] = keywords.simplify_sent(idea[key])


for i in nanhua_old:
    if i in idea:
        nanhua_old[i] = idea[i] + " 南华 " +nanhua_old[i]
    else:
        nanhua_old[i] = ""

nanhua_idea = idea

###########################################东证

# with open('东证.txt',encoding='utf-8') as f:
#     lines = f.readlines()
# total = ""
# for l in lines:
#     total += l
idea = {}
# items = ["黑色金属（焦煤/焦炭）","黑色金属（螺纹钢/热轧卷板）","有色金属（镍）","有色金属（铝）","农产品（棉花）","农产品（豆粕）","航运指数（集装箱运价）"]
# index = 0
# for i in items[:-1]:
#     after = total.split(i)[1]
#     comment = after.split("投资建议：")[1]
#     final = comment.split(items[index + 1])[0]
#     idea[i.split("（")[1].split("）")[0]] = final
#     index += 1
#     total = after
#
# dongzheng_old = {}
# for i in idea:
#     dongzheng_old[i] = idea[i][:]
#
# topop = []
# toadd = []
# for key in idea:
#     if key == "黄金":
#         toadd.append(["白银", idea[key]])
#     if key == "焦煤/焦炭":
#         topop.append("焦煤/焦炭")
#         toadd.append(["焦煤", idea[key]])
#         toadd.append(["焦炭", idea[key]])
#     if key == "螺纹钢/热轧卷板":
#         topop.append("螺纹钢/热轧卷板")
#         toadd.append(["螺纹", idea[key]])
#         toadd.append(["热卷", idea[key]])
#
#
# for i in topop:
#     idea.pop(i)
# for i in toadd:
#    idea[i[0]] = i[1]

dongzheng_old = {}
# for i in idea:
#     dongzheng_old[i] = idea[i][:]
#
# for key in idea:
#     if not idea[key].isdecimal():
#         idea[key] = keywords.simplify_sent(idea[key])
#
#
# for i in dongzheng_old:
#     if i in idea:
#         dongzheng_old[i] = idea[i] + " 东证 " +dongzheng_old[i]
#     else:
#        dongzheng_old[i] = ""

dongzheng_idea = idea

###########################################东兴开始

with open('东兴.txt',encoding='utf8') as f:
    lines = f.readlines()
idea = {}
items = ["期指","期债","动力煤","铜","PTA","TA","PVC","天然橡胶","生猪","玉米","橡胶"]
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
    if key == "TA":
        topop.append("TA")
        toadd.append(["PTA", idea[key]])

for i in topop:
    idea.pop(i)
for i in toadd:
    idea[i[0]] = i[1]

dongxing_old = {}
for i in idea:
    dongxing_old[i] = idea[i][:]

for key in idea:
    if not idea[key].isdecimal():
        idea[key] = keywords.simplify_sent(idea[key])


for i in dongxing_old:
    if i in idea:
        dongxing_old[i] = idea[i] + " 东兴 " + dongxing_old[i]
    else:
        dongxing_old[i] = ""

dongxing_idea = idea

###########################################混沌天成工业品开始
with open('混沌天成工业品.txt',encoding='utf-8') as f:
    lines = f.readlines()
idea = {}
items = ["钢材","铁矿石","焦煤","焦炭","铜","铝","锌","镍","不锈钢"]
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
hundungong_old = {}
for i in idea:
    hundungong_old[i] = idea[i][:]

topop = []
toadd = []
for key in idea:
    if key == "钢材":
        topop.append("钢材")
        toadd.append(["螺纹", idea[key]])
        toadd.append(["热卷", idea[key]])
    if key == "铁矿石":
        topop.append("铁矿石")
        toadd.append(["铁矿", idea[key]])

for i in topop:
    idea.pop(i)
for i in toadd:
    idea[i[0]] = i[1]

hundungong_old = {}
for i in idea:
    hundungong_old[i] = idea[i][:]

for key in idea:
    if not idea[key].isdecimal():
        idea[key] = keywords.simplify_sent(idea[key])


for i in hundungong_old:
    if i in idea:
        hundungong_old[i] = idea[i] + " 混沌工业 " + hundungong_old[i]
    else:
        hundungong_old[i] = ""

hundungong_idea = idea

###########################################混沌天成能化开始

with open('混沌天成能化.txt',encoding='utf-8') as f:
    lines = f.readlines()
idea = {}
items = ["纯碱玻璃","橡胶","PVC","LLDPE日评","尿素","甲醇","MEG日评：","PTA日评","原油","PP日评："]
next = False
prev_item = ""
for l in lines:
    stripped = l.strip().strip('\n').strip('【').strip('】')
    if stripped == "":
        continue
    if "关于商品研究提升的三点结论" in stripped:
        break
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
hundunneng_old = {}
for i in idea:
    hundunneng_old[i] = idea[i][:]

topop = []
toadd = []
for key in idea:
    if key == "纯碱玻璃":
        topop.append("纯碱玻璃")
        toadd.append(["纯碱", idea[key]])
        toadd.append(["玻璃", idea[key]])
    if key == "LLDPE日评":
        topop.append("LLDPE日评")
        toadd.append(["塑料", idea[key]])
    if key == "MEG日评：":
        topop.append("MEG日评：")
        toadd.append(["MEG", idea[key]])
    if key == "PTA日评":
        topop.append("PTA日评")
        toadd.append(["PTA", idea[key]])
    if key == "PP日评：":
        topop.append("PP日评：")
        toadd.append(["PP", idea[key]])

for i in topop:
    idea.pop(i)
for i in toadd:
    idea[i[0]] = i[1]

hundunneng_old = {}
for i in idea:
    hundunneng_old[i] = idea[i][:]

for key in idea:
    if not idea[key].isdecimal():
        idea[key] = keywords.simplify_sent(idea[key])


for i in hundunneng_old:
    if i in idea:
        hundunneng_old[i] = idea[i] + " 混沌能化 " + hundunneng_old[i]
    else:
        hundunneng_old[i] = ""

hundunneng_idea = idea

###########################################混沌天成农产品开始

with open('混沌天成农产品.txt',encoding='utf-8') as f:
    lines = f.readlines()
idea = {}
items = ["油脂油料","棉花","玉  米","豆  粕","鸡  蛋","生  猪","苹  果","纸  浆"]
next = False
prev_item = ""
for l in lines:
    stripped = l.strip().strip('\n').strip('【').strip('】')
    if stripped == "":
        continue
    if "关于商品研究提升的三点结论" in stripped:
        break
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
hundunagri_old = {}
for i in idea:
    hundunagri_old[i] = idea[i][:]

topop = []
toadd = []
for key in idea:
    if key == "油脂油料":
        topop.append("油脂油料")
        toadd.append(["豆油", idea[key]])
        toadd.append(["菜油", idea[key]])
        toadd.append(["棕榈油", idea[key]])
    if key == "玉  米":
        topop.append("玉  米")
        toadd.append(["玉米", idea[key]])
    if key == "豆  粕":
        topop.append("豆  粕")
        toadd.append(["豆粕", idea[key]])
    if key == "鸡  蛋":
        topop.append("鸡  蛋")
        toadd.append(["鸡蛋", idea[key]])
    if key == "生  猪":
        topop.append("生  猪")
        toadd.append(["生猪", idea[key]])
    if key == "苹  果":
        topop.append("苹  果")
        toadd.append(["苹果", idea[key]])
    if key == "纸  浆":
        topop.append("纸  浆")
        toadd.append(["纸浆", idea[key]])
if "鸡肉" in idea:
    idea.pop('鸡肉')

for i in topop:
    idea.pop(i)
for i in toadd:
    idea[i[0]] = i[1]

hundunagri_old = {}
for i in idea:
    hundunagri_old[i] = idea[i][:]

for key in idea:
    if not idea[key].isdecimal():
        idea[key] = keywords.simplify_sent(idea[key])


for i in hundunagri_old:
    if i in idea:
        hundunagri_old[i] = idea[i] + " 混沌农产品 " + hundunagri_old[i]
    else:
        hundunagri_old[i] = ""

hundunagri_idea = idea

###########################################弘业开始

with open('弘业.txt',encoding='utf8') as f:
    lines = f.readlines()
idea = {}
items = ["原油","PTA","乙二醇","短纤","聚烯烃","液化石油气","沥青","甲醇","苯乙烯","橡胶","玻璃","纯碱","尿素","纸浆","黄金&白银","沪镍","沪铜&国际铜","沪铝","沪锌","沪铅",
         "螺纹&热卷","铁矿石","焦煤&焦炭","动力煤","铁合金","油脂","油料","花生","玉米&淀粉","棉花&棉纱","生猪","鸡蛋","白糖","苹果","红枣"]
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
hongye_old = {}
for i in idea:
    hongye_old[i] = idea[i][:]

topop = []
toadd = []
for key in idea:
    if key == "棉花&棉纱":
        topop.append("棉花&棉纱")
        toadd.append(["棉花", idea[key]])
        toadd.append(["棉纱", idea[key]])
    if key == "玉米&淀粉":
        topop.append("玉米&淀粉")
        toadd.append(["玉米", idea[key]])
        toadd.append(["淀粉", idea[key]])
    if key == "油料":
        topop.append("油料")
        toadd.append(["豆粕", idea[key]])
        toadd.append(["菜粕", idea[key]])
    if key == "油脂":
        topop.append("油脂")
        toadd.append(["豆油", idea[key]])
        toadd.append(["菜油", idea[key]])
        toadd.append(["棕榈油", idea[key]])

    if key == "铁合金":
        topop.append("铁合金")
        toadd.append(["硅铁", idea[key]])
        toadd.append(["锰硅", idea[key]])
    if key == "焦煤&焦炭":
        topop.append("焦煤&焦炭")
        toadd.append(["焦煤", idea[key]])
        toadd.append(["焦炭", idea[key]])
    if key == "铁矿石":
        topop.append("铁矿石")
        toadd.append(["铁矿", idea[key]])
    if key == "螺纹&热卷":
        topop.append("螺纹&热卷")
        toadd.append(["螺纹", idea[key]])
        toadd.append(["热卷", idea[key]])
    if key == "沪镍":
        topop.append("沪镍")
        toadd.append(["镍", idea[key]])
    if key == "沪铜&国际铜":
        topop.append("沪铜&国际铜")
        toadd.append(["铜", idea[key]])
    if key == "沪铝":
        topop.append("沪铝")
        toadd.append(["铝", idea[key]])
    if key == "沪锌":
        topop.append("沪锌")
        toadd.append(["锌", idea[key]])
    if key == "沪铅":
        topop.append("沪铅")
        toadd.append(["铅", idea[key]])
    if key == "黄金&白银":
        topop.append("黄金&白银")
        toadd.append(["黄金", idea[key]])
        toadd.append(["白银", idea[key]])
    if key == "液化石油气":
        topop.append("液化石油气")
        toadd.append(["LPG", idea[key]])
    if key == "聚烯烃":
        topop.append("聚烯烃")
        toadd.append(["PP", idea[key]])
        toadd.append(["塑料", idea[key]])
        toadd.append(["PVC", idea[key]])

for i in topop:
    idea.pop(i)
for i in toadd:
    idea[i[0]] = i[1]

hongye_old = {}
for i in idea:
    hongye_old[i] = idea[i][:]

for key in idea:
    if not idea[key].isdecimal():
        idea[key] = keywords.simplify_sent(idea[key])


for i in hongye_old:
    if i in idea:
        hongye_old[i] = idea[i] + " 弘业 " + hongye_old[i]
    else:
        hongye_old[i] = ""

hongye_idea = idea

###########################################整合开始

with open('东吴.txt',encoding='utf-8') as f:
    lines = f.readlines()
idea = {}
items = ["螺卷","铁矿","双焦","双硅","原油","沥青","LPG","甲醇","PVC","天然橡胶",
         "沪铜","沪铝","沪锌","沪铅","油脂","豆粕/菜粕","玉米","白糖","鸡蛋",
         "生猪","苹果","红枣","花生"]
next = False
prev_item = ""
for l in lines:
    stripped = l.strip().strip('\n').strip('【').strip('】').strip("：")
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
dongwu_old = {}
for i in idea:
    dongwu_old[i] = idea[i][:]

topop = []
toadd = []
for key in idea:
    if key == "螺卷":
        topop.append("螺卷")
        toadd.append(["螺纹", idea[key]])
        toadd.append(["热卷", idea[key]])
    if key == "双焦":
        topop.append("双焦")
        toadd.append(["焦煤", idea[key]])
        toadd.append(["焦炭", idea[key]])
    if key == "双硅":
        topop.append("双硅")
        toadd.append(["硅铁", idea[key]])
        toadd.append(["锰硅", idea[key]])
    if key == "天然橡胶":
        topop.append("天然橡胶")
        toadd.append(["橡胶", idea[key]])

    if key == "沪铜":
        topop.append("沪铜")
        toadd.append(["铜", idea[key]])
    if key == "沪铝":
        topop.append("沪铝")
        toadd.append(["铝", idea[key]])
    if key == "沪锌":
        topop.append("沪锌")
        toadd.append(["锌", idea[key]])
    if key == "沪铅":
        topop.append("沪铅")
        toadd.append(["铅", idea[key]])
    if key == "油脂":
        topop.append("油脂")
        toadd.append(["棕榈油", idea[key]])
        toadd.append(["豆油", idea[key]])
        toadd.append(["菜油", idea[key]])

    if key == "豆粕/菜粕":
        topop.append("豆粕/菜粕")
        toadd.append(["豆粕", idea[key]])
        toadd.append(["菜粕", idea[key]])

for i in topop:
    idea.pop(i)
for i in toadd:
    idea[i[0]] = i[1]

dongwu_old = {}
for i in idea:
    dongwu_old[i] = idea[i][:]

for key in idea:
    if not idea[key].isdecimal():
        idea[key] = keywords.simplify_sent(idea[key])


for i in dongwu_old:
    if i in idea:
        dongwu_old[i] = idea[i] + " 东吴 " + dongwu_old[i]
    else:
        dongwu_old[i] = ""

dongwu_idea = idea

###########################################整合开始

idea_combined = {}
for i in [zhongxin_old, guotai_old, guotou_old, guangda_old, zhongqi_old, wukuang_old, beite_old,
          yinhe_old, yinhenong_old, guangfa_old, guangzhou_old, guoxin_old, yongan_old, haitong_old,
          guodu_old, luzheng_old, nanhua_old, dongxing_old, hundungong_old, hundunneng_old, hundunagri_old,
          hongye_old, dongwu_old]:
    for j in i:
        if j in idea_combined:
            idea_combined[j].append(i[j])
        else:
            idea_combined[j] = [i[j]]

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

with open('其他.txt', encoding='gbk') as f:
    lines = f.readlines()
for l in lines:
    if is_number(l.strip('\n').split(" ")[-1]):
        if len(l.strip('\n').split(" ")) == 2:
            name = l.strip('\n').split(" ")[0]
            score = l.strip('\n').split(" ")[1]
            if not is_number(score):
                score = keywords.simplify_sent(score)
            for i in idea_combined:
                if i == "MEG" and name == "乙二醇":
                    idea_combined[i].append(score)
                if i == name:
                    idea_combined[i].append(score)
        elif len(l.strip('\n').split(" ")) > 2:
            name = l.strip('\n').split(" ")[:-1]
            score = l.strip('\n').split(" ")[-1]
            if not is_number(score):
                score = keywords.simplify_sent(score)
            for i in idea_combined:
                for j in name:
                    if i == "MEG" and j == "乙二醇":
                        idea_combined[i].append(score)
                    if i == j:
                        idea_combined[i].append(score)
order = ["黑色金属","铁矿","焦煤","焦炭","动力煤","螺纹","热卷","硅铁","锰硅","有色金属","铝","铜","锌","锡","镍","不锈钢","铅","贵金属","黄金","白银","能源化工",
 "原油","燃油","低硫燃油","LPG","沥青","甲醇","MEG","PTA","短纤","苯乙烯","PVC","PP","塑料","尿素","橡胶","纯碱","玻璃","纸浆","农产品","棕榈油","豆油","菜油","豆粕","菜粕","豆一","玉米","淀粉","鸡蛋","白糖","棉花","棉纱"
 "苹果","花生","红枣","生猪"]
idea_combined_sorted = {}
total = 0
count = 0
prev_type = ""
total_all = 0.0
count_all = 0.0
for i in order:
    if i not in idea_combined and i in ["黑色金属","有色金属","贵金属","能源化工","农产品"]:
        if count != 0 and prev_type != "":
            idea_combined_sorted[prev_type] = total / count
        total = 0.0
        count = 0.0
        prev_type = i
        idea_combined_sorted[i] = 999.99
    elif i in idea_combined:
        count_sub = 0.0
        total_sub = 0.0
        for j in idea_combined[i]:
            count += 1
            total += float(j.split(" ")[0])
            count_sub += 1
            total_sub += float(j.split(" ")[0])
            count_all += 1
            total_all += float(j.split(" ")[0])
        idea_combined_sorted[i + " " + str('{0:.4}'.format(round(total_sub / count_sub, 4)))] = idea_combined[i]
if count != 0:
    idea_combined_sorted[prev_type] = total / count

with open('详细观点.txt', 'w') as f:
    last = []
    last_spec = []
    for i in idea_combined_sorted:
        f.write(i + '\n')
        last_spec.append(i + '\n')
        if type(idea_combined_sorted[i]) == float:
            f.write(i + " " + str('{0:.6}'.format(round(idea_combined_sorted[i], 4))))
            f.write('\n')
            f.write('\n')
            last.append(i + " " + str('{0:.6}'.format(round(idea_combined_sorted[i], 4)) + '\n'))
            continue
        for j in idea_combined_sorted[i]:
            if j.strip():
                for i in range(len(j)//100+1):
                    if i != 0:
                        f.write("       ")
                    try:
                        f.write(j[i*100:(i+1)*100].strip('\n') + '\n')
                    except Exception:
                        a = 1
        f.write('\n')
    f.write("分数总结:\n")
    for i in last_spec:
        f.write(i)
    f.write('\n')
    f.write("类别总结:\n")
    f.write("全市场：" + str('{0:.6}'.format(round(total_all/count_all, 4)) + '\n'))
    for i in last:
        f.write(i)

combined = {}
for i in [guotai_idea, anxin_idea, guangda_idea, citrix_idea,zhongqi_idea, wukuang_idea, beite_idea,
          yinhe_idea, yinhenong_idea, guangfa_idea, guangzhou_idea, guoxin_idea, yongan_idea,
          haitong_idea, guodu_idea, luzheng_idea, nanhua_idea, dongxing_idea, hundungong_idea,
          hundunneng_idea, hundunagri_idea, hongye_idea, dongwu_idea]:
    for j in i:
        if j.strip() == "":
            abc = 1
        if j in combined:
            combined[j].append(float(i[j]))
        else:
            combined[j] = [float(i[j])]





############## 详细观点
with open('其他.txt', encoding='gbk') as f:
    lines = f.readlines()
for l in lines:
    if is_number(l.strip('\n').split(" ")[-1]):
        if len(l.strip('\n').split(" ")) == 2:
            name = l.strip('\n').split(" ")[0]
            score = l.strip('\n').split(" ")[1]
            if not is_number(score):
                continue
            for i in combined:
                if i == "MEG" and name == "乙二醇":
                    combined[i].append(float(score))
                if i == name:
                    combined[i].append(float(score))
        elif len(l.strip('\n').split(" ")) > 2:
            name = l.strip('\n').split(" ")[:-1]
            score = l.strip('\n').split(" ")[-1]
            if not is_number(score):
                continue
            for i in combined:
                for j in name:
                    if i == "MEG" and j == "乙二醇":
                        combined[i].append(float(score))
                    if i == j:
                        combined[i].append(float(score))

import xlwt
try:
    f = open("详细观点.txt")
    xls = xlwt.Workbook()
    sheet = xls.add_sheet('sheet1',cell_overwrite_ok=True)
    x = 0
    while x < 5000:
        line = f.readline()
        sheet.write(x,0,line)
        x+=1
    f.close()
    xls.save("详细观点.xls")
except:
    raise

############## 详细观点分公司
with open('详细观点分公司.txt', 'w') as f:
    for i in [zhongxin_old, guotai_old, guotou_old, guangda_old, zhongqi_old, wukuang_old,
              beite_old, yinhe_old, yinhenong_old, guangfa_old, guangzhou_old, guoxin_old, yongan_old,
              haitong_old, guodu_old, luzheng_old, nanhua_old, dongxing_old, hundungong_old,
              hundunneng_old, hundunagri_old, hongye_old, dongwu_old]:
        new = True
        for j in i:
            if new:
                f.write(i[j].split(" ")[1] + "\n\n")
                new = False
            try:
                f.write( j + " "+ i[j].split(" ")[0] + "  " + "".join(i[j].split(" ")[2:]) + '\n')
            except Exception:
                a = 1
        f.write('\n\n\n')

try:
    f = open("详细观点分公司.txt")
    xls = xlwt.Workbook()
    sheet = xls.add_sheet('sheet1',cell_overwrite_ok=True)
    x = 0
    while x < 5000:
        line = f.readline()
        sheet.write(x,0,line)
        x+=1
    f.close()
    xls.save("详细观点分公司.xls")
except:
    raise


for i in combined:
    print(i + " " + str(sum(combined[i])) + " " + str(len(combined[i])))
    if len(combined[i]) == 1:
        combined[i] = sum(combined[i]) / (len(combined[i]) + (4 - len(combined[i])) * (4 - len(combined[i])) * 0.5)
    elif len(combined[i]) == 2:
        combined[i] = sum(combined[i]) / (len(combined[i]) + (4 - len(combined[i])) * (4 - len(combined[i])) * 0.2)
    elif len(combined[i]) <= 4:
        combined[i] = sum(combined[i]) / (len(combined[i]) + (4 - len(combined[i])) * (4 - len(combined[i])) * 0.2)
    elif len(combined[i]) == 5:
        combined[i] = sum(combined[i]) / ((len(combined[i])) - 0.7)
    elif len(combined[i]) >= 6:
        combined[i] = sum(combined[i]) / ((len(combined[i])) - 0.15 * len(combined[i]))
import pandas as pd

result = pd.DataFrame(combined.items(), columns=['Name', 'Value'])
final = result.sort_values(by='Value', ascending=False)

for index, row in final.iterrows():
    same = []
    if row["Name"] not in ["能源：","金融:","股指期权","期权","宏观","金融","股指","股指期权","国债"]:
        print(row["Name"] + " " + str('{0:.6}'.format(round(row["Value"], 6))))
