# CDLEVENINGSTAR
## 概述
中文名称：暮星。

用法：暮星永远是看跌信号。虽然本指标不强调趋势，但若在上涨趋势中出现暮星，尤其需要注意。

调用方法：talib.CDLEVENINGSTAR(open, high, low, close)

可选参数：penetration=0.3，一根k线在另一根k线范围内的渗透百分比

输出：0代表不符合k线形态，-100代表符合。

## 指标介绍
第一根k线：有长实体的阳线。

第二根k线：星形态（实体短，且跳出第一根k线）。

第三根k线：阴线，实体部分在第一根k线实体范围以内。

## 图例

![](/assets/CDLEVENINGSTAR_sz300511.png)

上图中最后3根K线，即为CDLEVENINGSTAR


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
      <th>2017-01-13</th>
      <td>sz300511</td>
      <td>45.00</td>
      <td>45.25</td>
      <td>41.69</td>
      <td>42.03</td>
    </tr>
    <tr>
      <th>2017-01-16</th>
      <td>sz300511</td>
      <td>41.97</td>
      <td>41.97</td>
      <td>37.83</td>
      <td>38.69</td>
    </tr>
    <tr>
      <th>2017-01-17</th>
      <td>sz300511</td>
      <td>38.50</td>
      <td>40.24</td>
      <td>36.89</td>
      <td>39.86</td>
    </tr>
    <tr>
      <th>2017-01-18</th>
      <td>sz300511</td>
      <td>39.55</td>
      <td>39.55</td>
      <td>38.66</td>
      <td>38.70</td>
    </tr>
    <tr>
      <th>2017-01-19</th>
      <td>sz300511</td>
      <td>38.47</td>
      <td>39.43</td>
      <td>38.00</td>
      <td>38.53</td>
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
      <th>2017-02-08</th>
      <td>sz300511</td>
      <td>39.51</td>
      <td>40.60</td>
      <td>39.51</td>
      <td>40.48</td>
    </tr>
    <tr>
      <th>2017-02-09</th>
      <td>sz300511</td>
      <td>40.48</td>
      <td>41.38</td>
      <td>40.17</td>
      <td>41.04</td>
    </tr>
    <tr>
      <th>2017-02-10</th>
      <td>sz300511</td>
      <td>41.17</td>
      <td>41.17</td>
      <td>40.04</td>
      <td>40.11</td>
    </tr>
    <tr>
      <th>2017-02-13</th>
      <td>sz300511</td>
      <td>40.25</td>
      <td>40.91</td>
      <td>39.66</td>
      <td>40.88</td>
    </tr>
    <tr>
      <th>2017-02-14</th>
      <td>sz300511</td>
      <td>40.92</td>
      <td>40.95</td>
      <td>40.20</td>
      <td>40.69</td>
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




    array([ 45.  ,  41.97,  38.5 ,  39.55,  38.47,  38.42,  39.53,  39.96,
            39.31,  40.15,  39.44,  39.13,  39.99,  39.51,  40.48,  41.17,
            40.25,  40.92])




```python
# 调用函数
talib.CDLEVENINGSTAR(open_p, high_p, low_p, close_p)
```




    array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], dtype=int32)



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
      <th>CDLEVENINGSTAR</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="8" valign="top">-100</th>
      <th>count</th>
      <td>40535.000000</td>
      <td>40535.000000</td>
      <td>40535.000000</td>
      <td>40535.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>0.002405</td>
      <td>0.003778</td>
      <td>0.005507</td>
      <td>0.011481</td>
    </tr>
    <tr>
      <th>std</th>
      <td>0.034404</td>
      <td>0.060135</td>
      <td>0.079212</td>
      <td>0.118962</td>
    </tr>
    <tr>
      <th>min</th>
      <td>-0.206503</td>
      <td>-0.299218</td>
      <td>-0.409503</td>
      <td>-0.573858</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>-0.013476</td>
      <td>-0.028017</td>
      <td>-0.035655</td>
      <td>-0.050055</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>0.003101</td>
      <td>0.001067</td>
      <td>0.002571</td>
      <td>0.005063</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>0.018750</td>
      <td>0.033207</td>
      <td>0.044391</td>
      <td>0.064345</td>
    </tr>
    <tr>
      <th>max</th>
      <td>0.372881</td>
      <td>0.661695</td>
      <td>0.778182</td>
      <td>1.978183</td>
    </tr>
  </tbody>
</table>
</div>
