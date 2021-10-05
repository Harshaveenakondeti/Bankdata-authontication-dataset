
# coding: utf-8

# In[10]:


import pandas as pd
data= pd.read_csv('Banknote_dataset.csv')


# In[12]:


import numpy as np
x= data['V1']
y= data['V2']
x_mean= np.mean(x)
y_mean= np.mean(y)
x_std_dev= np.std(x)
y_std_dev= np.std(y)
print('mean')
print(x_mean,y_mean)
print('standard deviation')
print( y_std_dev,y_std_dev)

import matplotlib.pyplot as plt

plt.xlabel('V1')
plt.ylabel('V2')
plt.scatter(x,y)




# In[13]:



min1= np.min(x,0)
max1= np.max(x,0)
normed1= (x-min1)/(max1-min1)
min2= np.min(y,0)
max2= np.max(y,0)
normed2= (y-min2)/(max2-min2)
plt.xlabel('V1 normalised')
plt.ylabel('V2 normalised')
plt.scatter(normed1, normed2)


# In[19]:


from sklearn.cluster import KMeans
import numpy as np


V1_V2 = np.column_stack((normed1, normed2))

km_res = KMeans(n_clusters= 3).fit(V1_V2)
clusters = km_res.cluster_centers_
plt.xlabel('V1 normalised 3 clusters')
plt.ylabel('V2 normalised 3 clusters')
plt.title('KMeans with 3 clusters')
plt.scatter(normed1,normed2)
plt.scatter(clusters[:,0],clusters[:,1],s=23)

km_res.cluster_centers_


# In[20]:



from sklearn.cluster import KMeans
import numpy as np


V1_V2 = np.column_stack((normed1, normed2))

km_res = KMeans(n_clusters= 4).fit(V1_V2)
clusters = km_res.cluster_centers_
plt.xlabel('V1 normalised 4 clusters')
plt.ylabel('V2 normalised 4 clusters')
plt.title('KMeans with 4 clusters')
plt.scatter(normed1,normed2)
plt.scatter(clusters[:,0],clusters[:,1],s=23)

km_res.cluster_centers_


# In[21]:


from sklearn.cluster import KMeans
import numpy as np


V1_V2 = np.column_stack((normed1, normed2))

km_res = KMeans(n_clusters= 2).fit(V1_V2)
clusters = km_res.cluster_centers_
plt.xlabel('V1 normalised 2 clusters')
plt.ylabel('V2 normalised 2 clusters')
plt.title('KMeans with 2 clusters')
plt.scatter(normed1,normed2)
plt.scatter(clusters[:,0],clusters[:,1],s=23)

km_res.cluster_centers_

