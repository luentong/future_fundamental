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

def simplify_sent(c):
    result = []
    for tocut in c:
        tobreak = False
        cut = jieba.cut(tocut)
        cut_list = []
        for i in cut:
            cut_list.append(i)
        cut_list.reverse()
        for c in cut_list:
            if "观察" in c or "观望" in c or "震荡对待" in c or "上行空间受限" in c or "下行空间受限" in c or "波动风险加大" in c \
                    or "震荡为主" in c or "高位震荡" in c or "盘面震荡" in c or "反弹空间有限" in c or "反弹幅度已经较高" in c \
                    or "反弹难持续" in c or "跟涨情绪减弱" in c or "阶段性震荡" in c or "震荡中" in c or "上行空间有限" in c or "下行空间有限" in c or \
                    "底部空间或将有限" in c or "短期内震荡行情" in c or "呈现震荡格局" in c or "震荡走势为主" in c or "震荡整理" in c or "反复震荡" in c:
                result.append("0")
                tobreak = True
                break
            if "短期反弹,趋势偏弱" in c or "先扬后抑" in c or "近强远弱" in c or "底部价格已现" in c or "底部已现" in c or "短线持多" in c \
                    or "短多看待" in c or '多单轻仓持有' in c:
                result.append('0.8')
                tobreak = True
                break
            if "布局多单" in c:
                result.append("1")
                tobreak = True
                break
            if "反弹难持续" in c or "布局空单" in c:
                result.append("-1")
                tobreak = True
                break
            if "近弱远强" in c or "顶部价格已现" in c or "顶部已现" in c or "反弹后抛空" in c or "逢高抛空" in c or '空单轻仓持有' in c:
                result.append("-0.8")
                tobreak = True
                break
            if "下行驱动逐渐放缓" in c or "弱平衡" in c or "不过于追空" in c:
                result.append('-0.5')
                tobreak = True
                break
            if "正套" in c or "多单谨慎持有" in c or "低点支撑" in c or "涨势趋缓" in c or "空单止盈" in c or "仍较抗跌" in c or "反弹幅度有限" in c or "短多长空" in \
                    c or "不宜过分看多" in c or "不过于追多" in c:
                result.append('0.5')
                tobreak = True
                break
            if "反套" in c or "空单谨慎持有" in c or "多单止盈" in c or "不宜过分看跌" in c or "限制价格回升" in c or "短空长多" in c:
                result.append('-0.5')
                tobreak = True
                break
            if "反弹难持续" in c:
                for i in low:
                    if i in c:
                        result.append("-1")
                        tobreak = True
                        break
            if tobreak:
                break
            if "多TA" in c:
                idea["PTA"] += '1'
                if "空EG" in c:
                    idea["乙二醇"] += '-1'
                result.append("1")
                break
            for i in fluc:
                if i in c:
                    result.append("0")
                    tobreak = True
                    break
            if tobreak:
                break
            for i in high:
                if i in c:
                    result.append("1")
                    tobreak = True
                    break
            if tobreak:
                break
            for i in low:
                if i in c:
                    result.append("-1")
                    tobreak = True
                    break
        if tobreak:
            continue
        result.append("0")
        print("result", result)
    return result

with open('国泰多天.txt', encoding='utf-8') as f:
    lines = f.readlines()
idea = {}
for l in lines:
    if ':' in l:
        if l.split(":")[0] in idea:
            idea[l.split(":")[0]] = idea[l.split(":")[0]] + [(l.split(":")[1].strip('\n'))]
        else:
            idea[l.split(":")[0]] = [l.split(":")[1].strip('\n')]
    if '：' in l:
        if l.split("：")[0] in idea:
            idea[l.split("：")[0]] = idea[l.split("：")[0]] + [(l.split("：")[1].strip('\n'))]
        else:
            idea[l.split("：")[0]] = [l.split("：")[1].strip('\n')]

print(idea)
topop = []
toadd = []
for key in idea:
    if not idea[key][0].isdecimal():
        print(idea[key])
        idea[key] = simplify_sent(idea[key])
        print(idea[key])
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
print(toadd)
print(topop)
for i in topop:
    idea.pop(i)
for i in toadd:
    idea[i[0]] = i[1]


for key in idea:
    print(key)
    print(idea[key])