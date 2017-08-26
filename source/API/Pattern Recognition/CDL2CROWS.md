
# CDL2CROWS
中文名称：两只乌鸦。

用法：出现两只乌鸦形态，是显著空头信号，特别是在上升趋势中。

调用方法：talib.CDL2CROWS(open, high, low, close)

输出：0代表不符合k线形态，-100表示符合形态。

## 指标介绍
第一跟K线：长阳线。

第二根K线：阴线，和第一根K线之间存在缺口。

第三根K线：阴线，开盘价位于第二根k线实体之间，收盘价位于第一根k线实体之间。

## 图例



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
talib.CDL2CROWS(open_p, high_p, low_p, close_p)
```




    array([   0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
              0,    0,    0,    0, -100,    0,    0], dtype=int32)



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
      <th>CDL2CROWS</th>
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
      <td>34.000000</td>
      <td>34.000000</td>
      <td>34.000000</td>
      <td>34.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>-0.002158</td>
      <td>0.001180</td>
      <td>-0.000287</td>
      <td>-0.009711</td>
    </tr>
    <tr>
      <th>std</th>
      <td>0.027048</td>
      <td>0.054963</td>
      <td>0.060065</td>
      <td>0.074107</td>
    </tr>
    <tr>
      <th>min</th>
      <td>-0.096723</td>
      <td>-0.128500</td>
      <td>-0.130147</td>
      <td>-0.171334</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>-0.016116</td>
      <td>-0.016516</td>
      <td>-0.033160</td>
      <td>-0.045401</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>-0.000563</td>
      <td>-0.004753</td>
      <td>-0.003107</td>
      <td>0.002785</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>0.013170</td>
      <td>0.019518</td>
      <td>0.027201</td>
      <td>0.029367</td>
    </tr>
    <tr>
      <th>max</th>
      <td>0.050000</td>
      <td>0.184547</td>
      <td>0.159533</td>
      <td>0.139522</td>
    </tr>
  </tbody>
</table>
</div>




```python

```
