# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 10:14:05 2018

@author: Leo
"""
#导入科学计算库(拼表及各种分析汇总)
import pandas as pd
#导入结巴分词(关键词提取)
import jieba.analyse
#导入SnowNLP
from snownlp import SnowNLP


data = pd.read_csv('f://spiderTest//jd_table_phone.csv',header = None) #导入评论数据
l1 = len(data) #去重前评论的条数
data = pd.DataFrame(data[1].unique()) #去重
l2 = len(data) #去重后评论的条数
print(u'删除了%s条评论。' %(l1 - l2))
data.to_csv('f://spiderTest//jd_table_phone_cleansame.csv', index = False, header = None, encoding = 'utf-8')

#文本数据格式转换
word_str = ''.join(data[0])
#提取文字关键词
word_rank=jieba.analyse.extract_tags(word_str, topK=20, withWeight=True, allowPOS=())
#转化为数据表
word_rank = pd.DataFrame(word_rank,columns=['word','rank'])

print(word_rank)



sentences = data[0]

senti_score = []

for i in range(len(sentences)):
   a1 = SnowNLP(sentences[i])
   a2 = a1.sentiments
   senti_score.append(a2)

content = pd.DataFrame({'sentences':sentences,'senti_score':senti_score})
negative_content= content[content.senti_score<0.4]
negative_content.to_csv('f://spiderTest//jd_table_phone_neg.csv',mode='w', encoding='utf-8',header = None)
postive_content = content[content.senti_score>=0.4]
postive_content.to_csv('f://spiderTest//jd_table_phone_pos.csv',mode='w', encoding='utf-8',header = None)
print(content)