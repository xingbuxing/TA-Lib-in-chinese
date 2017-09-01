
# CDLTAKURI
中文名称：探水竿；

用法：出现该指标，并不意味着看涨，需要结合趋势进行分析；

调用方法：talib. CDLTAKURI (open, high, low, close)；

输出：0表示不符合形态，100表示符合形态。

## 指标介绍
单日K线；

实体很小；

开盘和收盘于当天的高点；

没有或有很短的上影线；

有很长的下影线。

## 图例

！[](TA-Lib-in-chinese/assets/CDLTAKURI_sh600063.png)

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
      <th>2016-07-19</th>
      <td>sh600063</td>
      <td>4.65</td>
      <td>4.70</td>
      <td>4.62</td>
      <td>4.67</td>
    </tr>
    <tr>
      <th>2016-07-20</th>
      <td>sh600063</td>
      <td>4.67</td>
      <td>4.72</td>
      <td>4.64</td>
      <td>4.65</td>
    </tr>
    <tr>
      <th>2016-07-21</th>
      <td>sh600063</td>
      <td>4.66</td>
      <td>4.69</td>
      <td>4.62</td>
      <td>4.63</td>
    </tr>
    <tr>
      <th>2016-07-22</th>
      <td>sh600063</td>
      <td>4.64</td>
      <td>4.64</td>
      <td>4.56</td>
      <td>4.60</td>
    </tr>
    <tr>
      <th>2016-07-25</th>
      <td>sh600063</td>
      <td>4.58</td>
      <td>4.63</td>
      <td>4.56</td>
      <td>4.59</td>
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
      <th>2016-08-05</th>
      <td>sh600063</td>
      <td>4.39</td>
      <td>4.43</td>
      <td>4.35</td>
      <td>4.42</td>
    </tr>
    <tr>
      <th>2016-08-08</th>
      <td>sh600063</td>
      <td>4.40</td>
      <td>4.52</td>
      <td>4.37</td>
      <td>4.51</td>
    </tr>
    <tr>
      <th>2016-08-09</th>
      <td>sh600063</td>
      <td>4.52</td>
      <td>4.52</td>
      <td>4.47</td>
      <td>4.51</td>
    </tr>
    <tr>
      <th>2016-08-10</th>
      <td>sh600063</td>
      <td>4.51</td>
      <td>4.57</td>
      <td>4.48</td>
      <td>4.49</td>
    </tr>
    <tr>
      <th>2016-08-11</th>
      <td>sh600063</td>
      <td>4.51</td>
      <td>4.58</td>
      <td>4.48</td>
      <td>4.55</td>
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




    array([ 4.65,  4.67,  4.66,  4.64,  4.58,  4.59,  4.65,  4.42,  4.43,
            4.38,  4.34,  4.35,  4.39,  4.39,  4.4 ,  4.52,  4.51,  4.51])




```python
# 调用函数
talib.CDLTAKURI(open_p, high_p, low_p, close_p)
```




    array([  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
             0,   0, 100,   0,   0])



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
      <th>CDLTAKURI</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="8" valign="top">100.0</th>
      <th>count</th>
      <td>132742.000000</td>
      <td>1.327420e+05</td>
      <td>132742.000000</td>
      <td>132742.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>0.003239</td>
      <td>2.857183e-03</td>
      <td>0.005568</td>
      <td>0.009105</td>
    </tr>
    <tr>
      <th>std</th>
      <td>0.048661</td>
      <td>7.515455e-02</td>
      <td>0.091139</td>
      <td>0.125261</td>
    </tr>
    <tr>
      <th>min</th>
      <td>-0.543566</td>
      <td>-6.304487e-01</td>
      <td>-0.666191</td>
      <td>-0.744156</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>-0.012701</td>
      <td>-2.525246e-02</td>
      <td>-0.032257</td>
      <td>-0.047708</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>0.001002</td>
      <td>-2.731309e-07</td>
      <td>0.000001</td>
      <td>0.000856</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>0.016501</td>
      <td>2.643460e-02</td>
      <td>0.036351</td>
      <td>0.053599</td>
    </tr>
    <tr>
      <th>max</th>
      <td>12.271869</td>
      <td>1.158803e+01</td>
      <td>10.965817</td>
      <td>11.146967</td>
    </tr>
  </tbody>
</table>
</div>




```python

```
