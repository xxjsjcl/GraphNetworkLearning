import operator as op

## itergetter对非数值对象排序
print('----------使用operator.itemgetter()方法指定key值----------')
a=[('john', 'A', 15), ('pan', 'B', 5), ('dave', 'C', 10),('john', 'B', 10)]
print('----------原列表----------')
print(a)
print('----------按照a中元素的下标0排序----------')
print(sorted(a, key=op.itemgetter(0)) ) # 按照a中元素的下标0排序
print('----------按照a中元素的下标0排序，从大到小----------')
print(sorted(a, key=op.itemgetter(0), reverse=True)) # 按照a中元素的下标0排序，从大到小
print('----------按照a中元素的下标0，2排序，先排0，后排2----------')
print(sorted(a, key=op.itemgetter(0,2))) 
print('----------按照a中元素的下标0，1排序，先排0，后排2，倒序----------')
print(sorted(a, key=op.itemgetter(0,2), reverse=True)) 

## lamda函数排序
print("----------也可以使用lamda函数指定key值进行排序----------")
print('----------按照a中元素的下标0排序----------')
print(sorted(a, key=lambda x:x[0])) # 按照a中元素的下标0排序

## 根据列表长度排序
a=['a', 'ac', 'fed','xyzw', 'oprs']
print('----------原列表----------')
print(a)
print('----------按照a中元素的长度排序----------')
print(sorted(a, key=lambda x:len(x), reverse=True)) # 按照a中元素长度排序
print(sorted(a, key=len, reverse=True)) # 按照a中元素长度排序

## 对字典排序
a={'a':[1,4], 'ac':[2,5,8], 'fed':[0],'xyzw':[3,7], 'oprs':[2,6,8,1]}
print('----------原字典----------')
print(a)
print('----------用dict.items()读取字典中的项目，每个项目作为一个元组，成为列表中的元素，排序后生成一个列表----------')
print('----------按照字典的value中的长度排序----------')
print(sorted(a.items(), key=lambda x:len(x[1]), reverse=True))