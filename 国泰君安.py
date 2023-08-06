import pdf
import keywords
idea = {}
path = './所长早读20230731.pdf'
res = pdf.pdf_to_string(path)
items = ["白银","铜","氧化铝","锌","铅","不锈钢","锡","工业硅","铁矿石","热轧卷板","锰硅","焦煤","动力煤","玻璃","MEG","橡胶","沥青","LLDPE","PP","纸浆","甲醇","尿素","苯乙烯","纯碱","LPG","短纤",
         "PVC","低硫燃料油","豆油","豆一","玉米","白糖","棉花","鸡蛋","生猪","花生"]

res_string = ""
for i in res:
    res_string += str(res[i])

print(len(res_string), "res_len")
print(res_string)
res_string = res_string.split(".................................................................................................................................")[-1]

for i in items:
    if i+"：" in res_string:
        sub = "".join(res_string.split(i+"：")[1:])
        if "观点及建议" in sub:
            idea[i] = sub.split("观点及建议")[1].split("请务必阅读")[0]

topop = []
toadd = []
for key in idea:
    if key == "不锈钢":
        toadd.append(["镍", idea[key]])
    if key == "热轧卷板":
        topop.append("热轧卷板")
        toadd.append(["螺纹", idea[key]])
        toadd.append(["热卷", idea[key]])
    if key == "锰硅":
        toadd.append(["硅铁", idea[key]])
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

for i in guotai_old:
    print(i)
    print(guotai_old[i])

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

print(guotai_idea)
for i in guotai_idea:
    print(i)
    print(guotai_idea[i])