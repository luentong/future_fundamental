#!/usr/bin/env python
# -*- coding: utf-8 -*-
import openai

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def chatgpt(input):
    #print('input: ' + input)
    openai.api_key = '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'
    content = '请用-1到1的小数描述行情的预测方向和强度，1为快速上涨，0为震荡，-1为快速下跌。例子1：在矿价走颓前，以偏多思路看待。回答：0.5.例子2：可关注JM2309， J2309合约高位做空机会。回答：-0.8.例子3: 震荡找寻方向。回答：0.请回答下一个例子, 只返回一个-1到1的小数: ' + input
    try:
        response = openai.Completion.create(
          engine='text-davinci-003',  # Specify the ChatGPT model
          prompt= content,
          max_tokens=15  # Set the maximum number of tokens in the response
        )
    except:
        print("skipped")
        return ""

    model_response = response.choices[0].text.strip()
    #print("Model response:", model_response)
    if "：" in model_response:
        if is_number(model_response.split("：")[1]):
            return model_response.split("：")[1]
        elif is_number(model_response.split("：")[1].split('。')[0]):
            return model_response.split("：")[1].split('。')[0]
        elif model_response.split("：")[1] != "" and model_response.split("：")[1][-1] == '.' and is_number(model_response.split("：")[1][:-1]):
            return model_response.split("：")[1][:-1]
        elif "（" in model_response.split("：")[1]:
            if is_number(model_response.split("：")[1].split("（")[0]):
                return model_response.split("：")[1].split("（")[0]
        elif "，" in model_response.split("：")[1]:
            if is_number(model_response.split("：")[1].split("，")[0]):
                return model_response.split("：")[1].split("，")[0]
    if ":" in model_response:
        if is_number(model_response.split(":")[1]):
            return model_response.split(":")[1]
        elif is_number(model_response.split(":")[1].split('。')[0]):
            return model_response.split(":")[1].split('。')[0]
        elif model_response.split(":")[1] != "" and model_response.split(":")[1][-1] == '.' and is_number(model_response.split(":")[1][:-1]):
            return model_response.split(":")[1][:-1]
        elif "（" in model_response.split(":")[1]:
            if is_number(model_response.split(":")[1].split("（")[0]):
                return model_response.split(":")[1].split("（")[0]
        elif "，" in model_response.split(":")[1]:
            if is_number(model_response.split(":")[1].split("，")[0]):
                return model_response.split(":")[1].split("，")[0]
    elif model_response[-1] == '.' and is_number(model_response[:-1]):
        return model_response[:-1]
    elif is_number(model_response):
        return model_response
    else:
        return ""