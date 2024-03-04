import itertools

# 无限迭代器（Infinite Iterators）
print("---------------Infinite Iterators-----------------------")
## 这些函数可以生成无限的迭代器，我们主要学习以下三个函数的用法。

### (1)count函数：count([start=0, step=1]) 接收两个可选整形参数，第一个指定了迭代开始的值，第二个指定了迭代的步长。
print("---------------count函数-----------------------")
for i in itertools.count(10,2):
    print(i)
    if i>20: 
        break

### (2)cycle函数：cycle(iterable) 是用一个可迭代对象中的元素来创建一个迭代器，并且复制自己的值，一直无限的重复下去。
print("---------------cycle函数-----------------------")
aa = 0
for i in itertools.cycle("abcd"):
    print(i)     # 具有无限的输出，可以按ctrl+c来停止。
    aa = aa+1
    if aa > 10:
        break



### (3)repeat函数：repeat(elem [,n])是将一个元素重复n遍或者无穷多遍，并返回一个迭代器。
print("---------------repeat函数-----------------------")
for i in itertools.repeat("abcd",6):
    print(i)


# 组合迭代器（Combinatoric Iterators）
print("---------------Combinatoric Iterators-----------------------")
## 组合操作包括排列，笛卡儿积，或者一些离散元素的选择，组合迭代器就是产生这样序列的迭代器。我们来看看这几个函数的用法。
### (1)product函数：product(*iterables, repeat=1) 得到的是可迭代对象的笛卡儿积，*iterables参数表示需要多个可迭代对象。
### 这些可迭代对象之间的笛卡儿积，也可以使用for循环来实现，例如 product(A, B) 与 ((x,y) for x in A for y in B)就实现一样的功能。
print("---------------product函数-----------------------")
for i in itertools.product([1,2,3],[4,5,6]):
    print(i)
print("---------------product函数repeat,把笛卡尔乘积的结果再乘一次-----------------------")
for i in itertools.product([1,2,3],[4,5,6],repeat = 2):
    print(i)

### (2)permutations函数：permutations(iterable,r=None)返回的是可迭代元素中的一个排列组合，并且是按顺序返回的，且不包含重复的结果。
print("---------------permutations排列-----------------------")
for i in itertools.permutations('abc'):
    print(i)
print("---------------permutations组合和排列-----------------------")
for i in itertools.permutations('abc', 2):
    print(i)

### (3)combinations函数：combinations(iterable,r) 返回的是可迭代对象所有的长度为 r 的子序列，
### 注意这与前一个函数 permutation 不同，permutation 返回的是排列，而 combinations 返回的是组合。
print("---------------combinations组合-----------------------")
for i in itertools.combinations('abcd',2):
    print(i)
print("---------------combinations组合-----------------------")
for i in itertools.combinations('abcd', 3):
    print(i)

### (4)combinations_with_replacement函数：combinations_with_replacement(iterable, r) 返回一个可与自身重复的元素组合。
print("---------------combinations_with_replacement组合-----------------------")
for i in itertools.combinations_with_replacement('abcd',2):
    print(i)


# 有限迭代器（Iterators Terminating on the Shortest Input Sequence）
print("---------------Iterators Terminating on the Shortest Input Sequence-----------------------")
## 这里的函数有十来个，主要为大家介绍其中几个常用的函数。
## accumulate, chain, chain.from_iterable
## compress, dropwhile, filterfalse
## groupby, islice, starmap, takewhile
## tee, zip_longest


### (1)chain函数：chain(*iterables) 可以把多个可迭代对象组合起来，形成一个更大的迭代器。
print("---------------chain函数-----------------------")
for i in itertools.chain('good','bye'):
    print(i)

### (2)groupby函数：groupby(iterable,key=None) 可以把 '相邻' 元素按照 key 函数分组，
### 并返回相应的 key 和 groupby，如果key函数为 None，则只有相同的元素才能放在一组。
print("---------------groupby函数-----------------------")
for key, group in itertools.groupby('AaaBBbcCAAa', key=lambda c: c.upper()):
    print(list(group))

for key, group in itertools.groupby([[1,2,3],[2,2,3],[3,1,4],[3,2,4],[5,1,3],[6,1,3]], key=lambda x:x[1]):
    print(list(group))

### (3)accumulate函数：accumulate(iterable [,func]) 可以计算出一个迭代器，
### 这个迭代器是由特定的二元函数的累计结果生成的，如果不指定的话，默认函数为求和函数。
print("---------------accumulate函数,累积叠加-----------------------")
for i in itertools.accumulate([0,1,0,1,1,2,3,5]):
    print(i)
print("---------------accumulate函数,最大值-----------------------")
for i in itertools.accumulate([2,1,4,3,5],max):
    print(i)