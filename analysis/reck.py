#!/usr/bin/env python
# coding: utf-8

# In[5]:


import datetime

import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("reckless.csv")


# In[8]:


df=df.dropna()
df["Date"]=pd.to_datetime(df["Date"])
df["hour"]=df["Date"].dt.hour
df["count"]=1
results=df.groupby("hour").count()
hour_sorted=results.sort_values("count",ascending=False)
print(hour_sorted["Quantity"])


# In[9]:


df["Date"]=pd.to_datetime(df["Date"])
df["month"]=df["Date"].dt.month
payed=df[df["Status"]=="Payed"]
payed["Price"]=payed["Price"].str[3:]
payed["Price"]=pd.to_numeric(payed["Price"])
payed["Date"]=pd.to_datetime(payed["Date"])
payed["year"]=payed["Date"].dt.year
payed=payed[payed["Price"]!=0]
payed1=payed[payed["year"]==2021]
results_payed1=payed1.groupby("month").sum()


# In[10]:


print(results_payed1["Price"])


# In[11]:


clothes=payed.groupby("Product Name").sum("Quantity")
clothes_sorted=clothes["Quantity"].sort_values(ascending=False)
print(clothes_sorted)


# In[12]:


payed.head()


# In[13]:


payed=payed[payed["Order ID"].duplicated(keep=False)]
payed["grouped"]=payed.groupby("Order ID")["Product Name"].transform(lambda x:",".join(x))


# In[14]:


payed=payed[["Order ID","grouped"]].drop_duplicates()


# In[15]:


from itertools import combinations
from collections import Counter

count=Counter()
for row in payed["grouped"]:
    row_list=row.split(',')
    count.update(Counter(combinations(row_list,2)))

grouped=count.most_common(10)


# In[16]:


grouped_df=pd.DataFrame(grouped)
grouped_df


# In[ ]:




