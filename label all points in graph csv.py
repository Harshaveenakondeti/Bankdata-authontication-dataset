
# coding: utf-8

# In[3]:


import pandas as pd
data= pd.read_csv('happyscore_income.csv')


# In[4]:


import pandas as pd
data= pd.read_csv('happyscore_income.csv')


# In[23]:


data.sort_values('avg_income', inplace=True)
richest= data[data['avg_income']>15000]

plt.scatter(richest['avg_income'], richest['happyScore'])

for k, row in richest.iterrows():
    plt.text(row['avg_income'], row['happyScore'], row['country'])
    # print(row['country'])

