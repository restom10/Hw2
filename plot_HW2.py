#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


u1 = np.genfromtxt('U1.txt',delimiter=';')
u2 = np.genfromtxt('U2.txt',delimiter=';')
u3 = np.genfromtxt('U3.txt',delimiter=';')


# In[2]:


w1=u1[:,0]
max1=u1[:,1]
w2=u2[:,0]
max2=u2[:,1]
w3=u3[:,0]
max3=u3[:,1]


# In[3]:


plt.figure()
plt.xlim(2.5,4)
plt.title('Edificios')
plt.plot(w1,max1,label='Edificio 1')
plt.plot(w2,max2,label='Edificio 2')
plt.plot(w3,max3,label='Edificio 3')
plt.legend()
plt.show()
plt.savefig('Graficas de edificios')
plt.close()


# In[ ]:




