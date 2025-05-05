import keywords
import huaan
from datetime import date
import pdf

import io
import sys

#sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
path = './所长早读_' + str(date.today()) + '.pdf'
print("path:", path)
############################################华安开始
#idea = huaan.huaan_idea()
idea = {}
huaan_old = {}
for i in idea:
    huaan_old[i] = idea[i][:]
topop = []
toadd = []
for key in idea:

    if key == "集运指数（欧线）":
        topop.append("集运指数（欧线）")
        toadd.append(["集运", idea[key]])
    if key == "PTA乙二醇":
        topop.append("PTA乙二醇")
        toadd.append(["PTA", idea[key]])
        toadd.append(["短纤", idea[key]])
        toadd.append(["MEG", idea[key]])
    if key == "黑色金属":
        topop.append("黑色金属")
        toadd.append(["螺纹", idea[key]])
        toadd.append(["热卷", idea[key]])
    if key == "焦煤焦炭":
        topop.append("焦煤焦炭")
        toadd.append(["焦煤", idea[key]])
        toadd.append(["焦炭", idea[key]])
    if key == "不锈钢镍":
        topop.append("不锈钢镍")
        toadd.append(["不锈钢", idea[key]])
        toadd.append(["镍", idea[key]])
    if key == "豆粕菜粕":
        topop.append("豆粕菜粕")
        toadd.append(["豆粕", idea[key]])
        toadd.append(["菜粕", idea[key]])
    if key == "淀粉玉米":
        topop.append("淀粉玉米")
        toadd.append(["淀粉", idea[key]])
        toadd.append(["玉米", idea[key]])
    if key == "棉花棉纱":
        topop.append("棉花棉纱")
        toadd.append(["棉花", idea[key]])
    if key == "油脂":
        topop.append("油脂")
        toadd.append(["棕榈油", idea[key]])
        toadd.append(["豆油", idea[key]])
        toadd.append(["菜油", idea[key]])


for i in topop:
    idea.pop(i)
for i in toadd:
    idea[i[0]] = i[1]

huaan_old = {}
for i in idea:
    huaan_old[i] = idea[i][:]

for key in idea:
    if not idea[key].isdecimal():
        idea[key] = keywords.simplify_sent(idea[key])


for i in huaan_old:
    if i in idea:
        if i == "":
            huaan_old[i] = idea[i] + " !!华安跟风!! " + huaan_old[i]
        elif i == "":
            huaan_old[i] = idea[i] + " !!华安很准!! " + huaan_old[i]
        else:
            huaan_old[i] = idea[i] + " 华安 " + huaan_old[i]
    else:
        huaan_old[i] = ""

huaan_idea = idea

###########################################中信开始

with open('中信.txt') as f:
    lines = f.readlines()
    lines = []

if not lines:
    zhongxin_old = {}
    citrix_idea = {}
else:
    line = lines[0]
    keyword = ["黄金/白银", "黑色", "钢材", "铁矿", "焦炭", "焦煤", "动力煤", "有色", "铜", "铝", "锌", "铅", "镍", "不锈钢", "锡", "能源", "原油", "沥青",
               "燃料油", "低硫燃料油","纯碱", "高硫燃油","低硫燃油",
               "LPG", "化工", "甲醇", "尿素", "乙二醇", "PTA", "短纤", "PP", "塑料", "苯乙烯",
               "PVC", "软商品", "橡胶", "纸浆", "棉花", "白糖", "农产品", "油脂", "蛋白粕", "玉米/淀粉", "生猪", "鸡蛋", "玻璃"]
    indexes = [0, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 22, 23, 24, 25, 26, 27, 28, 29, 30, 32, 33,
               34, 35, 37, 38, 39, 40, 41]
    idea = {}
    for l in lines:
        if " "  in l and len(l.split(" ")[0]) < 7 and l.split(" ")[0] in keyword:
            idea[l.split(" ")[0]] = "".join(l.split(" ")[1:])

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
        if key == "高硫燃油":
            topop.append("高硫燃油")
            toadd.append(["燃油", idea[key]])
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
            if i == "":
                zhongxin_old[i] = idea[i] + " ！！中信傻逼！！ " + zhongxin_old[i]
            elif i == "":
                zhongxin_old[i] = idea[i] + " ！！中信很准！！ " + zhongxin_old[i]
            else:
                zhongxin_old[i] = idea[i] + " 中信 " + zhongxin_old[i]
        else:
            zhongxin_old[i] = ""
    citrix_idea = idea

###########################################国泰开始

idea = {}
try:
    res = pdf.pdf_to_string(path)
    print("res true")
except:
    res = ""
    print("res false")

items = ["白银","铜","氧化铝","锌","铅","不锈钢","锡","工业硅","碳酸锂","铁矿石","热轧卷板","锰硅","焦煤","动力煤","集运指数（欧线）","玻璃",
         "MEG","橡胶","合成橡胶","沥青","LLDPE","PP","烧碱","纸浆","甲醇","尿素","苯乙烯","纯碱","LPG","短纤",
         "PVC","低硫燃料油","豆油","豆粕","豆一","玉米","白糖","棉花","鸡蛋","生猪","花生"]

prev_item = ""
res_string = ""
started = False
for res_index in res:
    print("Res:", res[res_index])
    res_string = ""
    for res_sub in res[res_index]:
        res_string += str(res_sub)
    print("Res_string", type(res_string))
#
# res_string = res_string.split(".................................................................................................................................")[-1]
    if not started and "花生：" not in res_string:
        continue
    if not started and "花生："  in res_string:
        started = True
    inside = False
    for i in items:
        #print("res:", res_string)
        if i+"：" in res_string:
            inside = True
            if prev_item != "" and prev_item in idea:
                idea[prev_item] += "".join(res_string.split(i+"：")[0])
            prev_item = i
            sub = "".join(res_string.split(i+"：")[1:])
            if "请务必阅读正文" in sub:
                sub = sub.split("请务必阅读正文")[0]
            if "分析师声明作者具有" in sub:
                sub = sub.split("分析师声明作者具有")[0]
            if "不应被视为任何投资" in sub:
                sub = sub.split("不应被视为任何投资")[0]
            if "个人观点，仅供参" in res_string:
                sub = sub.split("个人观点，仅供参")[0]

            if "观点及建议" in sub:
                #to_add = sub.split("观点及建议")[1].split("商品研究")[0]
                to_add = sub.split("观点及建议")[1]
                to_add = to_add.strip("").strip(" ")
                if to_add.startswith("】，\', \'"):
                    to_add = to_add.split("】，\', \'")[1]
                elif to_add.startswith("】\', \'"):
                    to_add = to_add.split("】\', \'")[1]
                elif to_add.startswith("】\'][\'"):
                    to_add = to_add.split("】\'][\'")[1]
                if to_add.endswith("\', \'【"):
                    to_add = "".join(to_add.split("\', \'【")[:-1])
                idea[i] = to_add
    if not inside and prev_item != "" and prev_item in idea:
        if "请务必阅读正文" in res_string:
            res_string = res_string.split("请务必阅读正文")[0]
        if "分析师声明作者具有" in res_string:
            res_string = res_string.split("分析师声明作者具有")[0]
        if "不应被视为任何投资" in res_string:
            res_string = res_string.split("不应被视为任何投资")[0]
        if "个人观点" in res_string:
            res_string = res_string.split("个人观点")[0]
        idea[prev_item] += res_string


    elif not inside and prev_item != "" and prev_item not in idea:
        if "请务必阅读正文" in res_string:
            res_string = res_string.split("请务必阅读正文")[0]
        if "分析师声明作者具有" in res_string:
            res_string = res_string.split("分析师声明作者具有")[0]
        if "不应被视为任何投资" in res_string:
            res_string = res_string.split("不应被视为任何投资")[0]
        if "个人观点" in res_string:
            res_string = res_string.split("个人观点")[0]
        idea[prev_item] = res_string
topop = []
toadd = []
for key in idea:
    if key == "集运指数（欧线）":
        topop.append("集运指数（欧线）")
        toadd.append(["集运", idea[key]])
    if key == "铁矿石":
        topop.append("铁矿石")
        toadd.append(["铁矿", idea[key]])
    if key == "不锈钢":
        toadd.append(["镍", idea[key]])
    if key == "热轧卷板":
        topop.append("热轧卷板")
        toadd.append(["螺纹", idea[key]])
        toadd.append(["热卷", idea[key]])
    if key == "锰硅":
        toadd.append(["硅铁", idea[key]])
    if key == "豆油":
        toadd.append(["棕榈油", idea[key]])
        toadd.append(["菜油", idea[key]])
    if key == "白银":
        toadd.append(["黄金", idea[key]])
    if key == "MEG":
        toadd.append(["PTA", idea[key]])
    if key == "LLDPE":
        topop.append("LLDPE")
        toadd.append(["塑料", idea[key]])
    if key == "低硫燃料油":
        topop.append("低硫燃料油")
        toadd.append(["低硫燃油", idea[key]])
        toadd.append(["燃油", idea[key]])
    if key == "豆一":
        toadd.append(["豆粕", idea[key]])
    if key == "氧化铝":
        toadd.append(["铝", idea[key]])
    if key == "焦煤":
        toadd.append(["焦炭", idea[key]])

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
        if i == "":
            guotai_old[i] = idea[i] + " ！！国泰很准！！ " + guotai_old[i]
        if i == "":
            guotai_old[i] = idea[i] + " ！！国泰傻逼！！ " + guotai_old[i]
        else:
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
    if l.strip("\n") == "Image" and prev != "":
        break
    if "【" in l and len(l) < 30:
        a1 = l.replace("【", "")
        a2 = a1.replace("】", "")
        a3 = a2.replace("\n", "")
        prev = a3
    elif l.strip("\n") == "图片" and prev != "":
        break
    elif l.strip("\n") != "":
        a4 = l.replace("\n", "")
        if prev != "":
            idea[prev] = a4


topop = []
toadd = []
for key in idea:
    if key == "短纤&瓶片":
        topop.append("短纤&瓶片")
        toadd.append(["短纤", idea[key]])
        toadd.append(["PR", idea[key]])
    if key == "PX&PTA":
        topop.append("PX&PTA")
        toadd.append(["PTA", idea[key]])
        toadd.append(["PX", idea[key]])
    if key == "投资咨询&20号胶&天然橡胶&丁二烯橡胶":
        topop.append("投资咨询&20号胶&天然橡胶&丁二烯橡胶")
        toadd.append(["橡胶", idea[key]])
        toadd.append(["合成橡胶", idea[key]])
    if key == "聚丙烯&塑料&PVC&烧碱":
        topop.append("聚丙烯&塑料&PVC&烧碱")
        toadd.append(["PP", idea[key]])
        toadd.append(["塑料", idea[key]])
        toadd.append(["PVC", idea[key]])
        toadd.append(["烧碱", idea[key]])
    if key == "PVC&烧碱":
        topop.append("PVC&烧碱")
        toadd.append(["PVC", idea[key]])
        toadd.append(["烧碱", idea[key]])
    if key == "PX&PTA&短纤":
        topop.append("PX&PTA&短纤")
        toadd.append(["PTA", idea[key]])
        toadd.append(["PX", idea[key]])
        toadd.append(["短纤", idea[key]])
    if key == "PTA&PX&乙二醇&短纤":
        topop.append("PTA&PX&乙二醇&短纤")
        toadd.append(["MEG", idea[key]])
        toadd.append(["PTA", idea[key]])
        toadd.append(["PX", idea[key]])
        toadd.append(["短纤", idea[key]])
    if key == "PTA&PX&短纤&乙二醇":
        topop.append("PTA&PX&短纤&乙二醇")
        toadd.append(["MEG", idea[key]])
        toadd.append(["PTA", idea[key]])
        toadd.append(["PX", idea[key]])
        toadd.append(["短纤", idea[key]])
    if key == "集运指数（欧线）":
        topop.append("集运指数（欧线）")
        toadd.append(["集运", idea[key]])
    if key == "20号胶&天然橡胶&丁二烯橡胶":
        topop.append("20号胶&天然橡胶&丁二烯橡胶")
        toadd.append(["橡胶", idea[key]])
        toadd.append(["合成橡胶", idea[key]])
    if key == "20号胶&天然橡胶":
        topop.append("20号胶&天然橡胶")
        toadd.append(["橡胶", idea[key]])
    if key == "镍及不锈钢":
        topop.append("镍及不锈钢")
        toadd.append(["镍", idea[key]])
        toadd.append(["不锈钢", idea[key]])
    if key == "天然橡胶":
        topop.append("天然橡胶")
        toadd.append(["橡胶", idea[key]])
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
    if key == "锂":
        topop.append("锂")
        toadd.append(["碳酸锂", idea[key]])
    if key == "棕榈油&豆油":
        topop.append("棕榈油&豆油")
        toadd.append(["棕榈油", idea[key]])
        toadd.append(["豆油", idea[key]])
    if key == "20号胶&天然橡胶&丁二烯橡胶":
        topop.append("20号胶&天然橡胶&丁二烯橡胶")
        toadd.append(["橡胶", idea[key]])
        toadd.append(["合成橡胶", idea[key]])
    if key == "豆油&棕榈油":
        topop.append("豆油&棕榈油")
        toadd.append(["棕榈油", idea[key]])
        toadd.append(["豆油", idea[key]])
    if key == "棕榈油&菜油":
        topop.append("棕榈油&菜油")
        toadd.append(["棕榈油", idea[key]])
        toadd.append(["菜油", idea[key]])
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
    if key == "糖":
        topop.append("糖")
        toadd.append(["白糖", idea[key]])
    if key == "低硫燃料油":
        topop.append("低硫燃料油")
        toadd.append(["低硫燃油", idea[key]])
    if key == "棕榈油&豆油":
        topop.append("棕榈油&豆油")
        toadd.append(["棕榈油", idea[key]])
        toadd.append(["豆油", idea[key]])
    if key == "菜粕&菜油":
        topop.append("菜粕&菜油")
        toadd.append(["菜粕", idea[key]])
    if key == "乙二醇":
        topop.append("乙二醇")
        toadd.append(["MEG", idea[key]])
    if key == "PTA&乙二醇&短纤":
        topop.append("PTA&乙二醇&短纤")
        toadd.append(["MEG", idea[key]])
        toadd.append(["PTA", idea[key]])
        toadd.append(["短纤", idea[key]])
    if key == "低硫燃料油&燃料油":
        topop.append("低硫燃料油&燃料油")
        toadd.append(["燃油", idea[key]])
        toadd.append(["低硫燃油", idea[key]])
    if key == "燃料油&低硫燃料油":
        topop.append("燃料油&低硫燃料油")
        toadd.append(["燃油", idea[key]])
        toadd.append(["低硫燃油", idea[key]])
    if key == "豆粕&大豆":
        topop.append("豆粕&大豆")
        toadd.append(["豆粕", idea[key]])
        toadd.append(["豆一", idea[key]])
    if key == "大豆&豆粕":
        topop.append("大豆&豆粕")
        toadd.append(["豆粕", idea[key]])
        toadd.append(["豆一", idea[key]])

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
        if i == "":
            guotou_old[i] = idea[i] + " ！！国投跟风！！ " + guotou_old[i]
        if i == "":
            guotou_old[i] = idea[i] + " ！！国投很准！！ " + guotou_old[i]
        else:
            guotou_old[i] = idea[i] + " 国投 " + guotou_old[i]
    else:
        guotou_old[i] = ""
guotou_idea = idea

###########################################光大开始

with open('光大.txt', encoding='utf-8') as f:
    lines = f.readlines()
idea = {}
prev_item = ""
topop = []
toadd = []
items = ["股指","国债","贵金属","螺纹钢","铁矿石","焦煤","焦炭","硅铁","锰硅","铜","镍&不锈钢","氧化铝&电解铝","锡","锌","锰硅","工业硅&多晶硅",
         "工业硅","碳酸锂","原油","燃料油","沥青","橡胶","聚酯","甲醇","聚烯烃","聚氯乙烯","尿素","纯碱","玻璃","蛋白粕","油脂","生猪","鸡蛋",
         "玉米","白糖","棉花","双焦","废钢","油脂油料","PVC","纯碱&玻璃","PX","PX&PTA&MEG"]
for l in lines:
    stripped = l.strip().strip('\n')
    if "完整报告请联系" in stripped:
        break
    if "风险：" in stripped:
        prev_item = ""
        continue
    if "免责声明" in stripped:
        break
    if ("后期关注" in stripped):
        if prev_item.strip("：") in idea:
            idea[prev_item.strip()] += l.strip().strip('\n').split("后期关注")[0]
        else:
            idea[prev_item.strip()] = l.strip().strip('\n').split("后期关注")[0]
        continue
    if stripped.split("：")[0] in items and l.strip().strip("\n") != "" and "操作建议" not in l and "期货方面" not in l and "小结" not in l\
            and "现货方面" not in l and "图片" not in l and l.strip("\n") != " " and "重要提示" not in l and "免责声明" not in l:
        prev_item = stripped.split("：")[0]
        idea[prev_item] = l.strip().strip('\n').split("：")[1]
        next = True
        continue
    if next:
        if prev_item in idea:
            idea[prev_item] += l.strip().strip('\n')
        else:
            idea[prev_item] = l.strip().strip('\n')


for key in idea:
    if key == "工业硅&多晶硅":
        topop.append("工业硅&多晶硅")
        toadd.append(["工业硅", idea[key]])
        toadd.append(["多晶硅", idea[key]])
    if key == "PX&PTA&MEG":
        topop.append("PX&PTA&MEG")
        toadd.append(["PTA", idea[key]])
        toadd.append(["PX", idea[key]])
        toadd.append(["MEG", idea[key]])
    if key == "纯碱&玻璃":
        topop.append("纯碱&玻璃")
        toadd.append(["纯碱", idea[key]])
        toadd.append(["玻璃", idea[key]])
    if key == "聚乙烯":
        topop.append("聚乙烯")
        toadd.append(["塑料", idea[key]])
    if key == "聚氯乙烯":
        topop.append("聚氯乙烯")
        toadd.append(["PVC", idea[key]])
    if key == "聚丙烯":
        topop.append("聚丙烯")
        toadd.append(["PP", idea[key]])
    if key == "PPX&PTA&MEG":
        topop.append("PPX&PTA&MEG")
        toadd.append(["短纤", idea[key]])
        toadd.append(["PTA", idea[key]])
        toadd.append(["PX", idea[key]])
        toadd.append(["MEG", idea[key]])
    if key == "纯碱玻璃":
        topop.append("纯碱玻璃")
        toadd.append(["玻璃", idea[key]])
        toadd.append(["纯碱", idea[key]])
    if key == "铁矿石":
        topop.append("铁矿石")
        toadd.append(["铁矿", idea[key]])
    if key == "氧化铝&电解铝":
        topop.append("氧化铝&电解铝")
        toadd.append(["氧化铝", idea[key]])
        toadd.append(["铝", idea[key]])
    if key == "贵金属":
        topop.append("贵金属")
        toadd.append(["黄金", idea[key]])
        toadd.append(["白银", idea[key]])
    if key == "双焦":
        topop.append("双焦")
        toadd.append(["焦煤", idea[key]])
        toadd.append(["焦炭", idea[key]])
    if key == "燃料油":
        topop.append("燃料油")
        toadd.append(["燃油", idea[key]])
    if key == "聚烯烃":
        topop.append("聚烯烃")
        toadd.append(["塑料", idea[key]])
        toadd.append(["PP", idea[key]])
    if key == "硅":
        topop.append("硅")
        toadd.append(["工业硅", idea[key]])
    if key == "豆类":
        topop.append("豆类")
        toadd.append(["菜粕", idea[key]])
        toadd.append(["豆粕", idea[key]])
    if key == "螺纹钢":
        topop.append("螺纹钢")
        toadd.append(["螺纹", idea[key]])
        toadd.append(["热卷", idea[key]])
    if key == "天胶":
        topop.append("天胶")
        toadd.append(["橡胶", idea[key]])
    if key == "PTA&MEG":
        topop.append("PTA&MEG")
        toadd.append(["短纤", idea[key]])
        toadd.append(["PTA", idea[key]])
        toadd.append(["MEG", idea[key]])
    if key == "聚酯":
        topop.append("聚酯")
        toadd.append(["短纤", idea[key]])
        toadd.append(["PTA", idea[key]])
        toadd.append(["MEG", idea[key]])
    if key == "蛋白粕":
        topop.append("蛋白粕")
        toadd.append(["豆粕", idea[key]])
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
    if key == "油脂":
        topop.append("油脂")
        toadd.append(["豆油", idea[key]])
        toadd.append(["菜油", idea[key]])
        toadd.append(["棕榈油", idea[key]])
    if key == "钢材":
        topop.append("钢材")
        toadd.append(["螺纹", idea[key]])
        toadd.append(["热卷", idea[key]])
    if key == "镍&不锈钢":
        topop.append("镍&不锈钢")
        toadd.append(["镍", idea[key]])
        toadd.append(["不锈钢", idea[key]])

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
        if i == "":
            guangda_old[i] = idea[i] + " ！！光大很准！！ " + guangda_old[i]
        else:
            guangda_old[i] = idea[i] + " 光大 " + guangda_old[i]
    else:
        guangda_old[i] = ""
guangda_idea = idea

###########################################上海中期期货
with open('上海中期.txt', encoding='utf-8') as f:
    lines = f.readlines()
idea = {}
items = ["贵金属","铜(CU)","螺纹(RB)","热卷(HC)","铝(AL)","锌(ZN)","铅(PB)","镍(NI)","不锈钢(SS)","铁矿石(I)","钢材","双焦","合成橡胶",
         "天胶及20号胶","原油(SC)","燃油(FU)","乙二醇(EG)","PVC(V)","沥青(BU)","塑料(L)","聚丙烯(PP)","PTA(TA)","苯乙烯(EB)","焦炭(J)","焦煤(JM)","动力煤(TC)","甲醇(ME)","尿素(UR)",
         "玻璃(FG)","白糖(SR)","大豆(A)","豆粕(M)","豆油(Y)","棕榈油(P)","菜籽类","鸡蛋(JD)","苹果(AP)","生猪(LH)","花生(PK)","棉花及棉纱","工业硅","燃油及低硫燃油",
         "铜及国际铜","镍及不锈钢","PTA及短纤","天然橡胶","棉花及棉纱","玉米及玉米淀粉","原油","沥青","聚丙烯","塑料","PVC","甲醇","苯乙烯","纯碱","尿素","焦煤","焦炭","聚酯产业链",
         "生猪","花生","白糖","鸡蛋","苹果","豆粕","集运指数（欧线）","烧碱","碳酸锂","铝及氧化铝","棕榈油","豆油","大豆","股指","宏观","铝","铅","锌","螺纹","热卷","铁矿石","工业硅","生猪及鸡蛋","玉米"]
next = False
prev_item = ""
for l in lines:
    stripped = l.strip().strip('\n')
    if stripped == "":
        continue
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
    if key == "聚酯产业链":
        topop.append("聚酯产业链")
        toadd.append(["PTA", idea[key]])
        toadd.append(["PX", idea[key]])
        toadd.append(["短纤", idea[key]])
    if key == "集运指数（欧线）":
        topop.append("集运指数（欧线）")
        toadd.append(["集运", idea[key]])
    if key == "钢材":
        topop.append("钢材")
        toadd.append(["螺纹", idea[key]])
        toadd.append(["热卷", idea[key]])
    if key == "双焦":
        topop.append("双焦")
        toadd.append(["焦煤", idea[key]])
        toadd.append(["焦炭", idea[key]])
    if key == "铜及国际铜":
        topop.append("铜及国际铜")
        toadd.append(["铜", idea[key]])
    if key == "生猪及鸡蛋":
        topop.append("生猪及鸡蛋")
        toadd.append(["生猪", idea[key]])
        toadd.append(["鸡蛋", idea[key]])
    if key == "铝及氧化铝":
        topop.append("铝及氧化铝")
        toadd.append(["铝", idea[key]])
        toadd.append(["氧化铝", idea[key]])
    if key == "铁矿石":
        topop.append("铁矿石")
        toadd.append(["铁矿", idea[key]])
    if key == "燃油及低硫燃油":
        topop.append("燃油及低硫燃油")
        toadd.append(["燃油", idea[key]])
        toadd.append(["低硫燃油", idea[key]])
    if key == "镍及不锈钢":
        topop.append("镍及不锈钢")
        toadd.append(["镍", idea[key]])
        toadd.append(["不锈钢", idea[key]])
    if key == "PTA及短纤":
        topop.append("PTA及短纤")
        toadd.append(["PTA", idea[key]])
        toadd.append(["短纤", idea[key]])
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
        if i == "":
            zhongqi_old[i] = idea[i] + " ！！中期傻逼！！ " + zhongqi_old[i]
        else:
            zhongqi_old[i] = idea[i] + " 中期 " + zhongqi_old[i]
    else:
        zhongqi_old[i] = ""

zhongqi_idea = idea


###########################################五矿开始

with open('五矿.txt', encoding='utf-8') as f:
    lines = f.readlines()
idea = {}
items = ["股指","国债","油脂","碳酸锂","蛋白粕","焦炭：","焦煤：","焦煤焦炭","高、低硫燃料油","鸡蛋","生猪","不锈钢","锰硅硅铁",
        "白糖","苹果","棉花","贵金属","铜","锌","铅","原油","玻璃纯碱","PX","贵 金 属","乙二醇","PX",
         "铝","镍","锡","锰硅","硅铁","铁矿石","碳酸锂","工业硅","聚乙烯","钢材","双焦","橡胶","甲醇","尿素","苯乙烯","PVC","PTA","玻璃","纯碱","LPG","沥青","动力煤","FU燃料油","LU低硫燃料油"]
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
            if prev_item == "甲醇":
                idea[prev_item] += stripped.strip('\n').split("基本面看看")[0]
                next = False
            else:
                idea[prev_item] += stripped.strip('\n')
        else:
            if prev_item == "甲醇":
                idea[prev_item] = stripped.strip('\n').split("基本面看看")[0]
                next = False
            else:
                idea[prev_item] = stripped.strip('\n')

topop = []
toadd = []
for key in idea:
    if key == "锰硅硅铁":
        topop.append("锰硅硅铁")
        toadd.append(["硅铁", idea[key]])
        toadd.append(["锰硅", idea[key]])
    if key == "贵 金 属":
        topop.append("贵 金 属")
        toadd.append(["黄金", idea[key]])
        toadd.append(["白银", idea[key]])
    if key == "聚乙烯":
        topop.append("聚乙烯")
        toadd.append(["PP", idea[key]])
        toadd.append(["塑料", idea[key]])
    if key == "铁矿石":
        topop.append("铁矿石")
        toadd.append(["铁矿", idea[key]])
    if key == "油脂":
        topop.append("油脂")
        toadd.append(["豆油", idea[key]])
        toadd.append(["菜油", idea[key]])
        toadd.append(["棕榈油", idea[key]])
    if key == "蛋白粕":
        topop.append("蛋白粕")
        toadd.append(["豆粕", idea[key]])
        toadd.append(["菜粕", idea[key]])
    if key == "高、低硫燃料油":
        topop.append("高、低硫燃料油")
        toadd.append(["燃油", idea[key]])
        toadd.append(["低硫燃油", idea[key]])
    if key == "FU燃料油":
        toadd.append(["燃油", idea[key]])
    if key == "LU低硫燃料油":
        toadd.append(["低硫燃油", idea[key]])
    if key == "贵金属":
        topop.append("贵金属")
        toadd.append(["黄金", idea[key]])
        toadd.append(["白银", idea[key]])
    if key == "双焦":
        topop.append("双焦")
        toadd.append(["焦煤", idea[key]])
        toadd.append(["焦炭", idea[key]])
    if key == "焦煤焦炭":
        topop.append("焦煤焦炭")
        toadd.append(["焦煤", idea[key]])
        toadd.append(["焦炭", idea[key]])
    if key == "钢材":
        topop.append("钢材")
        toadd.append(["螺纹", idea[key]])
        toadd.append(["热卷", idea[key]])
    if key == "焦炭：":
        topop.append("焦炭：")
        toadd.append(["焦炭", idea[key]])
    if key == "焦煤：":
        topop.append("焦煤：")
        toadd.append(["焦煤", idea[key]])
    if key == "玻璃纯碱":
        topop.append("玻璃纯碱")
        toadd.append(["纯碱", idea[key]])
        toadd.append(["玻璃", idea[key]])
    if key == "乙二醇":
        topop.append("乙二醇")
        toadd.append(["MEG", idea[key]])

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
        if i == "":
            wukuang_old[i] = idea[i] + " ！！五矿很准！！ " + wukuang_old[i]
        elif i == "":
            wukuang_old[i] = idea[i] + " ！！五矿傻逼！！ " + wukuang_old[i]
        else:
            wukuang_old[i] = idea[i] + " 五矿 " + wukuang_old[i]
    else:
        wukuang_old[i] = ""

wukuang_idea = idea

###########################################倍特期货


with open('倍特.txt', encoding='utf-8') as f:
    lines = f.readlines()
idea = {}
items = ["金银","铜","尿素","橡胶","苹果","豆粕","螺纹钢","鸡蛋","油脂","花生","原油","工业硅"]
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
        if i == "":
            beite_old[i] = idea[i] + " ！！倍特跟风！！" + beite_old[i]
        elif i == "":
            beite_old[i] = idea[i] + " ！！倍特很准！！ " + beite_old[i]
        else:
            beite_old[i] = idea[i] + " 倍特 " + beite_old[i]
    else:
        beite_old[i] = ""

beite_idea = idea

###########################################银河开始

with open('银河.txt', encoding='utf-8') as f:
    lines = f.readlines()
idea = {}
items = ["铁矿","钢材","焦煤焦炭","镍及不锈钢","电解铝","氧化铝","铜","锌","铝","沥青","原油","燃料油","航运板块","纸浆","天然橡胶及20号胶","甲醇","尿素",
         "动力煤","PTA","PF","MEG","EB","PP","塑料","PVC","烧碱","纯碱“,“玻璃","EB","PX","工业硅","纯碱","玻璃","丁二烯橡胶","PVC烧碱",
         "贵金属","短纤","苯乙烯","乙二醇","液化气","双硅","铅","镍","不锈钢","锡","碳酸锂","塑料PP"]
next = False
prev_item = ""
for l in lines:
    stripped = l.strip().strip('\n').strip('【').strip('】')
    if stripped == "":
        continue
    if ("想要每个交易日早上" in stripped) and next:
        if prev_item.strip("：") in items:
            idea[prev_item.strip()] += l.strip().strip('\n').split("想要每个交易日早上")[0]
        else:
            idea[prev_item.strip()] = l.strip().strip('\n').split("想要每个交易日早上")[0]
        next = False
        continue
    if ("以上观点仅供参" in stripped) and next:
        if prev_item.strip("：") in idea:
            idea[prev_item.strip()] += l.strip().strip('\n').split("以上观点仅供参")[0]
        else:
            idea[prev_item.strip()] = l.strip().strip('\n').split("以上观点仅供参")[0]
        next = False
        continue
    if ("风险点" in stripped) and next:
        if prev_item.strip("：") in idea:
            idea[prev_item.strip()] += l.strip().strip('\n').split("风险点")[0]
        else:
            idea[prev_item.strip()] = l.strip().strip('\n').split("风险点")[0]
        next = False
        continue
    # if ("相关价格" in stripped) and next:
    #     if prev_item.strip("：") in idea:
    #         idea[prev_item.strip()] += l.strip().strip('\n').split("相关价格")[0]
    #     else:
    #         idea[prev_item.strip()] = l.strip().strip('\n').split("相关价格")[0]
    #     next = False
    #     continue
    if stripped in items:
        next = True
        prev_item = stripped
        continue
    if l.startswith('银河期货') and stripped not in items:
        next = False
        continue
    if next:
        # if "套利：" in l:
        #     next = False
        #     idea[prev_item] += l.strip().strip('\n').split("套利：")[0]
        #     continue
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
    if key == "塑料PP":
        topop.append("塑料PP")
        toadd.append(["塑料", idea[key]])
        toadd.append(["PP", idea[key]])
    if key == "PVC烧碱":
        topop.append("PVC烧碱")
        toadd.append(["PVC", idea[key]])
        toadd.append(["烧碱", idea[key]])
    if key == "丁二烯橡胶":
        topop.append("丁二烯橡胶")
        toadd.append(["合成橡胶", idea[key]])
    if key == "双硅":
        topop.append("双硅")
        toadd.append(["硅铁", idea[key]])
        toadd.append(["锰硅", idea[key]])
    if key == "液化气":
        topop.append("液化气")
        toadd.append(["LPG", idea[key]])
    if key == "电解铝":
        topop.append("电解铝")
        toadd.append(["铝", idea[key]])
    if key == "焦煤焦炭":
        topop.append("焦煤焦炭")
        toadd.append(["焦煤", idea[key]])
        toadd.append(["焦炭", idea[key]])
    if key == "贵金属":
        topop.append("贵金属")
        toadd.append(["黄金", idea[key]])
        toadd.append(["白银", idea[key]])
    if key == "航运板块":
        topop.append("航运板块")
        toadd.append(["集运", idea[key]])
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
    if key == "PTA":
        toadd.append(["短纤", idea[key]])
    if key == "PF":
        topop.append("PF")
        toadd.append(["短纤", idea[key]])
    if key == "EB":
        topop.append("EB")
        toadd.append(["苯乙烯", idea[key]])
    if key == "乙二醇":
        topop.append("乙二醇")
        toadd.append(["MEG", idea[key]])
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
        if i == "":
            yinhe_old[i] = idea[i] + " !!银河跟风!! " + yinhe_old[i]
        elif i == "":
            yinhe_old[i] = idea[i] + " ！！银河很准！！ " + yinhe_old[i]
        else:
            yinhe_old[i] = idea[i] + " 银河 " + yinhe_old[i]
    else:
        yinhe_old[i] = ""

yinhe_idea = idea

###########################################银河农产品开始

#!/usr/bin/python
# -*- coding: gbk -*-
import keywords

with open('银河农产品.txt', encoding='utf-8') as f:
    lines = f.readlines()
idea = {}
items = ["花生","棉花-棉纱","白糖","鸡蛋","生猪","玉米/玉米淀粉","油脂板块","大豆/粕类","瓦楞纸"]

next = False
prev_item = ""
for l in lines:
    stripped = l.strip().strip('\n').strip('【').strip('】')
    if stripped == "":
        continue
    if ("想要每个交易日早上" in stripped) and next:
        if prev_item.strip("：") in items:
            idea[prev_item.strip()] += l.strip().strip('\n').split("想要每个交易日早上")[0]
        else:
            idea[prev_item.strip()] = l.strip().strip('\n').split("想要每个交易日早上")[0]
        next = False
        continue
    if ("套利:" in stripped) and next:
        if prev_item.strip("：") in idea:
            idea[prev_item] += l.strip().strip('\n').split("套利:")[0]
        else:
            idea[prev_item] = l.strip().strip('\n').split("套利:")[0]
        next = False
        continue
    if ("点击“阅读原文”" in stripped) and next:
        if prev_item.strip("：") in idea:
            idea[prev_item.strip("：") ] += l.strip().strip('\n').split("点击“阅读原文”")[0]
        else:
            idea[prev_item.strip("：") ] = l.strip().strip('\n').split("点击“阅读原文”")[0]
        next = False
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
    if key == "瓦楞纸":
        topop.append("瓦楞纸")
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

with open('广发.txt', encoding='utf-8') as f:
    lines = f.readlines()
idea = {}
items = ["股指期货：","国债期货：","贵金属：","铜：","锌：","铝：","镍：","不锈钢：","锡：","碳酸锂：","钢材：","铁矿石：","焦炭：","焦煤：","动力煤：","豆粕：","多晶硅：","工业硅：","瓶片：",
         "油脂：","生猪：","玉米：","白糖：","棉花：","鸡蛋：","花生：","红枣：","LLDPE:","PP:","氧化铝：","硅锰：","氧化铝：","锰硅：","合成橡胶：","尿素：",
         "原油：","沥青：","PTA：","PX：","乙二醇：","燃料油：","LPG：","短纤：","苯乙烯：","LLDPE：","PP：","尿素:","PVC：","烧碱：","硅铁：","硅锰：","甲醇：",
         "纯碱：","玻璃：","玻璃:","纯碱:","橡胶：","纸浆：","苹果：","工业硅","工业硅：","LPG:","粕类：","集运指数"]
next = False
prev_item = ""
for l in lines:
    stripped = l.strip().strip('\n').strip('【').strip('】')
    if stripped == "":
        continue
    # if "纸浆、纯碱玻璃、工业硅" in stripped:
    #     prev_item = ""
    #     continue
    if ("免责声明" in stripped) and next:
        if prev_item.strip("：") in idea:
            idea[prev_item.strip("：") ] += l.strip().strip('\n').split("免责声明")[0]
        else:
            idea[prev_item.strip("：") ] = l.strip().strip('\n').split("免责声明")[0]
        next = False
        continue
    # if ("国际方面：" in stripped) and next:
    #     if prev_item.strip("：") in idea:
    #         idea[prev_item.strip("：") ] += l.strip().strip('\n').split("国际方面：")[0]
    #     else:
    #         idea[prev_item.strip("：") ] = l.strip().strip('\n').split("国际方面：")[0]
    #     next = False
    #     continue
    if "纯碱：" in stripped:
        if "纯碱" in idea:
            idea["纯碱"] += stripped
        else:
            idea["纯碱"] = stripped
        prev_item = "纯碱"
        continue
    if "玻璃：" in stripped:
        if "玻璃" in idea:
            idea["玻璃"] += stripped
        else:
            idea["玻璃"] = stripped
        prev_item = "玻璃"
        continue
    # if "橡胶：" in stripped:
    #     idea["橡胶"] = stripped
    #     prev_item = "橡胶"
    #     next = True
    #     continue
    if stripped in items:
        next = True
        prev_item = stripped
        continue
    else:
        for i in items:
            if i in stripped:
                next = True
                if "：" in i:
                    prev_item = i.strip("：")
                else:
                    prev_item = i.strip(":")
                break
    if next:
        if prev_item.strip("：") in idea:
            idea[prev_item.strip("：") ] += l.strip().strip('\n')
        else:
            idea[prev_item.strip("：") ] = l.strip().strip('\n')


topop = []
toadd = []
for key in idea:
    if key == "PVC":
        toadd.append(["烧碱", idea[key]])
    if key == "铝":
        toadd.append(["氧化铝", idea[key]])
    if key == "集运指数":
        topop.append("集运指数")
        toadd.append(["集运", idea[key]])
    if key == "贵金属":
        topop.append("贵金属")
        toadd.append(["黄金", idea[key]])
        toadd.append(["白银", idea[key]])
    if key == "玻璃：":
        topop.append("玻璃：")
    if key == "纯碱：":
        topop.append("纯碱：")
    if key == "纯碱:":
        topop.append("纯碱:")
    if key == "玻璃:":
        topop.append("玻璃:")
    if key == "油脂":
        topop.append("油脂")
        toadd.append(["豆油", idea[key]])
        toadd.append(["菜油", idea[key]])
        toadd.append(["棕榈油", idea[key]])
    if key == "股指期货":
        topop.append("股指期货")
        toadd.append(["股指", idea[key]])
    if key == "国债期货":
        topop.append("国债期货")
        toadd.append(["国债", idea[key]])
    if key == "乙二醇":
        topop.append("乙二醇")
        toadd.append(["MEG", idea[key]])
    if key == "LLDPE":
        topop.append("LLDPE")
        toadd.append(["塑料", idea[key]])
    if key == "粕类":
        topop.append("粕类")
        toadd.append(["豆粕", idea[key]])
        toadd.append(["菜粕", idea[key]])
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
    if key == "硅锰":
        topop.append("硅锰")
        toadd.append(["锰硅", idea[key]])
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
        if i == "":
            guangfa_old[i] = idea[i] + " ！！广发跟风！！ " + guangfa_old[i]
        else:
            guangfa_old[i] = idea[i] + " 广发 " + guangfa_old[i]
    else:
        guangfa_old[i] = ""

guangfa_idea = idea

############################################广州开始

with open('广州.txt', encoding='utf-8') as f:
    lines = f.readlines()
idea = {}
items = ["原油","沥青","铜","郑棉","螺纹钢","焦炭","铝","锌","焦煤","镍","贵金属","不锈钢","玉米与淀粉","铅","锡","多晶硅",
         "天然橡胶","棉花","白糖","股指","铝","油脂类","PVC","PTA/PX/短纤","动力煤","纯碱","玻璃","生猪","豆粕","液化气","RU","聚烯烃","聚酯","工业硅","集运指数","畜禽养殖","碳酸锂","蛋白粕","PTA","乙二醇"]
next = False
prev_item = ""
for l in lines:
    if "：" in l and len(l) <= 40 and l.split('：')[0] in items:
        if "广州期货研究中心" in l.split('：')[1].replace('\n',""):
            to_sub = l.split('：')[1].replace('\n',"").split("广州期货研究中心")[0]
        else:
            to_sub = l.split('：')[1].replace('\n',"")
        idea[l.split('：')[0]] = to_sub
        prev_item = l.split('：')[0]
        next = True
    elif ":" in l and len(l) <= 40 and l.split(':')[0] in items:
        if "广州期货研究中心" in l.split(':')[1].replace('\n',""):
            to_sub = l.split(':')[1].replace('\n',"").split("广州期货研究中心")[0]
        else:
            to_sub = l.split(':')[1].replace('\n',"")
        idea[l.split(':')[0]] = to_sub
        prev_item = l.split(':')[0]
        next = True
    elif next:
        if "广州期货研究中心" in l.replace('\n',""):
            to_sub = l.replace('\n',"").split("广州期货研究中心")[0]
        else:
            to_sub = l.replace('\n',"")
        idea[prev_item] += to_sub





topop = []
toadd = []
for key in idea:
    if key == "PTA/PX/短纤":
        topop.append("PTA/PX/短纤")
        toadd.append(["PTA", idea[key]])
        toadd.append(["PX", idea[key]])
        toadd.append(["短纤", idea[key]])
    if key == "油脂类":
        topop.append("油脂类")
        toadd.append(["豆油", idea[key]])
        toadd.append(["菜油", idea[key]])
        toadd.append(["棕榈油", idea[key]])
    if key == "畜禽养殖":
        topop.append("畜禽养殖")
        toadd.append(["生猪", idea[key]])
        toadd.append(["鸡蛋", idea[key]])
    if key == "集运指数":
        topop.append("集运指数")
        toadd.append(["集运", idea[key]])
    if key == "贵金属":
        topop.append("贵金属")
        toadd.append(["黄金", idea[key]])
        toadd.append(["白银", idea[key]])
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
    if key == "玉米与淀粉":
        topop.append("玉米与淀粉")
        toadd.append(["玉米", idea[key]])
        toadd.append(["淀粉", idea[key]])
    if key == "聚酯":
        topop.append("聚酯")
        toadd.append(["PTA", idea[key]])
        toadd.append(["MEG", idea[key]])
    if key == "天然橡胶":
        topop.append("天然橡胶")
        toadd.append(["橡胶", idea[key]])
    if key == "豆粕":
        toadd.append(["菜粕", idea[key]])
    if key == "蛋白粕":
        topop.append("蛋白粕")
        toadd.append(["豆粕", idea[key]])
    if key == "乙二醇":
        topop.append("乙二醇")
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
        if i == "":
            guangzhou_old[i] = idea[i] + " ！！广州很准！！ " + guangzhou_old[i]
        elif i == "":
            guangzhou_old[i] = idea[i] + " ！！广州傻逼！！ " + guangzhou_old[i]
        else:
            guangzhou_old[i] = idea[i] + " 广州 " + guangzhou_old[i]
    else:
        guangzhou_old[i] = ""
guangzhou_idea = idea

###########################################国信开始

with open('国信.txt', encoding='utf-8') as f:
    lines = f.readlines()
idea = {}
items = ["股指","国债","贵金属","铜铝","碳酸锂","纯碱：","尿素","焦炭焦煤","玻璃","铜铝、氧化铝","铝、氧化铝","热卷","纸浆","玻璃纯碱","工业硅 多晶硅",
         "锌镍","锌","纯碱","铜","螺纹钢","工业硅","铝 氧化铝","锰硅：","硅铁：","铁合金","焦炭焦煤","焦煤焦炭","焦煤 焦炭","工业硅、多晶硅",
         "镍","豆类","油脂","白糖","棉花","玉米","生猪","花生","苹果","PTA","聚烯烃","原油","橡胶","燃料油","沥青","甲醇","铁矿石","动力煤"]
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
    # if "锰硅：" in stripped:
    #     next = False
    #     idea["锰硅"] = l.strip().strip('\n')
    #     continue
    # if "硅铁：" in stripped:
    #     next = False
    #     idea["硅铁"] = l.strip().strip('\n')
    #     continue
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
    if key == "工业硅 多晶硅":
        topop.append("工业硅 多晶硅")
        toadd.append(["工业硅", idea[key]])
    if key == "工业硅、多晶硅":
        topop.append("工业硅、多晶硅")
        toadd.append(["工业硅", idea[key]])
    if key == "焦煤 焦炭":
        topop.append("焦煤 焦炭")
        toadd.append(["焦煤", idea[key]])
        toadd.append(["焦炭", idea[key]])
    if key == "玻璃纯碱":
        topop.append("玻璃纯碱")
        toadd.append(["纯碱", idea[key]])
        toadd.append(["玻璃", idea[key]])
    if key == "纯碱：":
        topop.append("纯碱：")
        toadd.append(["纯碱", idea[key]])
    if key == "铝 氧化铝":
        topop.append("铝 氧化铝")
        toadd.append(["铝", idea[key]])
        toadd.append(["氧化铝", idea[key]])
    if key == "铝、氧化铝":
        topop.append("铝、氧化铝")
        toadd.append(["铝", idea[key]])
        toadd.append(["氧化铝", idea[key]])
    if key == "铜铝、氧化铝":
        topop.append("铜铝、氧化铝")
        toadd.append(["铜", idea[key]])
        toadd.append(["铝", idea[key]])
        toadd.append(["氧化铝", idea[key]])
    if key == "锌镍":
        topop.append("锌镍")
        toadd.append(["锌", idea[key]])
        toadd.append(["镍", idea[key]])
    if key == "铁矿石":
        topop.append("铁矿石")
        toadd.append(["铁矿", idea[key]])
    if key == "螺纹钢":
        topop.append("螺纹钢")
        toadd.append(["螺纹", idea[key]])
        toadd.append(["热卷", idea[key]])
    if key == "焦煤焦炭":
        topop.append("焦煤焦炭")
        toadd.append(["焦炭", idea[key]])
        toadd.append(["焦煤", idea[key]])
    if key == "焦炭焦煤":
        topop.append("焦炭焦煤")
        toadd.append(["焦炭", idea[key]])
        toadd.append(["焦煤", idea[key]])
    if key == "铁合金":
        topop.append("铁合金")
        toadd.append(["硅铁", idea[key]])
        toadd.append(["锰硅", idea[key]])
    if key == "燃料油":
        topop.append("燃料油")
        toadd.append(["燃油", idea[key]])
    if key == "PTA":
        toadd.append(["短纤", idea[key]])
    if key == "贵金属":
        topop.append("贵金属")
        toadd.append(["黄金", idea[key]])
        toadd.append(["白银", idea[key]])
    if key == "铜铝":
        topop.append("铜铝")
        toadd.append(["铜", idea[key]])
        toadd.append(["铝", idea[key]])
    if key == "锰硅：":
        topop.append("锰硅：")
        toadd.append(["锰硅", idea[key]])
    if key == "硅铁：":
        topop.append("硅铁：")
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
        if i == "":
            guoxin_old[i] = idea[i] + " ！！国信跟风！！ " + guoxin_old[i]
        elif i == "":
            guoxin_old[i] = idea[i] + " ！！国信很准！！ " + guoxin_old[i]
        else:
            guoxin_old[i] = idea[i] + " 国信 " + guoxin_old[i]
    else:
        guoxin_old[i] = ""

guoxin_idea = idea

##########################################永安开始

with open('永安.txt', encoding='utf-8') as f:
    lines = f.readlines()
idea = {}
items = ["股指期货","钢 材","【铝】","【铜】","【锌】","【镍】","【不锈钢】","铁 矿 石","动 力 煤","ENERGY","焦煤焦炭","白糖","纸 浆","PULP","【原油】","【沥青】","橡胶","【ＬＰＧ】","【LPG】","尿 素",
         "豆类油脂","棉花","白 糖","生 猪","生猪","豆粕","液化气","RU","聚烯烃","聚酯","S T E E L","纯碱玻璃","SODA ASH & GLASS","ALKALI-RICH GLASS"]
next = False
prev_item = ""
for l in lines:
    stripped = l.strip()
    if stripped == "":
        continue
    if "LPG早报" in stripped:
        prev_item = "LPG"
    if ("永安期货知识产权" in stripped) and next:
        if prev_item.strip("：") in idea:
            idea[prev_item.strip("：") ] += l.strip().strip('\n').split("永安期货知识产权")[0]
        else:
            idea[prev_item.strip("：") ] = l.strip().strip('\n').split("永安期货知识产权")[0]
        next = False
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
    if key == "白 糖":
        topop.append("白 糖")
        toadd.append(["白糖", idea[key]])
    if key == "焦煤焦炭":
        topop.append("焦煤焦炭")
        toadd.append(["焦煤", idea[key]])
        toadd.append(["焦炭", idea[key]])
    if key == "SODA ASH & GLASS":
        topop.append("SODA ASH & GLASS")
        toadd.append(["纯碱", idea[key]])
        toadd.append(["玻璃", idea[key]])
    if key == "ALKALI-RICH GLASS":
        topop.append("ALKALI-RICH GLASS")
        toadd.append(["纯碱", idea[key]])
        toadd.append(["玻璃", idea[key]])
    if key == "钢 材":
        topop.append("钢 材")
        toadd.append(["螺纹", idea[key]])
        toadd.append(["热卷", idea[key]])
    # if key == "ENERGY":
    #     topop.append("ENERGY")
    #     toadd.append(["原油", idea[key]])
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
    if key == "【铝】":
        topop.append("【铝】")
        toadd.append(["铝", idea[key]])
    if key == "【铜】":
        topop.append("【铜】")
        toadd.append(["铜", idea[key]])
    if key == "【锌】":
        topop.append("【锌】")
        toadd.append(["锌", idea[key]])
    if key == "【镍】":
        topop.append("【镍】")
        toadd.append(["镍", idea[key]])
    if key == "【不锈钢】":
        topop.append("【不锈钢】")
        toadd.append(["不锈钢", idea[key]])
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
        toadd.append(["棕榈油", idea[key]])
        toadd.append(["豆油", idea[key]])
        toadd.append(["菜油", idea[key]])
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
        if i == "":
            yongan_old[i] = idea[i] + " ！！永安很准！！ " + yongan_old[i]
        else:
            yongan_old[i] = idea[i] + " 永安 " + yongan_old[i]
    else:
        yongan_old[i] = ""

yongan_idea = idea

###########################################国都开始


with open('国都.txt', encoding='utf-8') as f:
    lines = f.readlines()
idea = {}
items = ["图片豆粕","豆粕","PTA","涤纶短纤","橡胶","棉花","豆类","橡胶","油脂","白糖","玉米、淀粉","生猪","铁矿石","螺纹钢","热卷"]
next = False
prev_item = ""
for l in lines:
    stripped = l.strip()
    if stripped == "":
        continue
    if "图片阅读" in stripped and next:
        if prev_item.strip("：") in idea:
            idea[prev_item.strip()] += l.strip().strip('\n').split("图片阅读")[0]
        else:
            idea[prev_item.strip()] = l.strip().strip('\n').split("图片阅读")[0]
        next = False
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
    if key == "玉米、淀粉":
        topop.append("玉米、淀粉")
        toadd.append(["玉米", idea[key]])
        toadd.append(["淀粉", idea[key]])
    if key == "螺纹钢":
        topop.append("螺纹钢")
        toadd.append(["螺纹", idea[key]])
    if key == "铁矿石":
        topop.append("铁矿石")
        toadd.append(["铁矿", idea[key]])
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


# with open('鲁证.txt', encoding='utf-8') as f:
#     lines = f.readlines()
# idea = {}
# items = ["股指期货","国债期货","棉花","白糖","油脂油料","鸡蛋","苹果","玉米系","红枣","花生","生猪","原油","塑料","沥青","橡胶","甲醇",
#          "纯碱","PVC","聚酯产业链","纸浆","尿素","铜","铝","镍","不锈钢","贵金属","螺矿","煤焦","铁合金","苯乙烯","液化石油气","锡"]
# next = False
# prev_item = ""
# for l in lines:
#     stripped = l.strip()
#     if "中泰期货股份有限公司" in l:
#         break
#     if stripped == "":
#         continue
#     if ("中泰期货分析师团队" in stripped) and next:
#         if prev_item.strip("：") in idea:
#             idea[prev_item.strip()] += l.strip().strip('\n').split("中泰期货分析师团队")[0]
#         else:
#             idea[prev_item.strip()] = l.strip().strip('\n').split("投中泰期货分析师团队")[0]
#         next = False
#         continue
#     if ("套利上" in stripped) and next:
#         if prev_item.strip("：") in idea:
#             idea[prev_item.strip()] += l.strip().strip('\n').split("套利上")[0]
#         else:
#             idea[prev_item.strip()] = l.strip().strip('\n').split("套利上")[0]
#         next = False
#         continue
#     if ("套利方面" in stripped) and next:
#         if prev_item.strip("：") in idea:
#             idea[prev_item.strip()] += l.strip().strip('\n').split("套利方面")[0]
#         else:
#             idea[prev_item.strip()] = l.strip().strip('\n').split("套利方面")[0]
#         next = False
#         continue
#     if ("技术上看" in stripped) and next:
#         if prev_item.strip("：") in idea:
#             idea[prev_item.strip()] += l.strip().strip('\n').split("技术上看")[0]
#         else:
#             idea[prev_item.strip()] = l.strip().strip('\n').split("技术上看")[0]
#         next = False
#         continue
#     if stripped in items:
#         next = True
#         prev_item = stripped
#         continue
#     if next:
#         if prev_item.strip("：") in idea:
#             idea[prev_item.strip()] += l.strip().strip('\n')
#         else:
#             idea[prev_item.strip()] = l.strip().strip('\n')
#
# topop = []
# toadd = []
# for key in idea:
#     if key == "油脂油料":
#         topop.append("油脂油料")
#         toadd.append(["豆油", idea[key]])
#         toadd.append(["菜油", idea[key]])
#         toadd.append(["棕榈油", idea[key]])
#     if key == "玉米系":
#         topop.append("玉米系")
#         toadd.append(["玉米", idea[key]])
#         toadd.append(["淀粉", idea[key]])
#     if key == "塑料":
#         toadd.append(["PP", idea[key]])
#     if key == "聚酯产业链":
#         topop.append("聚酯产业链")
#         toadd.append(["PTA", idea[key]])
#         toadd.append(["短纤", idea[key]])
#         toadd.append(["MEG", idea[key]])
#     if key == "贵金属":
#         topop.append("贵金属")
#         toadd.append(["黄金", idea[key]])
#         toadd.append(["白银", idea[key]])
#     if key == "液化石油气":
#         topop.append("液化石油气")
#         toadd.append(["LPG", idea[key]])
#     if key == "螺矿":
#         topop.append("螺矿")
#         toadd.append(["螺纹", idea[key]])
#         toadd.append(["热卷", idea[key]])
#         toadd.append(["铁矿", idea[key]])
#     if key == "铁合金":
#         topop.append("铁合金")
#         toadd.append(["锰硅", idea[key]])
#         toadd.append(["硅铁", idea[key]])
#     if key == "煤焦":
#         topop.append("煤焦")
#         toadd.append(["焦煤", idea[key]])
#         toadd.append(["焦炭", idea[key]])
#     if key == "股指期货":
#         topop.append("股指期货")
#         toadd.append(["股指", idea[key]])
#     if key == "国债期货":
#         topop.append("国债期货")
#         toadd.append(["股指", idea[key]])
# for i in topop:
#     idea.pop(i)
# for i in toadd:
#     idea[i[0]] = i[1]
#
# luzheng_old = {}
# for i in idea:
#     luzheng_old[i] = idea[i][:]
#
# for key in idea:
#     if not idea[key].isdecimal():
#         idea[key] = keywords.simplify_sent(idea[key])
#
#
# for i in luzheng_old:
#     if i in idea:
#         if i == "":
#             luzheng_old[i] = idea[i] + " ！！鲁证跟风！！ " + luzheng_old[i]
#         elif i == "":
#             luzheng_old[i] = idea[i] + " ！！鲁证很准！！ " + luzheng_old[i]
#         else:
#             luzheng_old[i] = idea[i] + " 鲁证 " + luzheng_old[i]
#     else:
#         luzheng_old[i] = ""
#
# luzheng_idea = idea

############################################南华期市早餐开始

with open('南华.txt', encoding='utf-8') as f:
    lines = f.readlines()
idea = {}
items = ["国债日报","股指","黄金","螺纹","热卷","国债","碳酸锂","铁矿","焦煤","焦炭","锰硅","尿素","黄金&白银","镍，不锈钢","PP","PE",
         "动力煤","纯碱","玻璃","白糖","棉花","苹果","红枣","油料","油脂","原油","油脂油料","甲醇","燃料油","PVC","聚酯","沥青","原木",
         "PTA","MEG","PF","PX","TA","废钢","EG","铁合金","LPG","鸡蛋","集运","焦煤焦炭","人民币汇率","镍&不锈钢","铝产业链","MEG-瓶片",
         "焦煤焦炭","铝&氧化铝","RU2405","纸浆","橡胶","玉米&淀粉","工业硅","铜","铝","锌","镍不锈钢","锡","豆一","低硫燃料油","PTA-PX","硅锰&硅铁",
         "贵金属","聚烯烃","螺纹钢","铁矿石","郑棉","豆粕","生猪","MA","SC","RU","EB","乙二醇","苯乙烯","PTA&PF","黄金&白银","国产大豆"]
next = False
prev_item = ""
for l in lines:
    stripped = l.strip()
    if stripped == "":
        continue
    if ("重要声明：以上内容及观点仅供参考" in stripped) and next:
        if prev_item.strip("：") in items:
            idea[prev_item.strip()] += l.strip().strip('\n').split("重要声明：以上内容及观点仅供参考")[0]
        else:
            idea[prev_item.strip()] = l.strip().strip('\n').split("重要声明：以上内容及观点仅供参考")[0]
        next = False
        continue
    if "以上评论由分析师" in stripped:
        stripped = stripped.split("以上评论由分析师")[0]
        next = False
    if "以上评论由南华" in stripped:
        stripped = stripped.split("以上评论由南华")[0]
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
    if key == "PE":
        topop.append("PE")
        toadd.append(["塑料", idea[key]])
    if key == "硅锰&硅铁":
        topop.append("硅锰&硅铁")
        toadd.append(["锰硅", idea[key]])
        toadd.append(["硅铁", idea[key]])
    if key == "镍，不锈钢":
        topop.append("镍，不锈钢")
        toadd.append(["不锈钢", idea[key]])
        toadd.append(["镍", idea[key]])
    if key == "国产大豆":
        topop.append("国产大豆")
        toadd.append(["豆一", idea[key]])
    if key == "MEG-瓶片":
        topop.append("MEG-瓶片")
        toadd.append(["MEG", idea[key]])
        toadd.append(["瓶片", idea[key]])
    if key == "PTA-PX":
        topop.append("PTA-PX")
        toadd.append(["PTA", idea[key]])
        toadd.append(["PX", idea[key]])
    if key == "铝产业链":
        topop.append("铝产业链")
        toadd.append(["铝", idea[key]])
    if key == "黄金&白银":
        topop.append("黄金&白银")
        toadd.append(["黄金", idea[key]])
        toadd.append(["白银", idea[key]])
    if key == "低硫燃料油":
        topop.append("低硫燃料油")
        toadd.append(["低硫燃油", idea[key]])
    if key == "铁合金":
        topop.append("铁合金")
        toadd.append(["硅铁", idea[key]])
        toadd.append(["锰硅", idea[key]])
    if key == "焦煤焦炭":
        topop.append("焦煤焦炭")
        toadd.append(["焦煤", idea[key]])
        toadd.append(["焦炭", idea[key]])
    if key == "油脂":
        topop.append("油脂")
        toadd.append(["豆油", idea[key]])
        toadd.append(["菜油", idea[key]])
        toadd.append(["棕榈油", idea[key]])
    if key == "油料":
        topop.append("油料")
        toadd.append(["豆粕", idea[key]])
        toadd.append(["菜粕", idea[key]])
    if key == "玉米&淀粉":
        topop.append("玉米&淀粉")
        toadd.append(["玉米", idea[key]])
        toadd.append(["淀粉", idea[key]])
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
    # if key == "硅锰":
    #     topop.append("硅锰")
    #     toadd.append(["锰硅", idea[key]])
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
    if key == "TA":
        topop.append("TA")
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
    if key == "镍&不锈钢":
        topop.append("镍&不锈钢")
        toadd.append(["镍", idea[key]])
        toadd.append(["不锈钢", idea[key]])
    if key == "乙二醇":
        topop.append("乙二醇")
        toadd.append(["MEG", idea[key]])
    if key == "EG":
        topop.append("EG")
        toadd.append(["MEG", idea[key]])
    # if key == "硅锰观点":
    #     topop.append("硅锰观点")
    #     toadd.append(["锰硅", idea[key]])
    if key == "铝&氧化铝":
        topop.append("铝&氧化铝")
        toadd.append(["铝", idea[key]])
        toadd.append(["氧化铝", idea[key]])


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
        if i == "":
            nanhua_old[i] = idea[i] + " ！！南华很准！！ " + nanhua_old[i]
        elif i == "":
            nanhua_old[i] = idea[i] + " ！！南华傻逼！！ " + nanhua_old[i]
        else:
            nanhua_old[i] = idea[i] + " 南华 " +nanhua_old[i]
    else:
        nanhua_old[i] = ""

nanhua_idea = idea

###########################################东兴开始

with open('东兴.txt', encoding='utf-8') as f:
    lines = f.readlines()
idea = {}
items = ["期指","期债","动力煤","螺矿","铜","PTA","甲醇","TA","PVC","钢矿","天然橡胶","铁矿石","螺纹热卷",
         "生猪","玉米","橡胶","MA","煤焦","油脂","棉花","化工","螺纹"]
next = False
prev_item = ""
for l in lines:
    stripped = l.strip()
    if stripped == "":
        continue
    if ("免责声明" in stripped) and next:
        if prev_item.strip("：") in idea:
            idea[prev_item.strip("") ] += l.strip().strip('\n').split("免责声明")[0]
        else:
            idea[prev_item.strip("") ] = l.strip().strip('\n').split("免责声明")[0]
        next = False
        continue
    if stripped.split("：")[0] in items:
        next = True
        prev_item = stripped.split("：")[0]
    if stripped.split(":")[0] in items:
        next = True
        prev_item = stripped.split(":")[0]
    if next:
        if prev_item.strip("：") in idea:
            idea[prev_item.strip()] += l.strip().strip('\n')
        else:
            idea[prev_item.strip()] = l.strip().strip('\n')

topop = []
toadd = []
for key in idea:
    if key == "铁矿石":
        topop.append("铁矿石")
        toadd.append(["铁矿", idea[key]])
    if key == "螺纹热卷":
        topop.append("螺纹热卷")
        toadd.append(["螺纹", idea[key]])
        toadd.append(["热卷", idea[key]])
    if key == "油脂":
        topop.append("油脂")
        toadd.append(["豆油", idea[key]])
        toadd.append(["菜油", idea[key]])
        toadd.append(["棕榈油", idea[key]])
    if key == "期指":
        topop.append("期指")
        toadd.append(["股指", idea[key]])
    if key == "期债":
        topop.append("期债")
        toadd.append(["国债", idea[key]])
    if key == "天然橡胶":
        topop.append("天然橡胶")
        toadd.append(["橡胶", idea[key]])
    if key == "化工":
        topop.append("化工")
        toadd.append(["MEG", idea[key]])
    if key == "TA":
        topop.append("TA")
        toadd.append(["PTA", idea[key]])
        toadd.append(["短纤", idea[key]])
    if key == "MA":
        topop.append("MA")
        toadd.append(["甲醇", idea[key]])
    if key == "煤焦":
        topop.append("煤焦")
        toadd.append(["焦煤", idea[key]])
        toadd.append(["焦炭", idea[key]])
    if key == "钢矿":
        topop.append("钢矿")
        toadd.append(["螺纹", idea[key]])
        toadd.append(["热卷", idea[key]])
        toadd.append(["铁矿", idea[key]])
    if key == "螺矿":
        topop.append("螺矿")
        toadd.append(["螺纹", idea[key]])
        toadd.append(["热卷", idea[key]])
        toadd.append(["铁矿", idea[key]])

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
        if i == "":
            dongxing_old[i] = idea[i] + " ！！东兴很准！！" + dongxing_old[i]
        else:
            dongxing_old[i] = idea[i] + " 东兴 " + dongxing_old[i]
    else:
        dongxing_old[i] = ""

dongxing_idea = idea

###########################################混沌天成工业品开始
with open('混沌天成工业品.txt', encoding='utf-8') as f:
    lines = f.readlines()
idea = {}
items = ["钢材","铁矿石","焦煤","焦炭","铜","铝","锌","镍","不锈钢","双焦"]
next = False
prev_item = ""
for l in lines:
    stripped = l.strip().strip('\n').strip('【').strip('】')
    if stripped == "":
        continue
    if ("消息及数据" in stripped) and next:
        if prev_item.strip("：") in idea:
            idea[prev_item.strip()] += l.strip().strip('\n').split("消息及数据")[0]
        else:
            idea[prev_item.strip()] = l.strip().strip('\n').split("消息及数据")[0]
        next = False
        continue
    if ("消息与数据" in stripped) and next:
        if prev_item.strip("：") in idea:
            idea[prev_item.strip()] += l.strip().strip('\n').split("消息与数据")[0]
        else:
            idea[prev_item.strip()] = l.strip().strip('\n').split("消息与数据")[0]
        next = False
        continue
    if ("行业信息" in stripped) and next:
        if prev_item.strip("：") in idea:
            idea[prev_item.strip()] += l.strip().strip('\n').split("行业信息")[0]
        else:
            idea[prev_item.strip()] = l.strip().strip('\n').split("行业信息")[0]
        next = False
        continue
    if ("混沌天成研究院" in stripped) and next:
        if prev_item.strip("：") in idea:
            idea[prev_item.strip()] += l.strip().strip('\n').split("混沌天成研究院")[0]
        else:
            idea[prev_item.strip()] = l.strip().strip('\n').split("混沌天成研究院")[0]
        next = False
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
    if key == "双焦":
        topop.append("双焦")
        toadd.append(["焦煤", idea[key]])
        toadd.append(["焦炭", idea[key]])

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
        if i =="":
            hundungong_old[i] = idea[i] + " ！！混沌工业很准！！ " + hundungong_old[i]
        else:
            hundungong_old[i] = idea[i] + " 混沌工业 " + hundungong_old[i]
    else:
        hundungong_old[i] = ""

hundungong_idea = idea

###########################################混沌天成能化开始

with open('混沌天成能化.txt', encoding='utf-8') as f:
    lines = f.readlines()
idea = {}
items = ["纯碱玻璃","橡胶","PVC","LLDPE日评","PP","尿素","甲醇","MEG日评：","LPG","MEG日评:","PTA日评：","PTA日评","原油","PP日评：","PTA/MEG"]
next = False
prev_item = ""
for l in lines:
    stripped = l.strip().strip('\n').strip('【').strip('】')
    if stripped == "":
        continue
    if ("混沌天成研究院" in stripped) and next:
        if prev_item.strip("：") in idea:
            idea[prev_item.strip()] += l.strip().strip('\n').split("混沌天成研究院")[0]
        else:
            idea[prev_item.strip()] = l.strip().strip('\n').split("混沌天成研究院")[0]
        next = False
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
    if l.startswith('PTA：'):
        prev_item = 'PTA'
    if l.startswith('MEG：'):
        prev_item = 'MEG'
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
    if key == "PTA/MEG":
        topop.append("PTA/MEG")
        toadd.append(["PTA", idea[key]])
        toadd.append(["MEG", idea[key]])
    if key == "PTA":
        toadd.append(["短纤", idea[key]])
    if key == "MEG日评：":
        topop.append("MEG日评：")
        toadd.append(["MEG", idea[key]])
    if key == "MEG日评:":
        topop.append("MEG日评:")
        toadd.append(["MEG", idea[key]])
    if key == "PTA日评":
        topop.append("PTA日评")
        toadd.append(["PTA", idea[key]])
    if key == "PTA日评：":
        topop.append("PTA日评：")
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
        if i == "":
            hundunneng_old[i] = idea[i] + " ！！混沌能化很准！！ " + hundunneng_old[i]
        else:
            hundunneng_old[i] = idea[i] + " 混沌能化 " + hundunneng_old[i]
    else:
        hundunneng_old[i] = ""

hundunneng_idea = idea

###########################################混沌天成农产品开始

with open('混沌天成农产品.txt', encoding='utf-8') as f:
    lines = f.readlines()
idea = {}
items = ["油脂油料","棉花","棉  花","玉  米","豆  粕","鸡  蛋","生  猪","苹  果","纸  浆","红  枣","白  糖","油  脂","豆菜粕"]
next = False
prev_item = ""
for l in lines:
    stripped = l.strip().strip('\n').strip('【').strip('】')
    if stripped == "":
        continue
    if ("混沌天成研究院" in stripped) and next:
        if prev_item.strip("：") in idea:
            idea[prev_item.strip()] += l.strip().strip('\n').split("混沌天成研究院")[0]
        else:
            idea[prev_item.strip()] = l.strip().strip('\n').split("混沌天成研究院")[0]
        next = False
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
    if key == "豆菜粕":
        topop.append("豆菜粕")
        toadd.append(["豆粕", idea[key]])
    if key == "白  糖":
        topop.append("白  糖")
        toadd.append(["白糖", idea[key]])
    if key == "棉  花":
        topop.append("棉  花")
        toadd.append(["棉花", idea[key]])
    if key == "油  脂":
        topop.append("油  脂")
        toadd.append(["豆油", idea[key]])
        toadd.append(["菜油", idea[key]])
        toadd.append(["棕榈油", idea[key]])
    if key == "油脂油料":
        topop.append("油脂油料")
        toadd.append(["豆油", idea[key]])
        toadd.append(["菜油", idea[key]])
        toadd.append(["棕榈油", idea[key]])
    if key == "玉  米":
        topop.append("玉  米")
        toadd.append(["玉米", idea[key]])
    if key == "红  枣":
        topop.append("红  枣")
        toadd.append(["红枣", idea[key]])
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
        if i == "":
            hundunagri_old[i] = idea[i] + " ！！混沌农产品很准！！ " + hundunagri_old[i]
        else:
            hundunagri_old[i] = idea[i] + " 混沌农产品 " + hundunagri_old[i]
    else:
        hundunagri_old[i] = ""

hundunagri_idea = idea

###########################################弘业开始

with open('弘业.txt', encoding='utf-8') as f:
    lines = f.readlines()
idea = {}
items = ["原油","PTA","乙二醇","短纤","聚烯烃","液化石油气","集运指数欧线","铁合金","沥青","甲醇","苯乙烯","橡胶","玻璃","纯碱","尿素","纸浆","黄金&白银","沪镍","沪铜&国际铜","沪铝","沪锌","沪铅",
         "螺纹&热卷","铁矿石","焦煤&焦炭","碳酸锂","动力煤","烧碱","聚乙烯","PX","聚丙烯","钢材","沪铜&国际铜 ","集运指数（欧线）","集运欧线指数",
         "PVC","油脂","豆一","油料","工业硅","花生","玉米&淀粉","棉花&棉纱","生猪","鸡蛋","白糖","苹果","红枣","国债","股指","玉米、淀粉","短纤&瓶片"]
next = False
prev_item = ""
for l in lines:
    stripped = l.strip().strip('\n').strip('【').strip('】')
    if stripped == "":
        continue
    if "免责声明" in stripped and next:
        if prev_item.strip("：") in idea:
            idea[prev_item.strip()] += l.strip().strip('\n').split("免责声明")[0]
        else:
            idea[prev_item.strip()] = l.strip().strip('\n').split("免责声明")[0]
        next = False
        continue
    if ("从业资格证号" in stripped) and next:
        if prev_item.strip("：") in idea:
            idea[prev_item] += l.strip().strip('\n').split("从业资格证号")[0]
        else:
            idea[prev_item] = l.strip().strip('\n').split("从业资格证号")[0]
        next = False
        continue
    if "锰硅方面" in stripped:
        next = False
        idea["锰硅"] = stripped
        continue
    if "硅铁方面" in stripped:
        next = False
        idea["硅铁"] = stripped
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
    if key == "短纤&瓶片":
        topop.append("短纤&瓶片")
        toadd.append(["短纤", idea[key]])
        toadd.append(["瓶片", idea[key]])
    if key == "集运欧线指数":
        topop.append("集运欧线指数")
        toadd.append(["集运", idea[key]])
    if key == "集运指数（欧线）":
        topop.append("集运指数（欧线）")
        toadd.append(["集运", idea[key]])
    if key == "玉米、淀粉":
        topop.append("玉米、淀粉")
        toadd.append(["玉米", idea[key]])
        toadd.append(["淀粉", idea[key]])
    if key == "集运指数欧线":
        topop.append("集运指数欧线")
        toadd.append(["集运", idea[key]])
    if key == "棉花&棉纱":
        topop.append("棉花&棉纱")
        toadd.append(["棉花", idea[key]])
        toadd.append(["棉纱", idea[key]])
    if key == "玉米&淀粉":
        topop.append("玉米&淀粉")
        toadd.append(["玉米", idea[key]])
        toadd.append(["淀粉", idea[key]])
    if key == "乙二醇":
        topop.append("乙二醇")
        toadd.append(["MEG", idea[key]])
    if key == "油料":
        topop.append("油料")
        toadd.append(["豆粕", idea[key]])
        toadd.append(["菜粕", idea[key]])
        toadd.append(["菜油", idea[key]])
    if key == "油脂":
        topop.append("油脂")
        toadd.append(["豆油", idea[key]])
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
    if key == "钢材":
        topop.append("钢材")
        toadd.append(["螺纹", idea[key]])
        toadd.append(["热卷", idea[key]])
    if key == "沪镍":
        topop.append("沪镍")
        toadd.append(["镍", idea[key]])
    if key == "沪铜&国际铜":
        topop.append("沪铜&国际铜")
        toadd.append(["铜", idea[key]])
    if key == "沪铜&国际铜 ":
        topop.append("沪铜&国际铜 ")
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
    if key == "聚丙烯":
        topop.append("聚丙烯")
        toadd.append(["PP", idea[key]])
    if key == "聚乙烯":
        topop.append("聚乙烯")
        toadd.append(["塑料", idea[key]])




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
        if i == "":
            hongye_old[i] = idea[i] + " ！！弘业跟风！！ " + hongye_old[i]
        elif i == "":
            hongye_old[i] = idea[i] + " ！！弘业傻逼！！ " + hongye_old[i]
        elif i == "":
            hongye_old[i] = idea[i] + " ！！弘业很准！！ " + hongye_old[i]
        else:
            hongye_old[i] = idea[i] + " 弘业 " + hongye_old[i]
    else:
        hongye_old[i] = ""

hongye_idea = idea

###########################################东吴开始

with open('东吴.txt', encoding='utf-8') as f:
#with open('东吴.txt', encoding='utf-8') as f:
    lines = f.readlines()
idea = {}
items = ["螺卷","铁矿","双焦","双硅","原油","沥青","LPG","股指","贵金属","甲醇","天然橡胶","铝/氧化铝","镍/不锈钢","碳酸锂","工业硅","沪铜",
         "沪铝","沪锌","沪铅","油脂","豆粕/菜粕","玉米","白糖","鸡蛋","棉花","玻璃","纯碱","聚烯烃","瓶片","橡胶","纸浆","PX","PTA","MEG","PR","PVC",
         "生猪","苹果","红枣","花生","MEG","铜","铝","锌","铅","镍","不锈钢","工业硅","棉花棉纱","玻璃纯碱","沪铝/氧化铝"]

group = ["黑色系板块","能源化工","有色金属","农产品"]
next = False
prev_item = ""
for l in lines:
    value = ""
    stripped = ""
    if "：" in l and l.strip().split("：")[0] in group or ":" in l and l.strip().split(":")[0] in group:
        prev_item = ""
        next = False
        continue
    if "。" in l:
        stripped = l.strip().strip('\n').split("。")[0]
        value = "".join(l.strip().strip('\n').split("。")[1:])
        if stripped == "":
            continue
    elif "：" in l:
        stripped = l.strip().strip('\n').split("：")[0]
        value = "".join(l.strip().strip('\n').split("：")[1:])
        if stripped == "":
            continue
    if stripped in items:
        next = True
        prev_item = stripped
        if prev_item in idea:
            idea[prev_item.strip()] += value
        else:
            idea[prev_item.strip()] = value
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
    if key == "贵金属":
        topop.append("贵金属")
        toadd.append(["黄金", idea[key]])
        toadd.append(["白银", idea[key]])
    if key == "聚烯烃":
        topop.append("聚烯烃")
        toadd.append(["PP", idea[key]])
        toadd.append(["塑料", idea[key]])
    if key == "沪铝/氧化铝":
        topop.append("沪铝/氧化铝")
        toadd.append(["铝", idea[key]])
        toadd.append(["氧化铝", idea[key]])
    if key == "铝/氧化铝":
        topop.append("铝/氧化铝")
        toadd.append(["铝", idea[key]])
        toadd.append(["氧化铝", idea[key]])
    if key == "镍/不锈钢":
        topop.append("镍/不锈钢")
        toadd.append(["镍", idea[key]])
        toadd.append(["不锈钢", idea[key]])
    if key == "螺卷":
        topop.append("螺卷")
        toadd.append(["螺纹", idea[key]])
        toadd.append(["热卷", idea[key]])
    if key == "棉花棉纱":
        topop.append("棉花棉纱")
        toadd.append(["棉花", idea[key]])
        toadd.append(["棉纱", idea[key]])
    if key == "PTA":
        toadd.append(["短纤", idea[key]])
    if key == "双焦":
        topop.append("双焦")
        toadd.append(["焦煤", idea[key]])
        toadd.append(["焦炭", idea[key]])
    if key == "双硅":
        topop.append("双硅")
        toadd.append(["硅铁", idea[key]])
        toadd.append(["锰硅", idea[key]])
    if key == "玻璃纯碱":
        topop.append("玻璃纯碱")
        toadd.append(["玻璃", idea[key]])
        toadd.append(["纯碱", idea[key]])
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
        if i == "":
            dongwu_old[i] = idea[i] + " !!东吴跟风!! " + dongwu_old[i]
        elif i == "":
            dongwu_old[i] = idea[i] + " !!东吴很准!! " + dongwu_old[i]
        else:
            dongwu_old[i] = idea[i] + " 东吴 " + dongwu_old[i]
    else:
        dongwu_old[i] = ""

dongwu_idea = idea

###########################################华联开始


with open('华联.txt', encoding='utf-8') as f:
    lines = f.readlines()
idea = {}
items = ["股指","国债","铜","铝","橡胶","液化气","原油","锌","PVC","甲醇","工业硅","聚烯烃","锡","铁合金","碳酸锂",
         "螺纹钢","玻璃","焦煤","黄金","煤焦","铁矿石","白糖","鸡蛋","镍","生猪","油脂","饲料","集运指数","PTA"]
next = False
prev_item = ""
for l in lines:
    stripped = l.strip().strip('\n').strip('【').strip('】')
    if stripped == "":
        continue
    if '】' in stripped:
        stripped_first = l.strip().strip('\n').strip('【').split('】')[0]
        if stripped_first in items:
            next = True
            prev_item = stripped_first
    if "（孙伟涛" in stripped and next:
        if prev_item.strip("：") in idea:
            idea[prev_item.strip()] += l.strip().strip('\n').split("（孙伟涛")[0]
        else:
            idea[prev_item.strip()] = l.strip().strip('\n').split("（孙伟涛")[0]
        next = False
        continue
    if ("从业资格号" in stripped) and next:
        if prev_item.strip("：") in idea:
            idea[prev_item.strip()] += l.strip().strip('\n').split("从业资格号")[0]
        else:
            idea[prev_item.strip()] = l.strip().strip('\n').split("从业资格号")[0]
        next = False
        continue
    if next:
        if prev_item in idea:
            idea[prev_item] += l.strip().strip('\n')
        else:
            idea[prev_item] = l.strip().strip('\n')
hualian_old = {}
for i in idea:
    hualian_old[i] = idea[i][:]

topop = []
toadd = []
for key in idea:
    ###不做了
    if key == "铁合金":
        topop.append("铁合金")
        toadd.append(["硅铁", idea[key]])
        toadd.append(["锰硅", idea[key]])
    if key == "集运指数":
        topop.append("集运指数")
        toadd.append(["集运", idea[key]])
    if key == "液化气":
        topop.append("液化气")
        toadd.append(["LPG", idea[key]])
    if key == "聚烯烃":
        topop.append("聚烯烃")
        toadd.append(["塑料", idea[key]])
        toadd.append(["PP", idea[key]])
    if key == "螺纹钢":
        topop.append("螺纹钢")
        toadd.append(["螺纹", idea[key]])
        toadd.append(["热卷", idea[key]])
    if key == "铁矿石":
        topop.append("铁矿石")
        toadd.append(["铁矿", idea[key]])
    if key == "油脂":
        topop.append("油脂")
        toadd.append(["菜油", idea[key]])
        toadd.append(["棕榈油", idea[key]])
        toadd.append(["豆油", idea[key]])
    if key == "饲料":
        topop.append("饲料")
        toadd.append(["豆粕", idea[key]])
        toadd.append(["菜粕", idea[key]])
    if key == "煤焦":
        topop.append("煤焦")
        toadd.append(["焦煤", idea[key]])
        toadd.append(["焦炭", idea[key]])




for i in topop:
    idea.pop(i)
for i in toadd:
    idea[i[0]] = i[1]

hualian_old = {}
for i in idea:
    hualian_old[i] = idea[i][:]

for key in idea:
    if not idea[key].isdecimal():
        idea[key] = keywords.simplify_sent(idea[key])


for i in hualian_old:
    if i in idea:
        if i == "":
            hualian_old[i] = idea[i] + " !!华联跟风!! " + hualian_old[i]
        elif i == "":
            hualian_old[i] = idea[i] + " !!华联很准!! " + hualian_old[i]
        else:
            hualian_old[i] = idea[i] + " 华联 " + hualian_old[i]
    else:
        hualian_old[i] = ""

hualian_idea = idea

###########################################中洲开始

with open('中洲.txt', encoding='utf-8') as f:
    lines = f.readlines()
idea = {}
items = ["原油","钢材","铁矿","铁矿石","美豆","焦煤焦炭","沪铜","沪铝","苯乙烯","美豆、豆粕","玉米","白糖","鸡蛋","生猪","塑料","油脂","美豆&豆粕"]

next = False
prev_item = ""
for l in lines:
    stripped = l.strip().strip('\n').strip('【').strip('】')
    if stripped == "":
        continue
    if ("免责声明" in stripped) and next:
        if prev_item.strip("：") in items:
            idea[prev_item.strip()] += l.strip().strip('\n').split("免责声明")[0]
        else:
            idea[prev_item.strip()] = l.strip().strip('\n').split("免责声明")[0]
        next = False
        continue
    if '|' in stripped:
        stripped_first = l.strip().strip('\n').split('|')[0].strip(" ")
        if stripped_first in items:
            next = True
            prev_item = stripped_first
    if 'l' in stripped:
        stripped_first = l.strip().strip('\n').split('l')[0].strip(" ")
        if stripped_first in items:
            next = True
            prev_item = stripped_first
    stripped_first = l.strip().strip('\n').strip(" ")
    if stripped_first in items:
        next = True
        prev_item = stripped_first
    if next:
        if prev_item in idea:
            idea[prev_item] += l.strip().strip('\n')
        else:
            idea[prev_item] = l.strip().strip('\n')
zhongzhou_old = {}
for i in idea:
    zhongzhou_old[i] = idea[i][:]

topop = []
toadd = []
for key in idea:
    if key == "沪铜":
        topop.append("沪铜")
        toadd.append(["铜", idea[key]])
    if key == "沪铝":
        topop.append("沪铝")
        toadd.append(["铝", idea[key]])
    if key == "钢材":
        topop.append("钢材")
        toadd.append(["螺纹", idea[key]])
        toadd.append(["热卷", idea[key]])
    if key == "焦煤焦炭":
        topop.append("焦煤焦炭")
        toadd.append(["焦煤", idea[key]])
        toadd.append(["焦炭", idea[key]])
    if key == "铁矿石":
        topop.append("铁矿石")
        toadd.append(["铁矿", idea[key]])
    if key == "美豆、豆粕":
        topop.append("美豆、豆粕")
        toadd.append(["豆粕", idea[key]])
        toadd.append(["菜粕", idea[key]])
    if key == "美豆&豆粕":
        topop.append("美豆&豆粕")
        toadd.append(["豆粕", idea[key]])
        toadd.append(["菜粕", idea[key]])
    if key == "美豆":
        topop.append("美豆")
        toadd.append(["豆粕", idea[key]])
        toadd.append(["菜粕", idea[key]])
    if key == "油脂":
        topop.append("油脂")
        toadd.append(["豆油", idea[key]])
        toadd.append(["棕榈油", idea[key]])
        toadd.append(["菜油", idea[key]])

for i in topop:
    idea.pop(i)
for i in toadd:
    idea[i[0]] = i[1]

zhongzhou_old = {}
for i in idea:
    zhongzhou_old[i] = idea[i][:]

for key in idea:
    if not idea[key].isdecimal():
        idea[key] = keywords.simplify_sent(idea[key])


for i in zhongzhou_old:
    if i in idea:
        if i == "":
            zhongzhou_old[i] = idea[i] + " !!中洲跟风!! " + zhongzhou_old[i]
        elif i == "":
            zhongzhou_old[i] = idea[i] + " !!中洲很准!! " + zhongzhou_old[i]
        else:
            zhongzhou_old[i] = idea[i] + " 中洲 " + zhongzhou_old[i]
    else:
        zhongzhou_old[i] = ""

zhongzhou_idea = idea

###########################################一德开始

with open('一德.txt', encoding='utf-8') as f:
    lines = f.readlines()
idea = {}
items = ["期指","期债","黄金/白银","贵金属","螺纹/热卷","螺纹/热卷(RB2310/HC2310)","螺纹/热卷(RB2305/HC2305)","煤焦","塑料/PP","塑料/pp","硅锰","硅铁","动力煤","铁矿石","沪铝","沪镍","沪铜","沪锌",
         "沪铅","苹果","红枣","鸡蛋","PX","郑糖","外糖","烧碱","沥青","碳酸锂","生猪","燃料油","集运指数","锌","白糖","EC","硅","甲醇","PVC","PTA","MEG","集运指数",
         "尿素","纯碱","玻璃","塑料/PP","苯乙烯","聚酯","原油","工业硅","铅","沪锡","锰硅/硅铁","钢矿","焦煤/焦炭","合金","黑色品种","甲醇","塑料","PP"]


next = False
prev_item = ""
for l in lines:
    stripped = l.strip().strip('\n').strip('【').strip('】')
    if stripped == "":
        continue
    if ("一德期货研究团队：" in stripped) and next:
        if prev_item.strip("：") in items:
            idea[prev_item.strip()] += l.strip().strip('\n').split("一德期货研究团队：")[0]
        else:
            idea[prev_item.strip()] = l.strip().strip('\n').split("一德期货研究团队：")[0]
        next = False
        continue
    if ("本研究报告由" in stripped) and next:
        if prev_item.strip("：") in items:
            idea[prev_item.strip()] += l.strip().strip('\n').split("本研究报告由")[0]
        else:
            idea[prev_item.strip()] = l.strip().strip('\n').split("本研究报告由")[0]
        next = False
        continue
    if '黑色品种' in stripped:
        prev_item = '黑色品种'
        next = True
        continue
    if '：' in stripped:
        stripped_first = l.strip().strip('\n').split('：')[0].strip(" ")
        if "（" in stripped_first:
            stripped_first = stripped_first.split("（")[0]
        if stripped_first.strip("（2304）" )in items:
            next = True
            prev_item = stripped_first.strip("（2304）" )
    if ':' in stripped:
        stripped_first = l.strip().strip('\n').split(':')[0].strip(" ")
        if "（" in stripped_first:
            stripped_first = stripped_first.split("（")[0]
        if stripped_first.strip("（2304）" ) in items:
            next = True
            prev_item = stripped_first.strip("（2304）" )
    if len(stripped) <= 7:
        stripped_first = l.strip().strip('\n').strip(" ").strip('【').strip('】')
        if "（" in stripped_first:
            stripped_first = stripped_first.split("（")[0]
        if stripped_first.strip("（2304）" ) in items:
            next = True
            prev_item = stripped_first.strip("（2304）" )
    if '贵金属' in stripped:
        stripped_first = l.strip().strip('\n').split(':')[0].strip(" ")
        if stripped_first.strip("（2304）" ) in items:
            next = True
            prev_item = stripped_first.strip("（2304）" )
    if next:
        if prev_item in idea:
            idea[prev_item] += l.strip().strip('\n')
        else:
            idea[prev_item] = l.strip().strip('\n')
yide_old = {}
for i in idea:
    yide_old[i] = idea[i][:]

topop = []
toadd = []
for key in idea:
    if key == "黑色品种":
        topop.append("黑色品种")
        toadd.append(["螺纹", idea[key]])
        toadd.append(["热卷", idea[key]])
        toadd.append(["焦煤", idea[key]])
        toadd.append(["焦炭", idea[key]])
        toadd.append(["铁矿", idea[key]])
    if key == "EC":
        topop.append("EC")
        toadd.append(["集运", idea[key]])
    if key == "集运指数（欧线）":
        topop.append("集运指数（欧线）")
        toadd.append(["集运", idea[key]])
    if key == "集运指数":
        topop.append("集运指数")
        toadd.append(["集运", idea[key]])
    if key == "沪锡":
        topop.append("沪锡")
        toadd.append(["锡", idea[key]])
    if key == "硅":
        topop.append("硅")
        toadd.append(["工业硅", idea[key]])
    if key == "沪铜":
        topop.append("沪铜")
        toadd.append(["铜", idea[key]])
    if key == "期指":
        topop.append("期指")
        toadd.append(["股指", idea[key]])
    if key == "贵金属":
        topop.append("贵金属")
        toadd.append(["黄金", idea[key]])
        toadd.append(["白银", idea[key]])
    if key == "期债":
        topop.append("期债")
        toadd.append(["国债", idea[key]])
    if key == "郑糖":
        topop.append("郑糖")
        toadd.append(["白糖", idea[key]])
    if key == "外糖":
        topop.append("外糖")
    if key == "黄金/白银":
        topop.append("黄金/白银")
        toadd.append(["黄金", idea[key]])
        toadd.append(["白银", idea[key]])
    if key == "螺纹/热卷":
        topop.append("螺纹/热卷")
        toadd.append(["螺纹", idea[key]])
        toadd.append(["热卷", idea[key]])
    if key == "螺纹/热卷(RB2305/HC2305)":
        topop.append("螺纹/热卷(RB2305/HC2305)")
        toadd.append(["螺纹", idea[key]])
        toadd.append(["热卷", idea[key]])
    if key == "螺纹/热卷(RB2310/HC2310)":
        topop.append("螺纹/热卷(RB2310/HC2310)")
        toadd.append(["螺纹", idea[key]])
        toadd.append(["热卷", idea[key]])
    if key == "钢矿":
        topop.append("钢矿")
        toadd.append(["螺纹", idea[key]])
        toadd.append(["热卷", idea[key]])
        toadd.append(["铁矿", idea[key]])
    if key == "合金":
        topop.append("合金")
        toadd.append(["锰硅", idea[key]])
        toadd.append(["硅铁", idea[key]])
    if key == "锰硅/硅铁":
        topop.append("锰硅/硅铁")
        toadd.append(["锰硅", idea[key]])
        toadd.append(["硅铁", idea[key]])
    if key == "煤焦":
        topop.append("煤焦")
        toadd.append(["焦炭", idea[key]])
        toadd.append(["焦煤", idea[key]])
    if key == "焦煤/焦炭":
        topop.append("焦煤/焦炭")
        toadd.append(["焦炭", idea[key]])
        toadd.append(["焦煤", idea[key]])
    if key == "硅铁":
        topop.append("硅铁")
    if key == "硅锰":
        topop.append("硅锰")
        toadd.append(["锰硅", idea[key]])
    if key == "塑料/PP":
        topop.append("塑料/PP")
        toadd.append(["塑料", idea[key]])
        toadd.append(["PP", idea[key]])
    if key == "塑料/pp":
        topop.append("塑料/pp")
        toadd.append(["塑料", idea[key]])
        toadd.append(["PP", idea[key]])
    if key == "聚酯":
        topop.append("聚酯")
        toadd.append(["PTA", idea[key]])
        toadd.append(["MEG", idea[key]])
        toadd.append(["短纤", idea[key]])
    if key == "铁矿石":
        topop.append("铁矿石")
        toadd.append(["铁矿", idea[key]])
    if key == "沪铝":
        topop.append("沪铝")
        toadd.append(["铝", idea[key]])
    if key == "沪镍":
        topop.append("沪镍")
        toadd.append(["镍", idea[key]])
    if key == "沪锌":
        topop.append("沪锌")
        toadd.append(["锌", idea[key]])
        toadd.append(["铅", idea[key]])
    if key == "沪铅":
        topop.append("沪铅")
        toadd.append(["铅", idea[key]])
    if key == "燃料油":
        topop.append("燃料油")
        toadd.append(["燃油", idea[key]])

for i in topop:
    idea.pop(i)
for i in toadd:
    idea[i[0]] = i[1]

yide_old = {}
for i in idea:
    yide_old[i] = idea[i][:]

for key in idea:
    if not idea[key].isdecimal():
        idea[key] = keywords.simplify_sent(idea[key])


for i in yide_old:
    if i in idea:
        if i == "":
            yide_old[i] = idea[i] + " !!一德跟风!! " + yide_old[i]
        elif i == "":
            yide_old[i] = idea[i] + " !!一德很准!! " + yide_old[i]
        else:
            yide_old[i] = idea[i] + " 一德 " + yide_old[i]
    else:
        yide_old[i] = ""

yide_idea = idea

###########################################中泰开始#################################################################

with open('中泰.txt', encoding='utf-8') as f:
    lines = f.readlines()
idea = {}
items = ["股指期货","国债期货","棉花","白糖","油脂油料","鸡蛋","苹果","红枣","花生","生猪","原油","塑料","橡胶","甲醇","纯碱","沥青","PVC","苯乙烯","聚酯产业链","液化石油气","铝和氧化铝","镍",
         "碳酸锂","工业硅","螺矿","煤焦","铁合金","合成胶","烧碱","纸浆","纯碱玻璃","尿素","豆粕"]



next = False
prev_item = ""
for l in lines:
    stripped = l.strip().strip('\n').strip('【').strip('】')
    if stripped == "":
        continue
    else:
        stripped_first = l.strip().strip('\n').split('|')[0].strip(" ")
        if stripped_first in items:
            next = True
            prev_item = stripped_first
    if ("长按二维码" in stripped) and next:
        if prev_item.strip("：") in items:
            idea[prev_item.strip()] += l.strip().strip('\n').split("长按二维码")[0]
        else:
            idea[prev_item.strip()] = l.strip().strip('\n').split("长按二维码")[0]
        next = False
        continue
    if next:
        if prev_item in idea:
            idea[prev_item] += l.strip().strip('\n')
        else:
            idea[prev_item] = l.strip().strip('\n')

zhongtai_old = {}
for i in idea:
    zhongtai_old[i] = idea[i][:]

topop = []
toadd = []
for key in idea:
    if key == "纯碱玻璃":
        topop.append("纯碱玻璃")
        toadd.append(["纯碱", idea[key]])
        toadd.append(["玻璃", idea[key]])
    if key == "股指期货":
        topop.append("股指期货")
        toadd.append(["股指", idea[key]])
    if key == "国债期货":
        topop.append("国债期货")
        toadd.append(["国债", idea[key]])
    if key == "合成胶":
        topop.append("合成胶")
        toadd.append(["合成橡胶", idea[key]])
    if key == "油脂油料":
        topop.append("油脂油料")
        toadd.append(["豆粕", idea[key]])
        toadd.append(["豆油", idea[key]])
        toadd.append(["菜油", idea[key]])
        toadd.append(["棕榈油", idea[key]])
    if key == "聚酯产业链":
        topop.append("聚酯产业链")
        toadd.append(["PTA", idea[key]])
        toadd.append(["MEG", idea[key]])
        toadd.append(["短纤", idea[key]])
    if key == "液化石油气":
        topop.append("液化石油气")
        toadd.append(["LPG", idea[key]])
    if key == "铝和氧化铝":
        topop.append("铝和氧化铝")
        toadd.append(["铝", idea[key]])
        toadd.append(["氧化铝", idea[key]])
    if key == "螺矿":
        topop.append("螺矿")
        toadd.append(["螺纹", idea[key]])
        toadd.append(["热卷", idea[key]])
        toadd.append(["铁矿", idea[key]])
    if key == "煤焦":
        topop.append("煤焦")
        toadd.append(["焦煤", idea[key]])
        toadd.append(["焦炭", idea[key]])
    if key == "铁合金":
        topop.append("铁合金")
        toadd.append(["硅铁", idea[key]])
        toadd.append(["锰硅", idea[key]])

for i in topop:
    idea.pop(i)
for i in toadd:
    idea[i[0]] = i[1]

zhongtai_old = {}
for i in idea:
    zhongtai_old[i] = idea[i][:]

for key in idea:
    if not idea[key].isdecimal():
        idea[key] = keywords.simplify_sent(idea[key])

for i in zhongtai_old:
    if i in idea:
        if i == "":
            zhongtai_old[i] = idea[i] + " !!中泰跟风!! " + zhongtai_old[i]
        elif i == "":
            zhongtai_old[i] = idea[i] + " !!中泰很准!! " + zhongtai_old[i]
        else:
            zhongtai_old[i] = idea[i] + " 中泰 " + zhongtai_old[i]
    else:
        zhongtai_old[i] = ""

zhongtai_idea = idea

###########################################华泰开始##############

with open('华泰.txt',encoding='utf-8') as f:
    lines = f.readlines()
idea = {}
items = ["股指期货","航运","国债期货","原油","燃料油","液化石油气","石油沥青","PX、PTA、PF","苹果","甲醇","尿素","粕类","玉米","生猪","鸡蛋","苹果","红枣","棉花","纸浆","白糖","不锈钢",
         "聚烯烃","EG","EB","尿素","天然橡胶","PVC","烧碱","贵金属","顺丁橡胶","贵金属","镍不锈钢","钢材","天然橡胶与合成橡胶","氯碱","焦炭焦煤","碳酸锂","锂期货","果蔬品","天然橡胶与合成橡胶",
         "铜","锌","镍不锈钢","铝","铅","工业硅","碳酸锂","钢材","铁矿","双焦","玻璃纯碱","双硅","铁矿","大豆","花生","养殖","铁矿石","PX、PTA、PF、MEG","工业硅多晶硅","氯碱","苯乙烯",
         "油脂","大豆观点","花生观点","粕类观点","玉米观点","生猪观点","鸡蛋观点","苹果观点","红枣观点","棉花观点","纸浆观点","白糖观点","合金","PX、PTA、PF、PR"]
next = False
prev_item = ""
for l in lines:
    stripped = l.strip().strip('\n')
    if stripped == "":
        continue
    if "量化期权" in stripped:
        break
    if "：" in stripped and stripped.split("：")[0] in items:
        next = True
        prev_item = stripped.split("：")[0]
        continue
    if "更多内容" in stripped and next:
        if prev_item.strip("：") in idea:
            idea[prev_item.strip()] += l.strip().strip('\n').split("更多内容")[0]
        else:
            idea[prev_item.strip()] = l.strip().strip('\n').split("更多内容")[0]
        next = False
        continue
    if "策略摘要" in stripped and stripped.split("策略摘要")[0] in items:
        next = True
        prev_item = stripped.split("策略摘要")[0]
        continue
    if "观点" in stripped and stripped.split("观点")[0] in items:
        next = True
        prev_item = stripped.split("观点")[0]
        continue
    if l.startswith('银河期货') and stripped not in items:
        next = False
        continue
    if next:
        if prev_item in idea:
            idea[prev_item] += l.strip().strip('\n')
        else:
            idea[prev_item] = l.strip().strip('\n')
huatai_old = {}
for i in idea:
    huatai_old[i] = idea[i][:]

topop = []
toadd = []
for key in idea:
    if key == "氯碱":
        topop.append("氯碱")
        toadd.append(["PVC", idea[key]])
        toadd.append(["烧碱", idea[key]])
    if key == "天然橡胶与合成橡胶":
        topop.append("天然橡胶与合成橡胶")
        toadd.append(["橡胶", idea[key]])
        toadd.append(["合成橡胶", idea[key]])
    if key == "工业硅多晶硅":
        topop.append("工业硅多晶硅")
        toadd.append(["工业硅", idea[key]])
    if key == "果蔬品":
        topop.append("果蔬品")
        toadd.append(["苹果", idea[key]])
        toadd.append(["红枣", idea[key]])
    if key == "锂期货":
        topop.append("锂期货")
        toadd.append(["碳酸锂", idea[key]])
    if key == "焦炭焦煤":
        topop.append("焦炭焦煤")
        toadd.append(["焦煤", idea[key]])
        toadd.append(["焦炭", idea[key]])
    if key == "铁矿石":
        topop.append("铁矿石")
        toadd.append(["铁矿", idea[key]])
    if key == "粕类":
        topop.append("粕类")
        toadd.append(["豆粕", idea[key]])
    if key == "大豆":
        topop.append("大豆")
        toadd.append(["豆一", idea[key]])
    if key == "玻璃纯碱":
        topop.append("玻璃纯碱")
        toadd.append(["玻璃", idea[key]])
        toadd.append(["纯碱", idea[key]])
    if key == "钢材":
        topop.append("钢材")
        toadd.append(["螺纹", idea[key]])
        toadd.append(["热卷", idea[key]])
    if key == "镍不锈钢":
        topop.append("镍不锈钢")
        toadd.append(["镍", idea[key]])
        toadd.append(["不锈钢", idea[key]])
    if key == "贵金属":
        topop.append("贵金属")
        toadd.append(["黄金", idea[key]])
        toadd.append(["白银", idea[key]])
    if key == "顺丁橡胶":
        topop.append("顺丁橡胶")
        toadd.append(["合成橡胶", idea[key]])
    if key == "天然橡胶":
        topop.append("天然橡胶")
        toadd.append(["橡胶", idea[key]])
    if key == "EG":
        topop.append("EG")
        toadd.append(["MEG", idea[key]])
    if key == "EB":
        topop.append("EB")
        toadd.append(["苯乙烯", idea[key]])
    if key == "聚烯烃":
        topop.append("聚烯烃")
        toadd.append(["PP", idea[key]])
        toadd.append(["塑料", idea[key]])
    if key == "航运":
        topop.append("航运")
        toadd.append(["集运", idea[key]])
    if key == "PX、PTA、PF、MEG":
        topop.append("PX、PTA、PF、MEG")
        toadd.append(["PX", idea[key]])
        toadd.append(["PTA", idea[key]])
        toadd.append(["短纤", idea[key]])
        toadd.append(["MEG", idea[key]])
    if key == "PX、PTA、PF、PR":
        topop.append("PX、PTA、PF、PR")
        toadd.append(["PX", idea[key]])
        toadd.append(["PTA", idea[key]])
        toadd.append(["短纤", idea[key]])
        toadd.append(["瓶片", idea[key]])
    if key == "PX、PTA、PF":
        topop.append("PX、PTA、PF")
        toadd.append(["PX", idea[key]])
        toadd.append(["PTA", idea[key]])
        toadd.append(["短纤", idea[key]])
    if key == "石油沥青":
        topop.append("石油沥青")
        toadd.append(["沥青", idea[key]])
    if key == "液化石油气":
        topop.append("液化石油气")
        toadd.append(["LPG", idea[key]])
    if key == "燃料油":
        topop.append("燃料油")
        toadd.append(["燃油", idea[key]])
    if key == "国债期货":
        topop.append("国债期货")
        toadd.append(["国债", idea[key]])
    if key == "股指期货":
        topop.append("股指期货")
        toadd.append(["股指", idea[key]])
    if key == "双焦":
        topop.append("双焦")
        toadd.append(["焦煤", idea[key]])
        toadd.append(["焦炭", idea[key]])
    if key == "双硅":
        topop.append("双硅")
        toadd.append(["硅铁", idea[key]])
        toadd.append(["锰硅", idea[key]])
    if key == "合金":
        topop.append("合金")
        toadd.append(["硅铁", idea[key]])
        toadd.append(["锰硅", idea[key]])
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

huatai_idea = idea

###############################################华安开始############

with open('华安.txt',encoding='utf-8') as f:
    lines = f.readlines()
idea = {}
items = ["股指","集运指数（欧线）","黄金","铜","铝","碳酸锂","双焦","纯碱","玻璃","不锈钢","沪镍","钢材","塑料","PVC","纸浆","沪铝",
         "油脂","豆粕","鸡蛋","生猪","塑料PP","棉花","PTA","尿素","多晶硅","碳酸锂","原木"]
next = False
prev_item = ""
for l in lines:
    stripped = l.strip().strip('\n')
    if stripped == "":
        continue
    if "编辑：刘德勇" in stripped and next:
        if prev_item.strip("：") in idea:
            idea[prev_item.strip()] += l.strip().strip('\n').split("编辑：刘德勇")[0]
        else:
            idea[prev_item.strip()] = l.strip().strip('\n').split("编辑：刘德勇")[0]
        next = False
        continue
    if stripped in items:
        next = True
        prev_item = stripped.split("：")[0]
        continue
    if next:
        if prev_item in idea:
            idea[prev_item] += l.strip().strip('\n')
        else:
            idea[prev_item] = l.strip().strip('\n')
huaan_old = {}
for i in idea:
    huaan_old[i] = idea[i][:]

topop = []
toadd = []
for key in idea:
    if key == "多晶硅":
        topop.append("多晶硅")
        toadd.append(["工业硅", idea[key]])
    if key == "塑料PP":
        topop.append("塑料PP")
        toadd.append(["塑料", idea[key]])
        toadd.append(["PP", idea[key]])
    if key == "集运指数（欧线）":
        topop.append("集运指数（欧线）")
        toadd.append(["集运", idea[key]])
    if key == "双焦":
        topop.append("双焦")
        toadd.append(["焦煤", idea[key]])
        toadd.append(["焦炭", idea[key]])
    if key == "沪铝":
        topop.append("沪铝")
        toadd.append(["铝", idea[key]])
        toadd.append(["氧化铝",idea[key]])
    if key == "沪镍":
        topop.append("沪镍")
        toadd.append(["镍", idea[key]])
    if key == "钢材":
        topop.append("钢材")
        toadd.append(["螺纹", idea[key]])
        toadd.append(["热卷", idea[key]])
    if key == "油脂":
        topop.append("油脂")
        toadd.append(["棕榈油", idea[key]])
        toadd.append(["豆油", idea[key]])
        toadd.append(["菜油", idea[key]])

for i in topop:
    idea.pop(i)
for i in toadd:
    idea[i[0]] = i[1]

huaan_old = {}
for i in idea:
    huaan_old[i] = idea[i][:]

for key in idea:
    if not idea[key].isdecimal():
        idea[key] = keywords.simplify_sent(idea[key])


for i in huaan_old:
    if i in idea:
        huaan_old[i] = idea[i] + " 华安 " + huaan_old[i]
    else:
        huaan_old[i] = ""

huaan_idea = idea


################################################海通开始##########

with open('海通.txt',encoding='utf-8') as f:
    lines = f.readlines()
idea = {}
items = ["股指","集运指数（欧线）","黄金","铜","铝","碳酸锂","双焦","纯碱","玻璃","不锈钢","白糖","沪镍","钢材","塑料","PVC","纸浆","油脂","豆粕","鸡蛋","生猪",
         "棉花","国债","焦炭","甲醇","不锈钢","油脂","集装箱运价","镍","焦煤","短纤","玉米","铁矿石","PTA","PX"]
next = False
prev_item = ""
for l in lines:
    stripped = l.strip().strip('\n')
    if stripped == "":
        continue
    if ("投资咨询业务资格" in stripped) and next:
        if prev_item.strip("：") in items:
            idea[prev_item.strip()] += l.strip().strip('\n').split("投资咨询业务资格")[0]
        else:
            idea[prev_item.strip()] = l.strip().strip('\n').split("投资咨询业务资格")[0]
        next = False
        continue
    if "：" in stripped and stripped.split("：")[0] in items:
        next = True
        prev_item = stripped.split("：")[0]
        idea[prev_item] = stripped.split("：")[1]
        continue
    if next:
        if prev_item in idea:
            idea[prev_item] += l.strip().strip('\n')
        else:
            idea[prev_item] = l.strip().strip('\n')
haitong_old = {}
for i in idea:
    haitong_old[i] = idea[i][:]

topop = []
toadd = []
for key in idea:
    if key == "集装箱运价":
        topop.append("集装箱运价")
        toadd.append(["集运", idea[key]])
    if key == "焦炭":
        toadd.append(["焦煤", idea[key]])
    if key == "油脂":
        topop.append("油脂")
        toadd.append(["棕榈油", idea[key]])
        toadd.append(["豆油", idea[key]])
        toadd.append(["菜油", idea[key]])
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

###########################################东海######

with open('东海.txt',encoding='utf-8') as f:
    lines = f.readlines()
idea = {}
items = ["股指","钢材","铁矿石","焦炭/焦煤","硅锰/硅铁","铜","锡","碳酸锂","铝","锌","金/银","原油","沥青","PTA","白糖","LLDPE","油脂",
         "乙二醇","甲醇","聚丙烯","塑料","美豆","蛋白粕","豆菜油","棕榈油","玉米","生猪","棉花","镍&不锈钢","工业硅","饲料"]
next = False
prev_item = ""
for l in lines:
    stripped = l.strip().strip('\n')
    if stripped == "":
        continue
    if "作者栏" in stripped and next:
        if prev_item.strip("：") in idea:
            idea[prev_item.strip()] += l.strip().strip('\n').split("作者栏")[0]
        else:
            idea[prev_item.strip()] = l.strip().strip('\n').split("作者栏")[0]
        next = False
        continue
    if "黑色板块" in stripped:
        next = False
        continue
    if "【" in stripped and "】" in stripped and stripped.split("】")[0].split("【")[1] in items:
        next = True
        prev_item = stripped.split("】")[0].split("【")[1]
        idea[prev_item] = stripped.split("】")[1]
        continue
    if next:
        if prev_item in idea:
            idea[prev_item] += l.strip().strip('\n')
        else:
            idea[prev_item] = l.strip().strip('\n')
donghai_old = {}
for i in idea:
    donghai_old[i] = idea[i][:]

topop = []
toadd = []

for key in idea:
    if key == "饲料":
        topop.append("饲料")
        toadd.append(["豆粕", idea[key]])
        toadd.append(["玉米", idea[key]])
    if key == "油脂":
        topop.append("油脂")
        toadd.append(["豆油", idea[key]])
        toadd.append(["菜油", idea[key]])
    if key == "LLDPE":
        topop.append("LLDPE")
        toadd.append(["塑料", idea[key]])
    if key == "镍&不锈钢":
        topop.append("镍&不锈钢")
        toadd.append(["镍", idea[key]])
        toadd.append(["不锈钢", idea[key]])
    if key == "乙二醇":
        topop.append("乙二醇")
        toadd.append(["MEG", idea[key]])
    if key == "豆菜油":
        topop.append("豆菜油")
        toadd.append(["豆油", idea[key]])
        toadd.append(["菜油", idea[key]])
    if key == "蛋白粕":
        topop.append("蛋白粕")
        toadd.append(["豆粕", idea[key]])
    if key == "美豆":
        topop.append("美豆")
        toadd.append(["豆一", idea[key]])
    if key == "聚丙烯":
        topop.append("聚丙烯")
        toadd.append(["PP", idea[key]])
    if key == "焦炭/焦煤":
        topop.append("焦炭/焦煤")
        toadd.append(["焦煤", idea[key]])
        toadd.append(["焦炭", idea[key]])
    if key == "硅锰/硅铁":
        topop.append("硅锰/硅铁")
        toadd.append(["硅铁", idea[key]])
        toadd.append(["锰硅", idea[key]])
    if key == "金/银":
        topop.append("金/银")
        toadd.append(["黄金", idea[key]])
        toadd.append(["白银", idea[key]])
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

donghai_old = {}
for i in idea:
    donghai_old[i] = idea[i][:]

for key in idea:
    if not idea[key].isdecimal():
        idea[key] = keywords.simplify_sent(idea[key])


for i in donghai_old:
    if i in idea:
        donghai_old[i] = idea[i] + " 东海 " + donghai_old[i]
    else:
        donghai_old[i] = ""

donghai_idea = idea

###########################################整合开始

idea_combined = {}
for i in [guangzhou_old, hualian_old, dongxing_old, guotai_old, yongan_old, zhongxin_old,
          wukuang_old, guangfa_old, guotou_old, guangda_old, yinhe_old, yinhenong_old,
          zhongqi_old,
          guoxin_old, dongwu_old, yide_old, beite_old, nanhua_old, zhongzhou_old, hongye_old,
          hundungong_old, hundunneng_old, hundunagri_old, guodu_old, zhongtai_old, huatai_old, huaan_old, haitong_old, donghai_old
          ]:
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

with open('其他.txt', encoding='utf-8') as f:
    lines = f.readlines()
company = ""
for l in lines:
    if is_number(l.strip('\n').split(" ")[-1]):
        if len(l.strip('\n').split(" ")) == 2:
            name = l.strip('\n').split(" ")[0]
            score = l.strip('\n').split(" ")[1]
            if not is_number(score):
                score = keywords.simplify_sent(score)
            found = False
            for i in idea_combined:
                if i == "MEG" and name == "乙二醇":
                    idea_combined[i].append(str(score) + " " + company)
                    found = True
                if i == name:
                    idea_combined[i].append(str(score) + " " + company)
                    found = True
            if not found:
                idea_combined[name] = [str(float(score)) + " " + company]
        elif len(l.strip('\n').split(" ")) > 2:
            name = l.strip('\n').split(" ")[:-1]
            score = l.strip('\n').split(" ")[-1]
            if not is_number(score):
                score = keywords.simplify_sent(score)
            for j in name:
                found = False
                for i in idea_combined:
                    if i == "MEG" and j == "乙二醇":
                        idea_combined[i].append(str(score) + " " + company)
                        found = True
                    if i == j:
                        idea_combined[i].append(str(score) + " " + company)
                        found = True
                if not found:
                    idea_combined[j] = [str(float(score)) + " " + company]
    elif "##" in l.strip('\n'):
        company = l.strip('\n').strip("#")
order = ["","小结：","金融","股指","股指期权","国债","黑色金属","螺纹钢","纯碱玻璃","铁矿","焦煤","焦炭","螺纹","热卷","硅铁","锰硅","工业硅","多晶硅","有色金属","碳酸锂","氧化铝","铝","铜","锌","锡","镍","不锈钢","铅","贵金属","黄金","白银","能源化工",
 "原油","燃油","低硫燃油","LPG","沥青","甲醇","乙二醇","MEG","PTA","PX","短纤","瓶片","苯乙烯","PVC","烧碱","PP","塑料","尿素","橡胶","合成橡胶","纯碱","玻璃","纸浆","农产品","棕榈油","豆油","菜油","豆粕","豆一","玉米","淀粉","鸡蛋","白糖",'糖',"棉花",
 "苹果","花生","红枣","生猪","集运","集运指数（欧线）","集运指数","工业硅多晶硅","PX&PTA","短纤&瓶片","天然橡胶与合成橡胶","氯碱"]

idea_combined_sorted = {}
total = 0
count = 0
prev_type = ""
total_all = 0.0
count_all = 0.0
for i in order:
    if i not in idea_combined and i in ["金融","黑色金属","有色金属","贵金属","能源化工","农产品"]:
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
for i in [guangzhou_idea, hualian_idea, dongxing_idea, guotai_idea, yongan_idea, citrix_idea,
          wukuang_idea, guangfa_idea, guotou_idea, guangda_idea, yinhe_idea, yinhenong_idea,
          zhongqi_idea,
          guoxin_idea, dongwu_idea, yide_idea, beite_idea, nanhua_idea, zhongzhou_idea, hongye_idea,
          hundungong_idea, hundunneng_idea, hundunagri_idea, guodu_idea, zhongtai_idea, huatai_idea, huaan_idea, haitong_idea, donghai_idea
          ]:
    for j in i:
        if j.strip() == "":
            abc = 1
        if j in combined:
            combined[j].append(float(i[j]))
        else:
            combined[j] = [float(i[j])]





############## 详细观点
with open('其他.txt', encoding='utf-8') as f:
    lines = f.readlines()
for l in lines:
    if is_number(l.strip('\n').split(" ")[-1]):
        if len(l.strip('\n').split(" ")) == 2:
            name = l.strip('\n').split(" ")[0]
            score = l.strip('\n').split(" ")[1]
            if not is_number(score):
                continue
            found = False
            for i in combined:
                if i == "MEG" and name == "乙二醇":
                    combined[i].append(float(score))
                    found = True
                if i == name:
                    combined[i].append(float(score))
                    found = True
            if not found:
                combined[name] = [float(score)]
        elif len(l.strip('\n').split(" ")) > 2:
            name = l.strip('\n').split(" ")[:-1]
            score = l.strip('\n').split(" ")[-1]
            if not is_number(score):
                continue
            for j in name:
                found = False
                for i in combined:
                    if i == "MEG" and j == "乙二醇":
                        combined[i].append(float(score))
                        found = True
                    if i == j:
                        combined[i].append(float(score))
                        found = True
                if not found:
                    combined[j] = [float(score)]



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
    for i in [guangzhou_old, hualian_old, dongxing_old, guotai_old, yongan_old, zhongxin_old,
          wukuang_old, guangfa_old, guotou_old, guangda_old, yinhe_old, yinhenong_old,
          zhongqi_old,
          guoxin_old, dongwu_old, yide_old, beite_old, nanhua_old, zhongzhou_old, hongye_old,
          hundungong_old, hundunneng_old, hundunagri_old, guodu_old, zhongtai_old, huatai_old, huaan_old, haitong_old, donghai_old
          ]:
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
    if row["Name"] not in ["能源：","金融:","宏观","金融","动力煤"]:
        print(row["Name"] + " " + str('{0:.6}'.format(round(row["Value"], 6))))