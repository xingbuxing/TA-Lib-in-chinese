# CDLGAPSIDESIDEWHITE
## 概述
中文名称：向上/下跳空并列阳线。

用法：向上/下跳空并列阳线本身不直接看涨或看跌。如果出现在趋势中，则是非常显著的看涨或看跌信号。但本函数并不包含趋势判断。

调用方法：talib.CDLGAPSIDESIDEWHITE(open, high, low, close)

输出：向上跳空输出100，向下跳空输出-100，不符合形态输出0.

## 指标介绍
首先要向上/下跳空，实体间有缺口。

跳空后第一根k线：阳线。

跳空后第二根k线：阳线，长度和开盘价均与第一根k线相仿。且其不能填充跳空的缺口。

## 图例

![](/assets/CDLGAPSIDESIDEWHITE_sz300511.png)

上图中最后2根K线，即为CDLGAPSIDESIDEWHITE


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
      <th>2016-07-18</th>
      <td>sz300511</td>
      <td>72.30</td>
      <td>72.30</td>
      <td>69.40</td>
      <td>69.92</td>
    </tr>
    <tr>
      <th>2016-07-19</th>
      <td>sz300511</td>
      <td>69.48</td>
      <td>70.29</td>
      <td>67.66</td>
      <td>69.85</td>
    </tr>
    <tr>
      <th>2016-07-20</th>
      <td>sz300511</td>
      <td>69.86</td>
      <td>70.55</td>
      <td>69.20</td>
      <td>69.29</td>
    </tr>
    <tr>
      <th>2016-07-21</th>
      <td>sz300511</td>
      <td>69.00</td>
      <td>69.80</td>
      <td>67.51</td>
      <td>67.54</td>
    </tr>
    <tr>
      <th>2016-07-22</th>
      <td>sz300511</td>
      <td>67.05</td>
      <td>67.99</td>
      <td>65.01</td>
      <td>65.24</td>
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
      <th>2016-08-04</th>
      <td>sz300511</td>
      <td>62.43</td>
      <td>62.69</td>
      <td>61.48</td>
      <td>62.29</td>
    </tr>
    <tr>
      <th>2016-08-05</th>
      <td>sz300511</td>
      <td>62.58</td>
      <td>65.87</td>
      <td>62.56</td>
      <td>63.38</td>
    </tr>
    <tr>
      <th>2016-08-08</th>
      <td>sz300511</td>
      <td>62.50</td>
      <td>63.00</td>
      <td>59.88</td>
      <td>62.98</td>
    </tr>
    <tr>
      <th>2016-08-09</th>
      <td>sz300511</td>
      <td>62.74</td>
      <td>64.49</td>
      <td>62.17</td>
      <td>63.97</td>
    </tr>
    <tr>
      <th>2016-08-10</th>
      <td>sz300511</td>
      <td>64.09</td>
      <td>64.97</td>
      <td>63.28</td>
      <td>64.11</td>
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




    array([ 72.3 ,  69.48,  69.86,  69.  ,  67.05,  65.24,  64.68,  66.34,
            62.53,  62.08,  61.49,  59.29,  61.03,  62.43,  62.58,  62.5 ,
            62.74,  64.09])




```python
# 调用函数
talib.CDLGAPSIDESIDEWHITE(open_p, high_p, low_p, close_p)
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
      <th>CDLGAPSIDESIDEWHITE</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="5" valign="top">-100</th>
      <th>count</th>
      <td>8645.000000</td>
      <td>8645.000000</td>
      <td>8645.000000</td>
      <td>8645.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>0.000309</td>
      <td>-0.001562</td>
      <td>-0.000821</td>
      <td>0.002093</td>
    </tr>
    <tr>
      <th>std</th>
      <td>0.029490</td>
      <td>0.055526</td>
      <td>0.069997</td>
      <td>0.104296</td>
    </tr>
    <tr>
      <th>min</th>
      <td>-0.181818</td>
      <td>-0.308585</td>
      <td>-0.407490</td>
      <td>-0.652454</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>-0.013850</td>
      <td>-0.027778</td>
      <td>-0.034934</td>
      <td>-0.049871</td>
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
      <th rowspan="5" valign="top">100</th>
      <th>min</th>
      <td>-0.346457</td>
      <td>-0.343832</td>
      <td>-0.347126</td>
      <td>-0.539434</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>-0.014056</td>
      <td>-0.024312</td>
      <td>-0.032000</td>
      <td>-0.041667</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>0.000000</td>
      <td>0.001245</td>
      <td>0.002038</td>
      <td>0.006614</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>0.015385</td>
      <td>0.027595</td>
      <td>0.036824</td>
      <td>0.058198</td>
    </tr>
    <tr>
      <th>max</th>
      <td>0.195402</td>
      <td>0.496815</td>
      <td>0.618243</td>
      <td>1.206059</td>
    </tr>
  </tbody>
</table>
<p>16 rows × 4 columns</p>
</div>