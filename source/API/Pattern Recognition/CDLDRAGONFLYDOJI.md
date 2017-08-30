# CDLDRAGONFLYDOJI
## 概述
中文名称：蜻蜓十字星。

用法：蜻蜓十字星必须结合趋势一起使用，虽然本指标不考虑趋势。

调用方法：talib.CDLDRAGONFLYDOJI(open, high, low, close)

输出：符合形态输出100， 不符合形态输出0。（注意，虽然输出是正的，但并不代表该信号看涨）

## 指标介绍
k线呈十字线形态。

开盘价和收盘价在k线高位，上影线极短，甚至没有上影线。

长下影。

## 图例

![](/assets/CDLDRAGONFLYDOJI_sz300431.png)

上图中最后1根K线，即为CDLDRAGONFLYDOJI

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
      <th>2015-04-20</th>
      <td>sz300431</td>
      <td>57.15</td>
      <td>57.15</td>
      <td>57.15</td>
      <td>57.15</td>
    </tr>
    <tr>
      <th>2015-04-21</th>
      <td>sz300431</td>
      <td>62.87</td>
      <td>62.87</td>
      <td>62.87</td>
      <td>62.87</td>
    </tr>
    <tr>
      <th>2015-04-22</th>
      <td>sz300431</td>
      <td>69.16</td>
      <td>69.16</td>
      <td>69.16</td>
      <td>69.16</td>
    </tr>
    <tr>
      <th>2015-04-23</th>
      <td>sz300431</td>
      <td>76.08</td>
      <td>76.08</td>
      <td>76.08</td>
      <td>76.08</td>
    </tr>
    <tr>
      <th>2015-04-24</th>
      <td>sz300431</td>
      <td>83.69</td>
      <td>83.69</td>
      <td>83.69</td>
      <td>83.69</td>
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
      <th>2015-05-08</th>
      <td>sz300431</td>
      <td>179.00</td>
      <td>189.97</td>
      <td>169.03</td>
      <td>189.97</td>
    </tr>
    <tr>
      <th>2015-05-11</th>
      <td>sz300431</td>
      <td>200.00</td>
      <td>208.97</td>
      <td>198.11</td>
      <td>208.97</td>
    </tr>
    <tr>
      <th>2015-05-12</th>
      <td>sz300431</td>
      <td>229.87</td>
      <td>229.87</td>
      <td>228.00</td>
      <td>229.87</td>
    </tr>
    <tr>
      <th>2015-05-13</th>
      <td>sz300431</td>
      <td>240.00</td>
      <td>252.86</td>
      <td>235.20</td>
      <td>252.86</td>
    </tr>
    <tr>
      <th>2015-05-14</th>
      <td>sz300431</td>
      <td>278.15</td>
      <td>278.15</td>
      <td>235.00</td>
      <td>241.70</td>
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




    array([  57.15,   62.87,   69.16,   76.08,   83.69,   92.06,  101.27,
            111.4 ,  122.54,  134.79,  148.27,  148.27,  160.  ,  179.  ,
            200.  ,  229.87,  240.  ,  278.15])




```python
# 调用函数
talib.CDLDRAGONFLYDOJI(open_p, high_p, low_p, close_p)
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
      <th>CDLDRAGONFLYDOJI</th>
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
      <td>135071.000000</td>
      <td>1.350710e+05</td>
      <td>135071.000000</td>
      <td>135071.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>0.003129</td>
      <td>2.756202e-03</td>
      <td>0.005460</td>
      <td>0.009029</td>
    </tr>
    <tr>
      <th>std</th>
      <td>0.048340</td>
      <td>7.475175e-02</td>
      <td>0.090706</td>
      <td>0.124741</td>
    </tr>
    <tr>
      <th>min</th>
      <td>-0.543566</td>
      <td>-6.304487e-01</td>
      <td>-0.666191</td>
      <td>-0.744156</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>-0.012708</td>
      <td>-2.520980e-02</td>
      <td>-0.032213</td>
      <td>-0.047676</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>0.000994</td>
      <td>-2.891841e-07</td>
      <td>0.000001</td>
      <td>0.000841</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>0.016373</td>
      <td>2.631565e-02</td>
      <td>0.036272</td>
      <td>0.053511</td>
    </tr>
    <tr>
      <th>max</th>
      <td>12.271869</td>
      <td>1.158803e+01</td>
      <td>10.965817</td>
      <td>11.146967</td>
    </tr>
  </tbody>
</table>
</div>