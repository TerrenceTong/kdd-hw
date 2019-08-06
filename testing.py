import numpy as np
import pandas as pd
import train

""" df = pd.DataFrame(columns=['a','b','c'])
print(df.head())
print("-------------------------")
lst = [1,2,3]
df.loc[df.shape[0]] = lst
lst = train.softmax(lst)
#print(lst)
df.loc[df.shape[0]] = lst
lst = train.softmax(lst)
df.loc[df.shape[0]] = lst
print(df.head())
print("-------------------------")

df.insert(0,'c',df.pop('c'))
print(df.head())

df.to_csv('test.csv',index=False) """

""" a = 2413
b = 2413.00
print(a==b) """

""" df = pd.read_csv("test.csv")
formater="{0:.03f}".format
df.applymap(formater)
df.to_csv('test2.csv',index=False) """

data = pd.read_csv("preprocessed_data.csv")
result = data.dropna(axis=0, how='any')
result.to_csv("after.csv")