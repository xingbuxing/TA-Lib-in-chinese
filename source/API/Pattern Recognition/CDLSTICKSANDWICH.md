
# CDLSTICKSANDWICH
中文名称：条形三明治；

用法：在下跌趋势中，出现该形态，是显著的多头信号；

调用方法：talib. CDLSTICKSANDWICH (open, high, low, close)；

输出：0表示不符合形态，100表示符合形态。

## 指标介绍
三根K线模式；

第一跟K线：阴线；

第二根K线：阳线，成交最低价高于前一日收盘价；

第三根K线：阴线，收盘价等于第一根K线收盘价。

## 图例

![](/assets/CDLSTICKSANDWICH_sh600063.png)

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
      <th>2016-03-21</th>
      <td>sh600063</td>
      <td>5.13</td>
      <td>5.26</td>
      <td>5.05</td>
      <td>5.21</td>
    </tr>
    <tr>
      <th>2016-03-22</th>
      <td>sh600063</td>
      <td>5.13</td>
      <td>5.15</td>
      <td>5.05</td>
      <td>5.08</td>
    </tr>
    <tr>
      <th>2016-03-23</th>
      <td>sh600063</td>
      <td>5.05</td>
      <td>5.12</td>
      <td>5.01</td>
      <td>5.09</td>
    </tr>
    <tr>
      <th>2016-03-24</th>
      <td>sh600063</td>
      <td>5.05</td>
      <td>5.05</td>
      <td>4.95</td>
      <td>4.96</td>
    </tr>
    <tr>
      <th>2016-03-25</th>
      <td>sh600063</td>
      <td>4.95</td>
      <td>5.00</td>
      <td>4.92</td>
      <td>5.00</td>
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
      <th>2016-04-08</th>
      <td>sh600063</td>
      <td>5.06</td>
      <td>5.08</td>
      <td>4.95</td>
      <td>5.01</td>
    </tr>
    <tr>
      <th>2016-04-11</th>
      <td>sh600063</td>
      <td>5.05</td>
      <td>5.10</td>
      <td>5.02</td>
      <td>5.08</td>
    </tr>
    <tr>
      <th>2016-04-12</th>
      <td>sh600063</td>
      <td>5.08</td>
      <td>5.08</td>
      <td>4.97</td>
      <td>5.01</td>
    </tr>
    <tr>
      <th>2016-04-13</th>
      <td>sh600063</td>
      <td>5.04</td>
      <td>5.15</td>
      <td>5.04</td>
      <td>5.08</td>
    </tr>
    <tr>
      <th>2016-04-14</th>
      <td>sh600063</td>
      <td>5.13</td>
      <td>5.21</td>
      <td>5.05</td>
      <td>5.16</td>
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




    array([ 5.13,  5.13,  5.05,  5.05,  4.95,  5.  ,  4.95,  4.86,  4.97,
            5.02,  5.06,  5.16,  5.14,  5.06,  5.05,  5.08,  5.04,  5.13])




```python
# 调用函数
talib.CDLSTICKSANDWICH(open_p, high_p, low_p, close_p)
```




    array([  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
             0,   0, 100,   0,   0])



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
      <th>CDLSTICKSANDWICH</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="8" valign="top">100.0</th>
      <th>count</th>
      <td>6590.000000</td>
      <td>6590.000000</td>
      <td>6590.000000</td>
      <td>6590.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>-0.001592</td>
      <td>0.002853</td>
      <td>0.002602</td>
      <td>0.005345</td>
    </tr>
    <tr>
      <th>std</th>
      <td>0.028703</td>
      <td>0.052339</td>
      <td>0.071552</td>
      <td>0.234078</td>
    </tr>
    <tr>
      <th>min</th>
      <td>-0.129964</td>
      <td>-0.270972</td>
      <td>-0.652632</td>
      <td>-0.723809</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>-0.015927</td>
      <td>-0.025641</td>
      <td>-0.034604</td>
      <td>-0.051892</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>0.000000</td>
      <td>0.001830</td>
      <td>0.001378</td>
      <td>-0.003857</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>0.013559</td>
      <td>0.029533</td>
      <td>0.038663</td>
      <td>0.051437</td>
    </tr>
    <tr>
      <th>max</th>
      <td>0.125991</td>
      <td>0.643990</td>
      <td>0.553333</td>
      <td>16.913058</td>
    </tr>
  </tbody>
</table>
</div>




```python

```
