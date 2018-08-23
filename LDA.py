# -*- coding: utf-8 -*-
import pandas as pd
from gensim import corpora, models


#参数初始化
negfile = 'f://spiderTest//jd_table_phone_neg_cut.txt'
posfile = 'f://spiderTest//jd_table_phone_pos_cut.txt'
stoplist = 'f://spiderTest//stoplist.txt'

neg = pd.read_csv(negfile, encoding = 'utf-8', header = None) #读入数据
pos = pd.read_csv(posfile, encoding = 'utf-8', header = None)
stop = pd.read_csv(stoplist,encoding='utf-8',header = None, sep = 'tipdm',engine='python')  
#sep设置分割词，由于csv默认以半角逗号为分割词，而该词恰好在停用词表中，因此会导致读取出错
#所以解决办法是手动设置一个不存在的分割词，如tipdm。
stop = [' ', ''] + list(stop[0]) #Pandas自动过滤了空格符，这里手动添加
#stopwords = [line.strip() for line in open(stoplist, 'r').readlines()]  
#print stop

#下面这段代码可以分为两小段，这两小段代码几乎一致，前面一个是针对负面评论，后一个是针对正面评论，所以只详解其中一个
neg[1] = neg[0].apply(lambda s: s.split(' ')) #定义一个分割函数，然后用apply广播  
neg[2] = neg[1].apply(lambda x: [i for i in x if i not in stop]) #逐词判断是否停用词，思路同上
#上面这句代码的语法是：列表推导式子。意思是说，如果i不在停用词列表(stop)中，就保留该词语（也就是最前面的一个i），否则就进行删除  
#上面的这句代码中，把for i in x看做整体，把if i not in stop看做判断语句，把最前面的i看做满足if语句之后的执行语句即可。  
pos[1] = pos[0].apply(lambda s: s.split(' '))  
pos[2] = pos[1].apply(lambda x: [i for i in x if i not in stop])  

def LdaAnalysis(list):
    lda_dict = corpora.Dictionary(list)#建立词典
    lda_corpus = [lda_dict.doc2bow(i) for i in list]#建立语料库
    lda = models.LdaModel(lda_corpus, num_topics = 3, id2word = lda_dict)#LDA模型训练
    for i in range(3):
      print(lda.print_topic(i)) #输出每个主题
print("负面主题分析")
LdaAnalysis(neg[2])
print("正面主题分析")
LdaAnalysis(pos[2])
#上面的lamda s和lamda x中的s和x都是表示入口参数，apply的意思是，把apply前面的字符串当做入口参数，输入到appy后面所定义的函数中  
#负面主题分析
#neg_dict = corpora.Dictionary(neg[2]) #建立词典
#neg_corpus = [neg_dict.doc2bow(i) for i in neg[2]] #建立语料库
#neg_lda = models.LdaModel(neg_corpus, num_topics = 3, id2word = neg_dict) #LDA模型训练
#print(neg_lda.print_topic(0))
#print(neg_lda.print_topic(1))
#print(neg_lda.print_topic(2))

#for i in range(0,3):
#   #输出每个主题

#正面主题分析
#pos_dict = corpora.Dictionary(pos[2])
#pos_corpus = [pos_dict.doc2bow(i) for i in pos[2]]
#pos_lda = models.LdaModel(pos_corpus, num_topics = 3, id2word = pos_dict)
#for i in range(3):
#  print(pos_lda.print_topic(i)) #输出每个主题

