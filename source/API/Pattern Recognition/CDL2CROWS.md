# CDL2CROWS
-----------------
中文名称：两只乌鸦。
用法：出现两只乌鸦形态，是显著空头信号，特别是在上升趋势中。
调用方法：talib.CDL2CROWS(open, high, low, close)
输出：0代表不符合k线形态，-100表示符合形态。

## 指标介绍
第一跟K线：长阳线。
第二根K线：阴线，和第一根K线之间存在缺口。
第三根K线：阴线，开盘价位于第二根k线实体之间，收盘价位于第一根k线实体之间。

## 图例
![](/assets/Snip20170803_30.png)

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
      <th>交易日期</th>
      <th>股票代码</th>
      <th>开盘价</th>
      <th>最高价</th>
      <th>最低价</th>
      <th>收盘价</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2009-11-02</td>
      <td>sh600000</td>
      <td>21.20</td>
      <td>23.28</td>
      <td>21.08</td>
      <td>22.97</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2009-11-03</td>
      <td>sh600000</td>
      <td>23.00</td>
      <td>23.35</td>
      <td>22.90</td>
      <td>23.17</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2009-11-04</td>
      <td>sh600000</td>
      <td>23.11</td>
      <td>24.09</td>
      <td>23.01</td>
      <td>23.67</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2009-11-05</td>
      <td>sh600000</td>
      <td>23.58</td>
      <td>23.90</td>
      <td>23.37</td>
      <td>23.55</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2009-11-06</td>
      <td>sh600000</td>
      <td>23.80</td>
      <td>24.15</td>
      <td>23.50</td>
      <td>23.63</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2009-11-09</td>
      <td>sh600000</td>
      <td>23.60</td>
      <td>23.65</td>
      <td>22.95</td>
      <td>23.51</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2009-11-10</td>
      <td>sh600000</td>
      <td>23.57</td>
      <td>23.90</td>
      <td>23.40</td>
      <td>23.49</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2009-11-11</td>
      <td>sh600000</td>
      <td>23.39</td>
      <td>23.39</td>
      <td>23.08</td>
      <td>23.26</td>
    </tr>
    <tr>
      <th>8</th>
      <td>2009-11-12</td>
      <td>sh600000</td>
      <td>23.30</td>
      <td>23.58</td>
      <td>22.99</td>
      <td>23.11</td>
    </tr>
    <tr>
      <th>9</th>
      <td>2009-11-13</td>
      <td>sh600000</td>
      <td>23.00</td>
      <td>23.45</td>
      <td>22.88</td>
      <td>23.42</td>
    </tr>
    <tr>
      <th>10</th>
      <td>2009-11-16</td>
      <td>sh600000</td>
      <td>23.60</td>
      <td>24.12</td>
      <td>23.51</td>
      <td>24.01</td>
    </tr>
    <tr>
      <th>11</th>
      <td>2009-11-17</td>
      <td>sh600000</td>
      <td>24.19</td>
      <td>24.58</td>
      <td>24.00</td>
      <td>24.04</td>
    </tr>
    <tr>
      <th>12</th>
      <td>2009-11-18</td>
      <td>sh600000</td>
      <td>24.06</td>
      <td>24.23</td>
      <td>23.85</td>
      <td>23.98</td>
    </tr>
    <tr>
      <th>13</th>
      <td>2009-11-19</td>
      <td>sh600000</td>
      <td>24.01</td>
      <td>24.14</td>
      <td>23.55</td>
      <td>23.80</td>
    </tr>
    <tr>
      <th>14</th>
      <td>2009-11-20</td>
      <td>sh600000</td>
      <td>23.65</td>
      <td>23.79</td>
      <td>23.18</td>
      <td>23.62</td>
    </tr>
    <tr>
      <th>15</th>
      <td>2009-11-23</td>
      <td>sh600000</td>
      <td>23.61</td>
      <td>23.64</td>
      <td>23.25</td>
      <td>23.59</td>
    </tr>
    <tr>
      <th>16</th>
      <td>2009-11-24</td>
      <td>sh600000</td>
      <td>23.76</td>
      <td>23.83</td>
      <td>22.95</td>
      <td>23.01</td>
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

    array([ 21.2 ,  23.  ,  23.11,  23.58,  23.8 ,  23.6 ,  23.57,  23.39,
            23.3 ,  23.  ,  23.6 ,  24.19,  24.06,  24.01,  23.65,  23.61,
            23.76])

```python
# 调用函数
talib.CDL2CROWS(open_p, high_p, low_p, close_p)
```

    array([   0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
              0, -100,    0,    0,    0,    0], dtype=int32)
