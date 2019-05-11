#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import matplotlib.pyplot as plt


# In[19]:


signal=np.genfromtxt('SSignal.dat')
signalX=signal[:,0]
signalY=signal[:,1]


# In[24]:


signalS=np.genfromtxt('SSignalSuma.dat')
signalXS=signalS[:,0]
signalYS=signalS[:,1]


# In[31]:


plt.figure()
plt.subplot(2,1,1)
plt.xticks([]), plt.yticks([])
plt.title('Signal')
plt.scatter(signalX,signalY)

plt.subplot(2,1,2)
plt.title('SignalSuma')
plt.xticks([]), plt.yticks([])
plt.scatter(signalXS,signalYS)
plt.show()
plt.savefig('Signal_SignalSuma.pdf')
plt.close()


# In[ ]:




