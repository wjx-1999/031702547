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
    DataFrame = cpca.transform([rest_addr])  # use the ilst
    return (name, tel, DataFrame)

def address_book(str0 : str):
    name, phone, tmp = match_name_tel(str0)
    newaddr = []
    str_rest = tmp.values[0]
    for addr in str_rest:
        newaddr.append(addr)
    # split the street\town\village
    lastaddr = newaddr.pop()

    if newaddr[0] == '北京市' or'天津市'or'上海市'or '重庆市' :
        str = newaddr[0].replace('市','')
        newaddr[0] = str
    address = newaddr
    addr_rest = lastaddr.split('街道', 1)
    if len(addr_rest) > 1:
        addr_rest[0] += "街道"
    else:
        addr_rest = lastaddr.split('镇', 1)
        if len(addr_rest) > 1:
            addr_rest[0] += "镇"
        else:
            addr_rest = lastaddr.split('乡', 1)
            if len(addr_rest) > 1:
                addr_rest[0] += "乡"
            else:
                addr_rest.insert(0, '')
    address = newaddr + addr_rest
    info = {
        "姓名": name,
        "手机": phone,
        "地址": address
    }
    # get the json type data
    info_data = json.dumps(info, ensure_ascii=False)
    print(info_data)

while 1:
    str0 = input()
    if str0 == "END":
        break
    str0 = re.split("!",str0)
    level = int(str0[0]) #get level
    s = str0[1]
    address_book(s)
