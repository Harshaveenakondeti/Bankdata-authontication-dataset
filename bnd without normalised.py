
# coding: utf-8

# In[2]:


import pandas as pd
data= pd.read_csv('Banknote_dataset.csv')

import numpy as np

original= data['V1']
forged= data['V2']
originalmean= np.mean(original)
forgedmean= np.mean(forged)
originalstddev= np.std(original)
forgedstddev= np.std(forged)
print(' mean')
print(originalmean, forgedmean)
print('standard deviation')
print(originalstddev, forgedstddev)


# In[3]:


from sklearn.cluster import KMeans
import numpy as np
original= data['V1']
forged= data['V2']
originalmean= np.mean(original)
forgedmean= np.mean(forged)
originalstddev= np.std(original)
forgedstddev= np.std(forged)
print(' mean')
print(originalmean, forgedmean)
print('standard deviation')
print(originalstddev, forgedstddev)


import matplotlib.pyplot as plt
original_forged= np.column_stack((original,forged))


km_res= KMeans(n_clusters=4).fit(original_forged)

clusters= km_res.cluster_centers_
plt.xlabel('original')
plt.ylabel('forged')
plt.scatter(original,forged, s=1)
plt.scatter(clusters[:,0],clusters[:,1], s=100)


# In[4]:


km_res.cluster_centers_


# In[6]:


import numpy as np
import matplotlib.pyplot as plt
original_forged = np.column_stack((original,forged))


km_res= KMeans(n_clusters=2).fit(original_forged)

clusters= km_res.cluster_centers_
plt.xlabel('original')
plt.ylabel('forged')
plt.scatter(original,forged, s=1)
plt.scatter(clusters[:,0],clusters[:,1], s=100, marker='*',c='r')
km_res.cluster_centers_


# In[11]:


import numpy as np
import matplotlib.pyplot as plt
original_forged = np.column_stack((original,forged))


km_res= KMeans(n_clusters=3).fit(original_forged)

clusters= km_res.cluster_centers_
plt.xlabel('original')
plt.ylabel('forged')
plt.scatter(original,forged, s=1)
plt.scatter(clusters[:,0],clusters[:,1], s=100)
km_res.cluster_centers_

