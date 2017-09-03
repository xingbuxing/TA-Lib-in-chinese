# CDLEVENINGDOJISTAR
## 概述
中文名称：十字黄昏星。

用法：十字黄昏星永远是看跌信号。虽然本指标不强调趋势，但若在上涨趋势中出现十字黄昏星，尤其需要注意。

调用方法：talib.CDLEVENINGDOJISTAR(open, high, low, close)

可选参数：penetration=0.3，一根k线在另一根k线范围内的渗透百分比

输出：0代表不符合k线形态，-100代表符合。

## 指标介绍
第一根k线：长实体的阳线。

第二根k线：十字星形态，且跳出第一根k线。

第三根k线：阴线，实体部分在第一根k线实体范围以内。

## 图例

![](/assets/CDLEVENINGDOJISTAR_sh600713.png)

上图中最后3根K线，即为CDLEVENINGDOJISTAR


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
      <th>1996-08-13</th>
      <td>sh600713</td>
      <td>9.30</td>
      <td>9.30</td>
      <td>8.90</td>
      <td>9.05</td>
    </tr>
    <tr>
      <th>1996-08-14</th>
      <td>sh600713</td>
      <td>9.00</td>
      <td>9.10</td>
      <td>8.85</td>
      <td>9.10</td>
    </tr>
    <tr>
      <th>1996-08-15</th>
      <td>sh600713</td>
      <td>9.08</td>
      <td>9.17</td>
      <td>8.95</td>
      <td>9.00</td>
    </tr>
    <tr>
      <th>1996-08-16</th>
      <td>sh600713</td>
      <td>8.98</td>
      <td>8.98</td>
      <td>8.65</td>
      <td>8.95</td>
    </tr>
    <tr>
      <th>1996-08-19</th>
      <td>sh600713</td>
      <td>8.90</td>
      <td>8.95</td>
      <td>8.77</td>
      <td>8.90</td>
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
      <th>1996-08-30</th>
      <td>sh600713</td>
      <td>8.90</td>
      <td>9.15</td>
      <td>8.84</td>
      <td>9.10</td>
    </tr>
    <tr>
      <th>1996-09-02</th>
      <td>sh600713</td>
      <td>9.15</td>
      <td>9.17</td>
      <td>9.00</td>
      <td>9.16</td>
    </tr>
    <tr>
      <th>1996-09-03</th>
      <td>sh600713</td>
      <td>9.16</td>
      <td>9.25</td>
      <td>8.75</td>
      <td>8.80</td>
    </tr>
    <tr>
      <th>1996-09-04</th>
      <td>sh600713</td>
      <td>8.80</td>
      <td>8.96</td>
      <td>8.51</td>
      <td>8.94</td>
    </tr>
    <tr>
      <th>1996-09-05</th>
      <td>sh600713</td>
      <td>8.90</td>
      <td>9.19</td>
      <td>8.81</td>
      <td>8.89</td>
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




    array([ 9.3 ,  9.  ,  9.08,  8.98,  8.9 ,  8.8 ,  9.15,  9.38,  8.78,
            8.65,  8.45,  8.73,  8.94,  8.9 ,  9.15,  9.16,  8.8 ,  8.9 ])




```python
# 调用函数
talib.CDLEVENINGDOJISTAR(open_p, high_p, low_p, close_p)
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
      <th>CDLEVENINGDOJISTAR</th>
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
      <td>14125.000000</td>
      <td>14125.000000</td>
      <td>14125.000000</td>
      <td>14125.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>0.001802</td>
      <td>0.003566</td>
      <td>0.004879</td>
      <td>0.011343</td>
    </tr>
    <tr>
      <th>std</th>
      <td>0.032673</td>
      <td>0.058416</td>
      <td>0.076298</td>
      <td>0.110127</td>
    </tr>
    <tr>
      <th>min</th>
      <td>-0.206503</td>
      <td>-0.299218</td>
      <td>-0.365156</td>
      <td>-0.530226</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>-0.013529</td>
      <td>-0.027190</td>
      <td>-0.035176</td>
      <td>-0.048718</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>0.002421</td>
      <td>0.000465</td>
      <td>0.002090</td>
      <td>0.005055</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>0.017758</td>
      <td>0.032259</td>
      <td>0.042986</td>
      <td>0.063604</td>
    </tr>
    <tr>
      <th>max</th>
      <td>0.372881</td>
      <td>0.661695</td>
      <td>0.671863</td>
      <td>1.160001</td>
    </tr>
  </tbody>
</table>
</div>
