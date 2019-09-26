# !/usr/bin/env python
# -*- coding:utf-8 -*-

import re # 提供各种正则表达式的操作
import cpca #用于提取简体中文字符串中省，市和区
import json #将输出文件的格式转换为json

def split_name(s: str):  # 将名字从字符串中提取出来



def split_num(s: str):  # 将电话号码从字符串提取出来



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
