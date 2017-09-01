
# CDLSTALLEDPATTERN
中文名称：停顿形态；

用法：出现停顿形态，是显著空头信号，特别是在上升趋势中；

调用方法：talib. CDLSTALLEDPATTERN (open, high, low, close)；

输出：0表示不符合形态，-100表示符合形态。

## 指标介绍
三根K线模式；

连续三根阳线；

第一跟K线：长阳线；

第二根K线：长阳线，没有或是有很短的上影线，开盘于前一日收盘价附近，收盘高于前一日收盘价；

第三根K线：短阳线，开盘于前一日收盘价附近。

## 图例

！[](TA-Lib-in-chinese/assets/CDLSTALLEDPATTERN_sh600063.png)

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
      <th>2014-11-25</th>
      <td>sh600063</td>
      <td>4.24</td>
      <td>4.39</td>
      <td>4.22</td>
      <td>4.34</td>
    </tr>
    <tr>
      <th>2014-11-26</th>
      <td>sh600063</td>
      <td>4.35</td>
      <td>4.55</td>
      <td>4.30</td>
      <td>4.50</td>
    </tr>
    <tr>
      <th>2014-11-27</th>
      <td>sh600063</td>
      <td>4.48</td>
      <td>4.54</td>
      <td>4.41</td>
      <td>4.46</td>
    </tr>
    <tr>
      <th>2014-11-28</th>
      <td>sh600063</td>
      <td>4.51</td>
      <td>4.52</td>
      <td>4.34</td>
      <td>4.41</td>
    </tr>
    <tr>
      <th>2014-12-01</th>
      <td>sh600063</td>
      <td>4.41</td>
      <td>4.55</td>
      <td>4.35</td>
      <td>4.51</td>
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
      <th>2014-12-12</th>
      <td>sh600063</td>
      <td>4.34</td>
      <td>4.50</td>
      <td>4.33</td>
      <td>4.49</td>
    </tr>
    <tr>
      <th>2014-12-15</th>
      <td>sh600063</td>
      <td>4.47</td>
      <td>4.62</td>
      <td>4.44</td>
      <td>4.61</td>
    </tr>
    <tr>
      <th>2014-12-16</th>
      <td>sh600063</td>
      <td>4.59</td>
      <td>4.66</td>
      <td>4.54</td>
      <td>4.62</td>
    </tr>
    <tr>
      <th>2014-12-17</th>
      <td>sh600063</td>
      <td>4.62</td>
      <td>4.86</td>
      <td>4.57</td>
      <td>4.69</td>
    </tr>
    <tr>
      <th>2014-12-26</th>
      <td>sh600063</td>
      <td>4.66</td>
      <td>5.16</td>
      <td>4.51</td>
      <td>5.02</td>
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




    array([ 4.24,  4.35,  4.48,  4.51,  4.41,  4.51,  4.55,  4.52,  4.63,
            4.55,  4.59,  4.21,  4.3 ,  4.34,  4.47,  4.59,  4.62,  4.66])




```python
# 调用函数
talib.CDLSTALLEDPATTERN(open_p, high_p, low_p, close_p)
```




    array([   0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
              0,    0,    0,    0, -100,    0,    0])



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
      <th>CDLSTALLEDPATTERN</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="8" valign="top">-100.0</th>
      <th>count</th>
      <td>18736.000000</td>
      <td>18736.000000</td>
      <td>18736.000000</td>
      <td>18736.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>0.001070</td>
      <td>0.005946</td>
      <td>0.007217</td>
      <td>0.014805</td>
    </tr>
    <tr>
      <th>std</th>
      <td>0.045047</td>
      <td>0.110045</td>
      <td>0.119647</td>
      <td>0.148926</td>
    </tr>
    <tr>
      <th>min</th>
      <td>-0.687333</td>
      <td>-0.706512</td>
      <td>-0.727476</td>
      <td>-0.777877</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>-0.017589</td>
      <td>-0.028393</td>
      <td>-0.037888</td>
      <td>-0.051761</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>-0.001262</td>
      <td>0.001041</td>
      <td>0.000580</td>
      <td>0.004501</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>0.016583</td>
      <td>0.032397</td>
      <td>0.041073</td>
      <td>0.066375</td>
    </tr>
    <tr>
      <th>max</th>
      <td>3.303406</td>
      <td>11.588034</td>
      <td>10.965817</td>
      <td>9.589751</td>
    </tr>
  </tbody>
</table>
</div>




```python

```
