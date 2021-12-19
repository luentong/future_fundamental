
with open('国泰君安.txt') as f:
    lines = f.readlines()
idea = {}
for l in lines:
    if ':' in l:
        idea[l.split(":")[0]] = l.split(":")[1].strip('\n')
    if '：' in l:
        idea[l.split("：")[0]] = l.split("：")[1].strip('\n')

low = ["偏弱", "下滑", "悲观", "弱势", "下行", "走弱", "做空", "偏空", "下跌", "试空", "回落", "短空", "空单操作",
       "承压","超涨","沽空","回吐","逢高空","下破","跳水","弱调整","弱趋势","冲低","上冲","赶底","走低","大跌","布局空单"]
high = ["偏强", "上涨", "走强", "偏多", "做多", "试多", "上行", "企稳", "乐观", "强势", "走强", "提振", "坚挺",
        "反弹", "回升", "短多", "多单操作","超跌","沽多","逢低多","上破","强调整","冲高","下冲","赶顶","走高","大涨","布局多单"]
fluc = ["观望","不宜","离场","观察", "观望", "上行承压", "上行乏力", "震荡对待","先扬后抑","短期反弹,趋势偏弱","下行驱动逐渐放缓",
        "反弹难持续","正套","反套","上行空间受限","暂无利好","高位震荡","盘面震荡","反弹空间有限","多单谨慎持有","空单谨慎持有",
        "反弹幅度已经较高","低点支撑","反弹难持续","涨势趋缓","跟涨情绪减弱","近强远弱","近弱远强","止跌","弱平衡","阶段性震荡"]
other = ['高升水']
print(idea)
def simplify(c):
    if "观察" in c or "观望" in c or "震荡对待" in c or "上行空间受限" in c or "下行空间受限" in c or "波动风险加大" in c \
            or "震荡为主" in c or "高位震荡" in c or "盘面震荡" in c or "反弹空间有限" in c or "反弹幅度已经较高" in c \
            or "反弹难持续" in c or "跟涨情绪减弱" in c or "阶段性震荡" in c:
        return "0"
    if "短期反弹,趋势偏弱" in c or "先扬后抑" in c or "近强远弱" in c:
        return '0.8'
    if "近弱远强" in c:
        return "-0.8"
    if "布局多单" in c:
        return "1"
    if "反弹难持续" in c or "布局空单" in c:
         return "-1"
    if "下行驱动逐渐放缓" in c or "弱平衡" in c:
        return '-0.5'
    if "正套" in c or "多单谨慎持有" in c or "低点支撑" in c or "涨势趋缓" in c or "止跌" in c:
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
    if idea[key] not in ["0", "1", "-1","0.5","-0.5","0.8","-0.5"]:
        idea[key] = simplify(idea[key])
    if key == "铁矿石":
        topop.append("铁矿石")
        toadd.append(["铁矿", idea[key]])
    if key == "MEG":
        topop.append("MEG")
        if "乙二醇" not in idea:
         toadd.append(["乙二醇", idea[key]])
    if key == "螺纹钢":
        topop.append("螺纹钢")
        toadd.append(["螺纹", idea[key]])
    if key == "热轧卷板":
        topop.append("热轧卷板")
        toadd.append(["热卷", idea[key]])
    if key == "玉米":
        toadd.append(["淀粉", idea[key]])

    if key == "燃料油":
        topop.append("燃料油")
        toadd.append(["燃油", idea[key]])
    if key == "豆粕":
        toadd.append(["菜粕", idea[key]])
for i in topop:
    idea.pop(i)
for i in toadd:
    idea[i[0]] = i[1]

idea.pop("LLDPE")

guotai_idea = idea


for key in idea:
    print(key)
    print(idea[key])