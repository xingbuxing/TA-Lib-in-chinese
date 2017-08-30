# -*- coding: utf-8 -*-
"""
@author: xingbuxing
"""
from program import Functions
import pandas as pd
import talib
pd.set_option('expand_frame_repr', False)  # 当列太多时不换行


# 通过pattern_name设定要跑的指标，在此处设定指标名称
pattern_name = 'CDL2CROWS'

# 导入一只股票的数据，在此处设定股票代码
code = 'sz000001'
df = Functions.import_stock_data(code)

# 计算后复权价，计算指标要用复权价
df[[i + '_后复权' for i in ['开盘价', '最高价', '最低价', '收盘价']]] = Functions.cal_fuquan_price(df)

# 计算N天后涨跌幅
for i in [1, 3, 5, 10]:
    df[str(i)+'天后涨跌幅'] = df['收盘价_后复权'].shift(-i) / df['收盘价_后复权'] - 1

# 计算技术指标。不同指标此处需要参数可能不同，需要修改。
df[pattern_name] = getattr(talib, pattern_name)(df['开盘价_后复权'].values, df['最高价_后复权'].values,
                                                df['最低价_后复权'].values, df['收盘价_后复权'].values)

# 找出符合pattern的日期
pattern_df = df[df[pattern_name] != 0]
print pattern_df

# 作图
index_num = pattern_df.index[-1]
candle_num = 10
df = df.iloc[index_num-candle_num+1:index_num+1]
# Functions.plot_candle_chart(df, pattern_name + ' ' + code)
# 根据相关指标需要框出的k线数量确定 rectangle_num 的值
Functions.plot_candle_chart(df, rectangle_num=1, pic_name=pattern_name + ' ' + code)
