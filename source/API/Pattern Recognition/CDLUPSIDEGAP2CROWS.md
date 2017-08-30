
# CDLUPSIDEGAP2CROWS

中文名称：向上跳空两只乌鸦。

用法：与两只乌鸦形态一样，在股票上升趋势中出现两只乌鸦形态，是显著空头信号。

调用方法：talib.CDLUPSIDEGAP2CROWS(open, high, low, close)

输出：0代表不符合k线形态，-100表示符合形态。

# 指标介绍
第一跟K线：长阳线。

第二根K线：阴线，开盘跳空高开，实体部分与第一根K线实体部分之间存在缺口。

第三根K线：阴线，开盘价略高于第二根k线开盘，收盘价位于第一根k线实体与第二根K线实体之间。

## 图例


![CDLUPSIDEGAP2CROWS图例](/assets/CDLUPSIDEGAP2CROWS图例.png)

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
      <th>2009-02-23</th>
      <td>sh600057</td>
      <td>2.89</td>
      <td>3.05</td>
      <td>2.86</td>
      <td>3.04</td>
    </tr>
    <tr>
      <th>2009-02-24</th>
      <td>sh600057</td>
      <td>3.05</td>
      <td>3.14</td>
      <td>2.89</td>
      <td>2.89</td>
    </tr>
    <tr>
      <th>2009-02-25</th>
      <td>sh600057</td>
      <td>2.89</td>
      <td>2.96</td>
      <td>2.75</td>
      <td>2.88</td>
    </tr>
    <tr>
      <th>2009-02-26</th>
      <td>sh600057</td>
      <td>2.88</td>
      <td>3.02</td>
      <td>2.81</td>
      <td>2.99</td>
    </tr>
    <tr>
      <th>2009-02-27</th>
      <td>sh600057</td>
      <td>2.92</td>
      <td>2.98</td>
      <td>2.84</td>
      <td>2.84</td>
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
      <th>2009-03-18</th>
      <td>sh600057</td>
      <td>2.80</td>
      <td>2.94</td>
      <td>2.75</td>
      <td>2.94</td>
    </tr>
    <tr>
      <th>2009-03-19</th>
      <td>sh600057</td>
      <td>2.94</td>
      <td>3.04</td>
      <td>2.89</td>
      <td>2.99</td>
    </tr>
    <tr>
      <th>2009-03-20</th>
      <td>sh600057</td>
      <td>2.98</td>
      <td>3.02</td>
      <td>2.89</td>
      <td>2.98</td>
    </tr>
    <tr>
      <th>2009-03-23</th>
      <td>sh600057</td>
      <td>2.98</td>
      <td>3.06</td>
      <td>2.96</td>
      <td>3.04</td>
    </tr>
    <tr>
      <th>2009-03-24</th>
      <td>sh600057</td>
      <td>3.04</td>
      <td>3.06</td>
      <td>2.98</td>
      <td>2.99</td>
    </tr>
  </tbody>
</table>
<p>21 rows × 5 columns</p>
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




    array([ 2.89,  3.05,  2.89,  2.88,  2.92,  2.7 ,  2.68,  2.72,  2.7 ,
            2.59,  2.6 ,  2.62,  2.85,  2.87,  2.8 ,  2.75,  2.8 ,  2.94,
            2.98,  2.98,  3.04])




```python
np.where(talib.CDLUPSIDEGAP2CROWS(open_p, high_p, low_p, close_p)==-100)
```




    (array([13]),)




```python
# 调用函数
talib.CDLUPSIDEGAP2CROWS(open_p, high_p, low_p, close_p)
```




    array([   0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
              0,    0, -100,    0,    0,    0,    0,    0,    0,    0], dtype=int32)



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
      <th>CDLUPSIDEGAP2CROWS</th>
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
      <td>1023.000000</td>
      <td>1.023000e+03</td>
      <td>1.023000e+03</td>
      <td>1023.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>0.003735</td>
      <td>5.404645e-03</td>
      <td>7.574009e-03</td>
      <td>0.010445</td>
    </tr>
    <tr>
      <th>std</th>
      <td>0.034564</td>
      <td>5.733049e-02</td>
      <td>7.522322e-02</td>
      <td>0.112021</td>
    </tr>
    <tr>
      <th>min</th>
      <td>-0.100218</td>
      <td>-2.608698e-01</td>
      <td>-2.521741e-01</td>
      <td>-0.491572</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>-0.013694</td>
      <td>-2.446450e-02</td>
      <td>-3.217338e-02</td>
      <td>-0.047496</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>0.001855</td>
      <td>-9.106898e-07</td>
      <td>6.287444e-08</td>
      <td>-0.000627</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>0.018821</td>
      <td>2.779898e-02</td>
      <td>3.976559e-02</td>
      <td>0.051811</td>
    </tr>
    <tr>
      <th>max</th>
      <td>0.237234</td>
      <td>2.872334e-01</td>
      <td>3.831037e-01</td>
      <td>0.939528</td>
    </tr>
  </tbody>
</table>
</div>



