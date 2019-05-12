#!/usr/bin/env python
# coding: utf-8

# In[27]:


import numpy as np
import matplotlib.pyplot as plt

u1 = np.genfromtxt('U1.txt',delimiter=';')
u2 = np.genfromtxt('U2.txt',delimiter=';')
u3 = np.genfromtxt('U3.txt',delimiter=';')
u1B = np.genfromtxt('U1BONO.txt',delimiter=';')
u2B= np.genfromtxt('U2BONO.txt',delimiter=';')
u3B= np.genfromtxt('U3BONO.txt',delimiter=';')


# In[28]:


w1=u1[:,0]
max1=u1[:,1]
w2=u2[:,0]
max2=u2[:,1]
w3=u3[:,0]
max3=u3[:,1]

w1B=u1B[:,0]
max1B=u1B[:,1]
w2B=u2B[:,0]
max2B=u2B[:,1]
w3B=u3B[:,0]
max3B=u3B[:,1]


# In[31]:


plt.figure()
plt.xlim(2.5,3.05)
plt.title('Edificios')
plt.ylabel('Amplitud')
plt.xlabel('Amplitud')
plt.plot(w1,max1,label='Edificio 1')
plt.plot(w2,max2,label='Edificio 2')
plt.plot(w3,max3,label='Edificio 3')
plt.plot(w1B,max1B,label='Edificio 1 con 5% menos masa')
plt.plot(w2B,max2B,label='Edificio 2 con 5% menos masa')
plt.plot(w3B,max3B,label='Edificio 3 con 5% menos masa')
plt.legend()
plt.savefig('Graficas de edificios.pdf')
plt.close()

print('Se observa entonces que con la leve reduccion de masa los edificios tienden a tener amplitudes maximas de oscilacion un poco mayores para las mismas frecuencias, siendo asi mas inseguros y propensos a caer')


# In[ ]:




