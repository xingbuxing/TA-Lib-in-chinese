
# CDLKICKING

中文名称：  反冲形态

用法：二日 K 线模式，与分离线类似，助涨上升或下降趋势

调用方法：signal = talib.CDLKICKING(open, high, low, close)

输出：0代表不符合k线形态，100表示符合形态。

## 指标介绍
两日 K 线为秃线，颜色相反，存在跳空缺口。

## 图例
![](/assets/CDLKICKING.png)

## 使用案例


```python
# 展示数据

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
      <th>4472</th>
      <td>2017-04-12</td>
      <td>4.93</td>
      <td>5.02</td>
      <td>4.90</td>
      <td>4.93</td>
    </tr>
    <tr>
      <th>4473</th>
      <td>2017-04-13</td>
      <td>4.93</td>
      <td>5.01</td>
      <td>4.90</td>
      <td>4.95</td>
    </tr>
    <tr>
      <th>4474</th>
      <td>2017-04-14</td>
      <td>4.94</td>
      <td>5.03</td>
      <td>4.92</td>
      <td>5.03</td>
    </tr>
    <tr>
      <th>4475</th>
      <td>2017-04-17</td>
      <td>4.95</td>
      <td>5.17</td>
      <td>4.90</td>
      <td>5.02</td>
    </tr>
    <tr>
      <th>4476</th>
      <td>2017-04-19</td>
      <td>4.78</td>
      <td>4.98</td>
      <td>4.77</td>
      <td>4.77</td>
    </tr>
    <tr>
      <th>4477</th>
      <td>2017-04-20</td>
      <td>4.94</td>
      <td>5.01</td>
      <td>4.86</td>
      <td>5.01</td>
    </tr>
    <tr>
      <th>4478</th>
      <td>2017-04-21</td>
      <td>5.05</td>
      <td>5.18</td>
      <td>5.01</td>
      <td>5.04</td>
    </tr>
    <tr>
      <th>4479</th>
      <td>2017-04-24</td>
      <td>5.04</td>
      <td>5.06</td>
      <td>4.85</td>
      <td>4.90</td>
    </tr>
    <tr>
      <th>4480</th>
      <td>2017-04-25</td>
      <td>4.90</td>
      <td>5.03</td>
      <td>4.88</td>
      <td>4.95</td>
    </tr>
    <tr>
      <th>4481</th>
      <td>2017-04-26</td>
      <td>4.96</td>
      <td>5.08</td>
      <td>4.96</td>
      <td>5.05</td>
    </tr>
    <tr>
      <th>4482</th>
      <td>2017-04-27</td>
      <td>5.05</td>
      <td>5.13</td>
      <td>4.97</td>
      <td>5.10</td>
    </tr>
    <tr>
      <th>4483</th>
      <td>2017-04-28</td>
      <td>5.10</td>
      <td>5.15</td>
      <td>5.06</td>
      <td>5.14</td>
    </tr>
    <tr>
      <th>4484</th>
      <td>2017-05-02</td>
      <td>5.12</td>
      <td>5.15</td>
      <td>5.04</td>
      <td>5.08</td>
    </tr>
    <tr>
      <th>4485</th>
      <td>2017-05-03</td>
      <td>5.09</td>
      <td>5.12</td>
      <td>5.06</td>
      <td>5.09</td>
    </tr>
    <tr>
      <th>4486</th>
      <td>2017-05-04</td>
      <td>5.06</td>
      <td>5.10</td>
      <td>5.04</td>
      <td>5.05</td>
    </tr>
    <tr>
      <th>4487</th>
      <td>2017-05-05</td>
      <td>5.02</td>
      <td>5.04</td>
      <td>4.80</td>
      <td>4.86</td>
    </tr>
    <tr>
      <th>4488</th>
      <td>2017-05-08</td>
      <td>4.83</td>
      <td>4.86</td>
      <td>4.64</td>
      <td>4.66</td>
    </tr>
    <tr>
      <th>4489</th>
      <td>2017-05-09</td>
      <td>4.66</td>
      <td>4.76</td>
      <td>4.60</td>
      <td>4.69</td>
    </tr>
    <tr>
      <th>4490</th>
      <td>2017-05-10</td>
      <td>4.70</td>
      <td>4.76</td>
      <td>4.63</td>
      <td>4.66</td>
    </tr>
    <tr>
      <th>4491</th>
      <td>2017-05-11</td>
      <td>4.61</td>
      <td>4.67</td>
      <td>4.51</td>
      <td>4.62</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 将数据转为array格式
open_p = df['open'].values
high_p = df['high'].values
low_p = df['low'].values
close_p = df['close'].values

# 展示转换后数据
open_p      # 数据应具有一定长度以判断下跌趋势
```




    array([ 5.02,  4.94,  5.1 ,  5.08,  5.03,  4.89,  4.93,  4.93,  4.94,
            4.95,  4.78,  4.94,  5.05,  5.04,  4.9 ,  4.96,  5.05,  5.1 ,
            5.12,  5.09,  5.06,  5.02,  4.83,  4.66,  4.7 ,  4.61])




```python
# 调用函数并展示结果
signal = talib.CDLINVERTEDHAMMER(open_p, high_p, low_p, close_p)
signal
```




    array([  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
             0,   0,   0,   0,   0,   0,   0, 100,   0,   0,   0,   0,   0])




```python
# 找出符合k线的交易日期
df['signal'] = signal
df = df.loc[df['signal'] != 0]
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
      <th>signal</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>4486</th>
      <td>2017-05-04</td>
      <td>5.06</td>
      <td>5.1</td>
      <td>5.04</td>
      <td>5.05</td>
      <td>100</td>
    </tr>
  </tbody>
</table>
</div>


