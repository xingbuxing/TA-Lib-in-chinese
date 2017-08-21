# CDLHOMINGPIGEON

中文名称： 家鸽

用法：预示着趋势反转

调用方法：signal = talib.CDLHOMINGPIGEON(open, high, low, close)

输出：0代表不符合k线形态，100表示符合形态。

## 指标介绍

二日 K 线模式，与母子线类似，不同的的是二日 K 线颜色相同，第二日最高价、最低价都在第一日实体之内

## 图例
![](/assets/homingpigeon.png)

## 使用案例

```python
import talib
展示数据df
df
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>date</th>
      <th>open</th>
      <th>close</th>
      <th>high</th>
      <th>low</th>
      <th>volume</th>
      <th>code</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2014-06-11</td>
      <td>7.781</td>
      <td>7.800</td>
      <td>7.911</td>
      <td>7.725</td>
      <td>579668.0</td>
      <td>000002</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2014-06-12</td>
      <td>7.790</td>
      <td>7.809</td>
      <td>7.855</td>
      <td>7.614</td>
      <td>801011.0</td>
      <td>000002</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2014-06-13</td>
      <td>7.781</td>
      <td>7.827</td>
      <td>7.874</td>
      <td>7.688</td>
      <td>635541.0</td>
      <td>000002</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2014-06-16</td>
      <td>7.809</td>
      <td>7.670</td>
      <td>7.818</td>
      <td>7.595</td>
      <td>863513.0</td>
      <td>000002</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2014-06-17</td>
      <td>7.660</td>
      <td>7.540</td>
      <td>7.660</td>
      <td>7.465</td>
      <td>685986.0</td>
      <td>000002</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2014-06-18</td>
      <td>7.540</td>
      <td>7.521</td>
      <td>7.586</td>
      <td>7.493</td>
      <td>346365.0</td>
      <td>000002</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2014-06-19</td>
      <td>7.549</td>
      <td>7.419</td>
      <td>7.567</td>
      <td>7.400</td>
      <td>405218.0</td>
      <td>000002</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2014-06-20</td>
      <td>7.465</td>
      <td>7.549</td>
      <td>7.549</td>
      <td>7.419</td>
      <td>426682.0</td>
      <td>000002</td>
    </tr>
    <tr>
      <th>8</th>
      <td>2014-06-23</td>
      <td>7.549</td>
      <td>7.567</td>
      <td>7.595</td>
      <td>7.502</td>
      <td>249327.0</td>
      <td>000002</td>
    </tr>
    <tr>
      <th>9</th>
      <td>2014-06-24</td>
      <td>7.605</td>
      <td>7.512</td>
      <td>7.605</td>
      <td>7.475</td>
      <td>324250.0</td>
      <td>000002</td>
    </tr>
    <tr>
      <th>10</th>
      <td>2014-06-25</td>
      <td>7.549</td>
      <td>7.549</td>
      <td>7.558</td>
      <td>7.391</td>
      <td>536538.0</td>
      <td>000002</td>
    </tr>
    <tr>
      <th>11</th>
      <td>2014-06-26</td>
      <td>7.540</td>
      <td>7.670</td>
      <td>7.735</td>
      <td>7.512</td>
      <td>599034.0</td>
      <td>000002</td>
    </tr>
    <tr>
      <th>12</th>
      <td>2014-06-27</td>
      <td>7.679</td>
      <td>7.725</td>
      <td>7.781</td>
      <td>7.642</td>
      <td>550831.0</td>
      <td>000002</td>
    </tr>
    <tr>
      <th>13</th>
      <td>2014-06-30</td>
      <td>7.725</td>
      <td>7.679</td>
      <td>7.753</td>
      <td>7.632</td>
      <td>393736.0</td>
      <td>000002</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>631</th>
      <td>2017-07-28</td>
      <td>23.000</td>
      <td>23.630</td>
      <td>23.840</td>
      <td>23.000</td>
      <td>412507.0</td>
      <td>000002</td>
    </tr>
    <tr>
      <th>632</th>
      <td>2017-07-31</td>
      <td>23.520</td>
      <td>23.370</td>
      <td>23.580</td>
      <td>23.100</td>
      <td>309424.0</td>
      <td>000002</td>
    </tr>
    <tr>
      <th>633</th>
      <td>2017-08-01</td>
      <td>23.350</td>
      <td>23.420</td>
      <td>23.550</td>
      <td>23.200</td>
      <td>209522.0</td>
      <td>000002</td>
    </tr>
    <tr>
      <th>634</th>
      <td>2017-08-02</td>
      <td>23.450</td>
      <td>23.580</td>
      <td>24.120</td>
      <td>23.430</td>
      <td>353910.0</td>
      <td>000002</td>
    </tr>
    <tr>
      <th>635</th>
      <td>2017-08-03</td>
      <td>23.580</td>
      <td>23.110</td>
      <td>23.580</td>
      <td>22.790</td>
      <td>455189.0</td>
      <td>000002</td>
    </tr>
    <tr>
      <th>636</th>
      <td>2017-08-04</td>
      <td>23.000</td>
      <td>22.840</td>
      <td>23.060</td>
      <td>22.710</td>
      <td>296123.0</td>
      <td>000002</td>
    </tr>
    <tr>
      <th>637</th>
      <td>2017-08-07</td>
      <td>22.820</td>
      <td>22.710</td>
      <td>23.050</td>
      <td>22.680</td>
      <td>234091.0</td>
      <td>000002</td>
    </tr>
    <tr>
      <th>638</th>
      <td>2017-08-08</td>
      <td>22.810</td>
      <td>22.770</td>
      <td>22.810</td>
      <td>22.580</td>
      <td>191585.0</td>
      <td>000002</td>
    </tr>
    <tr>
      <th>639</th>
      <td>2017-08-09</td>
      <td>22.800</td>
      <td>22.950</td>
      <td>23.080</td>
      <td>22.710</td>
      <td>244983.0</td>
      <td>000002</td>
    </tr>
    <tr>
      <th>640</th>
      <td>2017-08-10</td>
      <td>22.990</td>
      <td>22.620</td>
      <td>22.990</td>
      <td>22.530</td>
      <td>132427.0</td>
      <td>000002</td>
    </tr>
  </tbody>
</table>
<p>641 rows × 7 columns</p>
</div>




```python
# 赋值开高收低价，np.array格式

open_p = df['open'].values
close_p = df['close'].values
high_p = df['close'].values
low_p = df['low'].values

# 展示open_p中的数据（显示后20个）
open_p[-20:]
```




    array([ 24.91,  24.45,  25.58,  24.85,  24.85,  25.19,  24.7 ,  23.6 ,
            23.28,  23.45,  23.  ,  23.52,  23.35,  23.45,  23.58,  23.  ,
            22.82,  22.81,  22.8 ,  22.99])




```python
# 调用函数
signal = talib.CDLHOMINGPIGEON(open_p,high_p,low_p,close_p)

# 展示signal
signal
```




    array([  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
             0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
             0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
             ``` ```
             0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
             0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
             0,   0,   0,   0,   0,   0,   0,   0,   0,   0, 100,   0,   0,
             0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
             0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
             0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
             0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
             ``` ```
             0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
             0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
             0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
             0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
             0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
             0,   0,   0, 100,   0,   0,   0,   0,   0,   0,   0,   0,   0,
             0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
             ``` ```
             0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
             0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
             0,   0,   0,   0])




```python
# 将signal赋予df
df['signal'] = signal
```


```python
# 找出符合k线形态的日期
df.loc[df['signal']==100]
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>date</th>
      <th>open</th>
      <th>close</th>
      <th>high</th>
      <th>low</th>
      <th>volume</th>
      <th>code</th>
      <th>signal</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>257</th>
      <td>2015-06-29</td>
      <td>12.86</td>
      <td>12.711</td>
      <td>13.278</td>
      <td>11.959</td>
      <td>4207973.0</td>
      <td>000002</td>
      <td>100</td>
    </tr>
    <tr>
      <th>536</th>
      <td>2017-03-06</td>
      <td>20.25</td>
      <td>20.220</td>
      <td>20.390</td>
      <td>20.140</td>
      <td>276336.0</td>
      <td>000002</td>
      <td>100</td>
    </tr>
  </tbody>
</table>
</div>
