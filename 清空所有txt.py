import warnings
print('您已删除所有公司的txt文件内容!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
for i in ["上海中期.txt","中信.txt","五矿.txt","倍特期货.txt","南华.txt","光大期货.txt","鲁证期货.txt","兴业期货.txt","华泰期货.txt","国信期货.txt","国投安信.txt","国泰君安.txt","广发期货.txt","海通期货.txt","广州期货.txt","东证.txt","银河期货.txt","永安期货.txt","国都期货.txt"]:
    file = open(i,"w")
    file.close()