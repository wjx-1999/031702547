# !/usr/bin/env python
# -*- coding:utf-8 -*-

import json #将输出文件的格式转换为json
import cpca #用于提取简体中文字符串中省，市和区
import re # 提供各种正则表达式的操作


def match_name_tel(s: str):  # get name and phone number
    match = s.split(",")
    name = match[0] #get name
    tel = re.search('\d{11}', match[1]).group(0) #get phone number
    mat = re.split('\d{11}', match[1])
    rest_addr = mat[0] + mat[1]  # join two string
    return (name, tel, rest_addr)


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
