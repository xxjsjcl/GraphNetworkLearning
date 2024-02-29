# 可以通过注释变量类型告诉编译器改提示什么样的代码

# 变量注释的格式是  # type:变量类型
# 例子1
a = [10,20,30]
b = {'aa':50,'bb':60,'cc':70}
# 默认情况下，python会将a处理成一个list，b当成一个字典处理
print(type(a))
print(type(b))
# 在编辑器输入'a.'后，会提示list类型变量的函数，输入'b.'后会提示dict类型的函数
# a.
# b.

# 如果注释了变量的格式
c = [10,20,30]      # type:dict
d = {'aa':50,'bb':60,'cc':70}   # type:list

# 这里把list类型的c注释成了dict类型，dict类型的d注释成了list类型
# 在编辑器输入'c.'后，会提示dict类型变量的函数，输入'd.'后会提示list类型的函数
# c.
# d.

# 但是这之影响代码提示，不会影响代码本身
print(type(c))
print(type(d))