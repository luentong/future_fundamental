import copy
low = ["偏弱", "下滑", "悲观", "弱势", "下行", "走弱", "做空", "偏空", "下跌", "试空", "回落", "短空", "空单操作",
       "承压","超涨","沽空","回吐","逢高空","下破","跳水","弱调整","弱趋势","冲低","上冲","赶底","走低","大跌"]
high = ["偏强", "上涨", "走强", "偏多", "做多", "试多", "上行", "企稳", "乐观", "强势", "走强", "提振", "坚挺",
        "反弹", "回升", "短多", "多单操作","超跌","沽多","逢低多","上破","强调整","冲高","下冲","赶顶","走高","大涨"]
fluc = ["观望","不宜","离场","观察", "观望", "上行承压", "上行乏力", "震荡对待","先扬后抑","短期反弹,趋势偏弱","下行驱动逐渐放缓",
        "反弹难持续","正套","反套","上行空间受限","暂无利好","高位震荡","盘面震荡","反弹空间有限","多单谨慎持有","空单谨慎持有",
        "反弹幅度已经较高","低点支撑","反弹难持续","涨势趋缓","跟涨情绪减弱","近强远弱","近弱远强","止跌","弱平衡","阶段性震荡"]
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
           "PVC", "软商品", "橡胶", "纸浆", "棉花","白糖", "农产品","油脂", "蛋白粕", "玉米/淀粉", "生猪", "鸡蛋"]
indexes = [0, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 22, 23, 24, 25, 26, 27, 28, 29, 30, 32, 33,
           34, 35, 37, 38, 39, 40,41]
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

def simplify(c):
    if "观察" in c or "观望" in c or "震荡对待" in c or "上行空间受限" in c or "下行空间受限" in c or "波动风险加大" in c \
            or "震荡为主" in c or "高位震荡" in c or "盘面震荡" in c or "反弹空间有限" in c or "反弹幅度已经较高" in c \
            or "反弹难持续" in c or "跟涨情绪减弱" in c or "阶段性震荡" in c:
        return "0"
    if "短期反弹,趋势偏弱" in c or "先扬后抑" in c or "近强远弱" in c:
        return '0.8'
    if "近弱远强" in c:
        return "-0.8"
    if "反弹难持续" in c:
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
    if idea[key] not in ["0", "1", "-1","0.5","-0.5",'0.8',"-0.5","-0.8"]:
        idea[key] = simplify(idea[key])
    if key == "黄金/白银":
        topop.append("黄金/白银")
        toadd.append(["黄金",idea[key]])
        toadd.append(["白银", idea[key]])
    if key == "钢材":
        topop.append("钢材")
        toadd.append(["热卷",idea[key]])
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
    if key == "纸浆":
        topop.append("纸浆")
        toadd.append(["纸浆", "1"])
    toadd.append(["锰硅", '1'])

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
    if idea[key] not in  ["0", "1", "-1","0.5","-0.5",'0.8',"-0.5","-0.8"]:
        idea[key] = simplify(idea[key])
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
print(idea)
guotai_idea = idea

###########################################国投安信开始
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

guotou_old = {}
for i in idea:
    guotou_old[i] = idea[i][:]

def simplify_sent(c):
    cut = jieba.cut(c)
    cut_list = []
    for i in cut:
        cut_list.append(i)
    cut_list.reverse()
    for c in cut_list:
        if "观察" in c or "观望" in c or "震荡对待" in c or "上行空间受限" in c or "下行空间受限" in c or "波动风险加大" in c \
                or "震荡为主" in c or "高位震荡" in c or "盘面震荡" in c or "反弹空间有限" in c or "反弹幅度已经较高" in c \
                or "反弹难持续" in c or "跟涨情绪减弱" in c or "阶段性震荡" in c:
            return "0"
        if "短期反弹,趋势偏弱" in c or "先扬后抑" in c or "近强远弱" in c:
            return '0.8'
        if "反弹难持续" in c:
            return "-1"
        if "近弱远强" in c:
            return "-0.8"
        if "下行驱动逐渐放缓" in c or "弱平衡" in c:
            return '-0.5'
        if "正套" in c or "多单谨慎持有" in c or "低点支撑" in c or "涨势趋缓" in c:
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
        idea[key] = simplify_sent(idea[key])
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
        toadd.append(["菜粕", "-0.5"])
        toadd.append(["菜油", "-0.5"])
    #玻璃纯碱自己改
    if key == "纯碱":
        topop.append("纯碱")
        toadd.append(["纯碱", "-1"])
    if key == "玻璃":
        topop.append("玻璃")
        toadd.append(["玻璃", "1"])
    if key == "塑料":
        topop.append("塑料")
        toadd.append(["塑料", "-1"])
    if key == "PP":
        topop.append("PP")
        toadd.append(["PP", "-1"])

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
        a1 = l.replace("【","")
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
    if idea[key] not in ["0", "1", "-1","0.5","-0.5",'0.8',"-0.5","-0.8","0.7"]:
        idea[key] = simplify_sent(idea[key])
    if key == "贵金属":
        topop.append("贵金属")
        toadd.append(["黄金",idea[key]])
        toadd.append(["白银", idea[key]])
    if key == "燃料油":
        topop.append("燃料油")
        toadd.append(["燃油", idea[key]])
    if key == "聚烯烃":
        topop.append("聚烯烃")
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
        toadd.append(["乙二醇", idea[key]])
    if key == "玉米、淀粉":
        topop.append("玉米、淀粉")
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
        toadd.append(["纯碱", "0"])

for i in topop:
    idea.pop(i)
for i in toadd:
    idea[i[0]] = i[1]

idea.pop("国债")
idea.pop("股指")
print(idea)
guangda_idea = idea

###########################################宏源期货
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

hongyuan_old = {}
for i in idea:
    hongyuan_old[i] = idea[i][:]

topop = []
toadd = []
for key in idea:
    if idea[key] not in ["0", "1", "-1","0.5","-0.5",'0.8',"-0.5","-0.8"]:
        idea[key] = simplify_sent(idea[key])
    if key == "螺纹钢":
        topop.append("螺纹钢")
        toadd.append(["螺纹", idea[key]])
    if key == "油脂":
        topop.append("油脂")
        toadd.append(["豆油", idea[key]])
        toadd.append(["菜油", idea[key]])
        toadd.append(["棕榈油", idea[key]])
    if key == "豆粕":
        toadd.append(["菜粕", idea[key]])


for i in toadd:
    idea[i[0]] = i[1]
for i in topop:
    idea.pop(i)
print(idea)
hongyuan_idea = idea
###########################################整合开始

idea_combined = {}
for i in [zhongxin_old, guotai_old, guotou_old, guangda_old,hongyuan_old]:
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
for i in [citrix_idea, guotai_idea, anxin_idea, guangda_idea,hongyuan_idea]:
    for j in i:
        if j in combined:
            combined[j].append(float(i[j]))
        else:
            combined[j] = [float(i[j])]
#自己加比如倍特的
# for i in combined:
#     if i == "PP":
#         combined[i].append(-1)
#     if i == "螺纹":
#         combined[i].append(0)
#     if i == "热卷":
#         combined[i].append(0)
#     if i == "黄金":
#         combined[i].append(0)
#     if i == "白银":
#         combined[i].append(0)
#     if i == "焦炭":
#         combined[i].append(0)
#     if i == "焦煤":
#         combined[i].append(0)
#     if i == "铝":
#         combined[i].append(0)
#     if i == "纸浆":
#         combined[i].append(0.5)
#     if i == "原油":
#         combined[i].append(-0.2)
#     if i == "棉花":
#         combined[i].append(-0.5)


for i in combined:
    print(i + " " + str(sum(combined[i])) + " " + str(len(combined[i])))
    if len(combined[i]) <= 4:
        combined[i] = sum(combined[i])/(len(combined[i]) + (4-len(combined[i])) * (4-len(combined[i]))  * 0.2)
    elif len(combined[i]) == 5:
        combined[i] = sum(combined[i]) / ((len(combined[i])) - 0.5)
    elif len(combined[i]) == 6:
        combined[i] = sum(combined[i]) / ((len(combined[i])) - 1.0)
import pandas as pd
result = pd.DataFrame(combined.items(), columns=['Name', 'Value'])
final = result.sort_values(by='Value', ascending=False)
print(final)
