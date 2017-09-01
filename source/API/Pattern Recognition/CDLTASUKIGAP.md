
# CDLTASUKIGAP
中文名称：跳空并列阴阳线；

用法：分向上跳空阴阳线和向下跳空阴阳线；在上升趋势中出现向上跳空并列阴阳线，则说明上涨还将持续；在下降趋势中出现向下跳空并列阴阳线，则说明下降还将持续；

调用方法：talib. CDLTASUKIGAP (open, high, low, close)；

输出：0表示不符合形态，100表示符合向上跳空阴阳线形态，-100表示符合向下跳空阴阳线形态。

## 指标介绍
三日K线模式；

向上跳空阴阳线：

第二根K线：阳线，向上跳空高开；

第三根K线：阴线，开盘价位于第二根阳线实体之中，收盘于缺口之中；

第二根K线实体和第三根K线实体长度接近。

向下跳空阴阳线：

第二根K线：阴线，向下跳空低开；

第三根K线：阳线，开盘价位于第二根阳线实体之中，收盘于缺口之中；

第二根K线实体和第三根K线实体长度接近。

## 图例

![](/assets/CDLTASUKIGAP_sh600063.png)

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
      <th>2016-03-18</th>
      <td>sh600063</td>
      <td>4.91</td>
      <td>5.10</td>
      <td>4.89</td>
      <td>5.09</td>
    </tr>
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
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>2016-04-07</th>
      <td>sh600063</td>
      <td>5.14</td>
      <td>5.30</td>
      <td>5.11</td>
      <td>5.11</td>
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




    array([ 4.91,  5.13,  5.13,  5.05,  5.05,  4.95,  5.  ,  4.95,  4.86,
            4.97,  5.02,  5.06,  5.16,  5.14,  5.06,  5.05,  5.08,  5.04])




```python
# 调用函数
talib.CDLTASUKIGAP(open_p, high_p, low_p, close_p)
```




    array([   0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
              0,    0,    0,    0, -100,    0,    0])



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
      <th>CDLTASUKIGAP</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="5" valign="top">-100.0</th>
      <th>count</th>
      <td>21804.000000</td>
      <td>2.180400e+04</td>
      <td>2.180400e+04</td>
      <td>21804.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>0.001456</td>
      <td>2.149689e-03</td>
      <td>6.224784e-03</td>
      <td>0.006802</td>
    </tr>
    <tr>
      <th>std</th>
      <td>0.030839</td>
      <td>5.784920e-02</td>
      <td>7.483012e-02</td>
      <td>0.112249</td>
    </tr>
    <tr>
      <th>min</th>
      <td>-0.140910</td>
      <td>-2.711417e-01</td>
      <td>-3.295570e-01</td>
      <td>-0.604055</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>-0.015246</td>
      <td>-2.702712e-02</td>
      <td>-3.360333e-02</td>
      <td>-0.051219</td>
    </tr>
    <tr>
      <th>...</th>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th rowspan="5" valign="top">100.0</th>
      <th>min</th>
      <td>-0.134126</td>
      <td>-2.710146e-01</td>
      <td>-4.013852e-01</td>
      <td>-0.566192</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>-0.016071</td>
      <td>-2.857166e-02</td>
      <td>-3.640411e-02</td>
      <td>-0.050395</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>0.000000</td>
      <td>-5.958206e-07</td>
      <td>6.707325e-08</td>
      <td>0.001674</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>0.014725</td>
      <td>2.878118e-02</td>
      <td>3.718330e-02</td>
      <td>0.058134</td>
    </tr>
    <tr>
      <th>max</th>
      <td>0.245263</td>
      <td>5.932210e-01</td>
      <td>7.215906e-01</td>
      <td>1.595832</td>
    </tr>
  </tbody>
</table>
<p>16 rows × 4 columns</p>
</div>




```python

```
