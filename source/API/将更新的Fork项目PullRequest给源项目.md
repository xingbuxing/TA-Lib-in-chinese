## 将更新的Fork项目PullRequest给源项目

### 我们Fork项目之后进行了修改或添加新文件，需要Pull Request（简称：PR）给源项目，让作者Merge融入到他的源项目里；我做了一个教程，步骤如下：

### 在PR之前，甚至开始修改或创建新文件之前，先看看源项目是否有更新，如有更新，可按上个教程[《在GitHub上更新Fork的方法》](https://github.com/bitbyte27/SoftwareTutorials/blob/master/Git/%E5%9C%A8GitHub%E4%B8%8A%E6%9B%B4%E6%96%B0Fork%E7%9A%84%E6%96%B9%E6%B3%95.md)先更新自己的Fork项目，再做创建新文件，老司机说这样冲突比较少。

#### 一、看到别人的好项目，如何“据为己有”？Fork一下咯！
![](/assets/fork1.png)
#### 点击Fork，会进入Fork进行中的界面；
![](/assets/fork2.jpg)
#### Fork完成后，可以在自己的主页（Your Profile）看到Fork的项目。
![](/assets/fork3.png)

#### 二、可以通过Create new file或upload file新建或上传文件，要注意的是：上传的文件会把原来同名文件覆盖掉！
![](/assets/fork4.png)
#### 这里的会有文件上传的进度条，如下图：共13个文件，已上传9个；上传完成的文件会在下方显示。
![](/assets/fork5.png)
#### 这个上传文件由于服务器在国外的缘故，死慢死慢，经常就废了，如下图。
![](/assets/fork6.png)
#### 当看到下面这个Processing your files…页面，那就恭喜你了，经过几十次的上传，总算work了；如果出现一片空白的页面，那么只好重复choose your files，再次Confirm Changes。
![](/assets/fork7.png)

#### 三、新建PR：可以在Fork项目的根目录下，或者任意的目录下，Pull Request。
![](/assets/PR1.png)
![](/assets/PR2.png)
#### Pull Request后会进入Comparing changes页面，核对一下Base Fork和Head Fork（蓝色圆圈）、以及更新的内容（紫色方框）；由于已经更新过最新的源项目内容，与源项目同步好了，所以此时显示“Able to merge”（红圈绿字）；一切就绪，点击Create创建PR。
![](/assets/PR3.png)
#### 输入主题，并Create PR；
![](/assets/PR4.png)
#### 这时可以看到已经将这个更新PR给源项目作者，PR序号为#52，状态open。
![](/assets/PR5.png)

#### 四、源项目作者Merge此PR，将此次的更改融入到源项目，并形成Commits记录。
#### 进入Pull Request，查看序号#52的PR：
![](/assets/PR6.png)
#### 序号#52的PR已经Merge：
![](/assets/PR7.png)
#### 进入源项目，查看Commit记录：
![](/assets/PR8.png)
![](/assets/PR9.png)

### 至此，整个Fork、修改或创建文件、Pull Request以及Merge的步骤已完成，玩的愉快！
