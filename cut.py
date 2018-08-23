#-*- coding: utf-8 -*-
import pandas as pd
import jieba #导入结巴分词，需要自行下载安装

#参数初始化
inputfile1 = 'f://spiderTest//jd_table_phone_pos.csv'
inputfile2 = 'f://spiderTest//jd_table_phone_neg.csv'
outputfile1 = 'f://spiderTest//jd_table_phone_pos_cut.txt'
outputfile2 = 'f://spiderTest//jd_table_phone_neg_cut.txt'

data1 = pd.read_csv(inputfile1, encoding = 'utf-8', header = None) #读入数据
data2 = pd.read_csv(inputfile2, encoding = 'utf-8', header = None)


mycut = lambda s: ' '.join(jieba.cut(s)) #自定义简单分词函数
data1 = data1[1].apply(mycut) #通过“广播”形式分词，加快速度。
data2 = data2[1].apply(mycut)

data1.to_csv(outputfile1, index = False, header = False, encoding = 'utf-8') #保存结果
data2.to_csv(outputfile2, index = False, header = False, encoding = 'utf-8')
