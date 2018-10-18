# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt

catering_sale = './invest_month.xlsx'  # 餐饮数据
data = pd.read_excel(catering_sale, index_col=u'日期')  # 读取数据，指定“日期”列为索引列


plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# plt.figure()  # 建立图像
p = data.plot(kind='bar')
plt.show()
