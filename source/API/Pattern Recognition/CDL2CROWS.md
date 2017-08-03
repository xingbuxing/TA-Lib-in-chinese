# CDL2CROWS
-----------------
中文名称：两只乌鸦

talib.CDL2CROWS(open, high, low, close)


## 指标介绍

英文原文：

first candle: long white candle

second candle: black real body

gap between the first and the second candle's real bodies

third candle: black candle that opens within the second real body and closes within the first real body

The meaning of "long" is specified with TA\_SetCandleSettings  
outInteger is negative \(-1 to -100\): two crows is always bearish;

the user should consider that two crows is significant when it appears in an uptrend, while this function does not consider the trend

第一跟K线长阳，……

## 使用案例

```python
# -*- coding: utf-8 -*-
"""
@author: xingbuxing
"""
from program import Functions
import config
import pandas as pd
import numpy as np
import talib
pd.set_option('expand_frame_repr', False)  # 当列太多时不换行


output = pd.DataFrame()
for code in Functions.get_stock_code_list_in_one_dir(config.input_data_path + '/stock_data'):
    print code

    # 导入数据
    df = Functions.import_stock_data(code)

    # 计算后复权价
    df[['开盘价', '最高价', '最低价', '收盘价']] = Functions.cal_fuquan_price(df)

    # 计算N天后涨跌幅
    for i in [1, 3, 5, 10]:
        df[str(i)+'天后涨跌幅'] = df['收盘价'].shift(-i) / df['收盘价'] - 1

    # 计算技术指标
    df['CDL2CROWS'] = talib.CDL2CROWS(df['开盘价'].values, df['最高价'].values, df['最低价'].values, df['收盘价'].values)

    # 合并数据
    output = output.append(df[df['CDL2CROWS'] != 0], ignore_index=True)

output.to_csv(config.output_data_path + '/CDL2CROWS.csv', index=False)

print output[[str(i)+'天后涨跌幅' for i in 1, 3, 5, 10]].describe()
```