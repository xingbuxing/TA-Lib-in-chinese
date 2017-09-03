# CDLENGULFING
## 概述
中文名称：鲸吞型。

用法：鲸吞型通常代表趋势反转，虽然本指标不考虑趋势，但必须要区分在牛市中下跌趋势出现的鲸吞型，还是在熊市中上升趋势出现的鲸吞型。

调用方法：talib.CDLENGULFING(open, high, low, close)

可选参数：penetration，一根k线在另一根k线范围内的渗透百分比

输出：看涨行情中符合形态输出80或100，看跌行情中符合形态输出-80或-100，不符合则输出0。
	若第二根实体线完全吞没第一根实体线（上下两端均超出第一根实体线），输出100或-100
	若两根实体线有其中一端处于水平状态，输出80或-80

## 指标介绍
第一根k线：阴（阳）实体线。

第二根k线：阳（阴）实体线吞没前一根实体线。

## 图例

![](/assets/CDLENGULFING_sz300431.png)

上图中最后2根K线，即为CDLENGULFING

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
      <th>2015-04-29</th>
      <td>sz300431</td>
      <td>111.40</td>
      <td>111.40</td>
      <td>111.40</td>
      <td>111.40</td>
    </tr>
    <tr>
      <th>2015-04-30</th>
      <td>sz300431</td>
      <td>122.54</td>
      <td>122.54</td>
      <td>122.54</td>
      <td>122.54</td>
    </tr>
    <tr>
      <th>2015-05-04</th>
      <td>sz300431</td>
      <td>134.79</td>
      <td>134.79</td>
      <td>134.79</td>
      <td>134.79</td>
    </tr>
    <tr>
      <th>2015-05-05</th>
      <td>sz300431</td>
      <td>148.27</td>
      <td>148.27</td>
      <td>148.27</td>
      <td>148.27</td>
    </tr>
    <tr>
      <th>2015-05-06</th>
      <td>sz300431</td>
      <td>148.27</td>
      <td>163.10</td>
      <td>140.80</td>
      <td>157.00</td>
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
      <th>2015-05-19</th>
      <td>sz300431</td>
      <td>264.00</td>
      <td>273.46</td>
      <td>248.60</td>
      <td>273.46</td>
    </tr>
    <tr>
      <th>2015-05-20</th>
      <td>sz300431</td>
      <td>297.00</td>
      <td>300.81</td>
      <td>291.00</td>
      <td>300.81</td>
    </tr>
    <tr>
      <th>2015-05-21</th>
      <td>sz300431</td>
      <td>324.00</td>
      <td>327.01</td>
      <td>276.89</td>
      <td>280.00</td>
    </tr>
    <tr>
      <th>2015-05-22</th>
      <td>sz300431</td>
      <td>288.00</td>
      <td>298.60</td>
      <td>261.34</td>
      <td>289.00</td>
    </tr>
    <tr>
      <th>2015-05-25</th>
      <td>sz300431</td>
      <td>262.00</td>
      <td>282.50</td>
      <td>260.10</td>
      <td>265.01</td>
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




    array([ 111.4 ,  122.54,  134.79,  148.27,  148.27,  160.  ,  179.  ,
            200.  ,  229.87,  240.  ,  278.15,  225.  ,  232.  ,  264.  ,
            297.  ,  324.  ,  288.  ,  262.  ])




```python
# 调用函数
talib.CDLENGULFING(open_p, high_p, low_p, close_p)
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
      <th>CDLENGULFING</th>
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
      <td>387058.000000</td>
      <td>387058.000000</td>
      <td>387058.000000</td>
      <td>387058.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>-0.002355</td>
      <td>0.001808</td>
      <td>0.004169</td>
      <td>0.007359</td>
    </tr>
    <tr>
      <th>std</th>
      <td>0.031933</td>
      <td>0.058814</td>
      <td>0.076950</td>
      <td>0.111190</td>
    </tr>
    <tr>
      <th>min</th>
      <td>-0.353234</td>
      <td>-0.388060</td>
      <td>-0.652632</td>
      <td>-0.866484</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>-0.017421</td>
      <td>-0.027331</td>
      <td>-0.033728</td>
      <td>-0.048053</td>
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
      <td>-0.483317</td>
      <td>-0.490576</td>
      <td>-0.504161</td>
      <td>-0.651150</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>-0.012780</td>
      <td>-0.025247</td>
      <td>-0.033638</td>
      <td>-0.046191</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>0.001770</td>
      <td>0.001475</td>
      <td>0.001822</td>
      <td>0.004510</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>0.018131</td>
      <td>0.029983</td>
      <td>0.039136</td>
      <td>0.058892</td>
    </tr>
    <tr>
      <th>max</th>
      <td>0.690141</td>
      <td>10.348104</td>
      <td>13.623543</td>
      <td>12.549258</td>
    </tr>
  </tbody>
</table>
<p>16 rows × 4 columns</p>
</div>

