#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import json
import time


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
# Set up API parameters
count = 0
def chatgpt(input):
    print('input: ' + input)
    content = "请回答下一个例子：" + input
    api_key = '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'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}'
    }
    endpoint = 'https://api.openai.com/v1/chat/completions'

    # Define the message payload
    payload = {
        'messages': [
            {'role': 'system', 'content': '请用-1到1的小数描述行情的预测方向，1为快速上涨，0为震荡，-1为快速下跌。例子1：在矿价走颓前，以偏多思路看待。回答：0.5.例子2：可关注JM2309， J2309合约高位做空机会。回答：-0.8.例子3: 反弹后还是应该找机会空。回答：-0.4.'},
            {'role': 'user', 'content': content}
        ],
        #'model': 'gpt-3.5-turbo'  # Specify the model here
        'model': 'gpt-4.0'  # Specify the model here
    }

    # Make the API request
    global count
    if count % 5 == 0:
        response = requests.post(endpoint, headers=headers, json=payload)
        time.sleep(5)
        count += 1
    else:
        count += 1
        return ""


    # Process the response
    print(response.status_code, "status_code")
    if response.status_code == 200:
        data = response.json()
        model_response = data['choices'][0]['message']['content']
        print("Model response:", model_response)
        if "：" in model_response:
            if is_number(model_response.split("：")[1]):
                return model_response.split("：")[1]
            elif is_number(model_response.split("：")[1].split('。')[0]):
                return model_response.split("：")[1].split('。')[0]
            elif is_number(model_response.split("：")[1].split('.')[0]):
                return model_response.split("：")[1].split('.')[0]
            elif "（" in model_response.split("：")[1]:
                if is_number(model_response.split("：")[1].split("（")[0]):
                    return model_response.split("：")[1].split("（")[0]
            elif "，" in model_response.split("：")[1]:
                if is_number(model_response.split("：")[1].split("，")[0]):
                    return model_response.split("：")[1].split("，")[0]
        elif is_number(model_response):
            return model_response
        else:
            return ""

    else:
        # print("Request failed with status code:", response.status_code)
        # print(response.json())
        return ""

# print(chatgpt("现货走稳后轻仓低买思路"))