# CDLHAMMER
## 概述
中文名称：锤头线

用法: 锤头线为看涨信号。请注意，锤头线必须出现在下跌趋势中，但本函数不包含趋势判断。

调用方法：talib.CDLHAMMER(open, high, low, close)

输出：符合形态输出100，不符合则输出0。

## 指标介绍
k线实体小。

下影线长。

上影线极短，甚至没有上影线。

该k线的实体低于前一根k线的最低价，或在其附近。

## 图例

![](/assets/CDLHAMMER_sz300431.png)

上图中最后1根K线，即为CDLHAMMER


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
      <th>2016-04-07</th>
      <td>sz300431</td>
      <td>91.00</td>
      <td>93.46</td>
      <td>87.21</td>
      <td>87.23</td>
    </tr>
    <tr>
      <th>2016-04-08</th>
      <td>sz300431</td>
      <td>84.24</td>
      <td>85.88</td>
      <td>80.50</td>
      <td>82.00</td>
    </tr>
    <tr>
      <th>2016-04-11</th>
      <td>sz300431</td>
      <td>82.84</td>
      <td>85.19</td>
      <td>81.39</td>
      <td>82.00</td>
    </tr>
    <tr>
      <th>2016-04-12</th>
      <td>sz300431</td>
      <td>82.00</td>
      <td>85.55</td>
      <td>81.50</td>
      <td>84.40</td>
    </tr>
    <tr>
      <th>2016-04-13</th>
      <td>sz300431</td>
      <td>82.93</td>
      <td>87.70</td>
      <td>82.59</td>
      <td>84.86</td>
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
      <th>2016-04-26</th>
      <td>sz300431</td>
      <td>71.50</td>
      <td>72.48</td>
      <td>70.30</td>
      <td>72.24</td>
    </tr>
    <tr>
      <th>2016-04-27</th>
      <td>sz300431</td>
      <td>72.01</td>
      <td>72.70</td>
      <td>70.62</td>
      <td>70.94</td>
    </tr>
    <tr>
      <th>2016-04-28</th>
      <td>sz300431</td>
      <td>70.80</td>
      <td>71.50</td>
      <td>68.10</td>
      <td>71.18</td>
    </tr>
    <tr>
      <th>2016-04-29</th>
      <td>sz300431</td>
      <td>70.21</td>
      <td>72.38</td>
      <td>69.72</td>
      <td>71.38</td>
    </tr>
    <tr>
      <th>2016-05-03</th>
      <td>sz300431</td>
      <td>71.75</td>
      <td>78.52</td>
      <td>69.80</td>
      <td>76.50</td>
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




    array([ 91.  ,  84.24,  82.84,  82.  ,  82.93,  85.67,  86.7 ,  83.35,
            85.  ,  83.4 ,  73.31,  70.1 ,  71.98,  71.5 ,  72.01,  70.8 ,
            70.21,  71.75])




```python
# 调用函数
talib.CDLHAMMER(open_p, high_p, low_p, close_p)
```




    array([  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
             0,   0, 100,   0,   0], dtype=int32)



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
      <th>CDLHAMMER</th>
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
      <td>180303.000000</td>
      <td>1.803030e+05</td>
      <td>180303.000000</td>
      <td>1.803030e+05</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>0.001974</td>
      <td>9.938469e-04</td>
      <td>0.002903</td>
      <td>5.744001e-03</td>
    </tr>
    <tr>
      <th>std</th>
      <td>0.028501</td>
      <td>5.305348e-02</td>
      <td>0.069905</td>
      <td>1.059323e-01</td>
    </tr>
    <tr>
      <th>min</th>
      <td>-0.275862</td>
      <td>-4.709708e-01</td>
      <td>-0.410716</td>
      <td>-5.885246e-01</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>-0.012299</td>
      <td>-2.547733e-02</td>
      <td>-0.033051</td>
      <td>-4.817264e-02</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>0.001576</td>
      <td>5.159964e-08</td>
      <td>0.000001</td>
      <td>2.459326e-07</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>0.015832</td>
      <td>2.708656e-02</td>
      <td>0.036272</td>
      <td>5.315313e-02</td>
    </tr>
    <tr>
      <th>max</th>
      <td>0.549708</td>
      <td>9.880485e-01</td>
      <td>3.475033</td>
      <td>8.518183e+00</td>
    </tr>
  </tbody>
</table>
</div>


