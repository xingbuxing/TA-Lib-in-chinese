# CDLIDENTICAL3CROWS

中文名称： 三胞胎乌鸦

用法：三胞胎乌鸦信号比三只乌鸦信号表现出更多的惊慌卖出,预示着市场趋势有一个更大的反转。

调用方法：signal = talib.CDLIDENTICAL3CROWS(open, high, low, close)

输出：0代表不符合k线形态，-100表示符合形态。

## 指标介绍
1.这三个蜡烛都必须为长的黑色实体，且长度应该大致相等。

2.前一天的市场趋势应该为上涨。

3.这三天中每天的开盘价必须等于前一天的收盘价。

4.这三天中每一天的收盘价的位置必须接近当天的最低价。

## 图例
![](/assets/CDLIDENTICAL3CROWS.png)

## 使用案例


```python
展示数据
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
      <th>0</th>
      <td>2017-05-11</td>
      <td>13.30</td>
      <td>13.55</td>
      <td>12.78</td>
      <td>13.27</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2017-05-10</td>
      <td>13.84</td>
      <td>14.07</td>
      <td>13.50</td>
      <td>13.61</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2017-05-09</td>
      <td>13.49</td>
      <td>13.86</td>
      <td>13.40</td>
      <td>13.76</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2017-05-08</td>
      <td>13.69</td>
      <td>14.14</td>
      <td>13.46</td>
      <td>13.49</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2017-05-05</td>
      <td>14.16</td>
      <td>14.48</td>
      <td>13.88</td>
      <td>13.90</td>
    </tr>
    
    <tr>
    	 ·······	
      <th>5408</th>
      <td>1993-11-12</td>
      <td>11.50</td>
      <td>11.51</td>
      <td>11.40</td>
      <td>11.48</td>
    </tr>
    <tr>
      <th>5409</th>
      <td>1993-11-11</td>
      <td>11.30</td>
      <td>11.67</td>
      <td>11.30</td>
      <td>11.42</td>
    </tr>
    <tr>
      <th>5410</th>
      <td>1993-11-10</td>
      <td>11.70</td>
      <td>11.78</td>
      <td>10.80</td>
      <td>11.32</td>
    </tr>
    <tr>
      <th>5411</th>
      <td>1993-11-09</td>
      <td>12.08</td>
      <td>12.18</td>
      <td>11.50</td>
      <td>11.70</td>
    </tr>
    <tr>
      <th>5412</th>
      <td>1993-11-08</td>
      <td>10.90</td>
      <td>11.98</td>
      <td>10.89</td>
      <td>11.97</td>
    </tr>
  </tbody>
</table>
<p>5413 rows × 5 columns</p>
</div>




```python
#将开高低收价转换为array根式
open_p = df['open'].values
high_p = df['high'].values
low_p = df['low'].values
close_p = df['close'].values
#展示转换格式后的开盘价
open_p
```




    array([ 13.3 ,  13.84,  13.49, ...,  11.7 ,  12.08,  10.9 ])




```python
#调用函数并展示
signal = talib.CDLIDENTICAL3CROWS(open_p, high_p, low_p, close_p)
signal
[   0    0    0    0    0    0    0    0    0    0    0    0    0    0    0
    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0
    ```````
    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0
    0    0    0    0    0    0    0    0    0 -100    0    0]
```

```python
#找出符合的K线日期
df['signal'] = signal
df = df.loc[df['signal'] != 0]
df
"""
date          open  high  low  close  signal
1995-05-10    6.7   6.95  6.6  6.65    -100
"""
```
		
## A股中的效果


```python

```

                                 1_change     3_change     5_change    10_change
    CDLIDENTICAL3CROWS                                                          
    -100               count  1636.000000  1635.000000  1616.000000  1612.000000
                       mean     -0.018174    -0.014900    -0.012500    -0.012173
                       std       0.023991     0.045415     0.060910     0.097351
                       min      -0.100461    -0.270723    -0.303350    -0.456723
                       25%      -0.027332    -0.034895    -0.043235    -0.059052
                       50%      -0.010682    -0.009430    -0.009754    -0.011981
                       75%      -0.001608     0.010996     0.020966     0.035546
                       max       0.073600     0.193628     0.283660     0.942856
    


```python

```