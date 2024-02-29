import operator as op

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

