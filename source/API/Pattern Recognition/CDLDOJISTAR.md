# CDLDOJISTAR
## 概述
中文名称：十字星线。

用法：第一根长实体为红k，第二根星形态k线跳空高开为看涨行情，
	第一根长实体为绿k，第二根星形态k线跳空低开为看跌行情。
	在上升趋势中出现十字星线视为看涨行情，在下跌趋势中出现十字星线则视为看跌行情。在判断看涨或看跌行情时，必须要参考股票的趋势。

调用方法：talib.CDLDOJISTAR(open, high, low, close)

输出：看涨行情中符合形态输出100， 看跌行情中符合形态输出-100， 不符合形态输出0。

## 指标介绍
第一根k线：长实体。

第二根k线：十字星形态，（在上升趋势中跳空高开，或下跌趋势中跳空低开）

## 图例

![](/assets/CDLDOJISTAR_sz300431.png)

上图中最后2根K线，即为CDLDOJISTAR

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
      <th>2015-04-20</th>
      <td>sz300431</td>
      <td>57.15</td>
      <td>57.15</td>
      <td>57.15</td>
      <td>57.15</td>
    </tr>
    <tr>
      <th>2015-04-21</th>
      <td>sz300431</td>
      <td>62.87</td>
      <td>62.87</td>
      <td>62.87</td>
      <td>62.87</td>
    </tr>
    <tr>
      <th>2015-04-22</th>
      <td>sz300431</td>
      <td>69.16</td>
      <td>69.16</td>
      <td>69.16</td>
      <td>69.16</td>
    </tr>
    <tr>
      <th>2015-04-23</th>
      <td>sz300431</td>
      <td>76.08</td>
      <td>76.08</td>
      <td>76.08</td>
      <td>76.08</td>
    </tr>
    <tr>
      <th>2015-04-24</th>
      <td>sz300431</td>
      <td>83.69</td>
      <td>83.69</td>
      <td>83.69</td>
      <td>83.69</td>
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
      <th>2015-05-08</th>
      <td>sz300431</td>
      <td>179.00</td>
      <td>189.97</td>
      <td>169.03</td>
      <td>189.97</td>
    </tr>
    <tr>
      <th>2015-05-11</th>
      <td>sz300431</td>
      <td>200.00</td>
      <td>208.97</td>
      <td>198.11</td>
      <td>208.97</td>
    </tr>
    <tr>
      <th>2015-05-12</th>
      <td>sz300431</td>
      <td>229.87</td>
      <td>229.87</td>
      <td>228.00</td>
      <td>229.87</td>
    </tr>
    <tr>
      <th>2015-05-13</th>
      <td>sz300431</td>
      <td>240.00</td>
      <td>252.86</td>
      <td>235.20</td>
      <td>252.86</td>
    </tr>
    <tr>
      <th>2015-05-14</th>
      <td>sz300431</td>
      <td>278.15</td>
      <td>278.15</td>
      <td>235.00</td>
      <td>241.70</td>
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




    array([  57.15,   62.87,   69.16,   76.08,   83.69,   92.06,  101.27,
            111.4 ,  122.54,  134.79,  148.27,  148.27,  160.  ,  179.  ,
            200.  ,  229.87,  240.  ,  278.15])




```python
# 调用函数
talib.CDLDOJISTAR(open_p, high_p, low_p, close_p)
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
      <th>CDLDOJISTAR</th>
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
      <td>89933.000000</td>
      <td>8.993300e+04</td>
      <td>89933.000000</td>
      <td>89933.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>0.003559</td>
      <td>8.340991e-03</td>
      <td>0.010084</td>
      <td>0.018640</td>
    </tr>
    <tr>
      <th>std</th>
      <td>0.037223</td>
      <td>8.909928e-02</td>
      <td>0.104974</td>
      <td>0.149631</td>
    </tr>
    <tr>
      <th>min</th>
      <td>-0.543566</td>
      <td>-6.304487e-01</td>
      <td>-0.664080</td>
      <td>-0.744156</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>-0.015271</td>
      <td>-2.558595e-02</td>
      <td>-0.034907</td>
      <td>-0.046153</td>
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
      <td>-0.236287</td>
      <td>-3.778045e-01</td>
      <td>-0.894158</td>
      <td>-0.889004</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>-0.015009</td>
      <td>-2.801360e-02</td>
      <td>-0.035431</td>
      <td>-0.049567</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>0.002227</td>
      <td>7.850951e-07</td>
      <td>0.001485</td>
      <td>0.000001</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>0.017483</td>
      <td>2.970874e-02</td>
      <td>0.040883</td>
      <td>0.057077</td>
    </tr>
    <tr>
      <th>max</th>
      <td>0.473684</td>
      <td>8.061844e+00</td>
      <td>10.360822</td>
      <td>13.373342</td>
    </tr>
  </tbody>
</table>
<p>16 rows × 4 columns</p>
</div>
