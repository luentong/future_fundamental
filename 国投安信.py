with open('国投安信.txt', encoding='utf-8') as f:
    lines = f.readlines()
idea = {}
prev = ""
for l in lines:
    if "【" in l and len(l) < 20:
        a1 = l.replace("【","")
        a2 = a1.replace("】", "")
        a3 = a2.replace("\n", "")
        prev = a3
    elif l.strip("\n") != "":
        a4 = l.replace("\n", "")
        idea[prev] = a4


low = ["偏弱", "下滑", "悲观", "弱势", "下行", "走弱", "做空", "偏空", "下跌", "试空", "回落", "短空", "空单操作",
       "承压", "超涨", "沽空", "回吐", "逢高空", "下破", "跳水", "弱调整", "弱趋势", "冲低", "上冲", "赶底", "走低", "大跌", "布局空单", "持空","下调","高抛","空单继续持有"]
high = ["偏强", "上涨", "走强", "偏多", "做多", "试多", "上行", "企稳", "乐观", "强势", "走强", "提振", "坚挺",
        "反弹", "回升", "短多", "多单操作", "超跌", "沽多", "逢低多", "上破", "强调整", "冲高", "下冲", "赶顶", "走高", "大涨", "布局多单", "持多","上调","多单继续持有"]
fluc = ["观望", "不宜", "离场", "观察", "观望", "上行承压", "上行乏力", "震荡对待", "先扬后抑", "短期反弹,趋势偏弱", "下行驱动逐渐放缓",
        "反弹难持续", "正套", "反套", "上行空间受限", "暂无利好", "高位震荡", "盘面震荡", "反弹空间有限", "多单谨慎持有", "空单谨慎持有",
        "反弹幅度已经较高", "低点支撑", "反弹难持续", "涨势趋缓", "跟涨情绪减弱", "近强远弱", "近弱远强", "止跌", "弱平衡", "阶段性震荡", "震荡中",
        "下行空间受限","上行空间有限","下行空间有限","底部价格已现","顶部已现","底部已现","顶部价格已现","反弹后抛空","逢高抛空","多单止盈",
        "不宜过分看跌","空单止盈","短线持多","短多看待","底部空间或将有限",'空单轻仓持有','多单轻仓持有',"短期内震荡行情","呈现震荡格局","仍较抗跌",
        "震荡走势为主","反弹幅度有限","震荡整理","限制价格回升"]
other = ['高升水']

import jieba
for i in low:
    jieba.add_word(i)
for i in high:
    jieba.add_word(i)
for i in fluc:
    jieba.add_word(i)
def simplify(c):
    cut = jieba.cut(c)
    cut_list = []
    for i in cut:
        cut_list.append(i)
    print(cut_list)
    cut_list.reverse()
    for c in cut_list:
        if "观察" in c or "观望" in c or "震荡对待" in c or "上行空间受限" in c or "下行空间受限" in c or "波动风险加大" in c \
                or "震荡为主" in c or "高位震荡" in c or "盘面震荡" in c or "反弹空间有限" in c or "反弹幅度已经较高" in c:
            return "0"
        if "短期反弹,趋势偏弱" in c or "先扬后抑" in c:
            return '0.8'
        if "反弹难持续" in c:
            return "-1"
        if "下行驱动逐渐放缓" in c:
            return '-0.5'
        if "正套" in c or "多单谨慎持有" in c:
            return '0.5'
        if "反套" in c or "空单谨慎持有" in c:
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
    if idea[key] not in ["0", "1", "-1","0.5","-0.5",'0.8',"-0.5","-0.8"]:
        idea[key] = simplify(idea[key])
    if key == "贵金属":
        topop.append("贵金属")
        toadd.append(["黄金",idea[key]])
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
    #菜粕菜油自己改
    if key == "菜粕&菜油":
        topop.append("菜粕&菜油")
        toadd.append(["菜粕", "0"])
        toadd.append(["菜油", "0"])
    #玻璃纯碱自己改
    if key == "纯碱":
        topop.append("纯碱")
        toadd.append(["纯碱", "-1"])
    if key == "玻璃":
        topop.append("玻璃")
        toadd.append(["玻璃", "1"])
    if key == "塑料":
        topop.append("塑料")
        toadd.append(["塑料", "0"])
    if key == "PP":
        topop.append("PP")
        toadd.append(["PP", "-1"])

for i in toadd:
    idea[i[0]] = i[1]
for i in topop:
    idea.pop(i)

idea.pop("股指")


for key in idea:
    print(key)
    print(idea[key])