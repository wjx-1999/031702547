# !/usr/bin/env python
# -*- coding:utf-8 -*-

import json #将输出文件的格式转换为json
import cpca #用于提取简体中文字符串中省，市和区
import re #提供各种正则表达式的操作


def match_name_tel(s: str):  # get name and phone number
    s = s.rstrip(".")
    match = s.split(",")
    name = match[0] #get name
    tel = re.search('\d{11}', match[1]).group(0) #get phone number
    mat = re.split('\d{11}', match[1])
    rest_addr = mat[0] + mat[1]  # join two string
    #DataFrame = cpca.transform([rest_addr], cut=False, pos_sensitive=True)  # 必须使用列表才能映射
    DataFrame = cpca.transform([rest_addr])  # 必须使用列表才能映射
    return (name, tel, DataFrame)

def test(str0 : str):
    name, phone, tmp = match_name_tel(str0)
    newaddr = []
    secondcut_list = tmp.values[0]
    for addr in secondcut_list:
        newaddr.append(addr)
    # 切分街道、镇、乡
    lastaddr = newaddr.pop()

    if newaddr[0] == '北京市' or'天津市'or'上海市'or '重庆市' :
        str = newaddr[0].replace('市','')
        newaddr[0] = str
    address = newaddr
    thridcut_list = lastaddr.split('街道', 1)
    if len(thridcut_list) > 1:
        thridcut_list[0] += "街道"
    else:
        thridcut_list = lastaddr.split('镇', 1)
        if len(thridcut_list) > 1:
            thridcut_list[0] += "镇"
        else:
            thridcut_list = lastaddr.split('乡', 1)
            if len(thridcut_list) > 1:
                thridcut_list[0] += "乡"
            else:
                thridcut_list.insert(0, '')
    address = newaddr + thridcut_list
    info = {
        "姓名": name,
        "手机": phone,
        "地址": address
    }
    # 编码成json类型数据
    info_data = json.dumps(info, ensure_ascii=False)
    print(info_data)

str0 = input()
str0 = re.split("!",str0)
level = int(str0[0])
s = str0[1]
test(s)
