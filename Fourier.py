#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# In[2]:


signal=np.genfromtxt('SSignal.dat')
signalX=signal[:,0]
signalY=signal[:,1]


# In[3]:


signalS=np.genfromtxt('SSignalSuma.dat')
signalXS=signalS[:,0]
signalYS=signalS[:,1]


# In[20]:


temblor=np.genfromtxt('temblor.txt')


# In[11]:


plt.figure()
plt.subplot(2,1,1)
plt.xticks([]), plt.yticks([])
plt.title('Signal')
plt.scatter(signalX,signalY)

plt.subplot(2,1,2)
plt.title('SignalSuma')
plt.scatter(signalXS,signalYS)
plt.show()
plt.savefig('Signal_SignalSuma.pdf')
plt.close()


# In[5]:


def Transfourier(N,sig):
    fourier=[]
    k=0
    while(k<N):
        x=0
        i=0
        while(i<N):
            x+=(sig[i])*np.exp(-2j*np.pi*k*i/N)
            i+=1
        fourier.append(x)
        k+=1
    return np.array(fourier)


# In[16]:


n = len(signalY)
fourier=Transfourier(n,signalY)
timestep = signalX[1]-signalX[0]
freq = np.fft.fftfreq(n, d=timestep)


# In[17]:


plt.figure()
plt.plot(freq,fourier)
plt.xlim(-1000,1000)
plt.ylim(-150,150)
plt.xlabel('Frecuencias')
plt.ylabel('signal_transformada')
plt.title('Signal_transformada')
plt.savefig('fourier_signal.pdf')
plt.show()
plt.close()


# In[44]:


plt.figure()
plt.specgram(fourier, NFFT=256, Fs=2,noverlap=128)
plt.title('SpecgramSignal')
plt.savefig('SpecgramSignal.pdf')
plt.show()
plt.close()


# In[18]:


nS = len(signalYS)
fourierS=Transfourier(nS,signalYS)
timestepS = signalXS[1]-signalXS[0]
freqS = np.fft.fftfreq(n, d=timestepS)


# In[19]:


plt.figure()
plt.plot(freqS,fourierS)
plt.xlim(-1000,1000)
plt.ylim(-150,150)
plt.xlabel('Frecuencias')
plt.ylabel('signalSuma_transformada')
plt.title('SignalSuma_transformada')
plt.savefig('fourier_signalSuma.pdf')
plt.show()
plt.close()


# In[39]:


plt.figure()
plt.specgram(fourierS, NFFT=256, Fs=2,noverlap=128)
plt.title('SpecgramSignalSuma')
plt.show()
plt.savefig('SpecgramSignalSuma.pdf')
plt.close()


# In[21]:


x=np.linspace(0,len(temblor),len(temblor))


# In[23]:


plt.figure()
plt.plot(x,temblor)
plt.title('Temblor')
plt.savefig('Temblor.pdf')
plt.show()
plt.savefig('Temblor.pdf')
plt.close()


# In[ ]:




