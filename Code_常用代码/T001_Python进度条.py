import time
from tqdm import tqdm

# 需要执行的函数
def action():

    time.sleep(0.5)

# tqdm进度条例子
'''
total总进度数
desc进度条的名字
leave程序结束后是否保留进度条
ncols进度条长度
unit进度单位
unit_scale是否自动单位的换算，如100000会写为100k
'''
with tqdm(total=100000, desc='Example', leave=True, ncols=100, unit='B', unit_scale=True) as pbar:
    for i in range(10):
        # 执行动作
        action()
        # 更新进度，里面的参数是每次更新多少进度
        pbar.update(10000)