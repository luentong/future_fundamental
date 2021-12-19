import copy

low = ["偏弱", "下滑", "悲观", "弱势", "下行", "走弱", "做空", "偏空", "下跌", "试空", "回落", "短空", "空单操作",
       "逐步布空","承压", "超涨", "沽空", "回吐", "逢高空", "下破", "跳水", "弱调整", "弱趋势", "冲低", "上冲", "赶底", "走低", "大跌", "布局空单", "持空","下调","高抛","空单继续持有","回调整理"]
high = ["偏强", "上涨", "走强", "偏多", "做多", "试多", "上行", "企稳", "乐观", "强势", "走强", "提振", "坚挺","探底回升","企稳反弹"
        "反弹", "回升", "短多", "多单操作", "超跌", "沽多", "逢低多", "上破", "强调整", "冲高", "下冲", "赶顶", "走高", "大涨", "布局多单", "持多","上调","多单继续持有"]
fluc = ["观望", "不宜", "离场", "观察", "观望", "上行承压", "上行乏力", "震荡对待", "先扬后抑", "短期反弹,趋势偏弱", "下行驱动逐渐放缓",
        "反弹难持续", "正套", "反套", "上行空间受限", "暂无利好", "高位震荡", "盘面震荡", "反弹空间有限", "多单谨慎持有", "空单谨慎持有",
        "反弹幅度已经较高", "低点支撑", "反弹难持续", "涨势趋缓", "跟涨情绪减弱", "近强远弱", "近弱远强", "止跌", "弱平衡", "阶段性震荡", "震荡中",
        "下行空间受限","上行空间有限","下行空间有限","底部价格已现","顶部已现","底部已现","顶部价格已现","反弹后抛空","逢高抛空","多单止盈",
        "不宜过分看跌","空单止盈","短线持多","短多看待","底部空间或将有限",'空单轻仓持有','多单轻仓持有',"短期内震荡行情","呈现震荡格局","仍较抗跌",
        "震荡走势为主","反弹幅度有限","震荡整理","限制价格回升","短多长空","短空长多","不宜过分看跌","不宜过分看多","反复震荡","不过于追空","不过与追多"]
other = ['高升水']
import jieba

for i in low:
    jieba.add_word(i)
for i in high:
    jieba.add_word(i)
for i in fluc:
    jieba.add_word(i)
for i in other:
    jieba.add_word(i)

###########################################中信开始

with open('中信.txt') as f:
    lines = f.readlines()

line = lines[0]
keyword = ["黄金/白银", "黑色", "钢材", "铁矿", "焦炭", "焦煤", "动力煤", "有色", "铜", "铝", "锌", "铅", "镍", "不锈钢", "锡", "能源", "原油", "沥青",
           "燃料油", "低硫燃料油",
           "LPG", "化工", "甲醇", "尿素", "乙二醇", "PTA", "短纤", "PP", "塑料", "苯乙烯",
           "PVC", "软商品", "橡胶", "纸浆", "棉花", "白糖", "农产品", "油脂", "蛋白粕", "玉米/淀粉", "生猪", "鸡蛋"]
indexes = [0, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 22, 23, 24, 25, 26, 27, 28, 29, 30, 32, 33,
           34, 35, 37, 38, 39, 40, 41]
idea = {}
for i in indexes:
    if i != 41:
        after = "".join(line.split(keyword[i])[1:])
        before = after.split(keyword[i + 1])[0]
        idea[keyword[i]] = before
    else:
        after = "".join(line.split(keyword[i])[1:])
        idea[keyword[i]] = after

zhongxin_old = {}
for i in idea:
    zhongxin_old[i] = idea[i][:]


def simplify_sent(c):
    cut = jieba.cut(c)
    cut_list = []
    for i in cut:
        cut_list.append(i)
    cut_list.reverse()
    for c in cut_list:
        if "观察" in c or "观望" in c or "震荡对待" in c or "上行空间受限" in c or "下行空间受限" in c or "波动风险加大" in c \
                or "震荡为主" in c or "高位震荡" in c or "盘面震荡" in c or "反弹空间有限" in c or "反弹幅度已经较高" in c \
                or "反弹难持续" in c or "跟涨情绪减弱" in c or "阶段性震荡" in c or "震荡中" in c or "上行空间有限" in c or "下行空间有限" in c or \
                "底部空间或将有限" in c or "短期内震荡行情" in c or "呈现震荡格局" in c or "震荡走势为主" in c or "震荡整理" in c or "反复震荡" in c:
            return "0"
        if "短期反弹,趋势偏弱" in c or "先扬后抑" in c or "近强远弱" in c or "底部价格已现" in c or "底部已现" in c or "短线持多" in c \
                or "短多看待" in c or '多单轻仓持有' in c:
            return '0.8'
        if "布局多单" in c:
            return "1"
        if "反弹难持续" in c or "布局空单" in c:
            return "-1"
        if "近弱远强" in c or "顶部价格已现" in c or "顶部已现" in c or "反弹后抛空" in c or "逢高抛空" in c or '空单轻仓持有' in c:
            return "-0.8"
        if "下行驱动逐渐放缓" in c or "弱平衡" in c or "不过于追空" in c:
            return '-0.5'
        if "正套" in c or "多单谨慎持有" in c or "低点支撑" in c or "涨势趋缓" in c or "空单止盈" in c or "仍较抗跌" in c or "反弹幅度有限" in c or "短多长空" in \
                c or "不宜过分看多" in c or "不过于追多" in c:
            return '0.5'
        if "反套" in c or "空单谨慎持有" in c or "多单止盈" in c or "不宜过分看跌" in c or "限制价格回升" in c or "短空长多" in c:
            return '-0.5'
        if "反弹难持续" in c:
            for i in low:
                if i in c:
                    return "-1"
        if "多TA" in c:
            idea["PTA"] = '1'
            if "空EG" in c:
                idea["乙二醇"] = '-1'
            return "1"
        for i in fluc:
            if i in c:
                return "0"
        for i in high:
            if i in c:
                return "1"
        for i in low:
            if i in c:
                return "-1"
    return "0"

topop = []
toadd = []
for key in idea:
    if not idea[key].isdecimal():
        idea[key] = simplify_sent(idea[key])
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
        toadd.append(["豆粕", '0'])
        toadd.append(["菜粕", '0'])
    if key == "乙二醇":
        topop.append("乙二醇")
        toadd.append(["MEG", idea[key]])
    if key == "白糖":
        topop.append("白糖")
        toadd.append(["白糖", '-0.3'])

for i in topop:
    idea.pop(i)
for i in toadd:
    idea[i[0]] = i[1]

idea.pop("低硫燃油")
print(idea)
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

guotai_old = {}
for i in idea:
    guotai_old[i] = idea[i][:]

topop = []
toadd = []
for key in idea:
    if not idea[key].isdecimal():
        idea[key] = simplify_sent(idea[key])
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
    if key == "铝":
        topop.append("铝")
        toadd.append(["铝", '0.3'])
for i in topop:
    idea.pop(i)
for i in toadd:
    idea[i[0]] = i[1]

print(idea)
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

guotou_old = {}
for i in idea:
    guotou_old[i] = idea[i][:]

topop = []
toadd = []
for key in idea:
    if not idea[key].isdecimal():
        idea[key] = simplify_sent(idea[key])
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
    # 菜粕菜油自己改
    if key == "菜粕&菜油":
        topop.append("菜粕&菜油")
        toadd.append(["菜粕", "0.7"])
        toadd.append(["菜油", "-0.7"])
    # 玻璃纯碱自己改
    if key == "纯碱":
        topop.append("纯碱")
        toadd.append(["纯碱", "0"])
    if key == "玻璃":
        topop.append("玻璃")
        toadd.append(["玻璃", "0"])
    if key == "塑料":
        topop.append("塑料")
        toadd.append(["塑料", "0"])
    if key == "PP":
        topop.append("PP")
        toadd.append(["PP", "-0.7"])

for i in topop:
    idea.pop(i)
for i in toadd:
    idea[i[0]] = i[1]

idea.pop("股指")
print(idea)
anxin_idea = idea

###########################################光大开始

with open('光大期货.txt', encoding='utf-8') as f:
    lines = f.readlines()
idea = {}
prev = ""
for l in lines:
    if len(l) < 20 and l.strip("\n") != "":
        a1 = l.replace("【", "")
        a2 = a1.replace("】", "")
        a3 = a2.replace("\n", "")
        prev = a3
    elif l.strip("\n") != "":
        a4 = l.replace("\n", "")
        idea[prev] = a4

guangda_old = {}
for i in idea:
    guangda_old[i] = idea[i][:]
topop = []
toadd = []
for key in idea:
    if not idea[key].isdecimal():
        idea[key] = simplify_sent(idea[key])
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
    if key == "铁矿石":
        topop.append("铁矿石")
        toadd.append(["铁矿", idea[key]])
    if key == "钢材":
        topop.append("钢材")
        toadd.append(["螺纹", idea[key]])
        toadd.append(["热卷", idea[key]])
    if key == "纯碱":
        topop.append("纯碱")
        toadd.append(["纯碱", "0.7"])

for i in topop:
    idea.pop(i)
for i in toadd:
    idea[i[0]] = i[1]

idea.pop("国债")
idea.pop("股指")
print(idea)
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
    if "：" in l and len(l) <= 30:
        idea[l.split('：')[0]] = l.split('：')[1]

zhongqi_old = {}
for i in idea:
    zhongqi_old[i] = idea[i][:]

topop = []
toadd = []
for key in idea:
    if not idea[key].isdecimal():
        idea[key] = simplify_sent(idea[key])
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



for i in topop:
    idea.pop(i)
for i in toadd:
    idea[i[0]] = i[1]

zhongqi_idea = idea


for key in idea:
    print(key)
    print(idea[key])

###########################################五矿开始

with open('五矿.txt',encoding='utf-8') as f:
    lines = f.readlines()
idea = {}
items = ["油脂","蛋白粕","鸡蛋","生猪","白糖","苹果","棉花","贵金属","铜","锌","铅",
         "铝","镍","锡","锰硅","硅铁","铁矿石","钢材","双焦","橡胶","甲醇","尿素","苯乙烯","PVC","PTA","玻璃","纯碱","LPG","沥青"]
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

wukuang_old = {}
for i in idea:
    wukuang_old[i] = idea[i][:]

topop = []
toadd = []
for key in idea:
    if not idea[key].isdecimal():
        idea[key] = simplify_sent(idea[key])
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
beite_old = {}
for i in idea:
    beite_old[i] = idea[i][:]

topop = []
toadd = []
for key in idea:
    if not idea[key].isdecimal():
        idea[key] = simplify_sent(idea[key])
    if key == "贵金属":
        topop.append("贵金属")
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
        toadd.append(["菜油", idea[key]])
        toadd.append(["棕榈油", idea[key]])
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

beite_idea = idea



###########################################整合开始

idea_combined = {}
for i in [zhongxin_old, guotai_old, guotou_old, guangda_old, zhongqi_old, wukuang_old, beite_old]:
    for j in i:
        if j in idea_combined:
            idea_combined[j].append(i[j])
        else:
            idea_combined[j] = [i[j]]
with open('详细观点.txt', 'w') as f:
    for i in idea_combined:
        f.write(i + '\n')
        for j in idea_combined[i]:
            f.write(j + '\n')
        f.write('\n')

combined = {}
for i in [guotai_idea, anxin_idea, guangda_idea, citrix_idea,zhongqi_idea, wukuang_idea, beite_idea]:
    for j in i:
        if j in combined:
            combined[j].append(float(i[j]))
        else:
            combined[j] = [float(i[j])]
# 自己加比如东证，华泰，宝城的

with open('其他.txt', encoding='utf-8') as f:
    lines = f.readlines()
for l in lines:
    if len(l.strip('\n').split(" ")) == 2:
        name = l.strip('\n').split(" ")[0]
        score = l.strip('\n').split(" ")[1]
        if not score.isdecimal():
            score = simplify_sent(score)
        for i in combined:
            if i == name:
                combined[i].append(float(score))
    elif len(l.strip('\n').split(" ")) > 2:
        name = l.strip('\n').split(" ")[:-1]
        score = l.strip('\n').split(" ")[-1]
        if not score.isdecimal():
            score = simplify_sent(score)
        for i in combined:
            for j in name:
                if i == j:
                    combined[i].append(float(score))

for i in combined:
    print(i + " " + str(sum(combined[i])) + " " + str(len(combined[i])))
    if len(combined[i]) == 1:
        combined[i] = sum(combined[i]) / (len(combined[i]) + (4 - len(combined[i])) * (4 - len(combined[i])) * 0.5)
    elif len(combined[i]) == 2:
        combined[i] = sum(combined[i]) / (len(combined[i]) + (4 - len(combined[i])) * (4 - len(combined[i])) * 0.2)
    elif len(combined[i]) <= 4:
        combined[i] = sum(combined[i]) / (len(combined[i]) + (4 - len(combined[i])) * (4 - len(combined[i])) * 0.2)
    elif len(combined[i]) == 5:
        combined[i] = sum(combined[i]) / ((len(combined[i])) - 0.4)
    elif len(combined[i]) >= 6:
        combined[i] = sum(combined[i]) / ((len(combined[i])) - 0.7)
import pandas as pd

result = pd.DataFrame(combined.items(), columns=['Name', 'Value'])
final = result.sort_values(by='Value', ascending=False)
#print(final)
with open('之前的数据.txt', encoding='utf-8') as f:
    lines = f.readlines()
before = []
for l in lines:
    if l != "\n":
        name = l.strip('\n').split()[1]
        score = l.strip('\n').split()[2]
        before.append([name,score])

for index, row in final.iterrows():
    same = []
    for i in before:
        if i[0] == row["Name"]:
            same.append(i[1])
    print(row["Name"] + " " + str('{0:.6}'.format(round(row["Value"], 6))))
for index, row in final.iterrows():
    same = []
    for i in before:
        if i[0] == row["Name"]:
            same.append(i[1])
    print(row["Name"] + " " + str('{0:.6}'.format(round(row["Value"],6))) + " " + " ".join(same))
