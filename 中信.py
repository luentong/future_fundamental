import keywords

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
for l in lines:
    print(l)
    if " "  in l:
        idea[l.split(" ")[0]] = l.split(" ")[1]


zhongxin_old = {}
for i in idea:
    zhongxin_old[i] = idea[i][:]




topop = []
toadd = []
for key in idea:
    if not idea[key].isdecimal():
        idea[key] = keywords.simplify_sent(idea[key])
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
print(idea)
citrix_idea = idea

for key in idea:
    print(key)
    print(idea[key])