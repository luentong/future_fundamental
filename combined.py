import keywords
###########################################中信开始

with open('中信.txt') as f:
    lines = f.readlines()

line = lines[0]
keyword = ["黄金/白银", "黑色", "钢材", "铁矿", "焦炭", "焦煤", "动力煤", "有色", "铜", "铝", "锌", "铅", "镍", "不锈钢", "锡", "能源", "原油", "沥青",
           "燃料油", "低硫燃料油",
           "LPG", "化工", "甲醇", "尿素", "乙二醇", "PTA", "短纤", "PP", "塑料", "苯乙烯",
           "PVC", "软商品", "橡胶", "纸浆", "棉花", "白糖", "农产品", "油脂", "蛋白粕", "玉米/淀粉", "生猪", "鸡蛋", "玻璃"]
indexes = [0, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 22, 23, 24, 25, 26, 27, 28, 29, 30, 32, 33,
           34, 35, 37, 38, 39, 40, 41]
idea = {}
for l in lines:
    print(l)
    if " "  in l:
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

idea.pop("低硫燃油")

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

with open('国泰君安.txt') as f:
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
    if key == "热轧卷板":
        topop.append("热轧卷板")
        toadd.append(["热卷", idea[key]])
    if key == "玉米":
        toadd.append(["淀粉", idea[key]])
    if key == "LLDPE":
        topop.append("LLDPE")
        toadd.append(["塑料", idea[key]])
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
with open('国投安信.txt', encoding='utf-8') as f:
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
    if key == "天然橡胶":
        topop.append("天然橡胶")
        toadd.append(["橡胶", idea[key]])
    if key == "棕榈油&豆油":
        topop.append("棕榈油&豆油")
        toadd.append(["棕榈油", idea[key]])
        toadd.append(["豆油", idea[key]])
    if key == "乙二醇":
        topop.append("乙二醇")
        toadd.append(["MEG", idea[key]])
    if key == "聚丙烯&纯碱":
        topop.append("聚丙烯&纯碱")
        toadd.append(["PP", idea[key]])
        toadd.append(["纯碱", idea[key]])
    # 菜粕菜油自己改
    if key == "菜粕&菜油":
        topop.append("菜粕&菜油")
        toadd.append(["菜粕", "0.8"])
        toadd.append(["菜油", "0.5"])
    # # 玻璃纯碱自己改
    # if key == "纯碱":
    #     topop.append("纯碱")
    #     toadd.append(["纯碱", "1"])
    # if key == "玻璃":
    #     topop.append("玻璃")
    #     toadd.append(["玻璃", "0"])
    # if key == "塑料":
    #     topop.append("塑料")
    #     toadd.append(["塑料", "0"])
    # if key == "PP":
    #     topop.append("PP")
    #     toadd.append(["PP", "-0.7"])

for i in topop:
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

with open('光大期货.txt', encoding='utf-8') as f:
    lines = f.readlines()
idea = {}
prev = ""
for l in lines:
    if len(l) < 20 and l.strip("\n") != "" and "操作建议" not in l and "期货方面" not in l and "现货方面" not in l:
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
    if key == "燃料油":
        topop.append("燃料油")
        toadd.append(["燃油", idea[key]])
    if key == "聚烯烃":
        topop.append("聚烯烃")
        toadd.append(["塑料", idea[key]])
        toadd.append(["PVC", idea[key]])
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
        toadd.append(["PTA", idea[key]])
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

for i in topop:
    idea.pop(i)
for i in toadd:
    idea[i[0]] = i[1]

if "国债" in idea:
    idea.pop("国债")
if "股指" in idea:
    idea.pop("股指")


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

topop = []
toadd = []
for key in idea:
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

with open('五矿.txt',encoding='utf-8') as f:
    lines = f.readlines()
idea = {}
items = ["油脂","蛋白粕","鸡蛋","生猪","白糖","苹果","棉花","贵金属","铜","锌","铅","原油",
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


with open('倍特期货.txt',encoding='utf-8') as f:
    lines = f.readlines()
idea = {}
items = ["金银","铜","尿素","橡胶","苹果","豆粕","螺纹钢","鸡蛋","油脂"]
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

with open('银河期货.txt',encoding='utf-8') as f:
    lines = f.readlines()
idea = {}
items = ["铁矿","钢材","焦煤焦炭","镍及不锈钢","铜","锌","铝","沥青","原油","燃料油","纸浆","天然橡胶及20号胶","甲醇","尿素","动力煤","PTA","PF","MEG","EB","PP","塑料","PVC","EB"]
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
        if prev_item == "焦煤焦炭":
            if "驱动角度看" in l:
                next = False
                idea[prev_item] = l.strip().strip('\n').split("驱动角度看")[0]
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


###########################################广发开始

import keywords

with open('广发期货.txt',encoding='utf-8') as f:
    lines = f.readlines()
idea = {}
items = ["贵金属：","铜：","锌：","铝：","镍：","不锈钢：","锡：","钢材：","铁矿石：","焦炭：","焦煤：","动力煤：","豆粕：","油脂：","生猪：","玉米：","白糖：","棉花：","鸡蛋：","花生：","红枣：",
         "原油：","沥青：","PTA：","乙二醇：","短纤：","苯乙烯：","LLDPE：","PP：","尿素:","PVC：","甲醇：","纯碱：","玻璃：","橡胶：","纸浆："]
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
    if stripped in items:
        next = True
        prev_item = stripped
        continue
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
    if key == "乙二醇":
        topop.append("乙二醇")
        toadd.append(["MEG", idea[key]])
    if key == "LLDPE":
        topop.append("LLDPE")
        toadd.append(["塑料", idea[key]])
        toadd.append(["PP", idea[key]])
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


with open('广州期货.txt',encoding='utf-8') as f:
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

with open('国信期货.txt',encoding='utf-8') as f:
    lines = f.readlines()
idea = {}
items = ["贵金属","铜铝","锌","螺纹钢","铁合金","焦煤焦炭","豆类","油脂","白糖","棉花","玉米","生猪","花生","苹果","PTA","聚烯烃","原油","橡胶","燃料油","沥青","甲醇"]
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
    if key == "焦煤焦炭":
        topop.append("焦煤焦炭")
        toadd.append(["焦煤", idea[key]])
        toadd.append(["焦炭", idea[key]])
    if key == "燃料油":
        topop.append("燃料油")
        toadd.append(["燃油", idea[key]])
    if key == "贵金属":
        topop.append("贵金属")
        toadd.append(["黄金", idea[key]])
        toadd.append(["白银", idea[key]])
    if key == "铜铝":
        topop.append("铜铝")
        toadd.append(["铜", idea[key]])
        toadd.append(["铝", idea[key]])
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
        toadd.append(["豆一", idea[key]])
        toadd.append(["豆粕", idea[key]])
    if key == "油脂":
        topop.append("油脂")
        toadd.append(["豆油", idea[key]])
        toadd.append(["菜油", idea[key]])
        toadd.append(["棕榈油", idea[key]])
    if key == "聚烯烃":
        topop.append("聚烯烃")
        toadd.append(["PVC", idea[key]])
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

###########################################华泰开始

with open('华泰期货.txt',encoding='utf-8') as f:
    lines = f.readlines()
idea = {}
items = ["原油","燃料油","沥青","PTA","甲醇","橡胶","贵金属","铜","镍不锈钢","锌铝","钢材","铁矿石","双焦","动力煤","玻璃纯碱","油脂油料","玉米与淀粉","鸡蛋","生猪","郑棉"]
next = False
prev_item = ""
for l in lines:
    print("华泰" + l)
    stripped = l.strip().strip('\n')
    if stripped == "":
        continue
    if stripped.split("：")[0] in items:
        next = True
        prev_item = stripped.split("：")[0]
        continue
    if "策略：" in l and len(l) < 5:
        next = False
    if next:
        if prev_item in idea:
            if "策略：" in l:
                if "套利：" in l:
                    idea[prev_item] = l.strip().strip('\n').split("套利：")[0]
                    next = False
                else:
                    idea[prev_item] = l.strip().strip('\n')
                    next = False
            else:
                idea[prev_item] += l.strip().strip('\n')
        else:
            if "策略：" in l:
                if "套利：" in l:
                    idea[prev_item] = l.strip().strip('\n').split("套利：")[0]
                    next = False
                else:
                    idea[prev_item] = l.strip().strip('\n')
                    next = False
            else:
                idea[prev_item] = l.strip().strip('\n')

topop = []
toadd = []
for key in idea:
    if key == "双焦":
        topop.append("双焦")
        toadd.append(["焦煤", idea[key]])
        toadd.append(["焦炭", idea[key]])
    if key == "燃料油":
        topop.append("燃料油")
        toadd.append(["燃油", idea[key]])
    if key == "贵金属":
        topop.append("贵金属")
        toadd.append(["黄金", idea[key]])
        toadd.append(["白银", idea[key]])
    if key == "锌铝":
        topop.append("锌铝")
        toadd.append(["锌", idea[key]])
        toadd.append(["铝", idea[key]])
    if key == "钢材":
        topop.append("钢材")
        toadd.append(["螺纹", idea[key]])
        toadd.append(["热卷", idea[key]])
    if key == "玻璃纯碱":
        topop.append("玻璃纯碱")
        toadd.append(["锰硅", idea[key]])
        toadd.append(["硅铁", idea[key]])
    if key == "镍不锈钢":
        topop.append("镍不锈钢")
        toadd.append(["镍", idea[key]])
        toadd.append(["不锈钢", idea[key]])
    if key == "铁矿石":
        topop.append("铁矿石")
        toadd.append(["铁矿", idea[key]])
    if key == "玉米与淀粉":
        topop.append("玉米与淀粉")
        toadd.append(["玉米", idea[key]])
        toadd.append(["淀粉", idea[key]])

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
        huatai_old[i] = idea[i] + " 华泰 " + huatai_old[i]
    else:
        huatai_old[i] = ""

for i in huatai_old:
    print(i)
    print(huatai_old[i])
huatai_idea = idea

###########################################整合开始

idea_combined = {}
for i in [zhongxin_old, guotai_old, guotou_old, guangda_old, zhongqi_old, wukuang_old, beite_old, yinhe_old, guangfa_old, guangzhou_old, guoxin_old, huatai_old]:
    for j in i:
        if j in idea_combined:
            idea_combined[j].append(i[j])
        else:
            idea_combined[j] = [i[j]]
with open('详细观点.txt', 'w') as f:
    for i in idea_combined:
        f.write(i + '\n')
        for j in idea_combined[i]:
            if j.strip():
                for i in range(len(j)//100+1):
                    if i != 0:
                        f.write("       ")
                    f.write(j[i*100:(i+1)*100].strip('\n') + '\n')
        f.write('\n')

combined = {}
for i in [guotai_idea, anxin_idea, guangda_idea, citrix_idea,zhongqi_idea, wukuang_idea, beite_idea, yinhe_idea, guangfa_idea, guangzhou_idea, guoxin_idea, huatai_idea]:
    for j in i:
        if j.strip() == "":
            print(i)
        if j in combined:
            combined[j].append(float(i[j]))
        else:
            combined[j] = [float(i[j])]

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
# 自己加比如东证，华泰，宝城的

with open('其他.txt', encoding='utf-8') as f:
    lines = f.readlines()
for l in lines:
    if is_number(l.strip('\n').split(" ")[-1]):
        if len(l.strip('\n').split(" ")) == 2:
            name = l.strip('\n').split(" ")[0]
            score = l.strip('\n').split(" ")[1]
            if not is_number(score):
                score = keywords.simplify_sent(score)
            for i in combined:
                if i == "MEG" and name == "乙二醇":
                    combined[i].append(float(score))
                if i == name:
                    combined[i].append(float(score))
        elif len(l.strip('\n').split(" ")) > 2:
            name = l.strip('\n').split(" ")[:-1]
            score = l.strip('\n').split(" ")[-1]
            if not is_number(score):
                score = keywords.simplify_sent(score)
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

with open('详细观点分公司.txt', 'w') as f:
    for i in [zhongxin_old, guotai_old, guotou_old, guangda_old, zhongqi_old, wukuang_old,
              beite_old, yinhe_old, guangfa_old, guangzhou_old, guoxin_old, huatai_old]:
        new = True
        for j in i:
            if new:
                f.write(i[j].split(" ")[1] + "\n\n")
                new = False
            f.write( j + " "+ i[j].split(" ")[0] + "  " + i[j].split(" ")[2] + '\n')
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
#print(final)
with open('之前的数据.txt', encoding='utf-8') as f:
    lines = f.readlines()
before = []
for l in lines:
    if l != "\n":
        name = l.strip('\n').split()[0]
        score = l.strip('\n').split()[1]
        before.append([name,score])

for index, row in final.iterrows():
    same = []
    for i in before:
        if i[0] == row["Name"]:
            same.append(i[1])
    if row["Name"] not in ["20号胶","能源：","金融:","股指期权","股指","花生","国际铜","低硫燃油","棉纱","国债","低硫燃料油"]:
        print(row["Name"] + " " + str('{0:.6}'.format(round(row["Value"], 6))))
for index, row in final.iterrows():
    same = []
    for i in before:
        if i[0] == row["Name"]:
            same.append(i[1])
    if row["Name"] not in ["20号胶", "能源：", "金融:", "股指期权", "股指", "花生", "国际铜", "低硫燃油", "棉纱", "国债", "低硫燃料油"]:
        print(row["Name"] + " " + str('{0:.6}'.format(round(row["Value"],6))) + " " + " ".join(same))
