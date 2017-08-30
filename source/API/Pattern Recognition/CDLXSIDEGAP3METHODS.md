
# CDLXSIDEGAP3METHODS

中文名称：上升／下降跳空三法。

用法：上升／下降跳空三法通常出现在震荡回档行情当中，上升三法为震荡上升信号，下降三法则反之。

调用方法：talib.CDLXSIDEGAP3METHODS(open, high, low, close)

输出：0代表不符合k线形态，-100表示符合形态下降三法形态，100符合上升三法形态。

# 指标介绍
## 上升三法
第一跟K线：阳线。

第二根K线：阳线，并且实体部分与第一根K线实体部分之间存在缺口。

第三根K线：阴线，价格回调，实体部分填补了第一根K线与第二根K线实体部分之间的空缺。

## 下降三法
第一跟K线：阴线。

第二根K线：阴线，并且实体部分与第一根K线实体部分之间存在缺口。

第三根K线：阳线，价格回升，实体部分填补了第一根K线与第二根K线实体部分之间的空缺。

## 图例

![CDLXSIDEGAP3METHODS图例](/assets/CDLXSIDEGAP3METHODS图例.png)

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
      <th>2008-01-25</th>
      <td>sh600057</td>
      <td>7.07</td>
      <td>7.07</td>
      <td>6.80</td>
      <td>6.85</td>
    </tr>
    <tr>
      <th>2008-01-28</th>
      <td>sh600057</td>
      <td>6.76</td>
      <td>6.76</td>
      <td>6.18</td>
      <td>6.48</td>
    </tr>
    <tr>
      <th>2008-01-29</th>
      <td>sh600057</td>
      <td>6.48</td>
      <td>6.68</td>
      <td>6.30</td>
      <td>6.59</td>
    </tr>
    <tr>
      <th>2008-01-30</th>
      <td>sh600057</td>
      <td>6.71</td>
      <td>6.72</td>
      <td>6.36</td>
      <td>6.51</td>
    </tr>
    <tr>
      <th>2008-01-31</th>
      <td>sh600057</td>
      <td>6.51</td>
      <td>6.55</td>
      <td>5.98</td>
      <td>6.00</td>
    </tr>
    <tr>
      <th>2008-02-01</th>
      <td>sh600057</td>
      <td>5.99</td>
      <td>6.10</td>
      <td>5.45</td>
      <td>5.60</td>
    </tr>
    <tr>
      <th>2008-02-04</th>
      <td>sh600057</td>
      <td>5.72</td>
      <td>6.10</td>
      <td>5.72</td>
      <td>6.08</td>
    </tr>
    <tr>
      <th>2008-02-05</th>
      <td>sh600057</td>
      <td>6.11</td>
      <td>6.11</td>
      <td>5.90</td>
      <td>6.00</td>
    </tr>
    <tr>
      <th>2008-02-13</th>
      <td>sh600057</td>
      <td>6.01</td>
      <td>6.09</td>
      <td>5.88</td>
      <td>6.04</td>
    </tr>
    <tr>
      <th>2008-02-14</th>
      <td>sh600057</td>
      <td>6.08</td>
      <td>6.15</td>
      <td>6.06</td>
      <td>6.14</td>
    </tr>
    <tr>
      <th>2008-02-15</th>
      <td>sh600057</td>
      <td>6.10</td>
      <td>6.10</td>
      <td>5.91</td>
      <td>6.04</td>
    </tr>
    <tr>
      <th>2008-02-18</th>
      <td>sh600057</td>
      <td>6.08</td>
      <td>6.19</td>
      <td>6.00</td>
      <td>6.17</td>
    </tr>
    <tr>
      <th>2008-02-19</th>
      <td>sh600057</td>
      <td>6.18</td>
      <td>6.26</td>
      <td>6.11</td>
      <td>6.26</td>
    </tr>
    <tr>
      <th>2008-02-20</th>
      <td>sh600057</td>
      <td>6.25</td>
      <td>6.34</td>
      <td>6.08</td>
      <td>6.09</td>
    </tr>
    <tr>
      <th>2008-02-21</th>
      <td>sh600057</td>
      <td>6.09</td>
      <td>6.27</td>
      <td>6.03</td>
      <td>6.18</td>
    </tr>
    <tr>
      <th>2008-02-22</th>
      <td>sh600057</td>
      <td>6.18</td>
      <td>6.25</td>
      <td>5.98</td>
      <td>6.00</td>
    </tr>
    <tr>
      <th>2008-02-25</th>
      <td>sh600057</td>
      <td>6.02</td>
      <td>6.10</td>
      <td>5.78</td>
      <td>5.81</td>
    </tr>
    <tr>
      <th>2008-02-26</th>
      <td>sh600057</td>
      <td>5.93</td>
      <td>6.05</td>
      <td>5.83</td>
      <td>6.03</td>
    </tr>
    <tr>
      <th>2008-02-27</th>
      <td>sh600057</td>
      <td>6.04</td>
      <td>6.14</td>
      <td>6.00</td>
      <td>6.12</td>
    </tr>
    <tr>
      <th>2008-02-28</th>
      <td>sh600057</td>
      <td>6.13</td>
      <td>6.13</td>
      <td>6.01</td>
      <td>6.07</td>
    </tr>
    <tr>
      <th>2008-02-29</th>
      <td>sh600057</td>
      <td>6.06</td>
      <td>6.14</td>
      <td>6.02</td>
      <td>6.13</td>
    </tr>
  </tbody>
</table>
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




    array([ 7.07,  6.76,  6.48,  6.71,  6.51,  5.99,  5.72,  6.11,  6.01,
            6.08,  6.1 ,  6.08,  6.18,  6.25,  6.09,  6.18,  6.02,  5.93,
            6.04,  6.13,  6.06])




```python
# 调用函数
talib.CDLXSIDEGAP3METHODS(open_p, high_p, low_p, close_p)
```




    array([   0,    0,    0,    0,    0,    0, -100,    0,    0,    0,    0,
              0,    0,  100,    0,    0,    0,    0,    0,    0,    0], dtype=int32)



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
      <th>CDLXSIDEGAP3METHODS</th>
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
      <td>37328.000000</td>
      <td>37328.000000</td>
      <td>37328.000000</td>
      <td>37328.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>0.002072</td>
      <td>0.005441</td>
      <td>0.008873</td>
      <td>0.010282</td>
    </tr>
    <tr>
      <th>std</th>
      <td>0.029573</td>
      <td>0.054545</td>
      <td>0.072655</td>
      <td>0.110503</td>
    </tr>
    <tr>
      <th>min</th>
      <td>-0.183516</td>
      <td>-0.271146</td>
      <td>-0.398398</td>
      <td>-0.585919</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>-0.014973</td>
      <td>-0.023974</td>
      <td>-0.030314</td>
      <td>-0.046427</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>0.000000</td>
      <td>0.003636</td>
      <td>0.004348</td>
      <td>0.003610</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>0.016923</td>
      <td>0.032258</td>
      <td>0.042432</td>
      <td>0.059179</td>
    </tr>
    <tr>
      <th>max</th>
      <td>0.419118</td>
      <td>0.837349</td>
      <td>1.066636</td>
      <td>2.931959</td>
    </tr>
    <tr>
      <th rowspan="8" valign="top">100</th>
      <th>count</th>
      <td>42820.000000</td>
      <td>42820.000000</td>
      <td>42820.000000</td>
      <td>42820.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>0.000986</td>
      <td>0.003464</td>
      <td>0.004888</td>
      <td>0.012073</td>
    </tr>
    <tr>
      <th>std</th>
      <td>0.033311</td>
      <td>0.064987</td>
      <td>0.081743</td>
      <td>0.119976</td>
    </tr>
    <tr>
      <th>min</th>
      <td>-0.153567</td>
      <td>-0.282297</td>
      <td>-0.409444</td>
      <td>-0.571172</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>-0.014579</td>
      <td>-0.027917</td>
      <td>-0.036634</td>
      <td>-0.048993</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>0.001973</td>
      <td>0.001436</td>
      <td>0.002220</td>
      <td>0.006442</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>0.017685</td>
      <td>0.032527</td>
      <td>0.042271</td>
      <td>0.064767</td>
    </tr>
    <tr>
      <th>max</th>
      <td>0.593985</td>
      <td>5.418122</td>
      <td>4.940770</td>
      <td>4.284848</td>
    </tr>
  </tbody>
</table>
</div>



