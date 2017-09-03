## 在GitHub上更新Fork的方法

#### 经常遇到的是Fork一个项目之后，源项目的作者做了新的更改，如果没有同步到我自己的Fork，我所做的更新进行Pull Request后，会产生冲突；因此在更新文件之前、至少是Pull Request之前，应当要更新自己的Fork的。

#### 更新Fork的方法有很多，Git写代码是很好的，当小白通常比较难做，步骤缺了就经常不奏效；所以我自己亲测了一个GitHub上更新Fork的方法，做一个教程，与朋友们共勉；废话少说，步骤如下。

#### 一、进入自己Fork来的项目，按New Pull Request按钮，新建一个Pull Request（简称：PR）。
![](/assets/ForkFetch1.png)

#### 二、如果自己还没有修改过Fork项目的文件，那么此时可以点击switching the base，切换到基于我自己的Fork项目。
![](/assets/ForkFetch2.png)
#### 如果已经修改或更新过Fork项目的文件，那么可以通过选择Base Fork和Head Fork来从源项目更新到我自己的Fork项目。
![](/assets/ForkFetch3.png)
![](/assets/ForkFetch4.png)
* 这里有个小技巧：在默认状态下，会是Base源项目，Head我自己的Fork项目；这样选择任何一个时，会调到某个无法更新的页面；解决方法是先Base或Head一个其他人的账号下的Fork，接着选择Head/Base源项目或我自己的Fork项目，这样就不会出现Base和Head都是自己或者都是源项目的情况。

#### 三、Base和Head设置完，就进入Camparing Changes页面，确认一下Base和Head，以及最新的更新内容。
![](/assets/ForkFetch5.png)
#### 内容没问题就Create PR了，绿色箭头所指向的绿色按钮；接着输入主题，Create。
![](/assets/ForkFetch6.png)

#### 四、新Create的PR在哪里可以找到呢？进入我自己的Fork项目，导航条上的PR进入，看到Open的有一个，就是刚才更新的：
![](/assets/ForkFetch7.png)
#### 点击进入确认一下。
![](/assets/ForkFetch8.png)

#### 五、把源项目的更新Merge到我的Fork项目。
![](/assets/ForkFetch9.png)
#### Confirm Merge，确定这个更新；
![](/assets/ForkFetch10.png)
#### 可以看到，这个PR已经更新完成，呈紫色的Merge状态。
![](/assets/ForkFetch11.png)

#### 六、最后验证一下是否更新到最新的项目，因为已知是更新了Pattern Recognition，所以直接进入。
![](/assets/ForkFetch12.png)
#### 查看到下面5个是最新修改的，15个小时之前修改了内容。
![](/assets/ForkFetch13.png)

### 至此整个更新Fork的方法步骤已完成，玩得愉快！
