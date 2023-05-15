# -*- coding: utf-8 -*-
import chardet
import requests
from datetime import date
import re

def huaan_idea():
    date_today = date.today()
    result = {}
    for category in [1,2,3,4,5]:
        url = "http://www.haqh.com/index.php?m=content&c=index&a=lists&catid=129&fenlei=" + str(category) + "&date=" + str(date_today)
        myParams = {"key":"", "username":""}
        response = requests.get(url=url, params=myParams).content.decode("utf-8")
        response = re.sub('\xa0;\xa9\ufe0f', '',response)
        response = re.sub('\xa0', '',response)
        response = re.sub('\ufeff', '',response)
        response = re.sub('\xa9', '',response)
        response = re.sub('\ufeff', '',response)
        response = re.sub('\ufeff', '',response)
        response = re.sub('\n', '', response)
        # response = re.sub(' 】  ：', '', response)
        # response = re.sub('】', '', response)

        # print(response)
        if category == 1:
            items = ["股指","国债"]
        elif category == 2:
            items = ["工业硅","铜","铝"]
        elif category == 3:
            items = ["黑色金属","不锈钢镍"]
        elif category == 4:
            items = ["PP","塑料","PVC","PTA乙二醇"]
        elif category == 5:
            items = ["豆粕菜粕","油脂","淀粉玉米","棉花棉纱","生猪"]

        for i in items:
            if i in response:
                res = "".join(response.split(i)[1:])
                # print("temp",res)
                res1 = ""
                if "市场分析】：" in res:
                    res1 = res.split("市场分析】：")[1].split('<a')[0]
                res2 = ""
                if "投资策略】：" in res:
                    res2 = res.split("投资策略】：")[1].split('<a')[0]
                # print(res1)
                # print(res2)
                result[i] = res1+res2

    print(result)
    return result
