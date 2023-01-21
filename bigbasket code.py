# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 14:37:55 2022

@author: forev
"""

import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

from importlib import reload
plt=reload(plt)
import sklearn

df=pd.read_csv('BigBasket Products.csv')
df1=df.dropna()
#print(df['category'])
#print(df1.isnull().any())
net_profit=df1['market_price']-df1['sale_price']
df1['net_profit']=net_profit
df2=df1.drop(['sale_price','market_price'],axis=1)




df3=df2.loc[df2['rating']<=4.5]


df4=df3.groupby('category',as_index=False)['net_profit'].mean().nlargest(10,columns='net_profit')
df7 = df4[:5].copy()



#others
new_row = pd.DataFrame(data = {
    'category' : ['others'],
    'net_profit' : [df4['net_profit'][5:].sum()]
})

#combining top 5 with others
df8 = pd.concat([df7, new_row])



ax=df8.plot(kind='pie',y='net_profit',title='Net Profit(by category[average rating])',labels=df8['category'],legend=False,autopct='%1.1f%%')
ax.set_ylabel('')
#print(df2)

df5=df2.loc[df2['rating']>=4.5]


df6=df5.groupby('category',as_index=False)['net_profit'].mean().nlargest(10,columns='net_profit')
df7 = df6[:5].copy()



#others
new_row = pd.DataFrame(data = {
    'category' : ['others'],
    'net_profit' : [df6['net_profit'][5:].sum()]
})

#combining top 5 with others
df8 = pd.concat([df7, new_row])

ax1=df8.plot(kind='pie',title='Net Profit(by category[high rated])',labels=df8['category'],y='net_profit',legend=False,autopct='%1.1f%%')
ax1.set_ylabel('')






df9=df2.groupby('sub_category',as_index=False)['net_profit'].mean().nlargest(10,columns='net_profit')
#print(df7)
df10 = df9[:7].copy()



#others
new_row1 = pd.DataFrame(data = {
    'sub_category' : ['others'],
    'net_profit' : [df9['net_profit'][7:].sum()]
})

#combining top 5 with others
df11 = pd.concat([df10, new_row1])


ax2=df11.plot(kind='pie',y='net_profit',shadow=True,title='Net Profit (by sub category)',labels = df11['sub_category'],legend=False,autopct='%1.1f%%')
ax2.set_ylabel('')




plt.show()
