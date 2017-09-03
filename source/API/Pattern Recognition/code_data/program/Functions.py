# -*- coding: utf-8 -*-
"""
@author: Xingbuxing
date: 2017年05月06日
汇总需要用到的一些常见函数
"""
import config  # 导入config
import pandas as pd  # 导入pandas，我们一般为pandas取一个别名叫做pd
import os
from matplotlib.finance import candlestick2_ohlc
import matplotlib.pyplot as plt
import numpy as np


# 导入数据
def import_stock_data(stock_code, other_columns=[]):
    """
    导入在data/input_data/stock_data下的股票数据。
    :param stock_code: 股票数据的代码，例如'sh600000'
    :param other_columns: 若为默认值，只导入以下基础字段：'交易日期', '股票代码', '开盘价', '最高价', '最低价', '收盘价', '涨跌幅', 
    '成交额'。
    若不为默认值，会导入除基础字段之外其他指定的字段
    :return:
    """
    df = pd.read_csv(config.input_data_path + '/stock_data/' + stock_code + '.csv', encoding='gbk')
    df.columns = [i.encode('utf8') for i in df.columns]
    df = df[['交易日期', '股票代码', '开盘价', '最高价', '最低价', '收盘价', '涨跌幅', '成交额'] + other_columns]
    df.sort_values(by=['交易日期'], inplace=True)
    df['交易日期'] = pd.to_datetime(df['交易日期'])
    df['股票代码'] = stock_code
    df.reset_index(inplace=True, drop=True)

    return df


# 计算复权价
def cal_fuquan_price(input_stock_data, fuquan_type='后复权'):
    """
    计算复权价
    :param input_stock_data:
    :param fuquan_type:复权类型，可以是'后复权'或者'前复权'
    :return:
    """
    # 创建空的df
    df = pd.DataFrame()

    # 计算复权收盘价
    num = {'后复权': 0, '前复权': -1}
    price1 = input_stock_data['收盘价'].iloc[num[fuquan_type]]
    df['复权因子'] = (1.0 + input_stock_data['涨跌幅']).cumprod()
    price2 = df['复权因子'].iloc[num[fuquan_type]]
    df['收盘价_' + fuquan_type] = df['复权因子'] * (price1 / price2)

    # 计算复权的开盘价、最高价、最低价
    df['开盘价_' + fuquan_type] = input_stock_data['开盘价'] / input_stock_data['收盘价'] * df['收盘价_' + fuquan_type]
    df['最高价_' + fuquan_type] = input_stock_data['最高价'] / input_stock_data['收盘价'] * df['收盘价_' + fuquan_type]
    df['最低价_' + fuquan_type] = input_stock_data['最低价'] / input_stock_data['收盘价'] * df['收盘价_' + fuquan_type]

    return df[[i + '_' + fuquan_type for i in '开盘价', '最高价', '最低价', '收盘价']]


# 导入某文件夹下所有股票的代码
def get_stock_code_list_in_one_dir(path):
    """
    从指定文件夹下，导入所有csv文件的文件名
    :param path:
    :return:
    """

    stock_list = []

    # 系统自带函数os.walk，用于遍历文件夹中的所有文件
    for root, dirs, files in os.walk(path):
        if files:  # 当files不为空的时候
            for f in files:
                if f.endswith('.csv'):
                    stock_list.append(f[:8])

    return stock_list


# 作图
def plot_candle_chart(df, pic_name='candle_chart'):

    # 对数据进行整理
    df.set_index(df['交易日期'], drop=True, inplace=True)
    df = df[['开盘价', '最高价', '最低价', '收盘价']]

    # 作图
    ll = np.arange(0, len(df), 1)
    my_xticks = df.index[ll].date

    fig, ax = plt.subplots()

    candlestick2_ohlc(ax, df['开盘价'].values, df['最高价'].values, df['最低价'].values, df['收盘价'].values,
                      width=0.6, colorup='r', colordown='g', alpha=1)

    plt.xticks(ll, my_xticks)
    plt.xticks(rotation=60)

    plt.title(pic_name)

    plt.subplots_adjust(left=0.09, bottom=0.20, right=0.94, top=0.90, wspace=0.2, hspace=0)

    # 保存数据
    plt.savefig(pic_name+'.png')
