import sys
import numpy as np
import matplotlib.pyplot as plt
from pylab import *
from scipy.interpolate import interp1d

x1shift = - 0.91
x2shift = - 0.44

ip1 = 291.7656 #Pbs C1
ip2 = 291.4435 #Dbs C1
ip3 = 294.31 #Pbs C2
ip4 = 293.99 #Dbs C2

ip5CH2 = 291.10
ip5CHF = 293.48

data1 = np.genfromtxt('CH2CHF_ee_Pbs.lor')
x1 = data1[:,0] 
y1 = (data1[:,1])
data1 = np.genfromtxt('CH2CHF_ee_Pbs.txt')
stcksx1 = data1[:,0] 
stcksy1 = (data1[:,1])

data2 = np.genfromtxt('CH2CHF_ee_Dbs.lor')
x2 = data2[:,0] 
y2 = (data2[:,1])
data2 = np.genfromtxt('CH2CHF_ee_Dbs.txt')
stcksx2 = data2[:,0]
stcksy2 = (data2[:,1])

data3 = np.genfromtxt('CH2CHF_ee_PRbs.lor')
x3 = data3[:,0] 
y3 = (data3[:,1])
data3 = np.genfromtxt('CH2CHF_ee_PRbs.txt')
stcksx3 = data3[:,0]
stcksy3 = (data3[:,1])

data4 = np.genfromtxt('CH2CHF_ee_DRbs.lor')
x4 = data4[:,0] 
y4 = (data4[:,1])
data4 = np.genfromtxt('CH2CHF_ee_DRbs.txt')
stcksx4 = data4[:,0]
stcksy4 = (data4[:,1])

#Experiment
data5 = np.genfromtxt('CH2CHF.csv')
ip5 = 290.8
x5 = data5[:,0] 
y5 = (data5[:,1])
f = interp1d(x5, y5, kind='slinear')
x5new = np.linspace(x5.min(),x5.max(),500) 
y5new = f(x5new)
params = {'mathtext.default': 'regular' }          
plt.rcParams.update(params)

#y5new = spline(x5,y5,x5new)

f = interp1d(x5, y5, kind='slinear')
y5new = f(x5new)

params = {'mathtext.default': 'regular' }          
plt.rcParams.update(params)

f, (ax1, ax2, ax3) = plt.subplots(3, sharex=True, sharey=True)


plt.xlim(283.75,291.1) #CH2CHF
yip = 0.1

plt.xlabel('Excitation energy (eV)')
plt.ylim(0,yip) 
plt.ylabel('                                                         Intensity (arb. units)')
plt.yticks([])

ax1.plot(x1+x1shift, y1, 'crimson', label='6-311++G** ( %.2f eV)' %x1shift, linewidth=2)#, linestyle='--')
ax1.plot(x2+x2shift, y2, 'darkblue', label='aug-cc-pVTZ ( %.2f eV)' %x2shift, linewidth=2)#, linestyle='--')

ax1.legend(loc='upper right',fontsize='small', framealpha=1)
ax1.plot([ip1+x1shift,ip1+x1shift],[0,yip],'crimson',linewidth=1.0, dashes=[5, 2])
ax1.plot([ip2+x2shift,ip2+x2shift],[0,yip],'darkblue',linewidth=1.0, dashes=[5, 2])

n=len(stcksx1)
for i in range(n):
    ax1.plot([stcksx1[i]+x1shift,stcksx1[i]+x1shift],[0,stcksy1[i]*1],'crimson',linewidth=1.0)
n=len(stcksx2)
for i in range(n):
    ax1.plot([stcksx2[i]+x2shift,stcksx2[i]+x2shift],[0,stcksy2[i]*1],'darkblue',linewidth=1.0)

ax2.plot(x3+x1shift, y3, 'crimson', label='6-311++G** + Rydberg ( %.2f eV)' %x1shift, linewidth=2)#, linestyle='--')
ax2.plot(x4+x2shift, y4, 'darkblue', label='aug-cc-pVTZ + Rydberg ( %.2f eV)' %x2shift, linewidth=2)#, linestyle='--')
ax2.plot([ip1+x1shift,ip1+x1shift],[0,yip],'crimson',linewidth=1.0, dashes=[5, 2])
ax2.plot([ip2+x2shift,ip2+x2shift],[0,yip],'darkblue',linewidth=1.0, dashes=[5, 2])
ax2.plot([ip3+x1shift,ip3+x1shift],[0,yip],'crimson',linewidth=1.0, dashes=[5, 2])
ax2.plot([ip4+x2shift,ip4+x2shift],[0,yip],'darkblue',linewidth=1.0, dashes=[5, 2])

ax2.legend(loc='upper right',fontsize='small', framealpha=1)

n=len(stcksx3)
for i in range(n):
    ax2.plot([stcksx3[i]+x1shift,stcksx3[i]+x1shift],[0,stcksy3[i]*1],'crimson',linewidth=1.0)
n=len(stcksx4)
for i in range(n):
    ax2.plot([stcksx4[i]+x2shift,stcksx4[i]+x2shift],[0,stcksy4[i]*1],'darkblue',linewidth=1.0)

ax3.plot(x5new, y5new/50, 'black', label='Experiment' , linewidth=2 )
ax3.plot([ip5,ip5],[0,yip],'black',linewidth=1.0, dashes=[5, 2])
ax3.legend(loc='upper right',fontsize='small', framealpha=1)

f.subplots_adjust(hspace=0)
plt.setp([a.get_xticklabels() for a in f.axes[:-1]], visible=False)


plt.savefig('CH2CHF.pdf')
plt.show()
