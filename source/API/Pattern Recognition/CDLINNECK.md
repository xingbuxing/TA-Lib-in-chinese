
# CDLINNECK

中文名称： 颈内线

用法：二日 K 线模式，预示着下跌继续。

调用方法：signal = talib.CDLINNECK(open, high, low, close)

输出：0代表不符合k线形态，-100表示符合形态。

## 指标介绍
下跌趋势中，第一日长阴线，第二日开盘价较低，收盘价略高于第一日收盘价，阳线，实体较短

## 图例
![](/assets/CDLINNECK.png)

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
      <th>540</th>
      <td>2017-03-07</td>
      <td>14.70</td>
      <td>15.38</td>
      <td>14.69</td>
      <td>14.97</td>
    </tr>
    <tr>
      <th>541</th>
      <td>2017-03-08</td>
      <td>14.97</td>
      <td>15.35</td>
      <td>14.90</td>
      <td>15.05</td>
    </tr>
    <tr>
      <th>542</th>
      <td>2017-03-09</td>
      <td>15.05</td>
      <td>15.09</td>
      <td>14.55</td>
      <td>14.69</td>
    </tr>
    <tr>
      <th>543</th>
      <td>2017-03-10</td>
      <td>14.66</td>
      <td>14.66</td>
      <td>14.45</td>
      <td>14.64</td>
    </tr>
    <tr>
      <th>544</th>
      <td>2017-03-13</td>
      <td>14.60</td>
      <td>14.80</td>
      <td>14.35</td>
      <td>14.78</td>
    </tr>
    <tr>
      <th>545</th>
      <td>2017-03-14</td>
      <td>14.79</td>
      <td>14.81</td>
      <td>14.51</td>
      <td>14.54</td>
    </tr>
    <tr>
      <th>546</th>
      <td>2017-03-15</td>
      <td>14.48</td>
      <td>14.68</td>
      <td>14.40</td>
      <td>14.56</td>
    </tr>
    <tr>
      <th>547</th>
      <td>2017-03-16</td>
      <td>14.43</td>
      <td>14.88</td>
      <td>14.43</td>
      <td>14.81</td>
    </tr>
    <tr>
      <th>548</th>
      <td>2017-03-17</td>
      <td>14.75</td>
      <td>15.50</td>
      <td>14.68</td>
      <td>15.02</td>
    </tr>
    <tr>
      <th>549</th>
      <td>2017-03-20</td>
      <td>15.05</td>
      <td>15.43</td>
      <td>14.84</td>
      <td>15.13</td>
    </tr>
    <tr>
      <th>550</th>
      <td>2017-03-21</td>
      <td>15.13</td>
      <td>15.16</td>
      <td>14.95</td>
      <td>15.12</td>
    </tr>
    <tr>
      <th>551</th>
      <td>2017-03-22</td>
      <td>15.02</td>
      <td>16.05</td>
      <td>14.95</td>
      <td>15.88</td>
    </tr>
    <tr>
      <th>552</th>
      <td>2017-03-23</td>
      <td>15.75</td>
      <td>16.20</td>
      <td>15.51</td>
      <td>16.13</td>
    </tr>
    <tr>
      <th>553</th>
      <td>2017-03-24</td>
      <td>16.01</td>
      <td>16.11</td>
      <td>15.80</td>
      <td>15.83</td>
    </tr>
    <tr>
      <th>554</th>
      <td>2017-03-27</td>
      <td>15.92</td>
      <td>15.92</td>
      <td>15.51</td>
      <td>15.53</td>
    </tr>
    <tr>
      <th>555</th>
      <td>2017-03-28</td>
      <td>15.50</td>
      <td>15.68</td>
      <td>15.50</td>
      <td>15.52</td>
    </tr>
    <tr>
      <th>556</th>
      <td>2017-03-29</td>
      <td>15.60</td>
      <td>15.60</td>
      <td>15.08</td>
      <td>15.43</td>
    </tr>
    <tr>
      <th>557</th>
      <td>2017-03-30</td>
      <td>15.29</td>
      <td>15.87</td>
      <td>15.11</td>
      <td>15.70</td>
    </tr>
    <tr>
      <th>558</th>
      <td>2017-03-31</td>
      <td>15.67</td>
      <td>15.83</td>
      <td>15.30</td>
      <td>15.33</td>
    </tr>
    <tr>
      <th>559</th>
      <td>2017-04-05</td>
      <td>15.35</td>
      <td>15.90</td>
      <td>15.18</td>
      <td>15.77</td>
    </tr>
    <tr>
      <th>560</th>
      <td>2017-04-06</td>
      <td>15.70</td>
      <td>15.80</td>
      <td>15.49</td>
      <td>15.69</td>
    </tr>
    <tr>
      <th>561</th>
      <td>2017-04-07</td>
      <td>15.67</td>
      <td>15.68</td>
      <td>15.34</td>
      <td>15.44</td>
    </tr>
    <tr>
      <th>562</th>
      <td>2017-04-10</td>
      <td>15.40</td>
      <td>15.45</td>
      <td>14.80</td>
      <td>14.80</td>
    </tr>
    <tr>
      <th>563</th>
      <td>2017-04-11</td>
      <td>14.79</td>
      <td>14.93</td>
      <td>14.43</td>
      <td>14.80</td>
    </tr>
    <tr>
      <th>564</th>
      <td>2017-04-12</td>
      <td>14.70</td>
      <td>14.70</td>
      <td>14.30</td>
      <td>14.45</td>
    </tr>
    <tr>
      <th>565</th>
      <td>2017-04-13</td>
      <td>14.39</td>
      <td>14.59</td>
      <td>14.34</td>
      <td>14.58</td>
    </tr>
    <tr>
      <th>566</th>
      <td>2017-04-14</td>
      <td>14.58</td>
      <td>14.60</td>
      <td>14.17</td>
      <td>14.23</td>
    </tr>
    <tr>
      <th>567</th>
      <td>2017-04-17</td>
      <td>14.23</td>
      <td>14.26</td>
      <td>13.99</td>
      <td>14.24</td>
    </tr>
    <tr>
      <th>568</th>
      <td>2017-04-18</td>
      <td>14.23</td>
      <td>14.32</td>
      <td>14.13</td>
      <td>14.26</td>
    </tr>
    <tr>
      <th>569</th>
      <td>2017-04-19</td>
      <td>14.20</td>
      <td>14.44</td>
      <td>13.85</td>
      <td>14.40</td>
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
open_p
```




    array([ 14.62,  14.58,  14.42,  14.16,  14.25,  14.7 ,  14.97,  15.05,
            14.66,  14.6 ,  14.79,  14.48,  14.43,  14.75,  15.05,  15.13,
            15.02,  15.75,  16.01,  15.92,  15.5 ,  15.6 ,  15.29,  15.67,
            15.35,  15.7 ,  15.67,  15.4 ,  14.79,  14.7 ,  14.39,  14.58,
            14.23,  14.23,  14.2 ,  14.37,  14.61,  14.26,  13.98,  14.  ,
            13.95,  13.9 ,  14.09,  13.92,  13.83,  13.79,  13.98,  14.08,
            13.98,  13.8 ])




```python
# 调用函数并展示结果
signal = talib.CDLINNECK(open_p, high_p, low_p, close_p)
signal
```




    array([   0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
           -100,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
              0,    0,    0,    0,    0,    0, -100,    0,    0,    0,    0,
              0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
              0,    0,    0,    0,    0,    0])




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
      <th>546</th>
      <td>2017-03-15</td>
      <td>14.48</td>
      <td>14.68</td>
      <td>14.40</td>
      <td>14.56</td>
      <td>-100</td>
    </tr>
    <tr>
      <th>563</th>
      <td>2017-04-11</td>
      <td>14.79</td>
      <td>14.93</td>
      <td>14.43</td>
      <td>14.80</td>
      <td>-100</td>
    </tr>
  </tbody>
</table>
</div>


