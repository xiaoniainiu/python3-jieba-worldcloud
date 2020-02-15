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
