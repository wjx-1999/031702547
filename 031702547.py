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



def solve_7(str0: str):



str0 = input()
level = str0.split("!")[0]
level = int(level)
str0 = str0.split("!")[1]
if level == 1:
    solve_5(str0)
if level == 2:
    solve_7(str0)
if level == 3:
    solve_7(str0)
