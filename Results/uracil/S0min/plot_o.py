import sys
import numpy as np
import matplotlib.pyplot as plt
from pylab import *
from scipy.interpolate import interp1d

#First peak at 533.21
x1shift = - 1.86 # = 531.35 - 533.21 

datadummy = np.genfromtxt('uracil_so_c.lor')
xdummy = datadummy[:,0] 
ydummy = datadummy[:,1]

data1 = np.genfromtxt('uracil_so_o.lor')
stcks1 = np.genfromtxt('uracil_so_o.txt')
ip1 = 539.7024
x1 = data1[:,0] 
y1 = data1[:,1]
stcksx1 = stcks1[:,0] 
stcksy1 = stcks1[:,1]

data2 = np.genfromtxt('uracil_s1_o.lor')
stcks2 = np.genfromtxt('uracil_s1_o.txt')
x2 = data2[:,0] 
y2 = data2[:,1]
stcksx2 = stcks2[:,0] 
stcksy2 = stcks2[:,1]

data3 = np.genfromtxt('uracil_s2_o.lor')
stcks3 = np.genfromtxt('uracil_s2_o.txt')
x3 = data3[:,0] 
y3 = data3[:,1]
stcksx3 = stcks3[:,0] 
stcksy3 = stcks3[:,1]

#First peak at 531.3 eV
#data4 = np.genfromtxt('uracil_o_exp.csv')
data4 = np.genfromtxt('Oxygen_Uracil.dat')
#ip = 291.0
x4 = data4[:,0] 
y4 = (data4[:,1])
f = interp1d(x4, y4, kind='slinear')
x4new = np.linspace(x4.min(),x4.max(),400) 
y4new = f(x4new)

params = {'mathtext.default': 'regular' }          
plt.rcParams.update(params)


f, (ax1, ax2) = plt.subplots(2, sharex=True, sharey=True)

plt.xlim(524,538) 
yip = 0.08

plt.xlabel('Excitation energy (eV)')
plt.ylim(0.0,yip)
plt.ylabel('                                             Intensity (arb. units)')
plt.yticks([])
ax1.plot([ip1+x1shift,ip1+x1shift],[0,yip],'crimson',linewidth=1.0, dashes=[5, 2])
ax1.plot(x1+x1shift, y1,'crimson', label='S0', linewidth=2)
ax1.plot(x2+x1shift, y2, 'darkblue', label='S1 ($n\pi^*$)', linewidth=2)
ax1.plot(x3+x1shift, y3, 'g', label='S2 ($\pi\pi^*$)', linewidth=2)
ax1.plot(xdummy, ydummy, 'white',      label='$\Delta x$ = %.2f eV' %x1shift, linewidth=2)
n=len(stcksx1)
for i in range(n):
    ax1.plot([stcksx1[i]+x1shift,stcksx1[i]+x1shift],[0,stcksy1[i]*1],'crimson',linewidth=1.0)
n=len(stcksx2)
for i in range(n):
    ax1.plot([stcksx2[i]+x1shift,stcksx2[i]+x1shift],[0,stcksy2[i]*1],'darkblue',linewidth=1.0)
n=len(stcksx3)
for i in range(n):
    ax1.plot([stcksx3[i]+x1shift,stcksx3[i]+x1shift],[0,stcksy3[i]*1],'g',linewidth=1.0)
ax1.legend(loc='upper left',fontsize='small')

ax2.plot(x4, y4/100-0.04, 'k', label='Experiment', linewidth=2)
ax2.legend(loc='upper left',fontsize='small')

f.subplots_adjust(hspace=0)
plt.setp([a.get_xticklabels() for a in f.axes[:-1]], visible=False)

plt.savefig('Uracil_Sn_O.pdf')
plt.show()


#yip = 0.10
#
#plt.xlabel('Excitation energy (eV)')
#plt.ylim(0.0,yip)
#plt.ylabel('                                                Intensity (arb. units)')
#plt.yticks([])
#ax1.plot([ip1+x1shift,ip1+x1shift],[0,yip],'crimson',linewidth=1.0, dashes=[5, 2])
#ax1.plot(x1+x1shift, y1,'crimson', label='S0 ', linewidth=2)
#ax1.plot(x2+x1shift, y2, 'darkblue', label='S1 ($n\pi^*$)', linewidth=2)
#ax1.plot(x3+x1shift, y3, 'g', label='S2 ($n\pi^*$)', linewidth=2)
#ax1.plot(xdummy, ydummy, 'white',      label='$\Delta x$ = %.2f eV' %x1shift, linewidth=2)
#ax1.legend(loc='upper left',fontsize='small')
#
#
#ax2.plot(x1+x1shift, y1,'crimson', label = 'S0 ($\Delta x$ = %.2f eV)' %x1shift, linewidth=2)
#ax2.plot([ip1+x1shift,ip1+x1shift],[0,yip],'crimson',linewidth=1.0, dashes=[5, 2])
#n=len(stcksx1)
#for i in range(n):
#    ax2.plot([stcksx1[i]+x1shift,stcksx1[i]+x1shift],[0,stcksy1[i]*1],'crimson',linewidth=1.0)
##plt.plot([ip,ip],[0,yip],'k',linewidth=1.0, dashes=[5, 2])
#ax2.plot(x4, y4/100, 'k', label='S0 Exp.', linewidth=2)
#ax2.legend(loc='upper left',fontsize='small')
#
#f.subplots_adjust(hspace=0)
#plt.setp([a.get_xticklabels() for a in f.axes[:-1]], visible=False)
#
#plt.savefig('Uracil_Sn_O_1.pdf')
#plt.show()
