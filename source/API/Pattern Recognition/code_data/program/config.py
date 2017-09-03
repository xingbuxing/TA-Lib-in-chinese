# coding=utf-8
"""
@author: Xingbuxing
date: 2017年05月06日
配置文件，配置文件路径
"""
import os

# 获取当前程序的地址
current_file = __file__

# 程序根目录地址
root_path = os.path.abspath(os.path.join(current_file, os.pardir, os.pardir))

# 输入数据根目录地址
input_data_path = os.path.abspath(os.path.join(root_path, 'data', 'input_data'))

# 输出数据根目录地址
output_data_path = os.path.abspath(os.path.join(root_path, 'data', 'output_data'))

# # 当前路径
# print os.path.abspath('.')
# # 父辈路径
# print os.path.abspath('..')
