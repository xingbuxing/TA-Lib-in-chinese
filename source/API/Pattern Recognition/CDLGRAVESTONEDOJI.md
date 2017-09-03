# CDLGRAVESTONEDOJI
## 概述
中文名称：墓碑十字线。

用法：墓碑十字线的效果需要结合趋势考虑，常被认为是趋势反转信号。

调用方法：talib.CDLGRAVESTONEDOJI(open, high, low, close)

输出：符合形态输出100，不符合输出0（注意，虽然输出是正的，但并不代表该信号看涨）。

# 指标介绍
k线呈十字线形态。

开盘价与收盘价均在该日k线靠下方位置，即下影线很短，甚至没有下影线。

上影线长。

## 图例

![](/assets/CDLGRAVESTONEDOJI_sz300431.png)

上图中最后1根K线，即为CDLGRAVESTONEDOJI


## 使用案例


```python
# 展示DataFrame中的数据
df
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>股票代码</th>
      <th>开盘价</th>
      <th>最高价</th>
      <th>最低价</th>
      <th>收盘价</th>
    </tr>
    <tr>
      <th>交易日期</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2015-06-05</th>
      <td>sz300431</td>
      <td>262.00</td>
      <td>274.47</td>
      <td>235.55</td>
      <td>241.98</td>
    </tr>
    <tr>
      <th>2015-06-08</th>
      <td>sz300431</td>
      <td>234.60</td>
      <td>266.18</td>
      <td>233.00</td>
      <td>266.18</td>
    </tr>
    <tr>
      <th>2015-06-09</th>
      <td>sz300431</td>
      <td>266.00</td>
      <td>290.00</td>
      <td>258.18</td>
      <td>279.60</td>
    </tr>
    <tr>
      <th>2015-06-10</th>
      <td>sz300431</td>
      <td>270.00</td>
      <td>307.56</td>
      <td>269.00</td>
      <td>307.56</td>
    </tr>
    <tr>
      <th>2015-07-13</th>
      <td>sz300431</td>
      <td>276.80</td>
      <td>276.80</td>
      <td>276.80</td>
      <td>276.80</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>2015-07-24</th>
      <td>sz300431</td>
      <td>187.10</td>
      <td>195.99</td>
      <td>178.20</td>
      <td>180.30</td>
    </tr>
    <tr>
      <th>2015-07-27</th>
      <td>sz300431</td>
      <td>169.00</td>
      <td>170.14</td>
      <td>162.27</td>
      <td>162.27</td>
    </tr>
    <tr>
      <th>2015-07-28</th>
      <td>sz300431</td>
      <td>146.04</td>
      <td>151.10</td>
      <td>146.04</td>
      <td>146.04</td>
    </tr>
    <tr>
      <th>2015-07-29</th>
      <td>sz300431</td>
      <td>141.11</td>
      <td>147.00</td>
      <td>131.44</td>
      <td>144.60</td>
    </tr>
    <tr>
      <th>2015-07-30</th>
      <td>sz300431</td>
      <td>137.97</td>
      <td>145.45</td>
      <td>130.14</td>
      <td>130.14</td>
    </tr>
  </tbody>
</table>
<p>18 rows × 5 columns</p>
</div>




```python
# 赋值开、高、收、低价格，np.array格式。
open_p = df['开盘价'].values
high_p = df['最高价'].values
low_p = df['最低价'].values
close_p = df['收盘价'].values
```


```python
# 展示open_p中的数据
open_p
```




    array([ 262.  ,  234.6 ,  266.  ,  270.  ,  276.8 ,  249.12,  224.21,
            201.79,  181.61,  172.2 ,  182.  ,  174.01,  182.  ,  187.1 ,
            169.  ,  146.04,  141.11,  137.97])




```python
# 调用函数
talib.CDLGRAVESTONEDOJI(open_p, high_p, low_p, close_p)
```




    array([  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
             0,   0, 100,   0,   0], dtype=int32)



## 在A股市场效果
遍历A股所有股票（包含退市），考察从上市至2017年1季度，所有出现


```python
# 展现统计结果
df.groupby(pattern_name)[[str(i)+'天后涨跌幅' for i in 1, 3, 5, 10]].describe()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>1天后涨跌幅</th>
      <th>3天后涨跌幅</th>
      <th>5天后涨跌幅</th>
      <th>10天后涨跌幅</th>
    </tr>
    <tr>
      <th>CDLGRAVESTONEDOJI</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="8" valign="top">100</th>
      <th>count</th>
      <td>129123.000000</td>
      <td>129123.000000</td>
      <td>129123.000000</td>
      <td>129123.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>-0.001600</td>
      <td>0.003523</td>
      <td>0.003819</td>
      <td>0.010679</td>
    </tr>
    <tr>
      <th>std</th>
      <td>0.037436</td>
      <td>0.074514</td>
      <td>0.112870</td>
      <td>0.142999</td>
    </tr>
    <tr>
      <th>min</th>
      <td>-0.330859</td>
      <td>-0.411573</td>
      <td>-0.894158</td>
      <td>-0.889004</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>-0.017897</td>
      <td>-0.026890</td>
      <td>-0.036951</td>
      <td>-0.048709</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>0.000000</td>
      <td>0.001894</td>
      <td>0.001240</td>
      <td>0.002085</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>0.015438</td>
      <td>0.031250</td>
      <td>0.039494</td>
      <td>0.058612</td>
    </tr>
    <tr>
      <th>max</th>
      <td>5.911000</td>
      <td>12.621615</td>
      <td>24.532402</td>
      <td>23.585921</td>
    </tr>
  </tbody>
</table>
</div>
