# !/usr/bin/env python
# -*- coding:utf-8 -*-

import json #将输出文件的格式转换为json
import cpca #用于提取简体中文字符串中省，市和区
import re # 提供各种正则表达式的操作


def match_name_tel(s: str):  # get name and phone number
    s = s.rstrip(".")
    match = s.split(",")
    name = match[0] #get name
    tel = re.search('\d{11}', match[1]).group(0) #get phone number
    mat = re.split('\d{11}', match[1])
    rest_addr = mat[0] + mat[1]  # join two string
    DataFrame = cpca.transform([rest_addr], cut=False, pos_sensitive=True)  # 必须使用列表才能映射
    tmp = dict(DataFrame.iloc[0, 0:4])
    return (name, tel, tmp)

def detail_address(addr: str):
    town = village = street = road = alley = None  # init detail address
    if "镇" in addr:
        town = addr.split("镇")[0] + "镇"
        addr = addr.split("镇")[1]
    if "乡" in addr:
        village = addr.split("乡")[0] + "乡"
        addr = addr.split("乡")[1]
    if "街" in addr:
        if "街道" in addr:
            street = addr.split("街道")[0] + "街道"
            addr = addr.split("街道")[1]
        else:
            street = addr.split("街")[0] + "街"
            addr = addr.split("街")[1]
    if "路" in addr:
        road = addr.split("路")[0] + "路"
        addr = addr.split("路")[1]
    if "巷" in addr:
        alley = addr.split("巷")[0] + "巷"
        addr = addr.split("巷")[1]
    return (town, village, street, road, alley)

def solve_5(str0: str):
    name, phone, tmp = match_name_tel(str0)
    addr1 = tmp['地址']  # get detail address
    town, village, street, road, alley = detail_address(addr1)

    addr = [tmp['省'], tmp['市'], tmp['区'], "", "", ]
    if town != None:
        addr[3] += (town)
    if village != None:
        addr[3] += (village)

    if street != None:
        addr[3] += (street)
    if road != None:
        addr[4] += (road)
    if alley != None:
        addr[4] += (alley)
    if street == None:
        if road == None:
            if alley == None:
                if town == None:
                    if village == None:
                        addr[4] = ""

    addr[4] += addr1

    info = {
        "姓名": name,
        "手机": phone,
        "地址": addr
    }
    # 编码成json类型数据
    info_data = json.dumps(info, ensure_ascii=False)
    print(info_data)
    # print(json.loads(info_data))#打印结果


def solve_7(str0: str):
    name, phone, tmp = match_name_tel(str0)
    addr1 = tmp['地址']  # 提取出详细地址
    town, village, street, road, alley = detail_address(addr1)

    if re.search(r"\d*号", addr1) is None:
        hao = None
    else:
        hao = re.search(r"\d*号", addr1).group(0)
        addr1 = addr1.split("号")[1]

    addr = [tmp['省'], tmp['市'], tmp['区'], "", "", "", ]
    if town != None:
        addr[3] += town
    if village != None:
        addr[3] += village
    # print(addr)
    if street != None:
        if town is None and village is None:
            addr[3] += street
        else:
            addr[4] += street
    if road != None:
        addr[4] += road
    if alley != None:
        addr[4] += alley
    if hao != None:
        addr[5] += hao

    addr.append(addr1)

    info = {
        "姓名": name,
        "手机": phone,
        "地址": addr
    }
    # 编码成json类型数据
    info_data = json.dumps(info, ensure_ascii=False)
    print(info_data)
    # print(json.loads(info_data))#打印结果


str0 = input()
str0 = re.split("!",str0)
level = int(str0[0])
s = str0[1]
if level == 1:
    solve_5(s)
if level == 2:
    solve_7(s)
if level == 3:
    solve_7(s)
