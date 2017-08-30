# CDLUNIQUE3RIVER

中文名称：奇特三河床。

用法：当股票处于下跌行情中，且出现奇特三河床形态时，表明下跌趋势减弱，多头的力量逐渐收复失地，控制住市场，表明后续上涨几率较大

调用方法：talib.CDLUNIQUE3RIVER(open, high, low, close)

输出：0代表不符合k线形态，100表示符合形态。

# 指标介绍

第一根K线：长阴线

第二根K线：阴线，且其下影线较长，其最低价低于第一根K线的最低价，但开盘价与收盘价略高于第一根K线的收盘价与开盘价

第三根K线：小阳线，其实体形态较短，整体位置在前一根K线实体部分里面

# 图例



## 使用案例


```python
# 展示DataFrame中的数据
df
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }
    
    .dataframe thead th {
        text-align: left;
    }
    
    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
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
      <th>2014-08-27</th>
      <td>sz000776</td>
      <td>10.19</td>
      <td>10.27</td>
      <td>10.18</td>
      <td>10.20</td>
    </tr>
    <tr>
      <th>2014-08-28</th>
      <td>sz000776</td>
      <td>10.20</td>
      <td>10.28</td>
      <td>10.09</td>
      <td>10.13</td>
    </tr>
    <tr>
      <th>2014-08-29</th>
      <td>sz000776</td>
      <td>10.16</td>
      <td>10.24</td>
      <td>10.09</td>
      <td>10.23</td>
    </tr>
    <tr>
      <th>2014-09-01</th>
      <td>sz000776</td>
      <td>10.22</td>
      <td>10.32</td>
      <td>10.20</td>
      <td>10.32</td>
    </tr>
    <tr>
      <th>2014-09-02</th>
      <td>sz000776</td>
      <td>10.32</td>
      <td>10.51</td>
      <td>10.27</td>
      <td>10.49</td>
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
      <th>2014-09-23</th>
      <td>sz000776</td>
      <td>10.36</td>
      <td>10.55</td>
      <td>10.36</td>
      <td>10.53</td>
    </tr>
    <tr>
      <th>2014-09-24</th>
      <td>sz000776</td>
      <td>10.48</td>
      <td>11.06</td>
      <td>10.48</td>
      <td>10.95</td>
    </tr>
    <tr>
      <th>2014-09-25</th>
      <td>sz000776</td>
      <td>11.01</td>
      <td>11.07</td>
      <td>10.77</td>
      <td>10.84</td>
    </tr>
    <tr>
      <th>2014-09-26</th>
      <td>sz000776</td>
      <td>10.81</td>
      <td>10.90</td>
      <td>10.75</td>
      <td>10.85</td>
    </tr>
    <tr>
      <th>2014-09-29</th>
      <td>sz000776</td>
      <td>10.95</td>
      <td>11.05</td>
      <td>10.90</td>
      <td>10.94</td>
    </tr>
  </tbody>
</table>
<p>23 rows × 5 columns</p>
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




    array([ 10.19,  10.2 ,  10.16,  10.22,  10.32,  10.5 ,  10.57,  10.76,
            10.84,  10.7 ,  10.61,  10.59,  10.65,  10.63,  10.42,  10.39,
            10.45,  10.5 ,  10.36,  10.48,  11.01,  10.81,  10.95])




```python
# 调用函数
talib.CDLUNIQUE3RIVER(open_p, high_p, low_p, close_p)
```




    array([  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
             0,   0, 100,   0,   0,   0,   0,   0,   0,   0], dtype=int32)



## 在A股市场效果
遍历A股所有股票（包含退市），考察从上市至2017年1季度，所有出现


```python
# 展现统计结果
df.groupby(pattern_name)[[str(i)+'天后涨跌幅' for i in 1, 3, 5, 10]].describe().stack()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }
    
    .dataframe thead th {
        text-align: left;
    }
    
    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
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
      <th>CDLUNIQUE3RIVER</th>
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
      <td>6441.000000</td>
      <td>6441.000000</td>
      <td>6441.000000</td>
      <td>6441.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>-0.000465</td>
      <td>0.000555</td>
      <td>-0.001681</td>
      <td>-0.000745</td>
    </tr>
    <tr>
      <th>std</th>
      <td>0.030802</td>
      <td>0.059109</td>
      <td>0.076148</td>
      <td>0.167065</td>
    </tr>
    <tr>
      <th>min</th>
      <td>-0.125000</td>
      <td>-0.271393</td>
      <td>-0.400977</td>
      <td>-0.574740</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>-0.015717</td>
      <td>-0.026415</td>
      <td>-0.039702</td>
      <td>-0.060080</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>0.000000</td>
      <td>0.002442</td>
      <td>-0.001320</td>
      <td>-0.007291</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>0.015274</td>
      <td>0.030937</td>
      <td>0.037831</td>
      <td>0.048589</td>
    </tr>
    <tr>
      <th>max</th>
      <td>0.271506</td>
      <td>0.342739</td>
      <td>0.563769</td>
      <td>10.150771</td>
    </tr>
  </tbody>
</table>
</div>




```python

```
