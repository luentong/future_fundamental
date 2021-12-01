with open('宏源.txt', encoding='utf-8') as f:
    lines = f.readlines()
idea = {}
prev = ""
content = ""
for l in lines:
    if len(l) < 5:
        if prev != "":
            idea[prev] = content
            content = ""
        a1 = l.replace("\n", "")
        prev = a1
    elif l.strip("\n") != "":
        a4 = l.replace("\n", "")
        content += a4
idea[prev] = content
print(idea)
low = ["偏弱", "下滑", "悲观", "弱势", "下行", "走弱", "做空", "偏空", "下跌", "试空", "回落", "短空", "空单操作", "承压","超涨","沽空","回吐","逢高空","下破","跳水","弱调整","弱趋势"]
high = ["偏强", "上涨", "走强", "偏多", "做多", "试多", "上行", "企稳", "乐观", "强势", "走强", "提振", "坚挺", "反弹", "回升", "短多", "多单操作","超跌","沽多","逢低多","上破","强调整"]
fluc = ["观望","不宜","离场","观察", "观望", "上行承压", "上行乏力", "震荡对待","先扬后抑","短期反弹,趋势偏弱","下行驱动逐渐放缓","反弹难持续","正套","反套","上行空间受限","暂无利好","高位震荡", "盘面震荡"]
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
def simplify(c):
    cut = jieba.cut(c)
    cut_list = []
    for i in cut:
        cut_list.append(i)
    print(cut_list)
    cut_list.reverse()
    for c in cut_list:
        if "观察" in c or "观望" in c or "震荡对待" in c or "上行空间受限" in c or "下行空间受限" in c or "波动风险加大" in c or "震荡为主" in c or "高位震荡" in c or "盘面震荡" in c:
            return "0"
        if "短期反弹,趋势偏弱" in c or "先扬后抑" in c:
            return '0.8'
        if "下行驱动逐渐放缓" in c or "暂无利好" in c:
            return '-0.5'
        if "正套" in c:
            return '0.5'
        if "反套" in c:
            return '-0.5'
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
    if idea[key] not in ["0", "1", "-1","0.5","-0.5","0.8","-0.5"]:
        idea[key] = simplify(idea[key])
    if key == "螺纹钢":
        topop.append("螺纹钢")
        toadd.append(["螺纹", idea[key]])


for i in toadd:
    idea[i[0]] = i[1]
for i in topop:
    idea.pop(i)


for key in idea:
    print(key)
    print(idea[key])