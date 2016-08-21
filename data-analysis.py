
# coding: utf-8

# In[1]:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[3]:

open.('data.csv').read()


# In[4]:

df = pd.read_csv('data.csv')


# In[ ]:




# In[5]:

df


# In[14]:

df.loc[(df['altitude']> '30000') & (df['speed']>'500'), ['altitude','speed']]


# In[28]:

df.loc[(df['hexcode']=='8006fc'), ['hexcode','altitude','speed']]


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[19]:

pv=df.pivot_table(values=[""], index=["hexcode","speed"], aggfunc=np.mean)


# In[20]:

sort = df.sort_values(['altitude','speed'], ascending=False)


# In[23]:

sort[['hexcode','altitude','speed']]


# In[32]:

total_rows = df.count



# In[33]:

total_rows


# In[35]:

dup = df.duplicated('hexcode')


# In[ ]:




# In[36]:

for i in dup:
    if(i==False):


# In[40]:

count=1
for i in dup:
    if(i==False):
        count=count+1
print(count)


# In[46]:

list = []
for i in df['mode']:
    list.append(i)


# In[49]:

count = 1
for i in list:
    if(i!='S'):
        count=count+1


# In[50]:

count


# In[161]:

u = df.hexcode.unique()
u


# In[ ]:




# In[160]:

for i in df['flight']:
    


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[53]:

u


# In[67]:




# In[68]:

count


# In[ ]:




# In[ ]:




# In[66]:

count


# In[ ]:




# In[ ]:




# In[ ]:




# In[55]:

i


# In[61]:

i[0:3]=='800'


# In[ ]:




# In[60]:

i[0:3]


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:

i


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:

lo


# In[44]:

list


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[78]:

from numpy.random import normal
gaussian_numbers = 10


# In[79]:

import matplotlib.pyplot as plt
from numpy.random import normal


# In[ ]:

gaussian_numbers = normal(size=1000)
plt.hist(gaussian_numbers)
plt.title("Gaussian Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()


# In[70]:

import matplotlib.pyplot as plt
from numpy.random import normal


# In[71]:

gaussian_numbers = normal(size=1000)
plt.hist(gaussian_numbers)
plt.title("Gaussian Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()


# In[72]:

plt.figure();


# In[73]:

df.ix[5].plot.bar(); plt.axhline(0, color='k')


# In[74]:

ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))


# In[75]:

ts = ts.cumsum()


# In[76]:

ts.plot()


# In[77]:

plt.figure()


# In[80]:

plt.show()


# In[82]:

gaussian_numbers = 29
plt.hist(gaussian_numbers)
plt.title("Gaussian Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()


# In[89]:

from numpy.random import normal
gaussian_numbers = 2


# In[ ]:




# In[ ]:




# In[ ]:




# In[93]:

import matplotlib.pyplot as plt
from numpy.random import normal
gaussian_numbers = 2
plt.hist(gaussian_numbers)
plt.title("Gaussian Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[94]:




# In[99]:

df4 = pd.DataFrame({'National': np.random.randn(1000) + 1,
'International': np.random.randn(1000) - 1}, columns=['a', 'b', 'c'])


# In[ ]:




# In[96]:

plt.figure();


# In[97]:

df4.plot.hist(alpha=0.5)


# In[98]:

plt.show()


# In[107]:

df4 = pd.DataFrame({'National': '29', 'International': '39' }, columns=['National', 'International'])

plt.figure();
df4.plot.hist(alpha=0.5)


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[103]:

plt.show()


# In[ ]:




# In[101]:

plt.show()


# In[108]:

import matplotlib.pyplot as plt


# In[109]:

plt.hist([1, 2, 1], bins=[0, 1, 2])


# In[110]:

plt.show()


# In[112]:

plt.bar(range(0,100), 11)
plt.show()


# In[ ]:




# In[113]:

df = pd.read_csv('planesvsflight.csv')


# In[114]:

df


# In[116]:

list = []
for i in df:
    list.append(i)


# In[117]:

list


# In[119]:

u = df.planes.unique()


# In[139]:

list = []
for i in u:
    list.append(i)


# In[150]:

len(list)


# In[152]:

count= 0
for i in range(1,len(list)):
    print(i)
    count=count+1


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[125]:

list = []
for i in u:
    print('-------')
    list.append(i)


# In[127]:

list[0]


# In[135]:

for i in list:
    print(i)


# In[137]:

type(list[0])


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[170]:

df = pd.read_csv('data.csv')


# In[ ]:




# In[155]:

df['flight']


# In[171]:

u = df.hexcode.unique()


# In[172]:

u


# In[ ]:




# In[165]:

u = df.hexcode.unique()
for i in plane:
    if(i[0:3]!='800'):
       print(i)


# In[167]:

u[0]


# In[168]:

i


# In[169]:

i[0:3]


# In[176]:

u = df.flight.unique()


# In[177]:

u


# In[ ]:




# In[179]:

list1 = []
for i in u:
        list1.append(i[0:3])
       


# In[180]:

list1


# In[182]:

from collections import Counter
Counter(list1)


# In[183]:

list1


# In[ ]:



