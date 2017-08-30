# CDL3WHITESOLDIERS
中文名称：三个白兵。

用法：出现三个白兵形态，是显著多头信号，强烈预示着从熊市转向牛市

调用方法：talib.CDL3WHITESOLDIERS(open, high, low, close)

输出：0代表不符合k线形态，-100表示符合形态。

## 指标介绍
三根K线均为阳线，每天收盘价不断抬升，且每天开盘价均在前一天蜡烛实体上半部分

## 图例
![](https://github.com/zqc945/TA-Lib-in-chinese/raw/master/assets/CDL3WHITESOLDIERS.png)



## 使用案例


```python
# 展示DataFrame中的数据
df
```

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
      <th>2009-10-28</th>
      <td>sh600000</td>
      <td>21.88</td>
      <td>22.14</td>
      <td>21.30</td>
      <td>21.83</td>
    </tr>
    <tr>
      <th>2009-10-29</th>
      <td>sh600000</td>
      <td>21.40</td>
      <td>21.80</td>
      <td>21.25</td>
      <td>21.57</td>
    </tr>
    <tr>
      <th>2009-10-30</th>
      <td>sh600000</td>
      <td>21.99</td>
      <td>22.34</td>
      <td>21.69</td>
      <td>21.74</td>
    </tr>
    <tr>
      <th>2009-11-02</th>
      <td>sh600000</td>
      <td>21.20</td>
      <td>23.28</td>
      <td>21.08</td>
      <td>22.97</td>
    </tr>
    <tr>
      <th>2009-11-03</th>
      <td>sh600000</td>
      <td>23.00</td>
      <td>23.35</td>
      <td>22.90</td>
      <td>23.17</td>
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
      <th>2009-11-16</th>
      <td>sh600000</td>
      <td>23.60</td>
      <td>24.12</td>
      <td>23.51</td>
      <td>24.01</td>
    </tr>
    <tr>
      <th>2009-11-17</th>
      <td>sh600000</td>
      <td>24.19</td>
      <td>24.58</td>
      <td>24.00</td>
      <td>24.04</td>
    </tr>
    <tr>
      <th>2009-11-18</th>
      <td>sh600000</td>
      <td>24.06</td>
      <td>24.23</td>
      <td>23.85</td>
      <td>23.98</td>
    </tr>
    <tr>
      <th>2009-11-19</th>
      <td>sh600000</td>
      <td>24.01</td>
      <td>24.14</td>
      <td>23.55</td>
      <td>23.80</td>
    </tr>
    <tr>
      <th>2009-11-20</th>
      <td>sh600000</td>
      <td>23.65</td>
      <td>23.79</td>
      <td>23.18</td>
      <td>23.62</td>
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




    array([ 21.88,  21.4 ,  21.99,  21.2 ,  23.  ,  23.11,  23.58,  23.8 ,
            23.6 ,  23.57,  23.39,  23.3 ,  23.  ,  23.6 ,  24.19,  24.06,
            24.01,  23.65])




```python
# 调用函数
talib.CDL3WHITESOLDIERS(open_p, high_p, low_p, close_p)
```




    array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])



## 在A股市场效果
遍历A股所有股票（包含退市），考察从上市至2017年1季度，所有出现


```python
# 展现统计结果
df.groupby(pattern_name)[[str(i)+'天后涨跌幅' for i in 1, 3, 5, 10]].describe()
```


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
      <th>CDL3WHITESOLDIERS</th>
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
      <td>4004.000000</td>
      <td>4004.000000</td>
      <td>4004.000000</td>
      <td>4.004000e+03</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>0.001841</td>
      <td>0.001909</td>
      <td>0.002312</td>
      <td>9.200762e-03</td>
    </tr>
    <tr>
      <th>std</th>
      <td>0.034457</td>
      <td>0.066668</td>
      <td>0.083661</td>
      <td>1.637279e-01</td>
    </tr>
    <tr>
      <th>min</th>
      <td>-0.171609</td>
      <td>-0.320754</td>
      <td>-0.372335</td>
      <td>-5.409223e-01</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>-0.015456</td>
      <td>-0.030399</td>
      <td>-0.038737</td>
      <td>-5.395958e-02</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>-0.001030</td>
      <td>-0.002101</td>
      <td>-0.002545</td>
      <td>6.035883e-07</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>0.015738</td>
      <td>0.028687</td>
      <td>0.037003</td>
      <td>5.486650e-02</td>
    </tr>
    <tr>
      <th>max</th>
      <td>0.206215</td>
      <td>1.019230</td>
      <td>0.857076</td>
      <td>5.966531e+00</td>
    </tr>
  </tbody>
</table>
</div>
