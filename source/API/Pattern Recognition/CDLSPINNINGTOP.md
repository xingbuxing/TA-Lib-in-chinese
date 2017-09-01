
# CDLSPINNINGTOP
中文名称：纺锤；

用法：反应买卖力量的强弱，并不意味着看涨或看跌；

调用方法：talib. CDLSPINNINGTOP (open, high, low, close)；

输出：0表示不符合形态，100表示符合形态（阳线），-100表示符合形态（阴线）。


## 指标介绍
单日K线；

小的实体；

影线长于实体。

## 图例

![](/assets/CDLSPINNINGTOP_sh600063.png)

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
      <th>2017-03-28</th>
      <td>sh600063</td>
      <td>4.99</td>
      <td>5.00</td>
      <td>4.92</td>
      <td>4.94</td>
    </tr>
    <tr>
      <th>2017-03-29</th>
      <td>sh600063</td>
      <td>4.95</td>
      <td>5.01</td>
      <td>4.89</td>
      <td>4.92</td>
    </tr>
    <tr>
      <th>2017-03-30</th>
      <td>sh600063</td>
      <td>4.92</td>
      <td>4.94</td>
      <td>4.82</td>
      <td>4.89</td>
    </tr>
    <tr>
      <th>2017-03-31</th>
      <td>sh600063</td>
      <td>4.89</td>
      <td>4.93</td>
      <td>4.85</td>
      <td>4.88</td>
    </tr>
    <tr>
      <th>2017-04-05</th>
      <td>sh600063</td>
      <td>4.88</td>
      <td>4.99</td>
      <td>4.88</td>
      <td>4.98</td>
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
      <th>2017-04-18</th>
      <td>sh600063</td>
      <td>4.89</td>
      <td>4.95</td>
      <td>4.72</td>
      <td>4.74</td>
    </tr>
    <tr>
      <th>2017-04-19</th>
      <td>sh600063</td>
      <td>4.70</td>
      <td>4.74</td>
      <td>4.61</td>
      <td>4.71</td>
    </tr>
    <tr>
      <th>2017-04-20</th>
      <td>sh600063</td>
      <td>4.71</td>
      <td>4.76</td>
      <td>4.63</td>
      <td>4.68</td>
    </tr>
    <tr>
      <th>2017-04-21</th>
      <td>sh600063</td>
      <td>4.69</td>
      <td>4.73</td>
      <td>4.68</td>
      <td>4.70</td>
    </tr>
    <tr>
      <th>2017-04-24</th>
      <td>sh600063</td>
      <td>4.70</td>
      <td>4.71</td>
      <td>4.57</td>
      <td>4.58</td>
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




    array([ 4.99,  4.95,  4.92,  4.89,  4.88,  4.98,  5.  ,  5.04,  5.02,
            5.  ,  4.97,  5.05,  4.91,  4.89,  4.7 ,  4.71,  4.69,  4.7 ])




```python
# 调用函数
talib.CDLSPINNINGTOP(open_p, high_p, low_p, close_p)
```




    array([   0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
              0, -100,    0,  100, -100,  100,    0])



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
      <th>CDLSPINNINGTOP</th>
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
      <td>648887.000000</td>
      <td>648887.000000</td>
      <td>648887.000000</td>
      <td>648887.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>0.000356</td>
      <td>0.001450</td>
      <td>0.002807</td>
      <td>0.007265</td>
    </tr>
    <tr>
      <th>std</th>
      <td>0.041015</td>
      <td>0.068804</td>
      <td>0.085260</td>
      <td>0.116840</td>
    </tr>
    <tr>
      <th>min</th>
      <td>-0.897858</td>
      <td>-0.894156</td>
      <td>-0.894158</td>
      <td>-0.903448</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>-0.015413</td>
      <td>-0.027668</td>
      <td>-0.035990</td>
      <td>-0.049429</td>
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
      <td>-0.500082</td>
      <td>-0.509794</td>
      <td>-0.513956</td>
      <td>-0.651186</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>-0.015224</td>
      <td>-0.026712</td>
      <td>-0.034586</td>
      <td>-0.047187</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000470</td>
      <td>0.002212</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>0.015478</td>
      <td>0.027937</td>
      <td>0.037314</td>
      <td>0.055794</td>
    </tr>
    <tr>
      <th>max</th>
      <td>15.441176</td>
      <td>13.835287</td>
      <td>12.382336</td>
      <td>11.072970</td>
    </tr>
  </tbody>
</table>
<p>16 rows × 4 columns</p>
</div>




```python

```
