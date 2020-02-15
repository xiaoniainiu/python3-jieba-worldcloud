# python3-jieba-worldcloud
python3-jieba-worldcloud-词云

### 在mac笔记本上安装python3
```
brew install python3
```
### pip3的安装过程
```
1.首先，进入下面链接，下载需要的Python脚本文件：
https://pip.readthedocs.io/en/stable/installing/
2.执行命令：
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
下载得到 get-pip.py文件。
3.执行 get-pip.py文件脚本：
python3 get-pip.py
备注：下载完成后，可以用 find /usr | grep get-pip.py 命令来查找下载位置
4.为在python 3的Frameworks目录下的bin目录下进行pip3在mac上建立软链：
ln -s /usr/local/Cellar/python3/3.7.3_1/Frameworks/Python.framework/Versions/3.7/bin/pip3 /usr/local/bin/
或者，设置全局变量
vim ~/.bash_profile
添加下面一行：
alias pip3=/usr/local/Cellar/python/3.7.3/Frameworks/Python.framework/Versions/3.7/bin/pip3
备注:这里的 /usr/local/Cellar/python3/3.7.3_1/Frameworks/Python.framework/Versions/3.7/bin/pip3 需要根据自己的电脑环境进行指定。
之后执行命令验证pip3正确安装:
pip3 -V
```
### 安装wordcloud
```
pip3 install WordCloud
```
### 安装 matplotlib
```
sudo pip3 install matplotlib
```
### 安装 jieba

```
sudo pip3 install jieba
```


# wordcloud.WordCloud()的参数
```
font_path : string //字体路径，需要展现什么字体就把该字体路径+后缀名写上，如：font_path = '黑体.ttf'
 
width : int (default=400) //输出的画布宽度，默认为400像素
 
height : int (default=200) //输出的画布高度，默认为200像素
 
prefer_horizontal : float (default=0.90) //词语水平方向排版出现的频率，默认 0.9 （所以词语垂直方向排版出现频率为 0.1 ）
 
mask : nd-array or None (default=None) //如果参数为空，则使用二维遮罩绘制词云。如果 mask 非空，设置的宽高值将被忽略，遮罩形状被 mask 取代。除全白（#FFFFFF）的部分将不会绘制，其余部分会用于绘制词云。如：bg_pic = imread('读取一张图片.png')，背景图片的画布一定要设置为白色（#FFFFFF），然后显示的形状为不是白色的其他颜色。可以用ps工具将自己要显示的形状复制到一个纯白色的画布上再保存，就ok了。
 
scale : float (default=1) //按照比例进行放大画布，如设置为1.5，则长和宽都是原来画布的1.5倍。
 
min_font_size : int (default=4) //显示的最小的字体大小
 
font_step : int (default=1) //字体步长，如果步长大于1，会加快运算但是可能导致结果出现较大的误差。
 
max_words : number (default=200) //要显示的词的最大个数
 
stopwords : set of strings or None //设置需要屏蔽的词，如果为空，则使用内置的STOPWORDS
 
background_color : color value (default=”black”) //背景颜色，如background_color='white',背景颜色为白色。
 
max_font_size : int or None (default=None) //显示的最大的字体大小
 
mode : string (default=”RGB”) //当参数为“RGBA”并且background_color不为空时，背景为透明。
 
relative_scaling : float (default=.5) //词频和字体大小的关联性
 
color_func : callable, default=None //生成新颜色的函数，如果为空，则使用 self.color_func
 
regexp : string or None (optional) //使用正则表达式分隔输入的文本
 
collocations : bool, default=True //是否包括两个词的搭配
 
colormap : string or matplotlib colormap, default=”viridis” //给每个单词随机分配颜色，若指定color_func，则忽略该方法。
 
fit_words(frequencies)  //根据词频生成词云
generate(text)  //根据文本生成词云
generate_from_frequencies(frequencies[, ...])   //根据词频生成词云
generate_from_text(text)    //根据文本生成词云
process_text(text)  //将长文本分词并去除屏蔽词（此处指英语，中文分词还是需要自己用别的库先行实现，使用上面的 fit_words(frequencies) ）
recolor([random_state, color_func, colormap])   //对现有输出重新着色。重新上色会比重新生成整个词云快很多。
to_array()  //转化为 numpy array
to_file(filename)   //输出到文件
```
