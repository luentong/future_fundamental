
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



low = ["偏弱", "下滑", "悲观", "弱势", "下行", "走弱", "做空", "偏空", "下跌", "试空", "回落", "短空", "空单操作",
       "承压", "超涨", "沽空", "回吐", "逢高空", "下破", "跳水", "弱调整", "弱趋势", "冲低", "上冲", "赶底", "走低", "大跌", "布局空单", "持空","下调","高抛","空单继续持有"]
high = ["偏强", "上涨", "走强", "偏多", "做多", "试多", "上行", "企稳", "乐观", "强势", "走强", "提振", "坚挺",
        "反弹", "回升", "短多", "多单操作", "超跌", "沽多", "逢低多", "上破", "强调整", "冲高", "下冲", "赶顶", "走高", "大涨", "布局多单", "持多","上调","多单继续持有"]
fluc = ["观望", "不宜", "离场", "观察", "观望", "上行承压", "上行乏力", "震荡对待", "先扬后抑", "短期反弹,趋势偏弱", "下行驱动逐渐放缓",
        "反弹难持续", "正套", "反套", "上行空间受限", "暂无利好", "高位震荡", "盘面震荡", "反弹空间有限", "多单谨慎持有", "空单谨慎持有",
        "反弹幅度已经较高", "低点支撑", "反弹难持续", "涨势趋缓", "跟涨情绪减弱", "近强远弱", "近弱远强", "止跌", "弱平衡", "阶段性震荡", "震荡中",
        "下行空间受限","上行空间有限","下行空间有限","底部价格已现","顶部已现","底部已现","顶部价格已现","反弹后抛空","逢高抛空","多单止盈",
        "不宜过分看跌","空单止盈","短线持多","短多看待","底部空间或将有限",'空单轻仓持有','多单轻仓持有',"短期内震荡行情","呈现震荡格局","仍较抗跌",
        "震荡走势为主","反弹幅度有限","震荡整理","限制价格回升","短多长空","短空长多","不宜过分看跌","不宜过分看多"]
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
                "底部空间或将有限" in c or "短期内震荡行情" in c or "呈现震荡格局" in c or "震荡走势为主" in c or "震荡整理" in c:
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
        if "下行驱动逐渐放缓" in c or "弱平衡" in c:
            return '-0.5'
        if "正套" in c or "多单谨慎持有" in c or "低点支撑" in c or "涨势趋缓" in c or "空单止盈" in c or "仍较抗跌" in c or "反弹幅度有限" in c or "短多长空" in \
                c or "不宜过分看多" in c:
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

guotai_idea = idea


for key in idea:
    print(key)
    print(idea[key])