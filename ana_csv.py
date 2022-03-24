import codecs
import csv
import re
import pandas as pd
import xml.dom.minidom
#在内存中创建一个空的文档
doc=xml.dom.minidom.Document()
#创建一个根节点companys对象
root=doc.createElement('tdb')
print('添加的xml标签为：',root.tagName)
#将根节点添加到文档对象中
doc.appendChild(root)
data = pd.read_csv(r'大型科学计算与仿真引擎数据.csv',sep=',',header=None,usecols=[0,2],encoding='GB18030')
list1=[]
list1=data.values[0::,0::]
# for i in range(0,len(list1)):
for i in range(0,1000):
    # 解析第一个字段
    ls=list1[i][0].replace('$','')
    ls=ls.strip('*_')
    list1[i][0]=ls
    #解析第二个字段
    if (list1[i][1][:3] == 'REA'):
        list1[i][1] = '9'
    elif (list1[i][1][:3] == 'DOU'):
        list1[i][1] = '2'
    elif (list1[i][1][:3] == 'INT'):
        list1[i][1] = '0'
    elif (list1[i][1][:3] == 'byt'):
        list1[i][1] = '0'
    else:
        list1[i][1]='5'
    # 给根节点添加一个叶子节点
    tdb = doc.createElement('variable')
    tdb.setAttribute('byte', '30')
    tdb.setAttribute('dimension', '0')
    tdb.setAttribute('idxvalue', '0')
    tdb.setAttribute('idxvar', '0')
    tdb.setAttribute('limits', '0')
    tdb.setAttribute('name', list1[i][0])
    tdb.setAttribute('remark', '')
    tdb.setAttribute('size', '0')
    tdb.setAttribute('type', list1[i][1])

    # 叶子节点下再嵌套叶子节点
    values = doc.createElement('values')
    values.setAttribute('current', '0')
    # 将各叶子节点添加到父节点company中
    tdb.appendChild(values)
    # 将company节点添加到根节点companys中
    root.appendChild(tdb)

    # 此处需要用codecs.open可以指定编码方式
    fp = open(r'var_demo.xml', 'w', encoding='utf-8')
    # 将内存中的xml写入到文件
    doc.writexml(fp, indent='', addindent='\t', newl='\n', encoding='utf-8')
fp.close()


# file=codecs.open('result.csv','w',encoding='utf-8')
# writer = csv.writer(file, delimiter=' ', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
# for item in list1:
#     writer.writerow(item)
# file.close()
# print("保存文件成功，处理结束")


