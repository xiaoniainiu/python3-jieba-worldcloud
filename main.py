import jieba.analyse
from wordcloud import WordCloud

import matplotlib.pyplot as plt


# 打开文本
text = open('allreimburse.txt').read()
# 中文分词
text = ' '.join(jieba.cut(text))

# 提取关键词和权重
# freq = jieba.analyse.extract_tags(text, topK=200, withWeight=True)
# print(freq[:20])
# freq = {i[0]: i[1] for i in freq}

# 生成对象
#wc = WordCloud(font_path='Hiragino.ttf', width=800, height=600, mode='RGBA', background_color=None).generate(text)
#wc = WordCloud(font_path='fangzhengsongke.ttf', width=1000, height=800, mode='RGBA', background_color=None).generate_from_frequencies(freq)
wc = WordCloud(font_path='fangzhengsongke.ttf', width=1000, height=800, mode='RGBA', background_color=None).generate(text)

# 显示词云
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.show()

# 保存到文件
wc.to_file('wordclound.png')  # 生成图像是透明的