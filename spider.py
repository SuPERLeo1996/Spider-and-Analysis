# coding=utf-8
import re
import time
import json
from urllib import request
import pandas as pd

#伪装成浏览器的header头 
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
'Connection':'close',
'Referer':'https://www.jd.com/'
}

file = open('F:\\spiderTest\\jd_phone.txt','w')
content1 = []
def crawlProductComment(url,page):  
    req = request.Request(url, headers=headers)
    html = request.urlopen(req).read()
    html = html.decode('gbk')
    reg0 = re.compile('^fetchJSON_comment98vv22958\(')
    reg1 = re.compile('\);')
    reg2 = re.compile('&[a-zA-Z]dquo')
    reg3 = re.compile('&hellip')
    reg4 = re.compile('\r\n')
    data = reg0.sub('',html)
    data = reg1.sub('', data)
    data = reg2.sub('',data)
    data = reg3.sub('',data)
    data = reg4.sub('',data)
    data = json.loads(data)#data1的内容为一个字典，用{}括起来的内容
    for i in data['comments']:
        content = i['content']
        content = content.replace("\n", "")
        content1.append(i['content'])
        file.write(content +'\n')

for i in range(0,100):
    #商品网站 https://item.jd.com/4538887.html
    url = 'https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv22958&productId=4538887&score=0&sortType=5&page='+ str(i) +'&pageSize=10&isShadowSku=0&fold=1'
    crawlProductComment(url,i)
    time.sleep(1)
    table=pd.DataFrame({'content':content1})
    table.to_csv('f://spiderTest//jd_table_phone.csv',mode='w', encoding='utf-8',header = None)
file.close()

print("数据采集完成！")