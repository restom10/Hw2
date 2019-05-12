#!/usr/bin/env python
# coding: utf-8

# In[51]:


import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, fftfreq


# In[52]:


signal=np.genfromtxt('SSignal.dat')
signalX=signal[:,0]
signalY=signal[:,1]


# In[53]:


signalS=np.genfromtxt('SSignalSuma.dat')
signalXS=signalS[:,0]
signalYS=signalS[:,1]


# In[54]:


temblor=np.genfromtxt('temblor.txt')


# In[89]:


plt.figure()
plt.subplot(2,1,1)
plt.xticks([]), plt.yticks([])
plt.title('Signal')
plt.plot(signalX,signalY)

plt.subplot(2,1,2)
plt.title('SignalSuma')
plt.plot(signalXS,signalYS)
plt.savefig('Signal_SignalSuma.pdf')
plt.close()


# In[57]:


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


# In[72]:


n = len(signalY)
fourier=Transfourier(n,signalY)
timestep = signalX[1]-signalX[0]
freq = np.fft.fftfreq(n, d=timestep)


# In[82]:


plt.figure()
plt.plot(freq,fourier)
plt.xlim(-1000,1000)
plt.ylim(-150,150)
plt.xlabel('Frecuencias')
plt.ylabel('signal_transformada')
plt.title('Signal_transformada')
plt.savefig('fourier_signal.pdf')
plt.close()


# In[83]:


plt.figure()
plt.specgram(fourier, NFFT=256, Fs=2,noverlap=128)
plt.title('SpecgramSignal')
plt.savefig('SpecgramSignal.pdf')
plt.close()


# In[62]:


nS = len(signalYS)
fourierS=Transfourier(nS,signalYS)
timestepS = signalXS[1]-signalXS[0]
freqS = np.fft.fftfreq(nS, d=timestepS)


# In[84]:


plt.figure()
plt.plot(freqS,fourierS)
plt.xlim(-1000,1000)
plt.ylim(-150,150)
plt.xlabel('Frecuencias')
plt.ylabel('signalSuma_transformada')
plt.title('SignalSuma_transformada')
plt.savefig('fourier_signalSuma.pdf')
plt.close()


# In[85]:


plt.figure()
plt.specgram(fourierS, NFFT=256, Fs=2,noverlap=128)
plt.title('SpecgramSignalSuma')
plt.savefig('SpecgramSignalSuma.pdf')
plt.close()


# In[65]:


x=np.linspace(0,len(temblor),len(temblor))


# In[86]:


plt.figure()
plt.plot(x,temblor)
plt.title('Temblor')
plt.savefig('Temblor.pdf')
plt.savefig('Temblor.pdf')
plt.close()


# In[67]:


Y = fft(temblor)
timestep=x[1]-x[0]
frq = np.fft.fftfreq(len(temblor), d=timestep)


# In[87]:


plt.figure()
plt.plot(frq,Y)
plt.title('Temblor con transformada')
plt.savefig('TemblorFourier.pdf')
plt.close()


# In[88]:


plt.figure()
plt.specgram(Y, NFFT=512, Fs=2,noverlap=128)
plt.title('SpecgramTemblor')
plt.savefig('SpecgramTemblor.pdf')
plt.close()


# In[ ]:




