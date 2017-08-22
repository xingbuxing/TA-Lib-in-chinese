
# CDLINVERTEDHAMMER

中文名称：  倒锤头

用法：在下跌趋势底部，预示着趋势反转。

调用方法：signal = talib.CDLINVERTEDHAMMER(open, high, low, close)

输出：0代表不符合k线形态，100表示符合形态。

## 指标介绍
一日 K 线模式，上影线较长，长度为实体 2 倍以上，无下影线。

## 图例
![](/assets/CDLINVERTEDHAMMER.png)

## 使用案例


```python
# 展示数据

df
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>date</th>
      <th>open</th>
      <th>high</th>
      <th>low</th>
      <th>close</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>3503</th>
      <td>2016-12-14</td>
      <td>17.92</td>
      <td>18.58</td>
      <td>17.92</td>
      <td>17.99</td>
    </tr>
    <tr>
      <th>3504</th>
      <td>2016-12-15</td>
      <td>17.80</td>
      <td>18.39</td>
      <td>17.68</td>
      <td>17.93</td>
    </tr>
    <tr>
      <th>3505</th>
      <td>2016-12-16</td>
      <td>17.80</td>
      <td>18.17</td>
      <td>17.79</td>
      <td>18.08</td>
    </tr>
    <tr>
      <th>3506</th>
      <td>2016-12-19</td>
      <td>18.08</td>
      <td>18.15</td>
      <td>17.73</td>
      <td>17.75</td>
    </tr>
    <tr>
      <th>3507</th>
      <td>2016-12-20</td>
      <td>17.74</td>
      <td>17.85</td>
      <td>17.10</td>
      <td>17.20</td>
    </tr>
    <tr>
      <th>3508</th>
      <td>2016-12-21</td>
      <td>17.27</td>
      <td>17.43</td>
      <td>17.22</td>
      <td>17.28</td>
    </tr>
    <tr>
      <th>3509</th>
      <td>2016-12-22</td>
      <td>17.26</td>
      <td>17.36</td>
      <td>16.43</td>
      <td>16.59</td>
    </tr>
    <tr>
      <th>3510</th>
      <td>2016-12-23</td>
      <td>16.59</td>
      <td>16.60</td>
      <td>15.76</td>
      <td>15.99</td>
    </tr>
    <tr>
      <th>3511</th>
      <td>2016-12-26</td>
      <td>16.25</td>
      <td>16.79</td>
      <td>16.02</td>
      <td>16.79</td>
    </tr>
    <tr>
      <th>3512</th>
      <td>2016-12-27</td>
      <td>17.22</td>
      <td>17.63</td>
      <td>17.22</td>
      <td>17.63</td>
    </tr>
    <tr>
      <th>3513</th>
      <td>2016-12-28</td>
      <td>17.96</td>
      <td>18.49</td>
      <td>17.70</td>
      <td>18.48</td>
    </tr>
    <tr>
      <th>3514</th>
      <td>2016-12-29</td>
      <td>18.08</td>
      <td>19.28</td>
      <td>18.08</td>
      <td>18.65</td>
    </tr>
    <tr>
      <th>3515</th>
      <td>2016-12-30</td>
      <td>18.47</td>
      <td>18.76</td>
      <td>18.17</td>
      <td>18.31</td>
    </tr>
    <tr>
      <th>3516</th>
      <td>2017-01-03</td>
      <td>18.18</td>
      <td>18.70</td>
      <td>18.16</td>
      <td>18.45</td>
    </tr>
    <tr>
      <th>3517</th>
      <td>2017-01-04</td>
      <td>18.50</td>
      <td>18.55</td>
      <td>18.26</td>
      <td>18.32</td>
    </tr>
    <tr>
      <th>3518</th>
      <td>2017-01-05</td>
      <td>18.20</td>
      <td>18.60</td>
      <td>18.20</td>
      <td>18.35</td>
    </tr>
    <tr>
      <th>3519</th>
      <td>2017-01-06</td>
      <td>18.20</td>
      <td>18.42</td>
      <td>17.90</td>
      <td>18.39</td>
    </tr>
    <tr>
      <th>3520</th>
      <td>2017-01-09</td>
      <td>18.35</td>
      <td>18.55</td>
      <td>18.32</td>
      <td>18.46</td>
    </tr>
    <tr>
      <th>3521</th>
      <td>2017-01-10</td>
      <td>18.50</td>
      <td>19.17</td>
      <td>18.30</td>
      <td>18.98</td>
    </tr>
    <tr>
      <th>3522</th>
      <td>2017-01-11</td>
      <td>18.98</td>
      <td>19.83</td>
      <td>18.87</td>
      <td>19.67</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 将数据转为array格式
open_p = df['open'].values
high_p = df['high'].values
low_p = df['low'].values
close_p = df['close'].values

# 展示转换后数据
open_p      # 数据应具有一定长度以判断下跌趋势
```




    array([ 18.21,  18.03,  17.94,  18.03,  17.95,  18.  ,  18.15,  18.25,
            18.04,  18.05,  17.96,  17.95,  18.04,  18.32,  19.1 ,  19.04,
            19.19,  20.47,  18.98,  18.06,  17.92,  17.8 ,  17.8 ,  18.08,
            17.74,  17.27,  17.26,  16.59,  16.25,  17.22,  17.96,  18.08,
            18.47,  18.18,  18.5 ,  18.2 ,  18.2 ,  18.35,  18.5 ,  18.98])




```python
# 调用函数并展示结果
signal = talib.CDLINVERTEDHAMMER(open_p, high_p, low_p, close_p)
signal
```




    array([  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
             0,   0,   0,   0,   0,   0,   0, 100,   0,   0,   0,   0,   0,
             0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0])




```python
# 找出符合k线的交易日期
df['signal'] = signal
df = df.loc[df['signal'] != 0]
df
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>date</th>
      <th>open</th>
      <th>high</th>
      <th>low</th>
      <th>close</th>
      <th>signal</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>3503</th>
      <td>2016-12-14</td>
      <td>17.92</td>
      <td>18.58</td>
      <td>17.92</td>
      <td>17.99</td>
      <td>100</td>
    </tr>
  </tbody>
</table>
</div>
