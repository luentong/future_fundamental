import warnings
import keywords
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
print('您已删除所有公司的txt文件内容!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
for i in ["上海中期.txt","中信.txt","五矿.txt","倍特期货.txt","南华.txt","光大期货.txt","鲁证期货.txt","华泰期货.txt","国信期货.txt","国投安信.txt","国泰君安.txt","广发期货.txt","海通期货.txt","广州期货.txt","东证.txt","银河期货.txt","永安期货.txt","国都期货.txt"]:
    file = open(i,"w")
    file.close()

cached = []
with open('其他.txt', encoding='gbk') as f:
    lines = f.readlines()
for l in lines:
    if is_number(l.strip('\n').split(" ")[-1]):
        if len(l.strip('\n').split(" ")) == 2:
            name = l.strip('\n').split(" ")[0]
            score = l.strip('\n').split(" ")[1]
            if not is_number(score):
                cached.append(l.strip("\n"))
            else:
                cached.append(" ".join(l.split(" ")[:-1]))
        elif len(l.strip('\n').split(" ")) > 2:
            name = l.strip('\n').split(" ")[:-1]
            score = l.strip('\n').split(" ")[-1]
            if not is_number(score):
                cached.append(l.strip("\n"))
            else:
                cached.append(" ".join(l.split(" ")[:-1]))
    else:
        cached.append(l.strip("\n"))

for i in cached:
    print(i)

with open('其他.txt', 'w+', encoding="gbk") as f:
    for i in cached:
        f.write(i + '\n')