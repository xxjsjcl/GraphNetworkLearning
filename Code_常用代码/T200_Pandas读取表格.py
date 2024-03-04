import pandas as pd

# 文件路径
filePath = r'Data\四大名著人物关系\三国演义\triples_simple.csv'

# sep=或delimiter=指定分隔符，names=指定表头的内容，header=表头在第几行，内容从表头后开始，如果不指定names，则header行为表头
df = pd.read_csv(filePath, sep=',',names=['人物1','人物2','关系1','关系2'],header=0)
print(df)
print('--------------------')
# 指定了name不指定header会把所有行当作表的内容
df = pd.read_csv(filePath, sep=',',names=['人物1','人物2','关系1','关系2'])
print(df)
print('--------------------')
# index_col=指定索引，不指定的话默认0，1，2。。。为索引
df = pd.read_csv(filePath, index_col='head')
print(df)
print('--------------------')
# usecols=指定读取特定列
df = pd.read_csv(filePath, usecols=['head','tail'])
print(df)
print('--------------------')
df = pd.read_csv(filePath, names=['人物1','人物2','关系1','关系2'],header=0,usecols=['人物1','人物2'])
print(df)
print('--------------------')

