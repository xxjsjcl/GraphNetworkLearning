import pandas as pd
import numpy as np
import seaborn as sns       # 封装了matplotlib的可视化包：https://seaborn.pydata.org/examples/index.html
import matplotlib as mpl
import matplotlib.pyplot as plt
## 配置windows 显示中文
plt.rcParams['font.sans-serif']=['SimHei'] # 用来显示中文标签
plt.rcParams['axes.unicode_minus']=False  # 用来正常显示正负号

def SeabornSample1():
    print('----------sample1----------')
    sns.set_theme(style="ticks")
    # Load the example dataset for Anscombe's quartet
    df = sns.load_dataset("anscombe", data_home=r'Data\seaborn-data',cache=True)
    # Show the results of a linear regression within each dataset
    sns.lmplot(
        data=df, x="x", y="y", col="dataset", hue="dataset",
        col_wrap=2, palette="muted", ci=None,
        height=4, scatter_kws={"s": 50, "alpha": 1}
    )

def SeabornSample2():
    print('----------sample2----------')
    sns.set_theme(style="dark")
    # Simulate data from a bivariate Gaussian
    n = 10000
    mean = [0, 0]
    cov = [(2, .4), (.4, .2)]
    rng = np.random.RandomState(0)
    x, y = rng.multivariate_normal(mean, cov, n).T  

    # Draw a combo histogram and scatterplot with density contours
    f, ax = plt.subplots(figsize=(6, 6))
    sns.scatterplot(x=x, y=y, s=5, color=".15")
    sns.histplot(x=x, y=y, bins=50, pthresh=.1, cmap="mako")
    sns.kdeplot(x=x, y=y, levels=5, color="w", linewidths=1)
    

if __name__ == "__main__":
    print('1')
    SeabornSample1()
    SeabornSample2()
    plt.show()