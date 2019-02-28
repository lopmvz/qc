import sys
import numpy as np
import matplotlib.pyplot as plt
import time
from scipy.interpolate import spline
from pylab import *
from scipy.interpolate import interp1d

data1 = np.genfromtxt('CH2CHF_o_exc_Pbs.lor')
ip1 = 291.7656
x1 = data1[:,0] 
y1 = (data1[:,1])

data2 = np.genfromtxt('CH2CHF_o_exc_Dbs.lor')
ip2 = 291.4435
x2 = data2[:,0] 
y2 = (data2[:,1])

data3 = np.genfromtxt('CH2CHF_ee_PRbs_aik_10e5.lor')
ip3 = 294.31
x3 = data3[:,0] 
y3 = (data3[:,1])

data4 = np.genfromtxt('CH2CHF_o_ee_DRbs.lor')
ip4 = 293.99
x4 = data4[:,0] 
y4 = (data4[:,1])

#Experiment
data5 = np.genfromtxt('CH2CHF.csv')
ip5CH2 = 291.10
ip5CHF = 293.48
x5 = data5[:,0] 
y5 = (data5[:,1])
x5new = np.linspace(x5.min(),x5.max(),500) #300 represents number of points to make between T.min and T.max

#y5new = spline(x5,y5,x5new)

f = interp1d(x5, y5, kind='slinear')
y5new = f(x5new)

params = {'mathtext.default': 'regular' }          
plt.rcParams.update(params)

plt.figure(1)
plt.title('')
#plt.xlim(285,297.5) #CO_C
#plt.xlim(292,297.5) #CO_C
#plt.xlim(866,871) #Ne
#plt.xlim(533,541) #H2O
#plt.xlim(400,408) #NH3
#plt.xlim(283,293) #C2H4
plt.xlim(283,294.35) #CH2CHF
plt.xlabel('Excitation energy (eV)')
yip = 3
plt.ylabel('Intensity (arb. units)')
plt.ylim(0.0,yip)#
plt.plot(x1, y1, 'xkcd:red', label='6-311++G**', linewidth=2, linestyle='--')
plt.plot(x3, y3, 'xkcd:red', label='6-311++G** + Rydberg', linewidth=2)
plt.plot(x2, y2, 'xkcd:darkblue', label='aug-cc-pVTZ', linewidth=2, linestyle='--')
plt.plot(x4, y4, 'xkcd:darkblue', label='aug-cc-pVTZ + Rydberg' , linewidth=2 )
plt.plot([ip1,ip1],[0,yip],'red',linewidth=2.0)
plt.plot([ip2,ip2],[0,yip],'darkblue',linewidth=2.0)
plt.plot([ip3,ip3],[0,yip],'red',linewidth=2.0)
plt.plot([ip4,ip4],[0,yip],'darkblue',linewidth=2.0)
plt.legend(loc='upper left',fontsize='small')
plt.savefig('CH2CHF_o.png')
plt.show()

plt.figure(2)
plt.title('')
#plt.xlim(285,297.5) #CO_C
#plt.xlim(292,297.5) #CO_C
#plt.xlim(866,871) #Ne
#plt.xlim(533,541) #H2O
#plt.xlim(400,408) #NH3
#plt.xlim(283,293) #C2H4
plt.xlim(283,294.35) #CH2CHF
yip = 1
plt.ylim(0.0,yip)
plt.xlabel('Excitation energy (eV)')
plt.ylabel('Intensity (arb. units)')
plt.plot(x5new, y5new/4, 'xkcd:black', label='Experiment' , linewidth=2 )
plt.plot([ip5CH2,ip5CH2],[0,yip],'black',linewidth=2.0)
plt.plot([ip5CHF,ip5CHF],[0,yip],'black',linewidth=2.0)
plt.legend(loc='upper left',fontsize='small')
plt.savefig('CH2CHFexp.png')
plt.show()
