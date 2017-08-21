
# CDLKICKINGBYLENGTH

中文名称：  由较长缺影线决定的反冲形态

用法：二日 K 线模式，与反冲形态类似，较长缺影线决定价格的涨跌。

调用方法：signal = talib.CDLKICKINGBYLENGTH(open, high, low, close)

输出：0代表不符合k线形态，100表示符合形态。

## 指标介绍
与反冲形态类似,两日 K 线为秃线，颜色相反，存在跳空缺口,有较长缺影线

## 图例
![](/assets/CDLKICKINGBYLENGTH.png)

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
      <th>3841</th>
      <td>2017-03-24</td>
      <td>15.30</td>
      <td>15.32</td>
      <td>15.17</td>
      <td>15.27</td>
    </tr>
    <tr>
      <th>3842</th>
      <td>2017-03-27</td>
      <td>15.26</td>
      <td>15.47</td>
      <td>15.22</td>
      <td>15.46</td>
    </tr>
    <tr>
      <th>3843</th>
      <td>2017-03-28</td>
      <td>15.42</td>
      <td>15.55</td>
      <td>15.37</td>
      <td>15.51</td>
    </tr>
    <tr>
      <th>3844</th>
      <td>2017-03-29</td>
      <td>15.54</td>
      <td>15.55</td>
      <td>15.39</td>
      <td>15.42</td>
    </tr>
    <tr>
      <th>3845</th>
      <td>2017-03-30</td>
      <td>15.42</td>
      <td>15.44</td>
      <td>15.10</td>
      <td>15.20</td>
    </tr>
    <tr>
      <th>3846</th>
      <td>2017-03-31</td>
      <td>15.16</td>
      <td>15.25</td>
      <td>15.11</td>
      <td>15.14</td>
    </tr>
    <tr>
      <th>3847</th>
      <td>2017-04-05</td>
      <td>15.35</td>
      <td>15.61</td>
      <td>15.35</td>
      <td>15.52</td>
    </tr>
    <tr>
      <th>3848</th>
      <td>2017-04-06</td>
      <td>15.55</td>
      <td>15.66</td>
      <td>15.39</td>
      <td>15.54</td>
    </tr>
    <tr>
      <th>3849</th>
      <td>2017-04-07</td>
      <td>15.60</td>
      <td>16.24</td>
      <td>15.50</td>
      <td>16.02</td>
    </tr>
    <tr>
      <th>3850</th>
      <td>2017-04-10</td>
      <td>16.01</td>
      <td>16.49</td>
      <td>15.90</td>
      <td>16.10</td>
    </tr>
    <tr>
      <th>3851</th>
      <td>2017-04-11</td>
      <td>16.00</td>
      <td>16.35</td>
      <td>15.96</td>
      <td>16.21</td>
    </tr>
    <tr>
      <th>3852</th>
      <td>2017-04-12</td>
      <td>16.02</td>
      <td>16.16</td>
      <td>15.76</td>
      <td>15.87</td>
    </tr>
    <tr>
      <th>3853</th>
      <td>2017-04-13</td>
      <td>15.84</td>
      <td>16.02</td>
      <td>15.76</td>
      <td>15.92</td>
    </tr>
    <tr>
      <th>3854</th>
      <td>2017-04-14</td>
      <td>15.86</td>
      <td>16.33</td>
      <td>15.75</td>
      <td>16.13</td>
    </tr>
    <tr>
      <th>3855</th>
      <td>2017-04-17</td>
      <td>16.06</td>
      <td>16.15</td>
      <td>15.60</td>
      <td>16.01</td>
    </tr>
    <tr>
      <th>3856</th>
      <td>2017-04-18</td>
      <td>15.95</td>
      <td>16.00</td>
      <td>15.65</td>
      <td>15.67</td>
    </tr>
    <tr>
      <th>3857</th>
      <td>2017-04-19</td>
      <td>15.62</td>
      <td>15.75</td>
      <td>15.10</td>
      <td>15.49</td>
    </tr>
    <tr>
      <th>3858</th>
      <td>2017-04-20</td>
      <td>15.45</td>
      <td>15.46</td>
      <td>15.10</td>
      <td>15.35</td>
    </tr>
    <tr>
      <th>3859</th>
      <td>2017-04-21</td>
      <td>15.35</td>
      <td>15.51</td>
      <td>15.16</td>
      <td>15.48</td>
    </tr>
    <tr>
      <th>3860</th>
      <td>2017-04-24</td>
      <td>15.33</td>
      <td>15.41</td>
      <td>14.95</td>
      <td>15.35</td>
    </tr>
    <tr>
      <th>3861</th>
      <td>2017-04-25</td>
      <td>15.22</td>
      <td>15.39</td>
      <td>15.14</td>
      <td>15.15</td>
    </tr>
    <tr>
      <th>3862</th>
      <td>2017-04-26</td>
      <td>15.17</td>
      <td>15.38</td>
      <td>15.13</td>
      <td>15.32</td>
    </tr>
    <tr>
      <th>3863</th>
      <td>2017-04-27</td>
      <td>15.29</td>
      <td>15.49</td>
      <td>15.14</td>
      <td>15.48</td>
    </tr>
    <tr>
      <th>3864</th>
      <td>2017-04-28</td>
      <td>15.42</td>
      <td>15.48</td>
      <td>15.25</td>
      <td>15.37</td>
    </tr>
    <tr>
      <th>3865</th>
      <td>2017-05-02</td>
      <td>15.18</td>
      <td>15.29</td>
      <td>15.10</td>
      <td>15.13</td>
    </tr>
    <tr>
      <th>3866</th>
      <td>2017-05-03</td>
      <td>15.17</td>
      <td>15.22</td>
      <td>15.10</td>
      <td>15.18</td>
    </tr>
    <tr>
      <th>3867</th>
      <td>2017-05-04</td>
      <td>15.17</td>
      <td>15.25</td>
      <td>14.95</td>
      <td>15.04</td>
    </tr>
    <tr>
      <th>3868</th>
      <td>2017-05-05</td>
      <td>15.02</td>
      <td>15.09</td>
      <td>14.40</td>
      <td>14.71</td>
    </tr>
    <tr>
      <th>3869</th>
      <td>2017-05-08</td>
      <td>14.62</td>
      <td>14.82</td>
      <td>14.45</td>
      <td>14.81</td>
    </tr>
    <tr>
      <th>3870</th>
      <td>2017-05-09</td>
      <td>14.67</td>
      <td>14.85</td>
      <td>14.48</td>
      <td>14.58</td>
    </tr>
    <tr>
      <th>3871</th>
      <td>2017-05-10</td>
      <td>14.54</td>
      <td>14.63</td>
      <td>13.97</td>
      <td>14.03</td>
    </tr>
    <tr>
      <th>3872</th>
      <td>2017-05-11</td>
      <td>13.95</td>
      <td>14.19</td>
      <td>13.61</td>
      <td>14.11</td>
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




    array([ 15.3 ,  15.26,  15.42,  15.54,  15.42,  15.16,  15.35,  15.55,
            15.6 ,  16.01,  16.  ,  16.02,  15.84,  15.86,  16.06,  15.95,
            15.62,  15.45,  15.35,  15.33,  15.22,  15.17,  15.29,  15.42,
            15.18,  15.17,  15.17,  15.02,  14.62,  14.67,  14.54,  13.95])




```python
# 调用函数并展示结果
signal = talib.CDLINVERTEDHAMMER(open_p, high_p, low_p, close_p)
signal
```




    array([  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
             0,   0,   0,   0,   0,   0,   0, 100,   0,   0,   0, 100,   0,
             0,   0,   0,   0,   0,   0])




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
      <th>3861</th>
      <td>2017-04-25</td>
      <td>15.22</td>
      <td>15.39</td>
      <td>15.14</td>
      <td>15.15</td>
      <td>100</td>
    </tr>
    <tr>
      <th>3865</th>
      <td>2017-05-02</td>
      <td>15.18</td>
      <td>15.29</td>
      <td>15.10</td>
      <td>15.13</td>
      <td>100</td>
    </tr>
  </tbody>
</table>
</div>



