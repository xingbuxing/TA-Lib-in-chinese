# -*- coding: utf-8 -*-
"""
@author: xingbuxing
"""
from program import Functions
from program import config
import pandas as pd
import talib
pd.set_option('expand_frame_repr', False)  # 当列太多时不换行


# 通过pattern_name设定要跑的指标，在此处设定指标名称
pattern_name = 'CDL3OUTSIDE'

# 得到所有股票的列表
code_list = Functions.get_stock_code_list_in_one_dir(config.input_data_path + '/stock_data')

# 遍历所有股票
output = pd.DataFrame()
for code in code_list:
    print code

    # 导入数据
    df = Functions.import_stock_data(code)

    # 计算后复权价，计算指标要用复权价
    df[[i + '_后复权' for i in ['开盘价', '最高价', '最低价', '收盘价']]] = Functions.cal_fuquan_price(df)

    # 计算N天后涨跌幅
    for i in [1, 3, 5, 10]:
        df[str(i) + '天后涨跌幅'] = df['收盘价_后复权'].shift(-i) / df['收盘价_后复权'] - 1

    # 取2017年1季度之前的数据
    df = df[df['交易日期'] < pd.to_datetime('20170401')]
    if df.empty:
        continue

    # 计算技术指标。不同指标此处需要参数可能不同，需要修改。
    df[pattern_name] = getattr(talib, pattern_name)(df['开盘价_后复权'].values, df['最高价_后复权'].values,
                                                    df['最低价_后复权'].values, df['收盘价_后复权'].values)

    # 去除N天后涨跌幅为空的情况
    for i in [1, 3, 5, 10]:
        df = df[df[str(i)+'天后涨跌幅'].notnull()]

    # 合并数据
    output = output.append(df[df[pattern_name] != 0], ignore_index=True)


# 输出数据
output.to_csv(config.output_data_path + '/' + pattern_name + '.csv', index=False)

# 效果统计
print output.groupby(pattern_name)[[str(i)+'天后涨跌幅' for i in 1, 3, 5, 10]].describe()
