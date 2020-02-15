from wordcloud import WordCloud
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import jieba

# 打开文本
text = open('allreimburse.txt').read()

# 中文分词
text = ' '.join(jieba.cut(text))

# 生成对象
mask = np.array(Image.open("demo_mask.png"))
wc = WordCloud(mask=mask, font_path='fangzhengsongke.ttf', mode='RGBA', background_color=None).generate(text)

# 显示词云
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.show()

# 保存到文件

wc.to_file('wordcloud1.png')